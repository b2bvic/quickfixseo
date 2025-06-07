#!/usr/bin/env python3
"""
Google Drive API Setup Script
Helps set up the Google Drive integration for the intelligent crawler
"""

import os
import json
from pathlib import Path

def create_credentials_template():
    """Create a template for Google Drive API credentials"""
    template = {
        "installed": {
            "client_id": "YOUR_CLIENT_ID.apps.googleusercontent.com",
            "project_id": "your-project-id",
            "auth_uri": "https://accounts.google.com/o/oauth2/auth",
            "token_uri": "https://oauth2.googleapis.com/token",
            "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
            "client_secret": "YOUR_CLIENT_SECRET",
            "redirect_uris": ["http://localhost"]
        }
    }
    
    with open('credentials_template.json', 'w') as f:
        json.dump(template, f, indent=2)
    
    print("✅ Created credentials_template.json")

def print_setup_instructions():
    """Print detailed setup instructions"""
    print("🔧 Google Drive API Setup Instructions")
    print("=" * 50)
    print()
    print("1️⃣  Go to Google Cloud Console:")
    print("   https://console.cloud.google.com/")
    print()
    print("2️⃣  Create a new project or select existing one")
    print()
    print("3️⃣  Enable Google Drive API:")
    print("   - Go to 'APIs & Services' > 'Library'")
    print("   - Search for 'Google Drive API'")
    print("   - Click 'Enable'")
    print()
    print("4️⃣  Create credentials:")
    print("   - Go to 'APIs & Services' > 'Credentials'")
    print("   - Click 'Create Credentials' > 'OAuth client ID'")
    print("   - Select 'Desktop application'")
    print("   - Name it 'SEO Crawler'")
    print("   - Download the JSON file")
    print()
    print("5️⃣  Rename the downloaded file to 'credentials.json'")
    print("   and place it in this directory")
    print()
    print("6️⃣  Make sure victor@scalewithsearch.com has:")
    print("   - Access to the shared drive")
    print("   - Permission to create folders")
    print("   - Permission to upload files")
    print()
    print("7️⃣  Install Python dependencies:")
    print("   pip install -r requirements.txt")
    print()
    print("8️⃣  Test the setup:")
    print("   python test_drive_connection.py")
    print()
    print("⚠️  IMPORTANT:")
    print("   - The first run will open a browser for authentication")
    print("   - You must authenticate with victor@scalewithsearch.com")
    print("   - Or an account that has access to the shared drive")

def check_setup():
    """Check if setup is complete"""
    print("🔍 Checking setup status...")
    print()
    
    # Check Python dependencies
    required_packages = [
        'google-api-python-client',
        'google-auth-httplib2',
        'google-auth-oauthlib',
        'requests',
        'beautifulsoup4'
    ]
    
    missing_packages = []
    for package in required_packages:
        try:
            __import__(package.replace('-', '_'))
            print(f"✅ {package} - installed")
        except ImportError:
            print(f"❌ {package} - not installed")
            missing_packages.append(package)
    
    print()
    
    # Check credentials file
    if os.path.exists('credentials.json'):
        print("✅ credentials.json - found")
        try:
            with open('credentials.json', 'r') as f:
                creds = json.load(f)
                if 'installed' in creds and 'client_id' in creds['installed']:
                    print("✅ credentials.json - appears valid")
                else:
                    print("❌ credentials.json - invalid format")
        except json.JSONDecodeError:
            print("❌ credentials.json - invalid JSON")
    else:
        print("❌ credentials.json - not found")
    
    # Check Screaming Frog installation
    screamingfrog_path = "/Applications/Screaming Frog SEO Spider.app/Contents/MacOS/ScreamingFrogSEOSpiderLauncher"
    if os.path.exists(screamingfrog_path):
        print("✅ Screaming Frog SEO Spider - installed")
    else:
        print("❌ Screaming Frog SEO Spider - not found")
    
    print()
    
    if missing_packages:
        print("❌ Setup incomplete!")
        print(f"Missing packages: {', '.join(missing_packages)}")
        print("Run: pip install -r requirements.txt")
        return False
    elif not os.path.exists('credentials.json'):
        print("❌ Setup incomplete!")
        print("Missing credentials.json file")
        return False
    else:
        print("✅ Setup appears complete!")
        print("Try running: python test_drive_connection.py")
        return True

def main():
    print("🚀 Google Drive API Setup for SEO Crawler")
    print("=" * 50)
    print()
    print("Choose an option:")
    print("1. Show setup instructions")
    print("2. Create credentials template")
    print("3. Check setup status")
    print("4. All of the above")
    print()
    
    choice = input("Enter your choice (1-4): ").strip()
    
    if choice == "1":
        print_setup_instructions()
    elif choice == "2":
        create_credentials_template()
    elif choice == "3":
        check_setup()
    elif choice == "4":
        print_setup_instructions()
        print("\n" + "=" * 50 + "\n")
        create_credentials_template()
        print("\n" + "=" * 50 + "\n")
        check_setup()
    else:
        print("Invalid choice!")

if __name__ == "__main__":
    main() 