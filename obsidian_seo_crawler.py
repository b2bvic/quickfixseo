#!/usr/bin/env python3
"""
Comprehensive Obsidian SEO Crawler - Multi-page analysis system
Enhanced with Technical SEO Pro checklist features + Advanced Enterprise Features
Crawls multiple pages to provide accurate, complete SEO insights
"""

import os
import sys
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse, urlunparse
from datetime import datetime
import time
import json
from collections import defaultdict, Counter
from concurrent.futures import ThreadPoolExecutor, as_completed
import threading
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
import re
import hashlib
from textstat import flesch_reading_ease, flesch_kincaid_grade
import statistics

class ComprehensiveSEOCrawler:
    def __init__(self, obsidian_vault_path=None, max_pages=None):
        """Initialize the comprehensive SEO crawler with advanced features"""
        
        # Configuration file for remembering settings
        self.config_file = os.path.expanduser("~/.obsidian_seo_config.json")
        
        # Crawling settings - default to unlimited like Screaming Frog
        self.max_pages = max_pages if max_pages else 50000  # Very high limit for full sites
        self.failed_pages = []
        self.crawl_stats = {
            'pages_found': 0,
            'pages_analyzed': 0,
            'pages_skipped': 0,
            'start_time': None
        }
        
        # Performance settings
        self.max_workers = 10  # Parallel threads
        self.request_timeout = 8  # Faster timeout
        self.stats_lock = threading.Lock()  # Thread safety
        
        # Obsidian vault setup
        if obsidian_vault_path:
            self.obsidian_vault_path = obsidian_vault_path
        else:
            self.obsidian_vault_path = self.load_vault_path()
        
        # SEO audit folder within Obsidian
        self.seo_audits_folder = os.path.join(self.obsidian_vault_path, "SEO Audits")
        os.makedirs(self.seo_audits_folder, exist_ok=True)
        
        # Optimized session with connection pooling
        self.session = self.create_optimized_session()
        
        # Technical SEO tracking
        self.robots_txt_data = None
        self.sitemap_data = []
        self.security_issues = []
        self.redirect_chains = []
        self.canonical_issues = []
        self.structured_data_pages = []
        
        # Advanced tracking features
        self.core_web_vitals = {}
        self.mobile_usability_issues = []
        self.content_quality_scores = {}
        self.competitive_data = {}
        self.schema_markup_analysis = {}
        self.page_experience_signals = {}
    
    def create_optimized_session(self):
        """Create optimized requests session with connection pooling and retries"""
        session = requests.Session()
        
        # Retry strategy
        retry_strategy = Retry(
            total=2,
            backoff_factor=0.1,
            status_forcelist=[429, 500, 502, 503, 504],
        )
        
        # Mount adapter with retry strategy
        adapter = HTTPAdapter(
            max_retries=retry_strategy,
            pool_connections=20,
            pool_maxsize=20
        )
        session.mount("http://", adapter)
        session.mount("https://", adapter)
        
        # Headers
        session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Accept-Encoding': 'gzip, deflate',
            'Connection': 'keep-alive'
        })
        
        return session
    
    def load_vault_path(self):
        """Load vault path from config"""
        try:
            if os.path.exists(self.config_file):
                with open(self.config_file, 'r') as f:
                    config = json.load(f)
                    saved_vault = config.get('obsidian_vault_path')
                    if saved_vault and os.path.exists(saved_vault):
                        print(f"📁 Using saved Obsidian vault: {saved_vault}")
                        return saved_vault
        except:
            pass
        return os.path.expanduser("~/Desktop/SEO_Audits")
    
    def comprehensive_analysis(self, url):
        """Perform comprehensive site analysis with technical SEO checks"""
        self.crawl_stats['start_time'] = time.time()
        
        print(f"🚀 Starting FULL SITE SEO analysis for {url}")
        print("=" * 60)
        print(f"🎯 Crawl Mode: Complete Site Analysis (like Screaming Frog)")
        if self.max_pages < 50000:
            print(f"📊 Page Limit: {self.max_pages} pages")
        else:
            print(f"📊 Page Limit: Full Site Crawl (up to 50,000 pages)")
        
        # Ensure URL has protocol
        if not url.startswith(('http://', 'https://')):
            url = 'https://' + url
        
        domain = urlparse(url).netloc.replace('www.', '')
        
        # Step 0: Technical SEO Infrastructure Analysis
        print(f"\n0️⃣  Analyzing technical SEO infrastructure...")
        self.analyze_robots_txt(url, domain)
        self.analyze_security(url, domain)
        
        # Step 1: Discover pages
        print(f"\n1️⃣  Discovering site structure...")
        discovered_pages = self.discover_pages(url, domain)
        
        # Step 1.5: Deduplicate URLs that resolve to the same final destination
        print(f"\n1️⃣.5️⃣  Deduplicating URLs and resolving redirects...")
        unique_pages = self.deduplicate_urls(discovered_pages)
        
        # Step 2: Analyze pages in parallel (SPEED BOOST!)
        print(f"\n2️⃣  Analyzing {len(unique_pages)} pages in parallel...")
        print(f"   ⚡ Using {self.max_workers} concurrent threads for maximum speed")
        analyzed_pages = self.analyze_pages_parallel(unique_pages, domain)
        
        # Step 3: Compile analysis
        elapsed = time.time() - self.crawl_stats['start_time']
        print(f"\n3️⃣  Compiling comprehensive analysis... ({elapsed:.1f}s total)")
        analysis = self.compile_site_analysis(url, domain, analyzed_pages)
        
        return analysis
    
    def analyze_robots_txt(self, base_url, domain):
        """Analyze robots.txt file for technical SEO issues"""
        try:
            robots_url = urljoin(base_url, '/robots.txt')
            response = self.session.get(robots_url, timeout=self.request_timeout)
            
            self.robots_txt_data = {
                'url': robots_url,
                'status_code': response.status_code,
                'exists': response.status_code == 200,
                'content': response.text if response.status_code == 200 else '',
                'size': len(response.content) if response.status_code == 200 else 0,
                'issues': []
            }
            
            if response.status_code == 200:
                content = response.text.lower()
                
                # Check for common issues
                if 'disallow: /' in content and 'allow:' not in content:
                    self.robots_txt_data['issues'].append("Robots.txt blocks all crawling")
                
                if '.css' in content and 'disallow' in content:
                    self.robots_txt_data['issues'].append("CSS files may be blocked")
                
                if '.js' in content and 'disallow' in content:
                    self.robots_txt_data['issues'].append("JavaScript files may be blocked")
                
                if 'sitemap:' not in content:
                    self.robots_txt_data['issues'].append("No sitemap reference found")
                
                # Extract sitemap URLs
                sitemap_matches = re.findall(r'sitemap:\s*(.+)', response.text, re.IGNORECASE)
                self.robots_txt_data['sitemaps'] = [s.strip() for s in sitemap_matches]
            
        except Exception as e:
            self.robots_txt_data = {
                'url': urljoin(base_url, '/robots.txt'),
                'status_code': None,
                'exists': False,
                'content': '',
                'size': 0,
                'issues': [f"Failed to fetch robots.txt: {str(e)}"]
            }
    
    def analyze_security(self, base_url, domain):
        """Analyze HTTPS and security configuration"""
        try:
            # Test HTTPS
            https_url = base_url.replace('http://', 'https://')
            http_url = base_url.replace('https://', 'http://')
            
            # Check HTTPS response
            try:
                https_response = self.session.get(https_url, timeout=self.request_timeout)
                https_works = https_response.status_code < 400
            except:
                https_works = False
            
            # Check HTTP to HTTPS redirect
            try:
                http_response = self.session.get(http_url, timeout=self.request_timeout, allow_redirects=False)
                redirects_to_https = (http_response.status_code in [301, 302] and 
                                    'https://' in http_response.headers.get('location', ''))
            except:
                redirects_to_https = False
            
            self.security_issues = {
                'https_available': https_works,
                'http_redirects_to_https': redirects_to_https,
                'mixed_content_risk': not https_works,
                'issues': []
            }
            
            if not https_works:
                self.security_issues['issues'].append("HTTPS not available")
            if not redirects_to_https:
                self.security_issues['issues'].append("HTTP does not redirect to HTTPS")
                
        except Exception as e:
            self.security_issues = {
                'https_available': False,
                'http_redirects_to_https': False,
                'mixed_content_risk': True,
                'issues': [f"Security analysis failed: {str(e)}"]
            }
    
    def discover_pages(self, start_url, domain):
        """Discover pages by crawling internal links like Screaming Frog"""
        to_crawl = [start_url]
        crawled = set()
        discovered_urls = set()
        depth_map = {start_url: 0}  # Track crawl depth
        
        print(f"   🔍 Starting crawl from: {start_url}")
        
        while to_crawl and len(crawled) < self.max_pages:
            current_url = to_crawl.pop(0)
            current_depth = depth_map.get(current_url, 0)
            
            if current_url in crawled:
                continue
                
            crawled.add(current_url)
            self.crawl_stats['pages_found'] += 1
            
            # Progress updates every 25 pages during discovery
            if len(crawled) % 25 == 0:
                print(f"   📄 Found {len(crawled)} pages, queue: {len(to_crawl)} remaining...")
            
            try:
                response = self.session.get(current_url, timeout=self.request_timeout)
                if response.status_code == 200:
                    soup = BeautifulSoup(response.content, 'html.parser')
                    
                    # Extract internal links more aggressively
                    links = soup.find_all('a', href=True)
                    new_links_found = 0
                    
                    for link in links:
                        href = link['href']
                        full_url = urljoin(current_url, href)
                        normalized_url = self.normalize_url(full_url)
                        
                        # Check if internal and valid
                        if (self.is_internal_url(normalized_url, domain) and 
                            normalized_url not in crawled and 
                            normalized_url not in discovered_urls and
                            self.is_valid_page_url(normalized_url) and
                            current_depth < 15):  # Max depth of 15 for deeper sites
                            
                            discovered_urls.add(normalized_url)
                            to_crawl.append(normalized_url)
                            depth_map[normalized_url] = current_depth + 1
                            new_links_found += 1
                    
                    # Also check for sitemaps if we're on the homepage
                    if current_depth == 0:
                        self.check_and_parse_sitemap(start_url, domain, crawled, to_crawl, depth_map)

                # No delay needed with session pooling
                pass
                
            except Exception as e:
                self.failed_pages.append(current_url)
                continue
        
        total_found = len(crawled)
        if len(crawled) >= self.max_pages:
            print(f"   ⚠️  Reached page limit of {self.max_pages}. Site likely has more pages.")
        else:
            print(f"   🎯 Discovered entire site structure!")
        
        print(f"   ✅ Discovery complete: {total_found} pages found")
        
        # Filter out HTTP URLs if HTTPS is available
        crawled_list = list(crawled)
        filtered_crawled = self.filter_http_urls_if_https_available(crawled_list, domain)
        
        if len(filtered_crawled) != len(crawled_list):
            print(f"   🔒 Final page count after HTTPS filtering: {len(filtered_crawled)} pages")
        
        return filtered_crawled
    
    def normalize_url(self, url):
        """Normalize URL to avoid duplicates"""
        parsed = urlparse(url)
        # Remove fragment and normalize
        normalized = urlunparse((
            parsed.scheme,
            parsed.netloc.lower(),
            parsed.path.rstrip('/') if parsed.path != '/' else '/',
            parsed.params,
            parsed.query,
            ''  # Remove fragment
        ))
        return normalized
    
    def resolve_final_url(self, url):
        """Resolve URL to its final destination after redirects"""
        try:
            # Use HEAD request to check redirects without downloading content
            response = self.session.head(url, timeout=5, allow_redirects=True)
            return response.url
        except:
            # If HEAD fails, return original URL
            return url
    
    def deduplicate_urls(self, urls):
        """Remove duplicate URLs that resolve to the same final destination"""
        url_mapping = {}  # final_url -> original_url
        unique_urls = []
        redirect_map = {}  # original_url -> final_url
        
        print(f"   🔄 Resolving redirects for {len(urls)} URLs...")
        
        # First pass: prefer HTTPS URLs over HTTP equivalents
        https_urls = set()
        filtered_urls = []
        
        for url in urls:
            if url.startswith('https://'):
                https_urls.add(url)
                filtered_urls.append(url)
            elif url.startswith('http://'):
                https_equivalent = url.replace('http://', 'https://')
                if https_equivalent not in https_urls:
                    filtered_urls.append(url)
                else:
                    print(f"   🔒 Skipping HTTP URL (HTTPS exists): {url}")
        
        print(f"   🔒 After HTTPS preference: {len(filtered_urls)} URLs")
        
        # Second pass: resolve redirects for remaining URLs
        for url in filtered_urls:
            try:
                final_url = self.resolve_final_url(url)
                final_normalized = self.normalize_url(final_url)
                redirect_map[url] = final_url
                
                if final_normalized not in url_mapping:
                    url_mapping[final_normalized] = url
                    unique_urls.append(url)
                else:
                    # Track that this URL redirects to an existing final URL
                    print(f"   ↪️  Skipping duplicate: {url} → {final_normalized}")
            except Exception as e:
                # If resolution fails, include the URL anyway
                unique_urls.append(url)
                redirect_map[url] = url
        
        print(f"   ✅ Reduced from {len(urls)} to {len(unique_urls)} unique URLs")
        
        # Store redirect mapping for later use
        self.redirect_map = redirect_map
        return unique_urls
    
    def check_and_parse_sitemap(self, base_url, domain, crawled, to_crawl, depth_map):
        """Check for and parse XML sitemaps comprehensively"""
        print(f"   🗺️  Checking for sitemaps...")
        
        # Common sitemap locations
        sitemap_urls = [
            urljoin(base_url, '/sitemap.xml'),
            urljoin(base_url, '/sitemap_index.xml'),
            urljoin(base_url, '/sitemap-index.xml'),
            urljoin(base_url, '/sitemaps.xml'),
            urljoin(base_url, '/sitemap1.xml'),
            urljoin(base_url, '/wp-sitemap.xml'),  # WordPress
            urljoin(base_url, '/post-sitemap.xml'),  # WordPress
            urljoin(base_url, '/page-sitemap.xml'),  # WordPress
        ]
        
        # First check robots.txt for sitemap references
        self.check_robots_txt_for_sitemaps(base_url, sitemap_urls)
        
        total_sitemap_urls = 0
        for sitemap_url in sitemap_urls:
            try:
                response = self.session.get(sitemap_url, timeout=self.request_timeout)
                if response.status_code == 200 and 'xml' in response.headers.get('content-type', ''):
                    soup = BeautifulSoup(response.content, 'xml')
                    
                    # Parse sitemap URLs
                    urls = soup.find_all('url')
                    sitemap_count = 0
                    
                    for url_tag in urls:
                        loc = url_tag.find('loc')
                        if loc and loc.text:
                            full_url = loc.text.strip()
                            normalized_url = self.normalize_url(full_url)
                            
                            if (self.is_internal_url(normalized_url, domain) and 
                                normalized_url not in crawled and
                                self.is_valid_page_url(normalized_url)):
                                to_crawl.append(normalized_url)
                                depth_map[normalized_url] = 1  # Sitemap URLs are depth 1
                                sitemap_count += 1
                    
                    if sitemap_count > 0:
                        total_sitemap_urls += sitemap_count
                        print(f"      ✅ Found {sitemap_count} URLs in {sitemap_url}")
                        
            except:
                continue
        
        if total_sitemap_urls > 0:
            print(f"   🗺️  Total sitemap URLs added: {total_sitemap_urls}")
    
    def check_robots_txt_for_sitemaps(self, base_url, sitemap_urls):
        """Parse robots.txt for additional sitemap references"""
        try:
            robots_url = urljoin(base_url, '/robots.txt')
            response = self.session.get(robots_url, timeout=self.request_timeout)
            if response.status_code == 200:
                robots_content = response.text
                
                # Look for sitemap references
                for line in robots_content.split('\n'):
                    line = line.strip()
                    if line.lower().startswith('sitemap:'):
                        sitemap_url = line.split(':', 1)[1].strip()
                        if sitemap_url not in sitemap_urls:
                            sitemap_urls.append(sitemap_url)
                            print(f"      🤖 Found sitemap in robots.txt: {sitemap_url}")
        except:
            pass
    
    def is_internal_url(self, url, domain):
        """Check if URL is internal"""
        parsed = urlparse(url)
        url_domain = parsed.netloc.replace('www.', '')
        return url_domain == domain
    
    def is_valid_page_url(self, url):
        """Check if URL is a valid page to analyze (more comprehensive filtering)"""
        url_lower = url.lower()
        
        # Skip URLs with query parameters
        if '?' in url:
            return False
        
        # Skip fragments
        if '#' in url:
            return False
            
        # Skip non-web protocols
        excluded_protocols = ['javascript:', 'mailto:', 'tel:', 'ftp:', 'file:']
        if any(url_lower.startswith(proto) for proto in excluded_protocols):
            return False
        
        # Skip file extensions that aren't web pages
        excluded_extensions = [
            '.jpg', '.jpeg', '.png', '.gif', '.svg', '.webp',  # Images
            '.pdf', '.doc', '.docx', '.xls', '.xlsx', '.ppt', '.pptx',  # Documents
            '.zip', '.rar', '.tar', '.gz',  # Archives
            '.css', '.js', '.xml', '.json',  # Web assets
            '.mp4', '.avi', '.mov', '.wmv', '.mp3', '.wav'  # Media
        ]
        if any(url_lower.endswith(ext) for ext in excluded_extensions):
            return False
        
        # Skip common non-content paths
        excluded_paths = [
            '/wp-admin/', '/admin/', '/wp-content/', '/wp-includes/',
            '/feed/', '/rss/', '/api/', '/ajax/',
            '/checkout/', '/cart/', '/account/', '/login/', '/register/',
            '?add-to-cart=', '?orderby=', '?filter=', '?s='
        ]
        if any(path in url_lower for path in excluded_paths):
            return False
        
        return True
    
    def check_https_availability(self, domain):
        """Check if HTTPS is available for the domain"""
        try:
            https_url = f"https://{domain}"
            response = self.session.head(https_url, timeout=5)
            return response.status_code < 400
        except:
            return False
    
    def filter_http_urls_if_https_available(self, urls, domain):
        """Remove HTTP URLs if HTTPS is available for the domain"""
        # Check if HTTPS is available
        if not hasattr(self, '_https_available'):
            self._https_available = self.check_https_availability(domain)
        
        if not self._https_available:
            return urls  # Keep all URLs if HTTPS not available
        
        # Filter out HTTP URLs when HTTPS is available
        filtered_urls = []
        http_urls_removed = 0
        
        for url in urls:
            if url.startswith('http://'):
                # Convert to HTTPS equivalent to check if it would be the same
                https_equivalent = url.replace('http://', 'https://')
                if https_equivalent in urls:
                    # Skip this HTTP URL since HTTPS version exists
                    http_urls_removed += 1
                    continue
                else:
                    # Keep HTTP URL but note it will redirect to HTTPS
                    filtered_urls.append(url)
            else:
                filtered_urls.append(url)
        
        if http_urls_removed > 0:
            print(f"   🔒 Filtered out {http_urls_removed} HTTP URLs (HTTPS available)")
        
        return filtered_urls
    
    def analyze_pages_parallel(self, urls, domain):
        """Analyze multiple pages in parallel for speed"""
        analyzed_pages = []
        
        with ThreadPoolExecutor(max_workers=self.max_workers) as executor:
            # Submit all tasks
            future_to_url = {executor.submit(self.analyze_page, url, domain): url for url in urls}
            
            # Process results as they complete
            completed = 0
            for future in as_completed(future_to_url):
                completed += 1
                url = future_to_url[future]
                
                # Progress update every 20 pages
                if completed % 20 == 0 or completed == len(urls):
                    elapsed = time.time() - self.crawl_stats['start_time']
                    print(f"   ⚡ Progress: {completed}/{len(urls)} pages ({elapsed:.1f}s, {completed/elapsed:.1f} pages/sec)")
                
                try:
                    page_data = future.result()
                    if page_data:
                        analyzed_pages.append(page_data)
                        with self.stats_lock:
                            self.crawl_stats['pages_analyzed'] += 1
                    else:
                        with self.stats_lock:
                            self.crawl_stats['pages_skipped'] += 1
                except Exception as e:
                    with self.stats_lock:
                        self.crawl_stats['pages_skipped'] += 1
                    self.failed_pages.append(url)
        
        return analyzed_pages
    
    def analyze_page(self, url, domain):
        """Analyze a single page with comprehensive content extraction and technical SEO checks"""
        try:
            response = self.session.get(url, timeout=self.request_timeout, allow_redirects=True)
            
            # Track redirects and detect issues
            redirect_chain = []
            original_url = url
            
            if response.history:
                for resp in response.history:
                    redirect_chain.append({
                        'url': resp.url,
                        'status_code': resp.status_code,
                        'location': resp.headers.get('location', ''),
                        'redirect_type': 'permanent' if resp.status_code == 301 else 'temporary'
                    })
                redirect_chain.append({
                    'url': response.url,
                    'status_code': response.status_code,
                    'location': '',
                    'redirect_type': 'final'
                })
            
            # Check for redirect loops (more than 5 redirects is suspicious)
            if len(redirect_chain) > 5:
                return {
                    'url': original_url,
                    'final_url': response.url,
                    'status_code': response.status_code,
                    'redirect_chain': redirect_chain,
                    'error': f"Redirect loop detected ({len(redirect_chain)} redirects)",
                    'has_redirect_loop': True
                }
            
            if response.status_code != 200:
                return {
                    'url': url,
                    'status_code': response.status_code,
                    'redirect_chain': redirect_chain,
                    'error': f"HTTP {response.status_code}"
                }
                
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # Extract body text for content analysis
            body_text = self.extract_body_text(soup)
            
            # Get all heading tags
            h1_tags = soup.find_all('h1')
            h2_tags = soup.find_all('h2')
            h3_tags = soup.find_all('h3')
            
            # Enhanced image analysis with performance metrics
            images = soup.find_all('img')
            image_data = []
            images_without_dimensions = 0
            large_images = []
            unoptimized_formats = []
            
            for img in images:
                src = img.get('src', '')
                width = img.get('width')
                height = img.get('height')
                loading = img.get('loading', '')
                
                # Check for explicit dimensions
                if not width or not height:
                    images_without_dimensions += 1
                
                # Check for modern formats and optimization
                if src:
                    if any(ext in src.lower() for ext in ['.jpg', '.jpeg', '.png', '.gif']):
                        if not any(ext in src.lower() for ext in ['.webp', '.avif']):
                            unoptimized_formats.append(src)
                
                image_data.append({
                    'src': src,
                    'alt': img.get('alt', ''),
                    'title': img.get('title', ''),
                    'has_alt': bool(img.get('alt')),
                    'has_dimensions': bool(width and height),
                    'loading': loading,
                    'lazy_loading': loading == 'lazy'
                })
            
            # Link analysis
            internal_links = self.get_internal_links(soup, domain)
            external_links = self.get_external_links(soup, domain)
            
            # Technical SEO analysis
            canonical_tag = soup.find('link', rel='canonical')
            canonical_url = canonical_tag.get('href') if canonical_tag else None
            
            # Check for structured data
            structured_data = []
            json_ld_scripts = soup.find_all('script', type='application/ld+json')
            for script in json_ld_scripts:
                try:
                    data = json.loads(script.string)
                    structured_data.append(data)
                except:
                    pass
            
            # Check for meta robots
            meta_robots = soup.find('meta', attrs={'name': 'robots'})
            robots_content = meta_robots.get('content', '') if meta_robots else ''
            
            # Security checks
            is_https = url.startswith('https://')
            mixed_content_images = []
            if is_https:
                for img in images:
                    src = img.get('src', '')
                    if src.startswith('http://'):
                        mixed_content_images.append(src)
            
            # Performance Analysis
            performance_data = self.analyze_page_performance(soup, response, url)
            
            page_data = {
                'url': url,
                'final_url': response.url,
                'status_code': response.status_code,
                'redirect_chain': redirect_chain,
                'has_redirects': len(redirect_chain) > 0,
                'redirect_count': len(redirect_chain),
                
                # Basic SEO elements
                'title': self.get_title(soup),
                'meta_description': self.get_meta_description(soup),
                'body_text': body_text,
                'word_count': len(body_text.split()) if body_text else 0,
                'body_text_length': len(body_text) if body_text else 0,
                
                # Heading analysis
                'h1_count': len(h1_tags),
                'h1_text': [h1.get_text().strip() for h1 in h1_tags],
                'h2_count': len(h2_tags),
                'h3_count': len(h3_tags),
                'total_headings': len(h1_tags) + len(h2_tags) + len(h3_tags),
                
                # Link analysis
                'internal_links': len(internal_links),
                'external_links': len(external_links),
                'internal_link_data': internal_links[:10],
                'external_link_data': external_links[:10],
                
                # Enhanced image analysis
                'images': len(images),
                'images_without_alt': len([img for img in image_data if not img['has_alt']]),
                'images_without_dimensions': images_without_dimensions,
                'images_with_lazy_loading': len([img for img in image_data if img['lazy_loading']]),
                'unoptimized_image_formats': len(unoptimized_formats),
                'image_data': image_data,
                'mixed_content_images': mixed_content_images,
                'has_mixed_content': len(mixed_content_images) > 0,
                
                # Technical SEO elements
                'canonical_url': canonical_url,
                'has_canonical': bool(canonical_url),
                'canonical_is_self': canonical_url == response.url if canonical_url else False,
                'meta_robots': robots_content,
                'is_noindex': 'noindex' in robots_content.lower(),
                'is_nofollow': 'nofollow' in robots_content.lower(),
                
                # Structured data
                'structured_data': structured_data,
                'has_schema': len(structured_data) > 0,
                'schema_types': [data.get('@type', '') for data in structured_data if isinstance(data, dict)],
                
                # Technical elements
                'has_viewport': bool(soup.find('meta', attrs={'name': 'viewport'})),
                'has_charset': bool(soup.find('meta', attrs={'charset': True})) or bool(soup.find('meta', attrs={'http-equiv': 'Content-Type'})),
                'has_doctype': response.content.startswith(b'<!DOCTYPE'),
                'is_https': is_https,
                
                # Content quality metrics
                'page_type': self.detect_page_type(url),
                'content_ratio': self.calculate_text_html_ratio(body_text, str(soup)) if body_text else 0,
                
                # Response details
                'response_time': response.elapsed.total_seconds(),
                'content_length': len(response.content),
                'content_type': response.headers.get('content-type', ''),
                
                # Performance data
                'performance': performance_data,
            }
            
            # Advanced content quality analysis
            page_data['content_quality'] = self.analyze_content_quality(body_text, soup)
            
            # Mobile-first indexing checks
            page_data['mobile_optimization'] = self.analyze_mobile_optimization(soup, response)
            
            # Enhanced schema markup analysis
            page_data['advanced_schema'] = self.analyze_advanced_schema_markup(structured_data, soup)
            
            return page_data
            
        except Exception as e:
            return {
                'url': url,
                'error': str(e),
                'status_code': None
            }
    
    def analyze_content_quality(self, body_text, soup):
        """Analyze content quality using advanced metrics"""
        if not body_text or len(body_text.strip()) < 50:
            return {
                'score': 0,
                'readability_score': 0,
                'grade_level': 0,
                'issues': ['Content too short for analysis'],
                'recommendations': ['Add more substantial content (minimum 300 words recommended)']
            }
        
        try:
            # Readability analysis
            readability_score = flesch_reading_ease(body_text)
            grade_level = flesch_kincaid_grade(body_text)
            
            # Content structure analysis
            paragraphs = soup.find_all('p')
            lists = soup.find_all(['ul', 'ol'])
            headings = soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])
            
            # Calculate content quality score
            quality_factors = {
                'word_count': min(len(body_text.split()) / 300, 1.0) * 20,  # Up to 20 points
                'readability': min(readability_score / 60, 1.0) * 20,  # Up to 20 points
                'structure': min(len(headings) / 5, 1.0) * 15,  # Up to 15 points
                'paragraphs': min(len(paragraphs) / 3, 1.0) * 15,  # Up to 15 points
                'lists': min(len(lists) / 2, 1.0) * 10,  # Up to 10 points
                'sentence_variety': self.analyze_sentence_variety(body_text) * 20  # Up to 20 points
            }
            
            total_score = sum(quality_factors.values())
            
            # Generate recommendations
            recommendations = []
            issues = []
            
            if quality_factors['word_count'] < 15:
                issues.append('Content length below recommended minimum')
                recommendations.append('Expand content to at least 300 words for better SEO value')
            
            if readability_score < 30:
                issues.append('Content may be too difficult to read')
                recommendations.append('Simplify language and sentence structure for better readability')
            elif readability_score > 90:
                issues.append('Content may be too simple')
                recommendations.append('Add more detailed explanations and technical depth')
            
            if len(headings) < 2:
                issues.append('Insufficient heading structure')
                recommendations.append('Add more headings (H2, H3) to improve content structure')
            
            if len(paragraphs) < 3:
                issues.append('Content lacks paragraph structure')
                recommendations.append('Break content into more paragraphs for better readability')
            
            return {
                'score': round(total_score, 1),
                'readability_score': round(readability_score, 1),
                'grade_level': round(grade_level, 1),
                'word_count': len(body_text.split()),
                'paragraph_count': len(paragraphs),
                'heading_count': len(headings),
                'list_count': len(lists),
                'quality_factors': quality_factors,
                'issues': issues,
                'recommendations': recommendations
            }
            
        except Exception as e:
            return {
                'score': 0,
                'error': f'Content analysis failed: {str(e)}',
                'issues': ['Content analysis unavailable'],
                'recommendations': ['Manual content review recommended']
            }
    
    def analyze_sentence_variety(self, text):
        """Analyze sentence length variety for content quality scoring"""
        sentences = re.split(r'[.!?]+', text)
        if len(sentences) < 3:
            return 0.5
        
        sentence_lengths = [len(s.split()) for s in sentences if s.strip()]
        if not sentence_lengths:
            return 0.5
        
        # Calculate coefficient of variation (std dev / mean)
        mean_length = statistics.mean(sentence_lengths)
        if mean_length == 0:
            return 0.5
        
        std_dev = statistics.stdev(sentence_lengths) if len(sentence_lengths) > 1 else 0
        variety_score = min(std_dev / mean_length, 1.0)
        
        return variety_score
    
    def analyze_mobile_optimization(self, soup, response):
        """Analyze mobile-first indexing optimization"""
        mobile_issues = []
        mobile_score = 100
        
        # Viewport meta tag analysis
        viewport_tag = soup.find('meta', attrs={'name': 'viewport'})
        if not viewport_tag:
            mobile_issues.append('Missing viewport meta tag')
            mobile_score -= 20
        else:
            viewport_content = viewport_tag.get('content', '').lower()
            if 'width=device-width' not in viewport_content:
                mobile_issues.append('Viewport not set to device width')
                mobile_score -= 10
            if 'initial-scale=1' not in viewport_content:
                mobile_issues.append('Initial scale not set to 1')
                mobile_score -= 5
        
        # Touch target analysis
        buttons = soup.find_all(['button', 'a', 'input'])
        small_touch_targets = 0
        for button in buttons:
            style = button.get('style', '')
            if 'font-size' in style:
                try:
                    font_size = re.search(r'font-size:\s*(\d+)', style)
                    if font_size and int(font_size.group(1)) < 16:
                        small_touch_targets += 1
                except:
                    pass
        
        if small_touch_targets > 0:
            mobile_issues.append(f'{small_touch_targets} potentially small touch targets detected')
            mobile_score -= min(small_touch_targets * 2, 15)
        
        # Font size analysis
        body_tag = soup.find('body')
        if body_tag:
            style = body_tag.get('style', '')
            if 'font-size' in style:
                try:
                    font_size = re.search(r'font-size:\s*(\d+)', style)
                    if font_size and int(font_size.group(1)) < 16:
                        mobile_issues.append('Base font size may be too small for mobile')
                        mobile_score -= 10
                except:
                    pass
        
        # Check for mobile-specific CSS
        css_links = soup.find_all('link', rel='stylesheet')
        has_responsive_css = False
        for link in css_links:
            media = link.get('media', '')
            if any(keyword in media.lower() for keyword in ['screen', 'max-width', 'min-width']):
                has_responsive_css = True
                break
        
        if not has_responsive_css:
            # Check for inline responsive CSS
            style_tags = soup.find_all('style')
            for style in style_tags:
                if style.string and '@media' in style.string:
                    has_responsive_css = True
                    break
        
        if not has_responsive_css:
            mobile_issues.append('No responsive CSS detected')
            mobile_score -= 15
        
        # Page speed considerations for mobile
        content_size = len(response.content)
        if content_size > 1024 * 1024:  # 1MB
            mobile_issues.append('Page size may be too large for mobile connections')
            mobile_score -= 10
        
        return {
            'score': max(mobile_score, 0),
            'issues': mobile_issues,
            'has_viewport': bool(viewport_tag),
            'has_responsive_css': has_responsive_css,
            'content_size_mb': round(content_size / (1024 * 1024), 2),
            'recommendations': self.generate_mobile_recommendations(mobile_issues)
        }
    
    def generate_mobile_recommendations(self, issues):
        """Generate mobile optimization recommendations"""
        recommendations = []
        
        for issue in issues:
            if 'viewport' in issue.lower():
                recommendations.append('Add <meta name="viewport" content="width=device-width, initial-scale=1"> to <head>')
            elif 'touch target' in issue.lower():
                recommendations.append('Ensure buttons and links are at least 44px in height for better touch accessibility')
            elif 'font size' in issue.lower():
                recommendations.append('Use minimum 16px font size for body text on mobile devices')
            elif 'responsive css' in issue.lower():
                recommendations.append('Implement responsive CSS with media queries for different screen sizes')
            elif 'page size' in issue.lower():
                recommendations.append('Optimize images and minify CSS/JS to reduce page size for mobile users')
        
        return recommendations
    
    def analyze_advanced_schema_markup(self, structured_data, soup):
        """Advanced schema markup analysis"""
        schema_analysis = {
            'total_schemas': len(structured_data),
            'schema_types': [],
            'critical_missing': [],
            'recommendations': [],
            'score': 0
        }
        
        # Analyze existing schema types
        for data in structured_data:
            if isinstance(data, dict):
                schema_type = data.get('@type', 'Unknown')
                schema_analysis['schema_types'].append(schema_type)
        
        # Check for critical schema types based on page content
        page_content = soup.get_text().lower()
        
        # Business/Organization schema
        if any(word in page_content for word in ['contact', 'about', 'company', 'business']):
            if not any('organization' in str(schema).lower() for schema in structured_data):
                schema_analysis['critical_missing'].append('Organization Schema')
                schema_analysis['recommendations'].append('Add Organization schema for business information')
        
        # Product schema for e-commerce
        if any(word in page_content for word in ['price', 'buy', 'product', 'shop', 'cart']):
            if not any('product' in str(schema).lower() for schema in structured_data):
                schema_analysis['critical_missing'].append('Product Schema')
                schema_analysis['recommendations'].append('Add Product schema for e-commerce items')
        
        # Article schema for content
        if any(word in page_content for word in ['article', 'blog', 'news', 'post']):
            if not any('article' in str(schema).lower() for schema in structured_data):
                schema_analysis['critical_missing'].append('Article Schema')
                schema_analysis['recommendations'].append('Add Article schema for content pages')
        
        # FAQ schema
        if any(word in page_content for word in ['faq', 'question', 'answer']):
            if not any('faq' in str(schema).lower() for schema in structured_data):
                schema_analysis['critical_missing'].append('FAQ Schema')
                schema_analysis['recommendations'].append('Add FAQ schema for question/answer content')
        
        # Calculate schema score
        base_score = min(len(structured_data) * 20, 60)  # Up to 60 points for having schemas
        missing_penalty = len(schema_analysis['critical_missing']) * 10  # -10 for each missing critical schema
        schema_analysis['score'] = max(base_score - missing_penalty, 0)
        
        return schema_analysis
    
    def analyze_competitive_landscape(self, domain, page_data):
        """Analyze competitive positioning and benchmarking"""
        competitive_analysis = {
            'domain_authority_indicators': {},
            'content_depth_comparison': {},
            'technical_advantage_areas': [],
            'improvement_opportunities': [],
            'competitive_score': 0
        }
        
        # Analyze domain authority indicators
        total_pages = len(page_data)
        pages_with_schema = sum(1 for page in page_data if page.get('has_schema', False))
        https_pages = sum(1 for page in page_data if page.get('is_https', False))
        pages_with_canonical = sum(1 for page in page_data if page.get('has_canonical', False))
        
        competitive_analysis['domain_authority_indicators'] = {
            'total_indexed_pages': total_pages,
            'schema_implementation_rate': (pages_with_schema / total_pages) * 100 if total_pages > 0 else 0,
            'https_adoption_rate': (https_pages / total_pages) * 100 if total_pages > 0 else 0,
            'canonical_implementation_rate': (pages_with_canonical / total_pages) * 100 if total_pages > 0 else 0,
            'average_content_length': sum(page.get('word_count', 0) for page in page_data) / total_pages if total_pages > 0 else 0
        }
        
        # Content depth analysis
        content_lengths = [page.get('word_count', 0) for page in page_data if page.get('word_count', 0) > 0]
        if content_lengths:
            competitive_analysis['content_depth_comparison'] = {
                'average_word_count': statistics.mean(content_lengths),
                'median_word_count': statistics.median(content_lengths),
                'content_depth_score': self.calculate_content_depth_score(content_lengths),
                'long_form_content_percentage': (sum(1 for length in content_lengths if length > 1000) / len(content_lengths)) * 100
            }
        else:
            competitive_analysis['content_depth_comparison'] = {
                'average_word_count': 0,
                'median_word_count': 0,
                'content_depth_score': 0,
                'long_form_content_percentage': 0
            }
        
        # Technical advantage areas
        if competitive_analysis['domain_authority_indicators']['schema_implementation_rate'] > 70:
            competitive_analysis['technical_advantage_areas'].append('Strong structured data implementation')
        
        if competitive_analysis['domain_authority_indicators']['https_adoption_rate'] > 95:
            competitive_analysis['technical_advantage_areas'].append('Excellent HTTPS security coverage')
        
        if competitive_analysis['content_depth_comparison'].get('average_word_count', 0) > 800:
            competitive_analysis['technical_advantage_areas'].append('Above-average content depth')
        
        # Mobile optimization analysis
        mobile_scores = [page.get('mobile_optimization', {}).get('score', 0) for page in page_data if 'mobile_optimization' in page]
        if mobile_scores and statistics.mean(mobile_scores) > 85:
            competitive_analysis['technical_advantage_areas'].append('Strong mobile optimization')
        
        # Improvement opportunities
        if competitive_analysis['domain_authority_indicators']['schema_implementation_rate'] < 50:
            competitive_analysis['improvement_opportunities'].append('Implement structured data across more pages')
        
        if competitive_analysis['content_depth_comparison'].get('long_form_content_percentage', 0) < 30:
            competitive_analysis['improvement_opportunities'].append('Develop more comprehensive, long-form content')
        
        if mobile_scores and statistics.mean(mobile_scores) < 70:
            competitive_analysis['improvement_opportunities'].append('Improve mobile user experience')
        
        # Calculate competitive score
        score_factors = [
            competitive_analysis['domain_authority_indicators']['schema_implementation_rate'] * 0.2,
            competitive_analysis['domain_authority_indicators']['https_adoption_rate'] * 0.15,
            competitive_analysis['domain_authority_indicators']['canonical_implementation_rate'] * 0.15,
            min(competitive_analysis['content_depth_comparison'].get('content_depth_score', 0), 100) * 0.25,
            (statistics.mean(mobile_scores) if mobile_scores else 0) * 0.25
        ]
        
        competitive_analysis['competitive_score'] = sum(score_factors)
        
        return competitive_analysis
    
    def calculate_content_depth_score(self, content_lengths):
        """Calculate content depth score based on word count distribution"""
        if not content_lengths:
            return 0
        
        # Score based on content length distribution
        excellent_content = sum(1 for length in content_lengths if length > 1500)  # 40 points max
        good_content = sum(1 for length in content_lengths if 800 <= length <= 1500)  # 30 points max
        adequate_content = sum(1 for length in content_lengths if 300 <= length < 800)  # 20 points max
        thin_content = sum(1 for length in content_lengths if length < 300)  # -10 points
        
        total_pages = len(content_lengths)
        
        score = (
            (excellent_content / total_pages) * 40 +
            (good_content / total_pages) * 30 +
            (adequate_content / total_pages) * 20 -
            (thin_content / total_pages) * 10
        )
        
        return max(0, min(100, score))
    
    def extract_body_text(self, soup):
        """Extract clean body text content for analysis"""
        # Create a copy to avoid modifying the original
        soup_copy = BeautifulSoup(str(soup), 'html.parser')
        
        # Remove script, style, and navigation elements
        for element in soup_copy(["script", "style", "nav", "footer", "header", "aside", "noscript"]):
            element.decompose()
        
        # Remove common non-content elements
        for element in soup_copy.find_all(['div'], class_=lambda x: x and any(cls in str(x).lower() for cls in ['nav', 'menu', 'sidebar', 'widget', 'footer', 'header'])):
            element.decompose()
        
        # Get body content
        body = soup_copy.find('body')
        if body:
            text = body.get_text(separator=' ', strip=True)
        else:
            text = soup_copy.get_text(separator=' ', strip=True)
        
        # Clean up text - remove extra whitespace and common navigation text
        import re
        text = re.sub(r'\s+', ' ', text).strip()
        
        # Remove common navigation patterns
        nav_patterns = [
            r'Home\s+About\s+Services\s+Contact',
            r'Skip to content',
            r'Menu\s+Toggle',
            r'Search for:',
            r'Copyright.*?All rights reserved',
        ]
        
        for pattern in nav_patterns:
            text = re.sub(pattern, '', text, flags=re.IGNORECASE)
        
        # Clean up again after pattern removal
        text = re.sub(r'\s+', ' ', text).strip()
        
        return text
    
    def calculate_text_html_ratio(self, text, html):
        """Calculate text to HTML ratio"""
        if not text or not html:
            return 0
        text_length = len(text)
        html_length = len(html)
        return round((text_length / html_length) * 100, 2) if html_length > 0 else 0
    
    def get_internal_links(self, soup, domain):
        """Get detailed internal link data"""
        internal_links = []
        for link in soup.find_all('a', href=True):
            href = link['href']
            if href.startswith('/') or domain in href:
                anchor_text = link.get_text().strip()
                internal_links.append({
                    'url': href,
                    'anchor_text': anchor_text,
                    'has_anchor_text': bool(anchor_text),
                    'is_descriptive': len(anchor_text) > 3 and not any(x in anchor_text.lower() for x in ['click here', 'read more', 'here', 'more'])
                })
        return internal_links
    
    def get_external_links(self, soup, domain):
        """Get detailed external link data"""
        external_links = []
        for link in soup.find_all('a', href=True):
            href = link['href']
            if href.startswith('http') and domain not in href:
                anchor_text = link.get_text().strip()
                external_links.append({
                    'url': href,
                    'anchor_text': anchor_text,
                    'has_anchor_text': bool(anchor_text),
                    'has_nofollow': 'nofollow' in link.get('rel', []),
                    'is_descriptive': len(anchor_text) > 3 and not any(x in anchor_text.lower() for x in ['click here', 'read more', 'here', 'more'])
                })
        return external_links

    def get_title(self, soup):
        """Extract page title"""
        title_tag = soup.find('title')
        return title_tag.get_text().strip() if title_tag else ''
    
    def get_meta_description(self, soup):
        """Extract meta description"""
        meta_desc = soup.find('meta', attrs={'name': 'description'})
        return meta_desc.get('content', '') if meta_desc else ''
    
    def detect_page_type(self, url):
        """Detect page type from URL"""
        url_lower = url.lower()
        if url_lower.endswith('/') and url_lower.count('/') <= 3:
            return 'homepage'
        elif any(k in url_lower for k in ['product', 'item']):
            return 'product'
        elif any(k in url_lower for k in ['blog', 'post', 'article']):
            return 'blog'
        elif any(k in url_lower for k in ['about', 'contact', 'services']):
            return 'informational'
        elif any(k in url_lower for k in ['category', 'collection']):
            return 'category'
        else:
            return 'content'
    
    def compile_site_analysis(self, url, domain, page_data):
        """Compile comprehensive analysis"""
        if not page_data:
            return {'error': 'No pages could be analyzed'}
        
        analysis = {
            'url': url,
            'domain': domain,
            'crawl_date': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'total_pages_analyzed': len(page_data),
            'pages_failed': len(self.failed_pages),
            'success_rate': round((len(page_data) / (len(page_data) + len(self.failed_pages))) * 100, 1),
            
            # Aggregate metrics
            'total_word_count': sum(p.get('word_count', 0) for p in page_data),
            'avg_word_count': round(sum(p.get('word_count', 0) for p in page_data) / len(page_data)) if page_data else 0,
            'total_internal_links': sum(p.get('internal_links', 0) for p in page_data),
            'total_external_links': sum(p.get('external_links', 0) for p in page_data),
            'total_images': sum(p.get('images', 0) for p in page_data),
            'images_without_alt': sum(p.get('images_without_alt', 0) for p in page_data),
            'pages_with_schema': len([p for p in page_data if p.get('has_schema', False)]),
            
            # SEO Issues
            'seo_issues': {
                'missing_titles': len([p for p in page_data if not p.get('title', '')]),
                'missing_descriptions': len([p for p in page_data if not p.get('meta_description', '')]),
                'duplicate_titles': len(page_data) - len(set(p.get('title', '') for p in page_data if p.get('title', ''))),
                'pages_no_h1': len([p for p in page_data if p.get('h1_count', 0) == 0]),
                'pages_multiple_h1': len([p for p in page_data if p.get('h1_count', 0) > 1]),
                'thin_content_pages': len([p for p in page_data if p.get('word_count', 0) < 300]),
            },
            
            # Redirect Analysis
            'redirect_analysis': {
                'pages_with_redirects': len([p for p in page_data if p.get('has_redirects', False)]),
                'total_redirects': sum(p.get('redirect_count', 0) for p in page_data),
                'redirect_loops': len([p for p in page_data if p.get('has_redirect_loop', False)]),
                'temporary_redirects': len([p for p in page_data if any(r.get('redirect_type') == 'temporary' for r in p.get('redirect_chain', []))]),
                'permanent_redirects': len([p for p in page_data if any(r.get('redirect_type') == 'permanent' for r in p.get('redirect_chain', []))]),
                'redirect_chains': [p for p in page_data if p.get('redirect_count', 0) > 1][:10],  # Sample of redirect chains
            },
            
            # Page types
            'page_types': dict(Counter(p.get('page_type', 'Unknown') for p in page_data)),
            
            # Sample issues
            'sample_issues': {
                'missing_titles': [p.get('url', '') for p in page_data if not p.get('title', '')][:5],
                'thin_content': [p.get('url', '') for p in page_data if p.get('word_count', 0) < 300][:5],
                'missing_descriptions': [p.get('url', '') for p in page_data if not p.get('meta_description', '')][:5],
            }
        }
        
        # Generate recommendations
        analysis['recommendations'] = self.generate_recommendations(analysis)
        analysis['top_issues'] = self.identify_top_issues(analysis)
        
        # Store page data for detailed report generation
        self._last_page_data = page_data
        
        # Advanced competitive analysis
        analysis['competitive_analysis'] = self.analyze_competitive_landscape(domain, page_data)
        
        return analysis
    
    def identify_top_issues(self, analysis):
        """Identify top issues"""
        issues = []
        seo = analysis['seo_issues']
        total = analysis['total_pages_analyzed']
        
        if seo['missing_titles'] > 0:
            issues.append(f"{seo['missing_titles']} pages missing titles ({round(seo['missing_titles']/total*100, 1)}%)")
        
        if seo['missing_descriptions'] > 0:
            issues.append(f"{seo['missing_descriptions']} pages missing meta descriptions ({round(seo['missing_descriptions']/total*100, 1)}%)")
        
        if seo['thin_content_pages'] > 0:
            issues.append(f"{seo['thin_content_pages']} pages with thin content ({round(seo['thin_content_pages']/total*100, 1)}%)")
        
        if analysis['images_without_alt'] > 0:
            issues.append(f"{analysis['images_without_alt']} images missing alt text")
        
        if seo['duplicate_titles'] > 0:
            issues.append(f"{seo['duplicate_titles']} duplicate page titles")
        
        return issues[:5]
    
    def generate_recommendations(self, analysis):
        """Generate comprehensive recommendations"""
        recommendations = []
        seo = analysis['seo_issues']
        
        # Critical issues
        if seo['missing_titles'] > 0:
            recommendations.append(f"🚨 CRITICAL: Add titles to {seo['missing_titles']} pages")
        
        if seo['missing_descriptions'] > 0:
            recommendations.append(f"🚨 CRITICAL: Add meta descriptions to {seo['missing_descriptions']} pages")
        
        # High priority
        if seo['thin_content_pages'] > analysis['total_pages_analyzed'] * 0.3:
            recommendations.append(f"⚠️ HIGH: Expand content on {seo['thin_content_pages']} thin pages")
        
        if analysis['images_without_alt'] > 10:
            recommendations.append(f"⚠️ HIGH: Add alt text to {analysis['images_without_alt']} images")
        
        # Medium priority
        if seo['duplicate_titles'] > 0:
            recommendations.append(f"📝 MEDIUM: Fix {seo['duplicate_titles']} duplicate titles")
        
        if analysis['pages_with_schema'] < analysis['total_pages_analyzed'] * 0.5:
            recommendations.append(f"📝 MEDIUM: Add schema markup to more pages")
        
        return recommendations
    
    def generate_comprehensive_markdown(self, analysis):
        """Generate comprehensive professional SEO audit report matching industry standards"""
        domain = analysis['domain']  
        date_timestamp = datetime.now().strftime('%Y-%m-%d %H%M%S')
        filename = f"{date_timestamp} - {domain}.md"
        filepath = os.path.join(self.seo_audits_folder, filename)
        
        # Extract page data for detailed analysis
        page_data = getattr(self, '_last_page_data', [])
        
        # Calculate detailed metrics
        duplicate_titles = {}
        duplicate_metas = {}
        long_titles = []
        long_metas = []
        missing_titles = []
        missing_metas = []
        missing_h1 = []
        multiple_h1 = []
        images_without_alt_pages = []
        images_without_alt_files = {}  # Track unique image files missing alt text
        
        for page in page_data:
            url = page.get('url', '')
            title = page.get('title', '')
            meta_desc = page.get('meta_description', '')
            h1_count = page.get('h1_count', 0)
            
            # Title analysis
            if not title:
                missing_titles.append(url)
            else:
                if len(title) > 70:
                    long_titles.append((url, len(title)))
                if title in duplicate_titles:
                    duplicate_titles[title].append(url)
                else:
                    duplicate_titles[title] = [url]
            
            # Meta description analysis  
            if not meta_desc:
                missing_metas.append(url)
            else:
                if len(meta_desc) > 160:
                    long_metas.append((url, len(meta_desc)))
                if meta_desc in duplicate_metas:
                    duplicate_metas[meta_desc].append(url)
                else:
                    duplicate_metas[meta_desc] = [url]
            
            # H1 analysis
            if h1_count == 0:
                missing_h1.append(url)
            elif h1_count > 1:
                multiple_h1.append((url, h1_count))
            
            # Images without alt - track by unique image files
            if page.get('images_without_alt', 0) > 0:
                images_without_alt_pages.append((url, page.get('images_without_alt', 0)))
                
                # Track unique image files missing alt text
                image_data = page.get('image_data', [])
                for img in image_data:
                    if not img.get('has_alt', False):
                        img_src = img.get('src', '')
                        if img_src:
                            # Normalize image URL
                            if img_src.startswith('//'):
                                img_src = 'https:' + img_src
                            elif img_src.startswith('/'):
                                img_src = f"https://{domain}{img_src}"
                            elif not img_src.startswith('http'):
                                img_src = f"https://{domain}/{img_src}"
                            
                            if img_src not in images_without_alt_files:
                                images_without_alt_files[img_src] = {
                                    'pages': [],
                                    'filename': img_src.split('/')[-1] if '/' in img_src else img_src
                                }
                            images_without_alt_files[img_src]['pages'].append(url)
        
        # Remove non-duplicates
        duplicate_titles = {k: v for k, v in duplicate_titles.items() if len(v) > 1 and k}
        duplicate_metas = {k: v for k, v in duplicate_metas.items() if len(v) > 1}
        
        # Store images_without_alt_files for use in report
        self._images_without_alt_files = images_without_alt_files
        
        with open(filepath, 'w', encoding='utf-8') as f:
            # Header in professional format
            f.write(f"# {domain.replace('.', ' ').title()} SEO Audit\n\n")
            
            # Executive Summary with key metrics
            f.write("## 📊 Executive Summary\n\n")
            f.write(f"**Website:** {domain} | **Pages Analyzed:** {len(page_data)} | **Audit Date:** {datetime.now().strftime('%B %d, %Y')}\n\n")
            
            # Quick health score
            total_issues = len(missing_titles) + len(duplicate_titles) + len(missing_metas) + len(missing_h1) + analysis['images_without_alt']
            health_score = max(0, 100 - (total_issues * 2))  # Rough health score
            health_emoji = "🟢" if health_score >= 80 else "🟡" if health_score >= 60 else "🔴"
            
            f.write(f"### {health_emoji} SEO Health Score: {health_score}/100\n\n")
            
            # Key metrics table
            f.write("| Metric | Count | Status |\n")
            f.write("|--------|-------|--------|\n")
            f.write(f"| Pages Crawled | {len(page_data)} | ✅ |\n")
            f.write(f"| Missing Titles | {len(missing_titles)} | {'❌' if missing_titles else '✅'} |\n")
            f.write(f"| Missing Meta Descriptions | {len(missing_metas)} | {'❌' if missing_metas else '✅'} |\n")
            f.write(f"| Images Without Alt Text | {analysis['images_without_alt']} | {'❌' if analysis['images_without_alt'] > 0 else '✅'} |\n")
            f.write(f"| Average Word Count | {analysis['avg_word_count']} | {'✅' if analysis['avg_word_count'] > 300 else '⚠️'} |\n\n")
            
            # Priority Action Plan
            f.write("## 🎯 Priority Action Plan\n\n")
            f.write("> **Focus Areas:** Based on the comprehensive analysis, these issues require immediate attention to improve search engine visibility and user experience.\n\n")
            
            # Calculate priority issues for the action plan
            critical_issues = []
            if missing_titles:
                critical_issues.append(f"**Missing Title Tags:** {len(missing_titles)} pages require immediate title optimization")
            if duplicate_titles:
                critical_issues.append(f"**Duplicate Title Tags:** {sum(len(urls) for urls in duplicate_titles.values())} pages competing against each other")
            if self.robots_txt_data and self.robots_txt_data.get('issues'):
                critical_issues.append(f"**Robots.txt Issues:** {len(self.robots_txt_data['issues'])} critical crawling problems")
            if self.security_issues and self.security_issues.get('issues'):
                critical_issues.append(f"**Security Issues:** {len(self.security_issues['issues'])} HTTPS/security problems")
            
            high_priority = []
            if missing_metas:
                high_priority.append(f"**Missing Meta Descriptions:** {len(missing_metas)} pages missing click-through optimization")
            if duplicate_metas:
                high_priority.append(f"**Duplicate Meta Descriptions:** {sum(len(urls) for urls in duplicate_metas.values())} pages with identical descriptions")
            if analysis['seo_issues']['thin_content_pages'] > 0:
                high_priority.append(f"**Thin Content:** {analysis['seo_issues']['thin_content_pages']} pages need content expansion")
            
            # Count technical issues
            canonical_issues = sum(1 for page in page_data if page.get('has_canonical') == False)
            noindex_pages = sum(1 for page in page_data if page.get('is_noindex'))
            redirect_pages = sum(1 for page in page_data if page.get('has_redirects'))
            mixed_content_pages = sum(1 for page in page_data if page.get('has_mixed_content'))
            
            if canonical_issues > 0:
                high_priority.append(f"**Missing Canonical Tags:** {canonical_issues} pages without canonical tags")
            if noindex_pages > 0:
                high_priority.append(f"**Noindex Pages:** {noindex_pages} pages blocked from indexing")
            if mixed_content_pages > 0:
                high_priority.append(f"**Mixed Content:** {mixed_content_pages} pages with HTTP resources on HTTPS")
            
            medium_priority = []
            if missing_h1:
                medium_priority.append(f"**Missing H1 Tags:** {len(missing_h1)} pages need heading structure")
            if analysis['images_without_alt'] > 0:
                medium_priority.append(f"**Image Accessibility:** {analysis['images_without_alt']} images need alt text")
            if multiple_h1:
                medium_priority.append(f"**Multiple H1 Tags:** {len(multiple_h1)} pages need heading structure fixes")
            if redirect_pages > 0:
                medium_priority.append(f"**Redirect Chains:** {redirect_pages} pages with redirects need optimization")
            
            # Count structured data
            schema_pages = sum(1 for page in page_data if page.get('has_schema'))
            if schema_pages < len(page_data) * 0.5:  # Less than 50% have schema
                medium_priority.append(f"**Structured Data:** Only {schema_pages} pages have schema markup")
            
            # Performance issues
            slow_pages = sum(1 for page in page_data if page.get('performance', {}).get('response_time_ms', 0) > 1000)
            large_pages = sum(1 for page in page_data if page.get('performance', {}).get('page_size', 0) > 1024 * 1024)
            render_blocking_issues = sum(1 for page in page_data 
                                       if any(issue.get('type') in ['render_blocking_css', 'render_blocking_js'] 
                                             for issue in page.get('performance', {}).get('issues', [])))
            
            if slow_pages > 0:
                high_priority.append(f"**Page Speed:** {slow_pages} pages with slow response times")
            if large_pages > 0:
                medium_priority.append(f"**Page Size:** {large_pages} pages over 1MB")
            if render_blocking_issues > 0:
                medium_priority.append(f"**Render Blocking:** {render_blocking_issues} pages with blocking resources")
            
            if critical_issues:
                f.write("### 🚨 Critical Priority (Fix Immediately)\n\n")
                f.write("> ⏰ **Timeline:** Fix within 24-48 hours  \n")
                f.write("> 💥 **Impact:** Directly affecting search rankings\n\n")
                f.write("| Issue | Impact | Action Required |\n")
                f.write("|-------|--------|----------------|\n")
                for issue in critical_issues:
                    issue_text = issue.replace("**", "").replace(":", "")
                    f.write(f"| {issue_text} | 🔴 High | Immediate fix required |\n")
                f.write("\n")
            
            if high_priority:
                f.write("### ⚠️ High Priority (Fix Within 2 Weeks)\n\n")
                f.write("> ⏰ **Timeline:** Fix within 1-2 weeks  \n")
                f.write("> 📈 **Impact:** Significantly affecting performance\n\n")
                f.write("| Issue | Impact | Action Required |\n")
                f.write("|-------|--------|----------------|\n")
                for issue in high_priority:
                    issue_text = issue.replace("**", "").replace(":", "")
                    f.write(f"| {issue_text} | 🟡 Medium | Schedule for next sprint |\n")
                f.write("\n")
            
            if medium_priority:
                f.write("### 📝 Medium Priority (Fix Within 1 Month)\n\n")
                f.write("> ⏰ **Timeline:** Fix within 2-4 weeks  \n")
                f.write("> ✨ **Impact:** Enhancement opportunities\n\n")
                f.write("| Issue | Impact | Action Required |\n")
                f.write("|-------|--------|----------------|\n")
                for issue in medium_priority:
                    issue_text = issue.replace("**", "").replace(":", "")
                    f.write(f"| {issue_text} | 🟢 Low | Plan for future iteration |\n")
                f.write("\n")
            
            # Implementation Timeline
            f.write("## 📅 Implementation Roadmap\n\n")
            f.write("### Phase 1: Foundation (Week 1-2) 🏗️\n\n")
            f.write("**Goal:** Establish SEO fundamentals\n\n")
            f.write("- [ ] Fix all missing and duplicate title tags\n")
            f.write("- [ ] Implement unique meta descriptions\n")
            f.write("- [ ] Address thin content pages\n")
            f.write("- [ ] Resolve critical technical issues\n\n")
            f.write("**Expected Impact:** 📈 15-25% improvement in click-through rates\n\n")
            
            f.write("### Phase 2: Technical Optimization (Week 3-4) ⚙️\n\n")
            f.write("**Goal:** Enhance technical SEO foundation\n\n")
            f.write("- [ ] Add missing H1 tags and fix multiples\n")
            f.write("- [ ] Implement comprehensive image alt text\n")
            f.write("- [ ] Optimize content structure and hierarchy\n")
            f.write("- [ ] Fix canonical tag issues\n\n")
            f.write("**Expected Impact:** 📊 10-20% improvement in search visibility\n\n")
            
            f.write("### Phase 3: Enhancement (Month 2) ✨\n\n")
            f.write("**Goal:** Advanced optimization and monitoring\n\n")
            f.write("- [ ] Implement structured data markup\n")
            f.write("- [ ] Optimize page loading speeds\n")
            f.write("- [ ] Enhance mobile optimization\n")
            f.write("- [ ] Set up comprehensive monitoring\n\n")
            f.write("**Expected Impact:** 🚀 5-15% improvement in overall rankings\n\n")
            
            f.write("### Ongoing: Monitoring & Growth 📈\n\n")
            f.write("- 📊 **Weekly:** Monitor search performance improvements\n")
            f.write("- 🔍 **Monthly:** Conduct follow-up SEO audits\n")
            f.write("- 📝 **Quarterly:** Expand and refine content strategy\n")
            f.write("- 🎯 **Annually:** Comprehensive SEO strategy review\n\n")
            
            # Main analysis starts
            f.write("---\n\n")
            f.write("## 🔍 Detailed Technical SEO Analysis\n\n")
            f.write("> **Note:** This section provides comprehensive technical details for each identified issue. Use this as your implementation guide.\n\n")
            
            # Technical Infrastructure Analysis
            f.write("## 🏗️ Technical Infrastructure\n\n")
            
            # Robots.txt Analysis
            if self.robots_txt_data:
                f.write("### Robots.txt Analysis\n\n")
                f.write(f"**Status:** {'✅ Found' if self.robots_txt_data['exists'] else '❌ Missing'}\n")
                f.write(f"**URL:** {self.robots_txt_data['url']}\n")
                f.write(f"**HTTP Status:** {self.robots_txt_data['status_code']}\n")
                if self.robots_txt_data['exists']:
                    f.write(f"**File Size:** {self.robots_txt_data['size']} bytes\n")
                    if self.robots_txt_data.get('sitemaps'):
                        f.write(f"**Sitemaps Referenced:** {len(self.robots_txt_data['sitemaps'])}\n")
                        for sitemap in self.robots_txt_data['sitemaps']:
                            f.write(f"• {sitemap}\n")
                    else:
                        f.write("**Sitemaps Referenced:** None\n")
                
                if self.robots_txt_data['issues']:
                    f.write("\n**Issues Found:**\n")
                    for issue in self.robots_txt_data['issues']:
                        f.write(f"• {issue}\n")
                f.write("\n")
            
            # Advanced Content Quality Analysis
            f.write("### Content Quality Analysis\n\n")
            
            # Calculate average content quality scores
            content_scores = []
            mobile_scores = []
            schema_scores = []
            
            for page in page_data:
                if 'content_quality' in page:
                    content_scores.append(page['content_quality'].get('score', 0))
                if 'mobile_optimization' in page:
                    mobile_scores.append(page['mobile_optimization'].get('score', 0))
                if 'advanced_schema' in page:
                    schema_scores.append(page['advanced_schema'].get('score', 0))
            
            if content_scores:
                avg_content_score = sum(content_scores) / len(content_scores)
                f.write(f"**Average Content Quality Score:** {avg_content_score:.1f}/100\n")
                
                # Content quality distribution
                excellent = sum(1 for score in content_scores if score >= 80)
                good = sum(1 for score in content_scores if 60 <= score < 80)
                needs_improvement = sum(1 for score in content_scores if score < 60)
                
                f.write(f"• Excellent Content (80+): {excellent} pages\n")
                f.write(f"• Good Content (60-79): {good} pages\n")
                f.write(f"• Needs Improvement (<60): {needs_improvement} pages\n\n")
                
                # Top content issues
                all_content_issues = []
                for page in page_data:
                    if 'content_quality' in page:
                        all_content_issues.extend(page['content_quality'].get('issues', []))
                
                if all_content_issues:
                    issue_counts = Counter(all_content_issues)
                    f.write("**Most Common Content Issues:**\n")
                    for issue, count in issue_counts.most_common(5):
                        f.write(f"• {issue}: {count} pages\n")
                    f.write("\n")
            
            # Mobile-First Indexing Analysis
            f.write("### Mobile-First Indexing Analysis\n\n")
            
            if mobile_scores:
                avg_mobile_score = sum(mobile_scores) / len(mobile_scores)
                f.write(f"**Average Mobile Optimization Score:** {avg_mobile_score:.1f}/100\n")
                
                # Mobile optimization distribution
                mobile_excellent = sum(1 for score in mobile_scores if score >= 90)
                mobile_good = sum(1 for score in mobile_scores if 70 <= score < 90)
                mobile_poor = sum(1 for score in mobile_scores if score < 70)
                
                f.write(f"• Excellent Mobile Optimization (90+): {mobile_excellent} pages\n")
                f.write(f"• Good Mobile Optimization (70-89): {mobile_good} pages\n")
                f.write(f"• Poor Mobile Optimization (<70): {mobile_poor} pages\n\n")
                
                # Top mobile issues
                all_mobile_issues = []
                for page in page_data:
                    if 'mobile_optimization' in page:
                        all_mobile_issues.extend(page['mobile_optimization'].get('issues', []))
                
                if all_mobile_issues:
                    mobile_issue_counts = Counter(all_mobile_issues)
                    f.write("**Most Common Mobile Issues:**\n")
                    for issue, count in mobile_issue_counts.most_common(5):
                        f.write(f"• {issue}: {count} pages\n")
                    f.write("\n")
            
            # Advanced Schema Markup Analysis
            f.write("### Advanced Schema Markup Analysis\n\n")
            
            if schema_scores:
                avg_schema_score = sum(schema_scores) / len(schema_scores)
                f.write(f"**Average Schema Implementation Score:** {avg_schema_score:.1f}/100\n")
                
                # Schema implementation stats
                pages_with_schema = sum(1 for page in page_data if page.get('advanced_schema', {}).get('total_schemas', 0) > 0)
                f.write(f"**Pages with Schema Markup:** {pages_with_schema}/{len(page_data)} ({pages_with_schema/len(page_data)*100:.1f}%)\n")
                
                # Schema types found
                all_schema_types = []
                for page in page_data:
                    if 'advanced_schema' in page:
                        all_schema_types.extend(page['advanced_schema'].get('schema_types', []))
                
                if all_schema_types:
                    schema_type_counts = Counter(all_schema_types)
                    f.write("\n**Schema Types Found:**\n")
                    for schema_type, count in schema_type_counts.most_common(10):
                        f.write(f"• {schema_type}: {count} pages\n")
                
                # Critical missing schema
                all_missing_schema = []
                for page in page_data:
                    if 'advanced_schema' in page:
                        all_missing_schema.extend(page['advanced_schema'].get('critical_missing', []))
                
                if all_missing_schema:
                    missing_schema_counts = Counter(all_missing_schema)
                    f.write("\n**Critical Missing Schema Types:**\n")
                    for schema_type, count in missing_schema_counts.most_common(5):
                        f.write(f"• {schema_type}: {count} pages\n")
                f.write("\n")
            
            # Page Experience Signals Summary
            f.write("### Page Experience Signals Summary\n\n")
            
            # Calculate overall page experience score
            page_experience_factors = []
            
            if mobile_scores:
                page_experience_factors.append(('Mobile Usability', sum(mobile_scores) / len(mobile_scores)))
            
            if content_scores:
                page_experience_factors.append(('Content Quality', sum(content_scores) / len(content_scores)))
            
            # HTTPS usage
            https_pages = sum(1 for page in page_data if page.get('is_https', False))
            https_score = (https_pages / len(page_data)) * 100 if page_data else 0
            page_experience_factors.append(('HTTPS Security', https_score))
            
            # Page speed (inverse of response time)
            response_times = [page.get('response_time', 1) for page in page_data if 'response_time' in page]
            if response_times:
                avg_response_time = sum(response_times) / len(response_times)
                speed_score = max(0, 100 - (avg_response_time * 20))  # Penalize slow pages
                page_experience_factors.append(('Page Speed', speed_score))
            
            if page_experience_factors:
                overall_experience_score = sum(score for _, score in page_experience_factors) / len(page_experience_factors)
                f.write(f"**Overall Page Experience Score:** {overall_experience_score:.1f}/100\n\n")
                
                f.write("**Component Scores:**\n")
                for factor, score in page_experience_factors:
                    status = "✅" if score >= 80 else "⚠️" if score >= 60 else "❌"
                    f.write(f"• {factor}: {score:.1f}/100 {status}\n")
                f.write("\n")
            
            # Competitive Analysis Section
            if 'competitive_analysis' in analysis:
                f.write("### Competitive Positioning Analysis\n\n")
                comp_analysis = analysis['competitive_analysis']
                
                f.write(f"**Overall Competitive Score:** {comp_analysis['competitive_score']:.1f}/100\n\n")
                
                # Domain authority indicators
                f.write("**Domain Authority Indicators:**\n")
                indicators = comp_analysis['domain_authority_indicators']
                f.write(f"• Total Indexed Pages: {indicators['total_indexed_pages']}\n")
                f.write(f"• Schema Implementation: {indicators['schema_implementation_rate']:.1f}%\n")
                f.write(f"• HTTPS Adoption: {indicators['https_adoption_rate']:.1f}%\n")
                f.write(f"• Canonical Implementation: {indicators['canonical_implementation_rate']:.1f}%\n")
                f.write(f"• Average Content Length: {indicators['average_content_length']:.0f} words\n\n")
                
                # Content depth comparison
                if 'content_depth_comparison' in comp_analysis:
                    content_depth = comp_analysis['content_depth_comparison']
                    f.write("**Content Depth Analysis:**\n")
                    f.write(f"• Average Word Count: {content_depth['average_word_count']:.0f} words\n")
                    f.write(f"• Median Word Count: {content_depth['median_word_count']:.0f} words\n")
                    f.write(f"• Content Depth Score: {content_depth['content_depth_score']:.1f}/100\n")
                    f.write(f"• Long-form Content: {content_depth['long_form_content_percentage']:.1f}% (>1000 words)\n\n")
                
                # Technical advantages
                if comp_analysis['technical_advantage_areas']:
                    f.write("**Technical Advantages:**\n")
                    for advantage in comp_analysis['technical_advantage_areas']:
                        f.write(f"• ✅ {advantage}\n")
                    f.write("\n")
                
                # Improvement opportunities
                if comp_analysis['improvement_opportunities']:
                    f.write("**Competitive Improvement Opportunities:**\n")
                    for opportunity in comp_analysis['improvement_opportunities']:
                        f.write(f"• 🎯 {opportunity}\n")
                    f.write("\n")
                
                # Competitive benchmarking insights
                f.write("**Competitive Insights:**\n")
                if comp_analysis['competitive_score'] >= 80:
                    f.write("• 🏆 Your website demonstrates strong technical SEO implementation\n")
                    f.write("• 📈 Well-positioned to compete in search rankings\n")
                elif comp_analysis['competitive_score'] >= 60:
                    f.write("• 📊 Good foundation with room for strategic improvements\n")
                    f.write("• 🎯 Focus on identified opportunities for competitive advantage\n")
                else:
                    f.write("• ⚠️ Significant technical SEO gaps compared to competitive standards\n")
                    f.write("• 🚀 High potential for ranking improvements with proper optimization\n")
                f.write("\n")
            
            # Security Analysis
            if self.security_issues:
                f.write("### HTTPS & Security Analysis\n\n")
                f.write(f"**HTTPS Available:** {'✅ Yes' if self.security_issues['https_available'] else '❌ No'}\n")
                f.write(f"**HTTP Redirects to HTTPS:** {'✅ Yes' if self.security_issues['http_redirects_to_https'] else '❌ No'}\n")
                f.write(f"**Mixed Content Risk:** {'⚠️ Yes' if self.security_issues['mixed_content_risk'] else '✅ No'}\n")
                
                if self.security_issues['issues']:
                    f.write("\n**Security Issues:**\n")
                    for issue in self.security_issues['issues']:
                        f.write(f"• {issue}\n")
                f.write("\n")
            
            # Executive summary with professional insights
            total_pages = analysis['total_pages_analyzed']
            success_rate = analysis['success_rate']
            
            f.write(f"**Comprehensive technical analysis of {total_pages:,} pages** reveals critical areas requiring immediate attention to improve search engine visibility and user experience. This audit identifies key technical SEO issues that may be significantly hindering your website's performance in search results.\n\n")
            
            f.write("**Key Performance Indicators:**\n")
            f.write(f"• **{total_pages:,} pages analyzed** with {success_rate}% crawl success rate\n")
            
            # Calculate percentages for professional reporting
            pages_with_titles = total_pages - analysis['seo_issues']['missing_titles'] 
            pages_with_descriptions = total_pages - analysis['seo_issues']['missing_descriptions']
            pages_with_h1 = total_pages - analysis['seo_issues']['pages_no_h1']
            
            f.write(f"• **{(pages_with_titles/total_pages*100):.1f}% of pages have optimized title tags** ({pages_with_titles:,}/{total_pages:,})\n")
            f.write(f"• **{(pages_with_descriptions/total_pages*100):.1f}% of pages have meta descriptions** ({pages_with_descriptions:,}/{total_pages:,})\n")
            f.write(f"• **{(pages_with_h1/total_pages*100):.1f}% of pages have proper H1 structure** ({pages_with_h1:,}/{total_pages:,})\n")
            
            if analysis['total_images'] > 0:
                alt_compliance = ((analysis['total_images'] - analysis['images_without_alt']) / analysis['total_images']) * 100
                f.write(f"• **{alt_compliance:.1f}% image accessibility compliance** ({analysis['total_images'] - analysis['images_without_alt']:,}/{analysis['total_images']:,} images have alt text)\n")
            
            f.write(f"• **Average content depth: {analysis['avg_word_count']} words per page**\n\n")
            
            # Title Tag Audits Section
            f.write("## 🏷️ Title Tag Audits\n\n")
            
            if missing_titles:
                f.write("### ❌ Title Tags Missing\n\n")
                f.write("A `<title>` tag is a key on-page SEO element. It appears in browsers and search results, and helps both search engines and users understand what your page is about.\n\n")
                f.write("If a page is missing a title, or a `<title>` tag is empty, Google may consider it low quality. In case you promote this page in search results, you will miss chances to rank high and gain a higher click-through rate.\n\n")
                f.write("**How to fix it**\n\n")
                f.write("Ensure that every page on your website has a unique and concise title containing your most important keywords.\n\n")
                f.write("For information on how to create effective titles, please see this Google article. You can also view the On-Page SEO Basics: Meta Descriptions article.\n\n")
                f.write(f"**{len(missing_titles)} pages missing title tags:**\n\n")
                for url in missing_titles:
                    f.write(f"• {url}\n")
                f.write("\n")
            
            if duplicate_titles:
                f.write("### 🔄 Duplicate Title Tags\n\n")
                f.write("Our crawler reports pages that have duplicate title tags only if they are exact matches.\n\n")
                f.write("Duplicate `<title>` tags make it difficult for search engines to determine which of a website's pages is relevant for a specific search query, and which one should be prioritized in search results. Pages with duplicate titles have a lower chance of ranking well and are at risk of being banned.\n\n")
                f.write("Moreover, identical `<title>` tags confuse users as to which webpage they should follow.\n\n")
                f.write("**How to fix it**\n\n")
                f.write("Provide a unique and concise title for each of your pages that contains your most important keywords.\n\n")
                f.write("For information on how to create effective titles, please see this Google article. You can also view the On-Page SEO Basics: Meta Descriptions article.\n\n")
                
                total_duplicate_pages = sum(len(urls) for urls in duplicate_titles.values())
                f.write(f"**{total_duplicate_pages} pages affected by duplicate title tags:**\n\n")
                for title, urls in duplicate_titles.items():
                    f.write(f"**\"{title}\"** appears on {len(urls)} pages:\n")
                    for url in urls:
                        f.write(f"• {url}\n")
                    f.write("\n")
            
            # Meta Description Audits
            f.write("## 📝 Meta Description Audits\n\n")
            
            if missing_metas:
                f.write("### ❌ Missing Meta Descriptions\n\n")
                f.write("Though meta descriptions don't have a direct influence on rankings, they are used by search engines to display your page's description in search results. A good description helps users know what your page is about and encourages them to click on it.\n\n")
                f.write("If your page's meta description tag is missing, search engines will usually display its first sentence, which may be irrelevant and unappealing to users.\n\n")
                f.write("For more information, please see these articles: Create good titles and snippets in Search Results and On-Page SEO Basics: Meta Descriptions\n\n")
                f.write("**How to fix it**\n\n")
                f.write("In order to gain a higher click-through rate, you should ensure that all of your webpages have meta descriptions that contain relevant keywords.\n\n")
                f.write(f"**{len(missing_metas)} pages missing meta descriptions:**\n\n")
                for url in missing_metas:
                    f.write(f"• {url}\n")
                f.write("\n")
            
            if duplicate_metas:
                f.write("### 🔄 Duplicate Meta Descriptions\n\n")
                f.write("Our crawler reports pages that have duplicate meta descriptions only if they are exact matches.\n\n")
                f.write("A `<meta description>` tag is a short summary of a webpage's content that helps search engines understand what the page is about and can be shown to users in search results.\n\n")
                f.write("Duplicate meta descriptions on different pages mean a lost opportunity to use more relevant keywords. Also, duplicate meta descriptions make it difficult for search engines and users to differentiate between different web pages. It is better to have no meta description at all than to have a duplicate one.\n\n")
                f.write("**How to fix it**\n\n")
                f.write("Provide a unique, relevant meta description for each of your webpages.\n\n")
                f.write("For information on how to create effective meta descriptions, please see this Google article. You can also view the On-Page SEO Basics: Meta Descriptions article.\n\n")
                
                total_duplicate_meta_pages = sum(len(urls) for urls in duplicate_metas.values())
                f.write(f"**{total_duplicate_meta_pages} pages affected by duplicate meta descriptions:**\n\n")
                for meta, urls in duplicate_metas.items():
                    f.write(f"**\"{meta}\"** appears on {len(urls)} pages:\n")
                    for url in urls:
                        f.write(f"• {url}\n")
                    f.write("\n")

            # Content Audits - Enhanced with body text analysis
            content_issues = []
            low_text_ratio_pages = []
            very_thin_content = []

            for page in page_data:
                url = page.get('url', '')
                word_count = page.get('word_count', 0)
                content_ratio = page.get('content_ratio', 0)

                if word_count < 200:
                    very_thin_content.append((url, word_count))
                if content_ratio < 10:
                    low_text_ratio_pages.append((url, content_ratio))

            if analysis['seo_issues']['thin_content_pages'] > 0 or low_text_ratio_pages or very_thin_content:
                f.write("## 📄 Content Audits\n\n")

                if very_thin_content:
                    f.write("### ⚠️ Low Word Count\n\n")
                    f.write("This issue is triggered if the number of words on your webpage is less than 200. The amount of text placed on your webpage is a quality signal to search engines.\n\n")
                    f.write("Search engines prefer to provide as much information to users as possible, so pages with longer content tend to be placed higher in search results, as opposed to those with lower word counts.\n\n")
                    f.write("**How to fix it**\n\n")
                    f.write("Improve your on-page content and be sure to include more than 200 meaningful words.\n\n")
                    f.write(f"**{len(very_thin_content)} pages have very thin content (under 200 words):**\n\n")
                    for url, word_count in very_thin_content:
                        f.write(f"• {url} ({word_count} words)\n")
                    f.write("\n")

                if low_text_ratio_pages:
                    f.write("### 📊 Low Text-HTML Ratio\n\n")
                    f.write("Your text to HTML ratio indicates the amount of actual text you have on your webpage compared to the amount of code. This issue is triggered when your text to HTML is 10% or less.\n\n")
                    f.write("Search engines have begun focusing on pages that contain more content. That's why a higher text to HTML ratio means your page has a better chance of getting a good position in search results.\n\n")
                    f.write("Less code increases your page's load speed and also helps your rankings. It also helps search engine robots crawl your website faster.\n\n")
                    f.write("**How to fix it**\n\n")
                    f.write("Split your webpage's text content and code into separate files and compare their size. If the size of your code file exceeds the size of the text file, review your page's HTML code and consider optimizing its structure and removing embedded scripts and styles.\n\n")
                    f.write(f"**{len(low_text_ratio_pages)} pages have low text-to-HTML ratio (under 10%):**\n\n")
                    for url, ratio in low_text_ratio_pages:
                        f.write(f"• {url} ({ratio}% text-to-HTML ratio)\n")
                    f.write("\n")

            # On-Page Audits
            f.write("## 📋 On-Page Audits\n\n")
            
            if missing_h1:
                f.write("### ❌ H1 Headings Missing\n\n")
                f.write("While less important than `<title>` tags, h1 headings still help define your page's topic for search engines and users. If an `<h1>` tag is empty or missing, search engines may place your page lower than they would otherwise. Besides, a lack of an `<h1>` tag breaks your page's heading hierarchy, which is not SEO friendly.\n\n")
                f.write("**How to fix it**\n\n")
                f.write("Provide a concise, relevant h1 heading for each of your pages.\n\n")
                f.write(f"**{len(missing_h1)} pages missing H1 tags:**\n\n")
                for url in missing_h1:
                    f.write(f"• {url}\n")
                f.write("\n")
            
            if multiple_h1:
                f.write("### ⚠️ More Than One H1 Tag\n\n")
                f.write("Although multiple `<h1>` tags are allowed in HTML5, we still do not recommend that you use more than one `<h1>` tag per page. Including multiple `<h1>` tags may confuse users.\n\n")
                f.write("**How to fix it**\n\n")
                f.write("Use multiple `<h2>`-`<h6>` tags instead of multiple `<h1>` tags.\n\n")
                f.write(f"**{len(multiple_h1)} pages have multiple H1 tags:**\n\n")
                for url, count in multiple_h1:
                    f.write(f"• {url} ({count} H1 tags)\n")
                f.write("\n")
            
            # Alt Image & Video Markup Audits
            if analysis['images_without_alt'] > 0:
                f.write("## 🖼️ Image & Accessibility Audits\n\n")
                f.write("### ❌ Image Alt Attributes Missing\n\n")
                f.write("Alt attributes within `<img>` tags are used by search engines to understand the contents of your images. If you neglect alt attributes, you may miss the chance to get a better placement in search results because alt attributes allow you to rank in image search results.\n\n")
                f.write("Not using alt attributes also negatively affects the experience of visually impaired users and those who have disabled images in their browsers.\n\n")
                f.write("For more information, please see these articles: Using ALT attributes smartly and Google Image Publishing Guidelines\n\n")
                f.write("**How to fix it**\n\n")
                f.write("Specify a relevant alternative attribute inside an `<img>` tag for each image on your website, e.g., `<img src=\"mylogo.png\" alt=\"This is my company logo\">`.\n\n")
                # Get stored images_without_alt_files
                images_without_alt_files = getattr(self, '_images_without_alt_files', {})
                
                # Sort images by frequency (most common first)
                sorted_images = sorted(images_without_alt_files.items(), 
                                     key=lambda x: len(x[1]['pages']), reverse=True)
                
                f.write(f"**{len(images_without_alt_files)} unique image files missing alt text across {len(images_without_alt_pages)} pages:**\n\n")
                
                for img_url, img_info in sorted_images:
                    page_count = len(img_info['pages'])
                    filename = img_info['filename']
                    
                    if page_count == 1:
                        f.write(f"• **{filename}** - `{img_url}` (appears on 1 page)\n")
                    else:
                        f.write(f"• **{filename}** - `{img_url}` (appears on {page_count} pages)\n")
                    
                    # Show first few pages where it appears
                    if page_count <= 3:
                        for page_url in img_info['pages']:
                            f.write(f"  - {page_url}\n")
                    else:
                        for page_url in img_info['pages'][:3]:
                            f.write(f"  - {page_url}\n")
                        f.write(f"  - ... and {page_count - 3} more pages\n")
                    f.write("\n")
                
                f.write("**Priority Fix:** Focus on images that appear on multiple pages first, as fixing their alt text will improve accessibility across the entire site.\n\n")
            
            # Technical SEO Audits
            f.write("## ⚙️ Technical SEO Audits\n\n")
            
            # Canonical Tags Analysis
            canonical_issues = [page for page in page_data if not page.get('has_canonical')]
            canonical_conflicts = [page for page in page_data if page.get('canonical_url') and page.get('canonical_url') != page.get('final_url', page.get('url'))]
            
            if canonical_issues or canonical_conflicts:
                f.write("### 🔗 Canonical Tags\n\n")
                
                if canonical_issues:
                    f.write("#### ❌ Missing Canonical Tags\n\n")
                    f.write("Canonical tags help search engines understand which version of a page should be indexed when there are multiple URLs with similar content.\n\n")
                    f.write("**How to fix it**\n\n")
                    f.write("Add self-referencing canonical tags to all pages: `<link rel=\"canonical\" href=\"https://example.com/page-url\">`\n\n")
                    f.write(f"**{len(canonical_issues)} pages missing canonical tags:**\n\n")
                    for page in canonical_issues:
                        f.write(f"• {page.get('url', 'Unknown URL')}\n")
                    f.write("\n")
                
                if canonical_conflicts:
                    f.write("#### 🔗 Non-Self-Referencing Canonicals\n\n")
                    f.write("> **What this means:** These pages have canonical tags pointing to different URLs. This is only correct when the page is a duplicate or variation of another page.\n\n")
                    
                    # Separate legitimate canonicals (redirected pages) from potential issues
                    legitimate_canonicals = []
                    potential_issues = []
                    
                    for page in canonical_conflicts:
                        original_url = page.get('url', '')
                        final_url = page.get('final_url', '')
                        canonical_url = page.get('canonical_url', '')
                        has_redirects = page.get('has_redirects', False)
                        
                        # If page redirects and canonical points to final URL, this is correct
                        if has_redirects and canonical_url == final_url:
                            legitimate_canonicals.append(page)
                        else:
                            potential_issues.append(page)
                    
                    if potential_issues:
                        f.write("**⚠️ Pages requiring review:**\n\n")
                        f.write("| Original URL | Canonical Points To | Status |\n")
                        f.write("|--------------|-------------------|--------|\n")
                        for page in potential_issues:
                            original_url = page.get('url', 'Unknown URL')
                            canonical_url = page.get('canonical_url', 'Unknown')
                            has_redirects = "🔄 Redirects" if page.get('has_redirects') else "📄 Direct"
                            f.write(f"| `{original_url}` | `{canonical_url}` | {has_redirects} |\n")
                        f.write("\n")
                        
                        f.write("**🔧 How to fix:**\n")
                        f.write("- ✅ **If intentional:** These are duplicate pages correctly pointing to the main version\n")
                        f.write("- ❌ **If unintentional:** Update canonical tags to be self-referencing or implement 301 redirects\n")
                        f.write("- 🔍 **Review each case:** Ensure canonical strategy aligns with your content architecture\n\n")
                    
                    if legitimate_canonicals:
                        f.write("**✅ Correctly configured canonicals:**\n\n")
                        f.write(f"Found {len(legitimate_canonicals)} pages with proper canonical implementation (redirected pages pointing to final URLs).\n\n")
                    
                    if not potential_issues:
                        f.write("**✅ All canonical tags are correctly configured!**\n\n")
                        f.write("Your redirected pages properly point their canonical tags to the final destination URLs.\n\n")
            
            # Redirect Analysis
            redirect_pages = [page for page in page_data if page.get('has_redirects')]
            if redirect_pages:
                f.write("### 🔄 Redirects & Chains\n\n")
                f.write("> **Impact:** Redirect chains can slow down page loading and waste crawl budget. Each redirect should be direct (301 to final URL).\n\n")
                
                # Categorize redirects by chain length
                single_redirects = [p for p in redirect_pages if p.get('redirect_count', 0) == 1]
                chain_redirects = [p for p in redirect_pages if p.get('redirect_count', 0) > 1]
                
                if single_redirects:
                    f.write(f"**✅ Simple redirects ({len(single_redirects)} pages):**\n")
                    f.write("These are properly configured single redirects.\n\n")
                
                if chain_redirects:
                    f.write(f"**⚠️ Redirect chains requiring attention ({len(chain_redirects)} pages):**\n\n")
                    f.write("| Original URL | Redirects | Final URL |\n")
                    f.write("|--------------|-----------|----------|\n")
                    for page in chain_redirects[:10]:  # Show first 10
                        redirect_count = page.get('redirect_count', 0)
                        original_url = page.get('url', 'Unknown URL')
                        final_url = page.get('final_url', 'Unknown')
                        f.write(f"| `{original_url}` | {redirect_count} | `{final_url}` |\n")
                    
                    if len(chain_redirects) > 10:
                        f.write(f"| ... | ... | *{len(chain_redirects) - 10} more redirect chains* |\n")
                    f.write("\n")
                
                f.write("**🔧 How to fix:**\n")
                f.write("- Update internal links to point directly to final URLs\n")
                f.write("- Eliminate unnecessary redirect chains\n")
                f.write("- Use 301 redirects for permanent moves\n\n")
            
            # Indexability Issues
            noindex_pages = [page for page in page_data if page.get('is_noindex')]
            if noindex_pages:
                f.write("### Indexability Issues\n\n")
                f.write("#### Pages with Noindex Tags\n\n")
                f.write("These pages are blocked from being indexed by search engines. Verify this is intentional.\n\n")
                f.write(f"**{len(noindex_pages)} pages with noindex tags:**\n\n")
                for page in noindex_pages:
                    robots_content = page.get('meta_robots', '')
                    f.write(f"• {page.get('url', 'Unknown URL')} (robots: {robots_content})\n")
                f.write("\n")
            
            # Mixed Content Issues
            mixed_content_pages = [page for page in page_data if page.get('has_mixed_content')]
            if mixed_content_pages:
                f.write("### Security Issues\n\n")
                f.write("#### Mixed Content\n\n")
                f.write("HTTPS pages loading HTTP resources can cause security warnings and may not load properly in browsers.\n\n")
                f.write("**How to fix it**\n\n")
                f.write("Update all HTTP resources (images, scripts, stylesheets) to use HTTPS URLs.\n\n")
                f.write(f"**{len(mixed_content_pages)} pages with mixed content:**\n\n")
                for page in mixed_content_pages:
                    mixed_images = page.get('mixed_content_images', [])
                    f.write(f"• {page.get('url', 'Unknown URL')} ({len(mixed_images)} HTTP resources)\n")
                f.write("\n")
            
            # Structured Data Analysis
            schema_pages = [page for page in page_data if page.get('has_schema')]
            if schema_pages:
                f.write("### Structured Data\n\n")
                f.write("Structured data helps search engines understand your content and can enable rich snippets in search results.\n\n")
                
                # Count schema types
                schema_types = {}
                for page in schema_pages:
                    for schema_type in page.get('schema_types', []):
                        if schema_type:
                            schema_types[schema_type] = schema_types.get(schema_type, 0) + 1
                
                f.write(f"**{len(schema_pages)} pages have structured data:**\n\n")
                f.write("**Schema Types Found:**\n")
                for schema_type, count in schema_types.items():
                    f.write(f"• {schema_type}: {count} pages\n")
                f.write("\n")
                
                if len(schema_pages) < len(page_data) * 0.5:
                    f.write("**Recommendation:** Consider adding structured data to more pages to improve search visibility.\n\n")
            
            # Page Speed & Performance Audits
            f.write("## Page Speed & Performance Audits\n\n")
            
            # Collect all performance issues
            all_performance_issues = {}
            all_opportunities = {}
            
            for page in page_data:
                perf = page.get('performance', {})
                for issue in perf.get('issues', []):
                    issue_type = issue['type']
                    if issue_type not in all_performance_issues:
                        all_performance_issues[issue_type] = {
                            'pages': [],
                            'impact': issue['impact'],
                            'description': issue['description'].split(':')[0]  # Get base description
                        }
                    all_performance_issues[issue_type]['pages'].append({
                        'url': page.get('url', ''),
                        'details': issue['description']
                    })
                
                for opp in perf.get('opportunities', []):
                    opp_type = opp['type']
                    if opp_type not in all_opportunities:
                        all_opportunities[opp_type] = {
                            'pages': [],
                            'impact': opp['impact'],
                            'description': opp['description'].split(':')[0]
                        }
                    all_opportunities[opp_type]['pages'].append({
                        'url': page.get('url', ''),
                        'details': opp['description']
                    })
            
            # Render-blocking resources
            if 'render_blocking_css' in all_performance_issues or 'render_blocking_js' in all_performance_issues:
                f.write("### Eliminate Render-Blocking Resources\n\n")
                f.write("Render-blocking resources prevent the page from displaying content quickly. These resources delay the First Contentful Paint (FCP).\n\n")
                f.write("**How to fix it**\n\n")
                f.write("• Inline critical CSS and defer non-critical CSS\n")
                f.write("• Add `async` or `defer` attributes to JavaScript files\n")
                f.write("• Remove unused CSS and JavaScript\n")
                f.write("• Use resource hints like `preload` for critical resources\n\n")
                
                if 'render_blocking_css' in all_performance_issues:
                    css_issue = all_performance_issues['render_blocking_css']
                    f.write(f"**{len(css_issue['pages'])} pages with render-blocking CSS:**\n\n")
                    for page_info in css_issue['pages']:
                        f.write(f"• {page_info['url']} - {page_info['details']}\n")
                    f.write("\n")
                
                if 'render_blocking_js' in all_performance_issues:
                    js_issue = all_performance_issues['render_blocking_js']
                    f.write(f"**{len(js_issue['pages'])} pages with render-blocking JavaScript:**\n\n")
                    for page_info in js_issue['pages']:
                        f.write(f"• {page_info['url']} - {page_info['details']}\n")
                    f.write("\n")
            
            # Image optimization
            if 'images_without_dimensions' in all_performance_issues or 'modern_image_formats' in all_opportunities:
                f.write("### Image Optimization\n\n")
                
                if 'images_without_dimensions' in all_performance_issues:
                    img_issue = all_performance_issues['images_without_dimensions']
                    f.write("#### Use Explicit Width and Height on Image Elements\n\n")
                    f.write("Images without explicit dimensions can cause layout shifts (CLS issues) as the page loads.\n\n")
                    f.write("**How to fix it**\n\n")
                    f.write("Add `width` and `height` attributes to all `<img>` elements to prevent layout shifts.\n\n")
                    f.write(f"**{len(img_issue['pages'])} pages with images missing dimensions:**\n\n")
                    for page_info in img_issue['pages']:
                        f.write(f"• {page_info['url']} - {page_info['details']}\n")
                    f.write("\n")
                
                if 'modern_image_formats' in all_opportunities:
                    format_opp = all_opportunities['modern_image_formats']
                    f.write("#### Serve Images in Next-Gen Formats\n\n")
                    f.write("Modern image formats like WebP and AVIF provide better compression than JPEG and PNG, leading to faster downloads.\n\n")
                    f.write("**How to fix it**\n\n")
                    f.write("• Convert images to WebP or AVIF format\n")
                    f.write("• Use `<picture>` element with fallbacks for older browsers\n")
                    f.write("• Implement server-side image optimization\n\n")
                    f.write(f"**{len(format_opp['pages'])} pages with unoptimized image formats:**\n\n")
                    for page_info in format_opp['pages']:
                        f.write(f"• {page_info['url']} - {page_info['details']}\n")
                    f.write("\n")
                
                if 'lazy_loading' in all_opportunities:
                    lazy_opp = all_opportunities['lazy_loading']
                    f.write("#### Implement Lazy Loading for Images\n\n")
                    f.write("Lazy loading defers the loading of off-screen images until they're needed, improving initial page load time.\n\n")
                    f.write("**How to fix it**\n\n")
                    f.write("Add `loading=\"lazy\"` attribute to images that are not immediately visible.\n\n")
                    f.write(f"**{len(lazy_opp['pages'])} pages could benefit from lazy loading:**\n\n")
                    for page_info in lazy_opp['pages']:
                        f.write(f"• {page_info['url']} - {page_info['details']}\n")
                    f.write("\n")
            
            # Page size and performance
            if 'large_page_size' in all_performance_issues:
                size_issue = all_performance_issues['large_page_size']
                f.write("### Reduce Page Size\n\n")
                f.write("Large page sizes can significantly impact loading times, especially on slower connections.\n\n")
                f.write("**How to fix it**\n\n")
                f.write("• Compress and optimize images\n")
                f.write("• Minify CSS and JavaScript\n")
                f.write("• Remove unused code and resources\n")
                f.write("• Enable gzip/brotli compression\n\n")
                f.write(f"**{len(size_issue['pages'])} pages with large file sizes:**\n\n")
                for page_info in size_issue['pages']:
                    f.write(f"• {page_info['url']} - {page_info['details']}\n")
                f.write("\n")
            
            # Server response time
            if 'slow_server_response' in all_performance_issues:
                response_issue = all_performance_issues['slow_server_response']
                f.write("### Reduce Server Response Time\n\n")
                f.write("Slow server response times directly impact all Core Web Vitals metrics.\n\n")
                f.write("**How to fix it**\n\n")
                f.write("• Optimize server configuration\n")
                f.write("• Use a Content Delivery Network (CDN)\n")
                f.write("• Implement server-side caching\n")
                f.write("• Optimize database queries\n\n")
                f.write(f"**{len(response_issue['pages'])} pages with slow response times:**\n\n")
                for page_info in response_issue['pages']:
                    f.write(f"• {page_info['url']} - {page_info['details']}\n")
                f.write("\n")
            
            # DOM size
            if 'excessive_dom_size' in all_performance_issues:
                dom_issue = all_performance_issues['excessive_dom_size']
                f.write("### Avoid an Excessive DOM Size\n\n")
                f.write("Large DOM trees can slow down page performance and increase memory usage.\n\n")
                f.write("**How to fix it**\n\n")
                f.write("• Simplify page structure and remove unnecessary elements\n")
                f.write("• Use CSS instead of HTML for styling\n")
                f.write("• Implement virtual scrolling for large lists\n")
                f.write("• Break large pages into smaller components\n\n")
                f.write(f"**{len(dom_issue['pages'])} pages with excessive DOM size:**\n\n")
                for page_info in dom_issue['pages']:
                    f.write(f"• {page_info['url']} - {page_info['details']}\n")
                f.write("\n")
            
            # Third-party resources
            if 'excessive_third_party' in all_performance_issues:
                third_party_issue = all_performance_issues['excessive_third_party']
                f.write("### Reduce the Impact of Third-Party Code\n\n")
                f.write("Third-party scripts can significantly impact page performance and Core Web Vitals.\n\n")
                f.write("**How to fix it**\n\n")
                f.write("• Audit and remove unnecessary third-party scripts\n")
                f.write("• Load third-party scripts asynchronously\n")
                f.write("• Use resource hints to optimize third-party loading\n")
                f.write("• Consider self-hosting critical third-party resources\n\n")
                f.write(f"**{len(third_party_issue['pages'])} pages with excessive third-party resources:**\n\n")
                for page_info in third_party_issue['pages']:
                    f.write(f"• {page_info['url']} - {page_info['details']}\n")
                f.write("\n")
            
            # Font optimization
            if 'font_preloading' in all_opportunities:
                font_opp = all_opportunities['font_preloading']
                f.write("### Optimize Web Font Loading\n\n")
                f.write("Preloading key web fonts can improve text rendering and reduce layout shifts.\n\n")
                f.write("**How to fix it**\n\n")
                f.write("Add `<link rel=\"preload\" as=\"font\" type=\"font/woff2\" href=\"font.woff2\" crossorigin>` for critical fonts.\n\n")
                f.write(f"**{len(font_opp['pages'])} pages could benefit from font preloading:**\n\n")
                for page_info in font_opp['pages']:
                    f.write(f"• {page_info['url']} - {page_info['details']}\n")
                f.write("\n")
            
            # Technical Stats Summary
            f.write("---\n\n")
            f.write("## Audit Summary\n\n")
            f.write(f"**Website Analyzed:** {domain}\n")
            f.write(f"**Total Pages:** {total_pages:,}\n")
            f.write(f"**Crawl Success Rate:** {success_rate}%\n")
            f.write(f"**Total Issues Identified:** {len(missing_titles) + len(duplicate_titles) + len(missing_metas) + len(duplicate_metas) + len(missing_h1) + len(multiple_h1) + analysis['seo_issues']['thin_content_pages']}\n")
            f.write(f"**Audit Date:** {analysis['crawl_date']}\n")
            f.write(f"**Total Content Analyzed:** {analysis['total_word_count']:,} words\n")
            f.write(f"**Images Analyzed:** {analysis['total_images']:,}\n\n")
            
            f.write("*This comprehensive audit provides actionable insights to improve your website's search engine visibility and user experience. Prioritize critical and high-priority fixes for maximum impact.*\n")
        
        # Store page data for reference
        self._last_page_data = page_data
        return filepath

    def analyze_page_performance(self, soup, response, url):
        """Analyze page performance metrics similar to PageSpeed Insights"""
        performance = {
            'page_size': len(response.content),
            'response_time_ms': int(response.elapsed.total_seconds() * 1000),
            'issues': [],
            'opportunities': [],
            'metrics': {}
        }
        
        # Analyze CSS
        css_links = soup.find_all('link', rel='stylesheet')
        css_inline = soup.find_all('style')
        performance['css_files'] = len(css_links)
        performance['inline_css'] = len(css_inline)
        
        # Check for render-blocking CSS
        render_blocking_css = 0
        for css in css_links:
            if not css.get('media') or css.get('media') == 'all':
                render_blocking_css += 1
        
        if render_blocking_css > 0:
            performance['issues'].append({
                'type': 'render_blocking_css',
                'count': render_blocking_css,
                'impact': 'High' if render_blocking_css > 3 else 'Medium',
                'description': f'{render_blocking_css} render-blocking CSS resources'
            })
        
        # Analyze JavaScript
        js_scripts = soup.find_all('script')
        js_external = len([s for s in js_scripts if s.get('src')])
        js_inline = len([s for s in js_scripts if not s.get('src') and s.string])
        
        performance['js_files'] = js_external
        performance['inline_js'] = js_inline
        
        # Check for render-blocking JavaScript
        render_blocking_js = 0
        for script in js_scripts:
            if script.get('src') and not script.get('async') and not script.get('defer'):
                render_blocking_js += 1
        
        if render_blocking_js > 0:
            performance['issues'].append({
                'type': 'render_blocking_js',
                'count': render_blocking_js,
                'impact': 'High' if render_blocking_js > 2 else 'Medium',
                'description': f'{render_blocking_js} render-blocking JavaScript resources'
            })
        
        # Analyze images
        images = soup.find_all('img')
        images_without_alt = len([img for img in images if not img.get('alt')])
        images_without_dimensions = len([img for img in images if not img.get('width') or not img.get('height')])
        images_without_lazy_loading = len([img for img in images if img.get('loading') != 'lazy'])
        
        if images_without_dimensions > 0:
            performance['issues'].append({
                'type': 'images_without_dimensions',
                'count': images_without_dimensions,
                'impact': 'Medium',
                'description': f'{images_without_dimensions} images without explicit width and height'
            })
        
        if images_without_lazy_loading > 3:  # Only flag if many images
            performance['opportunities'].append({
                'type': 'lazy_loading',
                'count': images_without_lazy_loading,
                'impact': 'Medium',
                'description': f'{images_without_lazy_loading} images could use lazy loading'
            })
        
        # Check for modern image formats
        unoptimized_images = 0
        for img in images:
            src = img.get('src', '')
            if any(ext in src.lower() for ext in ['.jpg', '.jpeg', '.png']):
                if not any(ext in src.lower() for ext in ['.webp', '.avif']):
                    unoptimized_images += 1
        
        if unoptimized_images > 0:
            performance['opportunities'].append({
                'type': 'modern_image_formats',
                'count': unoptimized_images,
                'impact': 'Medium',
                'description': f'{unoptimized_images} images could be served in modern formats (WebP, AVIF)'
            })
        
        # Check for excessive DOM size
        all_elements = soup.find_all()
        dom_size = len(all_elements)
        performance['dom_elements'] = dom_size
        
        if dom_size > 1500:
            performance['issues'].append({
                'type': 'excessive_dom_size',
                'count': dom_size,
                'impact': 'High' if dom_size > 3000 else 'Medium',
                'description': f'Large DOM size: {dom_size} elements'
            })
        
        # Check for third-party resources
        third_party_scripts = []
        for script in js_scripts:
            src = script.get('src', '')
            if src and not any(domain in src for domain in [url, 'localhost', '127.0.0.1']):
                third_party_scripts.append(src)
        
        if len(third_party_scripts) > 5:
            performance['issues'].append({
                'type': 'excessive_third_party',
                'count': len(third_party_scripts),
                'impact': 'Medium',
                'description': f'{len(third_party_scripts)} third-party scripts may impact performance'
            })
        
        # Check for font loading optimization
        font_links = soup.find_all('link', href=lambda x: x and 'font' in x.lower())
        preload_fonts = soup.find_all('link', rel='preload', as_='font')
        
        if len(font_links) > 0 and len(preload_fonts) == 0:
            performance['opportunities'].append({
                'type': 'font_preloading',
                'count': len(font_links),
                'impact': 'Low',
                'description': f'{len(font_links)} web fonts could be preloaded'
            })
        
        # Page size analysis
        if performance['page_size'] > 1024 * 1024:  # 1MB
            performance['issues'].append({
                'type': 'large_page_size',
                'size': performance['page_size'],
                'impact': 'High' if performance['page_size'] > 3 * 1024 * 1024 else 'Medium',
                'description': f'Large page size: {performance["page_size"] / 1024 / 1024:.1f}MB'
            })
        
        # Response time analysis
        if performance['response_time_ms'] > 1000:
            performance['issues'].append({
                'type': 'slow_server_response',
                'time': performance['response_time_ms'],
                'impact': 'High' if performance['response_time_ms'] > 3000 else 'Medium',
                'description': f'Slow server response: {performance["response_time_ms"]}ms'
            })
        
        return performance

def main():
    """Main function"""
    if len(sys.argv) < 2:
        print("🔍 Comprehensive SEO Crawler - Like Screaming Frog but Better!")
        print("=" * 60)
        print("Usage: python3 obsidian_seo_crawler.py <website_url> [max_pages]")
        print()
        print("Examples:")
        print("  python3 obsidian_seo_crawler.py example.com           # Crawl ENTIRE SITE (up to 50k pages)")
        print("  python3 obsidian_seo_crawler.py example.com 500       # Limit to 500 pages")
        print("  python3 obsidian_seo_crawler.py example.com unlimited # No limit (be careful!)")
        print()
        print("Features:")
        print("• Full site crawling with link discovery")
        print("• Sitemap parsing for comprehensive coverage")
        print("• Smart URL filtering and deduplication")
        print("• Progress tracking and performance stats")
        print("• Detailed SEO analysis of every page")
        print("• Professional Obsidian markdown reports")
        sys.exit(1)
    
    url = sys.argv[1]
    
    # Handle max_pages parameter
    if len(sys.argv) > 2:
        if sys.argv[2].lower() == 'unlimited':
            max_pages = None
        else:
            try:
                max_pages = int(sys.argv[2])
            except ValueError:
                print("❌ Invalid max_pages value. Use a number or 'unlimited'")
                sys.exit(1)
    else:
        max_pages = None  # Default to comprehensive crawling
    
    crawler = ComprehensiveSEOCrawler(max_pages=max_pages)
    analysis = crawler.comprehensive_analysis(url)
    
    if 'error' in analysis:
        print(f"❌ Error: {analysis['error']}")
        return
    
    report_path = crawler.generate_comprehensive_markdown(analysis)
    
    # Final summary with performance stats
    elapsed_total = time.time() - crawler.crawl_stats['start_time']
    
    print(f"\n🎉 FULL SITE AUDIT COMPLETE!")
    print("=" * 60)
    print(f"📊 Website: {url}")
    print(f"📄 Pages Discovered: {crawler.crawl_stats['pages_found']}")
    print(f"📄 Pages Analyzed: {analysis['total_pages_analyzed']}")
    print(f"🔍 Success Rate: {analysis['success_rate']}%")
    print(f"⏱️  Total Time: {elapsed_total:.1f} seconds")
    print(f"📝 Report: {os.path.basename(report_path)}")
    print(f"📁 Location: {report_path}")
    
    # Performance summary
    if analysis['total_pages_analyzed'] > 0:
        pages_per_second = analysis['total_pages_analyzed'] / elapsed_total
        print(f"⚡ Performance: {pages_per_second:.1f} pages/second")

if __name__ == "__main__":
    main()