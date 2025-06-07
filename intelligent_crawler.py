#!/usr/bin/env python3
"""
Intelligent Screaming Frog Crawler with Google Drive Integration
Analyzes website structure and automatically sets optimal crawl parameters
Uploads results directly to Google Workspace Shared Drive
"""

import os
import sys
import json
import requests
import subprocess
from datetime import datetime
from urllib.parse import urlparse, urljoin
from bs4 import BeautifulSoup
import time
from pathlib import Path

# Google Drive API imports
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow

class IntelligentCrawler:
    def __init__(self):
        self.screamingfrog_path = "/Applications/Screaming Frog SEO Spider.app/Contents/MacOS/ScreamingFrogSEOSpiderLauncher"
        self.drive_service = None
        self.shared_drive_id = None
        
        # Google Drive API scopes
        self.SCOPES = [
            'https://www.googleapis.com/auth/drive',
            'https://www.googleapis.com/auth/drive.file'
        ]
        
    def authenticate_google_drive(self):
        """Authenticate with Google Drive API"""
        creds = None
        token_file = 'token.json'
        credentials_file = 'credentials.json'
        
        # Check if token.json exists
        if os.path.exists(token_file):
            creds = Credentials.from_authorized_user_file(token_file, self.SCOPES)
        
        # If there are no (valid) credentials available, let the user log in
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                if not os.path.exists(credentials_file):
                    print("❌ ERROR: Google Drive credentials not found!")
                    print("Please follow the setup instructions to create credentials.json")
                    return False
                
                flow = InstalledAppFlow.from_client_secrets_file(
                    credentials_file, self.SCOPES)
                creds = flow.run_local_server(port=0)
            
            # Save the credentials for the next run
            with open(token_file, 'w') as token:
                token.write(creds.to_json())
        
        self.drive_service = build('drive', 'v3', credentials=creds)
        return True
    
    def find_shared_drive(self, email="victor@scalewithsearch.com"):
        """Find the shared drive for the specified email/workspace"""
        try:
            # List shared drives
            results = self.drive_service.drives().list().execute()
            drives = results.get('drives', [])
            
            if not drives:
                print("❌ No shared drives found!")
                return None
            
            # For now, we'll use the first shared drive found
            # In production, you might want to search by name
            self.shared_drive_id = drives[0]['id']
            print(f"✅ Found shared drive: {drives[0]['name']}")
            return self.shared_drive_id
            
        except Exception as e:
            print(f"❌ Error finding shared drive: {str(e)}")
            return None
    
    def analyze_website(self, url):
        """Analyze website to determine optimal crawl parameters"""
        print(f"🔍 Analyzing website structure for {url}...")
        
        analysis = {
            'url': url,
            'domain': urlparse(url).netloc,
            'has_sitemap': False,
            'estimated_pages': 0,
            'has_ecommerce': False,
            'has_blog': False,
            'cms_detected': None,
            'recommended_crawl_limit': 10000,
            'javascript_heavy': False,
            'multilingual': False,
            'crawl_parameters': []
        }
        
        try:
            # Basic site analysis
            headers = {
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36'
            }
            
            response = requests.get(url, headers=headers, timeout=10)
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Detect CMS and framework
            self._detect_cms(soup, analysis)
            
            # Check for sitemap
            sitemap_urls = [
                urljoin(url, '/sitemap.xml'),
                urljoin(url, '/sitemap_index.xml'),
                urljoin(url, '/sitemap/')
            ]
            
            for sitemap_url in sitemap_urls:
                try:
                    sitemap_response = requests.get(sitemap_url, headers=headers, timeout=5)
                    if sitemap_response.status_code == 200:
                        analysis['has_sitemap'] = True
                        # Basic sitemap parsing to estimate pages
                        if 'sitemap' in sitemap_response.text.lower():
                            analysis['estimated_pages'] = sitemap_response.text.count('<loc>')
                        break
                except:
                    continue
            
            # Detect ecommerce indicators
            ecommerce_indicators = ['add to cart', 'buy now', 'shopping cart', 'checkout', 'product', 'price']
            if any(indicator in response.text.lower() for indicator in ecommerce_indicators):
                analysis['has_ecommerce'] = True
            
            # Detect blog
            blog_indicators = ['blog', 'article', 'post', '/category/', '/tag/']
            if any(indicator in response.text.lower() for indicator in blog_indicators):
                analysis['has_blog'] = True
            
            # Check for heavy JavaScript usage
            scripts = soup.find_all('script')
            if len(scripts) > 10 or any('react' in str(script).lower() or 'angular' in str(script).lower() or 'vue' in str(script).lower() for script in scripts):
                analysis['javascript_heavy'] = True
            
            # Set recommended parameters based on analysis
            self._set_crawl_parameters(analysis)
            
        except Exception as e:
            print(f"⚠️  Warning: Could not fully analyze website: {str(e)}")
            print("Using default crawl parameters...")
        
        return analysis
    
    def _detect_cms(self, soup, analysis):
        """Detect CMS/framework being used"""
        html_str = str(soup).lower()
        
        cms_signatures = {
            'wordpress': ['wp-content', 'wp-includes', 'wordpress'],
            'shopify': ['shopify', 'shop.js', 'cdn.shopify'],
            'wix': ['wix.com', 'wixstatic'],
            'squarespace': ['squarespace', 'sqsp.com'],
            'drupal': ['drupal', 'sites/all/', 'sites/default/'],
            'joomla': ['joomla', 'com_content', 'mod_'],
            'magento': ['magento', 'mage/', 'skin/frontend/'],
            'webflow': ['webflow', 'wf-'],
            'react': ['react', 'reactjs'],
            'nextjs': ['next.js', '_next/'],
            'gatsby': ['gatsby', '__gatsby']
        }
        
        for cms, signatures in cms_signatures.items():
            if any(sig in html_str for sig in signatures):
                analysis['cms_detected'] = cms
                break
    
    def _set_crawl_parameters(self, analysis):
        """Set optimal crawl parameters based on analysis"""
        params = []
        
        # Base parameters for CSV export
        params.extend([
            '--export-format', 'csv',
            '--save-crawl'
        ])
        
        # Adjust crawl limit based on estimated size
        if analysis['estimated_pages'] > 50000:
            params.extend(['--crawl-limit', '50000'])
            analysis['recommended_crawl_limit'] = 50000
        elif analysis['estimated_pages'] > 10000:
            params.extend(['--crawl-limit', '25000'])
            analysis['recommended_crawl_limit'] = 25000
        else:
            params.extend(['--crawl-limit', '10000'])
        
        # JavaScript rendering for JS-heavy sites
        if analysis['javascript_heavy']:
            params.extend(['--render-javascript', 'true'])
        
        # Ecommerce-specific settings
        if analysis['has_ecommerce']:
            params.extend([
                '--include-images', 'true',
                '--include-pdfs', 'true',
                '--crawl-forms', 'true'
            ])
        
        # Blog-specific settings
        if analysis['has_blog']:
            params.extend([
                '--include-images', 'true',
                '--crawl-pagination', 'true'
            ])
        
        # Use sitemap if available
        if analysis['has_sitemap']:
            params.extend(['--use-sitemap', 'true'])
        
        analysis['crawl_parameters'] = params
    
    def run_crawl(self, url, analysis):
        """Execute the Screaming Frog crawl with optimized parameters"""
        print(f"🕷️  Starting intelligent crawl for {analysis['domain']}...")
        
        # Create local output directory
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        domain_clean = analysis['domain'].replace('.', '_').replace('www_', '')
        output_dir = f"./temp_crawl_{domain_clean}_{timestamp}"
        os.makedirs(output_dir, exist_ok=True)
        
        # Build the command
        cmd = [
            self.screamingfrog_path,
            '--crawl', url,
            '--headless',
            '--output-folder', output_dir
        ] + analysis['crawl_parameters']
        
        print(f"🚀 Crawl parameters: {' '.join(analysis['crawl_parameters'])}")
        print(f"📂 Temporary output: {output_dir}")
        print("⏳ This may take several minutes...")
        
        try:
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=3600)  # 1 hour timeout
            
            if result.returncode == 0:
                print("✅ Crawl completed successfully!")
                return output_dir
            else:
                print(f"❌ Crawl failed: {result.stderr}")
                return None
                
        except subprocess.TimeoutExpired:
            print("❌ Crawl timed out after 1 hour")
            return None
        except Exception as e:
            print(f"❌ Error running crawl: {str(e)}")
            return None
    
    def create_drive_folder_structure(self, client_name, audit_date):
        """Create folder structure in Google Drive: Shared Drive > Client Folder > Audit Folder"""
        try:
            if not self.shared_drive_id:
                print("❌ No shared drive found!")
                return None
            
            # Find or create client folder
            client_folder_id = self._find_or_create_folder(
                client_name, 
                self.shared_drive_id, 
                is_drive_root=True
            )
            
            if not client_folder_id:
                return None
            
            # Find or create audit folder within client folder
            audit_folder_name = f"Audit_{audit_date}"
            audit_folder_id = self._find_or_create_folder(
                audit_folder_name,
                client_folder_id
            )
            
            print(f"✅ Created folder structure: {client_name}/Audit_{audit_date}")
            return audit_folder_id
            
        except Exception as e:
            print(f"❌ Error creating folder structure: {str(e)}")
            return None
    
    def _find_or_create_folder(self, folder_name, parent_id, is_drive_root=False):
        """Find existing folder or create new one"""
        try:
            # Search for existing folder
            if is_drive_root:
                query = f"name='{folder_name}' and parents in '{parent_id}' and mimeType='application/vnd.google-apps.folder' and trashed=false"
                results = self.drive_service.files().list(
                    q=query,
                    driveId=self.shared_drive_id,
                    includeItemsFromAllDrives=True,
                    supportsAllDrives=True,
                    corpora='drive'
                ).execute()
            else:
                query = f"name='{folder_name}' and '{parent_id}' in parents and mimeType='application/vnd.google-apps.folder' and trashed=false"
                results = self.drive_service.files().list(
                    q=query,
                    includeItemsFromAllDrives=True,
                    supportsAllDrives=True
                ).execute()
            
            items = results.get('files', [])
            
            if items:
                print(f"📁 Found existing folder: {folder_name}")
                return items[0]['id']
            
            # Create new folder
            folder_metadata = {
                'name': folder_name,
                'mimeType': 'application/vnd.google-apps.folder',
                'parents': [parent_id]
            }
            
            folder = self.drive_service.files().create(
                body=folder_metadata,
                supportsAllDrives=True
            ).execute()
            
            print(f"📁 Created new folder: {folder_name}")
            return folder.get('id')
            
        except Exception as e:
            print(f"❌ Error with folder {folder_name}: {str(e)}")
            return None
    
    def upload_results_to_drive(self, local_dir, drive_folder_id, audit_timestamp):
        """Upload crawl results to Google Drive"""
        try:
            print("☁️  Uploading results to Google Drive...")
            
            uploaded_files = []
            
            # Find CSV files in the output directory
            csv_files = list(Path(local_dir).glob('*.csv'))
            other_files = [f for f in Path(local_dir).glob('*') if f.suffix != '.csv' and f.is_file()]
            
            all_files = csv_files + other_files
            
            for file_path in all_files:
                try:
                    # Create filename with timestamp
                    file_name = f"{audit_timestamp}_{file_path.name}"
                    
                    # Upload file
                    media = MediaFileUpload(str(file_path), resumable=True)
                    file_metadata = {
                        'name': file_name,
                        'parents': [drive_folder_id]
                    }
                    
                    file_obj = self.drive_service.files().create(
                        body=file_metadata,
                        media_body=media,
                        supportsAllDrives=True
                    ).execute()
                    
                    uploaded_files.append(file_name)
                    print(f"✅ Uploaded: {file_name}")
                    
                except Exception as e:
                    print(f"❌ Failed to upload {file_path.name}: {str(e)}")
            
            return uploaded_files
            
        except Exception as e:
            print(f"❌ Error uploading to Drive: {str(e)}")
            return []
    
    def cleanup_local_files(self, local_dir):
        """Clean up temporary local files"""
        try:
            import shutil
            shutil.rmtree(local_dir)
            print(f"🧹 Cleaned up temporary directory: {local_dir}")
        except Exception as e:
            print(f"⚠️  Could not clean up {local_dir}: {str(e)}")
    
    def run_intelligent_audit(self, url):
        """Main method to run complete intelligent audit"""
        print("🚀 Starting Intelligent SEO Audit")
        print("=" * 50)
        print(f"🎯 Target URL: {url}")
        
        # Step 1: Authenticate Google Drive
        print("\n1️⃣  Authenticating Google Drive...")
        if not self.authenticate_google_drive():
            return False
        
        # Step 2: Find shared drive
        print("\n2️⃣  Finding shared drive...")
        if not self.find_shared_drive():
            return False
        
        # Step 3: Analyze website
        print("\n3️⃣  Analyzing website...")
        analysis = self.analyze_website(url)
        
        # Print analysis summary
        print(f"✅ Analysis complete:")
        print(f"   - Domain: {analysis['domain']}")
        print(f"   - CMS: {analysis['cms_detected'] or 'Unknown'}")
        print(f"   - Estimated pages: {analysis['estimated_pages']}")
        print(f"   - Has sitemap: {analysis['has_sitemap']}")
        print(f"   - E-commerce: {analysis['has_ecommerce']}")
        print(f"   - JavaScript heavy: {analysis['javascript_heavy']}")
        print(f"   - Crawl limit: {analysis['recommended_crawl_limit']}")
        
        # Step 4: Run crawl
        print("\n4️⃣  Running optimized crawl...")
        local_output_dir = self.run_crawl(url, analysis)
        
        if not local_output_dir:
            print("❌ Crawl failed!")
            return False
        
        # Step 5: Create Drive folder structure
        print("\n5️⃣  Creating Google Drive folder structure...")
        audit_timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        client_name = analysis['domain'].replace('.', '_').replace('www_', '')
        
        drive_folder_id = self.create_drive_folder_structure(client_name, audit_timestamp)
        
        if not drive_folder_id:
            print("❌ Failed to create Drive folder structure!")
            return False
        
        # Step 6: Upload results
        print("\n6️⃣  Uploading results to Google Drive...")
        uploaded_files = self.upload_results_to_drive(local_output_dir, drive_folder_id, audit_timestamp)
        
        if not uploaded_files:
            print("❌ No files were uploaded!")
            return False
        
        # Step 7: Cleanup
        print("\n7️⃣  Cleaning up...")
        self.cleanup_local_files(local_output_dir)
        
        # Final summary
        print("\n🎉 AUDIT COMPLETE!")
        print("=" * 50)
        print(f"📊 Website: {url}")
        print(f"📁 Files uploaded: {len(uploaded_files)}")
        print(f"☁️  Location: Shared Drive > {client_name} > Audit_{audit_timestamp}")
        print(f"📅 Audit timestamp: {audit_timestamp}")
        print("\nUploaded files:")
        for file_name in uploaded_files:
            print(f"   - {file_name}")
        
        return True

def main():
    if len(sys.argv) != 2:
        print("🕷️  Intelligent SEO Crawler")
        print("")
        print("Usage: python intelligent_crawler.py <website_url>")
        print("Example: python intelligent_crawler.py https://example.com")
        print("")
        print("This script will:")
        print("• Analyze the website structure")
        print("• Set optimal crawl parameters automatically")
        print("• Run Screaming Frog crawl")
        print("• Upload results to Google Drive (victor@scalewithsearch.com)")
        print("• Organize files in: Shared Drive > Client Folder > Audit Folder")
        sys.exit(1)
    
    url = sys.argv[1]
    
    # Validate URL
    if not url.startswith(('http://', 'https://')):
        url = 'https://' + url
    
    crawler = IntelligentCrawler()
    success = crawler.run_intelligent_audit(url)
    
    if not success:
        sys.exit(1)

if __name__ == "__main__":
    main() 