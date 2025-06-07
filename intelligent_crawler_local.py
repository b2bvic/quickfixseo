#!/usr/bin/env python3
"""
Intelligent SEO Audit System - Obsidian Focused
Generates comprehensive markdown SEO audit reports directly to Obsidian vault
"""

import os
import sys
import subprocess
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
from datetime import datetime
from pathlib import Path
import time

class IntelligentSEOAnalyzer:
    def __init__(self, obsidian_vault_path=None):
        """Initialize the SEO analyzer with Obsidian vault integration"""
        self.screamingfrog_path = "/Applications/Screaming Frog SEO Spider.app/Contents/MacOS/ScreamingFrogSEOSpiderLauncher"
        
        # Obsidian vault setup - will prompt user if not provided
        if obsidian_vault_path:
            self.obsidian_vault_path = obsidian_vault_path
        else:
            self.obsidian_vault_path = self.setup_obsidian_integration()
        
        # SEO audit folder within Obsidian
        self.seo_audits_folder = os.path.join(self.obsidian_vault_path, "SEO Audits")
        os.makedirs(self.seo_audits_folder, exist_ok=True)
    
    def setup_obsidian_integration(self):
        """Setup Obsidian vault integration with user guidance"""
        print("🔧 OBSIDIAN VAULT SETUP")
        print("=" * 50)
        print("To save SEO audit reports directly to your Obsidian vault,")
        print("I need to know where your vault is located.\n")
        
        # Common Obsidian vault locations
        common_paths = [
            os.path.expanduser("~/Documents/Obsidian Vault"),
            os.path.expanduser("~/Obsidian"),
            os.path.expanduser("~/Documents/Notes"),
            os.path.expanduser("~/Desktop/Obsidian")
        ]
        
        print("Common Obsidian vault locations:")
        for i, path in enumerate(common_paths, 1):
            exists = "✅" if os.path.exists(path) else "❌"
            print(f"{i}. {path} {exists}")
        
        print(f"{len(common_paths) + 1}. Enter custom path")
        print("0. Skip Obsidian integration (save to Desktop)")
        
        while True:
            try:
                choice = input("\nSelect your Obsidian vault location (number): ").strip()
                
                if choice == "0":
                    return os.path.expanduser("~/Desktop/SEO_Audits")
                
                if choice.isdigit() and 1 <= int(choice) <= len(common_paths):
                    selected_path = common_paths[int(choice) - 1]
                    if os.path.exists(selected_path):
                        print(f"✅ Using: {selected_path}")
                        return selected_path
                    else:
                        print(f"❌ Path doesn't exist: {selected_path}")
                        continue
                
                if int(choice) == len(common_paths) + 1:
                    custom_path = input("Enter your Obsidian vault path: ").strip()
                    if os.path.exists(custom_path):
                        print(f"✅ Using: {custom_path}")
                        return custom_path
                    else:
                        print(f"❌ Path doesn't exist: {custom_path}")
                        continue
                
                print("❌ Invalid choice. Please try again.")
                
            except (ValueError, KeyboardInterrupt):
                print("\n❌ Invalid input or cancelled. Using Desktop fallback.")
                return os.path.expanduser("~/Desktop/SEO_Audits")
    
    def analyze_website(self, url):
        """Comprehensive website analysis for intelligent SEO insights"""
        print(f"🔍 Analyzing website structure for {url}...")
        
        # Ensure URL has protocol
        if not url.startswith(('http://', 'https://')):
            url = 'https://' + url
        
        analysis = {
            'url': url,
            'domain': urlparse(url).netloc.replace('www.', ''),
            'cms_detected': None,
            'estimated_pages': 0,
            'has_sitemap': False,
            'has_ecommerce': False,
            'has_blog': False,
            'javascript_heavy': False,
            'page_load_insights': {},
            'meta_analysis': {},
            'structure_analysis': {},
            'competitive_insights': {},
            'recommendations': []
        }
        
        try:
            # Fetch and analyze homepage
            headers = {
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
            }
            
            response = requests.get(url, headers=headers, timeout=10)
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # Core analysis
            self._detect_cms(soup, analysis)
            self._analyze_meta_tags(soup, analysis)
            self._analyze_page_structure(soup, analysis)
            self._detect_ecommerce_signals(soup, analysis)
            self._detect_blog_signals(soup, analysis)
            self._analyze_javascript_usage(soup, analysis)
            self._check_sitemap_existence(url, analysis)
            self._estimate_site_size(url, analysis)
            self._generate_intelligent_recommendations(analysis)
            
        except Exception as e:
            print(f"⚠️  Analysis warning: {str(e)}")
            analysis['estimated_pages'] = 50  # Default fallback
        
        return analysis
    
    def _detect_cms(self, soup, analysis):
        """Detect CMS and platform"""
        # WordPress detection
        if (soup.find('meta', attrs={'name': 'generator', 'content': lambda x: x and 'wordpress' in x.lower()}) or
            soup.find('link', href=lambda x: x and 'wp-content' in x) or
            soup.find('script', src=lambda x: x and 'wp-content' in x)):
            analysis['cms_detected'] = 'wordpress'
            return
        
        # Shopify detection
        if (soup.find('script', src=lambda x: x and 'shopify' in x) or
            soup.find('link', href=lambda x: x and 'shopify' in x)):
            analysis['cms_detected'] = 'shopify'
            analysis['has_ecommerce'] = True
            return
        
        # React detection
        if soup.find('div', id='root') or soup.find('script', src=lambda x: x and 'react' in x):
            analysis['cms_detected'] = 'react'
            analysis['javascript_heavy'] = True
            return
        
        # Squarespace detection
        if soup.find('script', src=lambda x: x and 'squarespace' in x):
            analysis['cms_detected'] = 'squarespace'
            return
    
    def _analyze_meta_tags(self, soup, analysis):
        """Analyze meta tags and SEO elements"""
        meta_analysis = {}
        
        # Title analysis
        title_tag = soup.find('title')
        if title_tag:
            title_text = title_tag.get_text().strip()
            meta_analysis['title'] = {
                'text': title_text,
                'length': len(title_text),
                'optimal': 30 <= len(title_text) <= 60
            }
        
        # Meta description
        meta_desc = soup.find('meta', attrs={'name': 'description'})
        if meta_desc:
            desc_content = meta_desc.get('content', '')
            meta_analysis['description'] = {
                'text': desc_content,
                'length': len(desc_content),
                'optimal': 120 <= len(desc_content) <= 160
            }
        
        # H1 analysis
        h1_tags = soup.find_all('h1')
        meta_analysis['h1_tags'] = {
            'count': len(h1_tags),
            'texts': [h1.get_text().strip() for h1 in h1_tags[:3]],  # First 3
            'optimal': len(h1_tags) == 1
        }
        
        analysis['meta_analysis'] = meta_analysis
    
    def _analyze_page_structure(self, soup, analysis):
        """Analyze page structure and content"""
        structure = {}
        
        # Count various elements
        structure['internal_links'] = len([a for a in soup.find_all('a', href=True) 
                                         if urlparse(a['href']).netloc == '' or 
                                         analysis['domain'] in urlparse(a['href']).netloc])
        
        structure['external_links'] = len([a for a in soup.find_all('a', href=True) 
                                         if urlparse(a['href']).netloc != '' and 
                                         analysis['domain'] not in urlparse(a['href']).netloc])
        
        structure['images'] = len(soup.find_all('img'))
        structure['images_without_alt'] = len([img for img in soup.find_all('img') if not img.get('alt')])
        
        # Content analysis
        text_content = soup.get_text()
        word_count = len(text_content.split())
        structure['word_count'] = word_count
        structure['content_quality'] = 'high' if word_count > 300 else 'low'
        
        analysis['structure_analysis'] = structure
    
    def _detect_ecommerce_signals(self, soup, analysis):
        """Detect e-commerce indicators"""
        ecommerce_indicators = [
            'add to cart', 'shopping cart', 'checkout', 'buy now',
            'product', 'price', '$', 'shop', 'store', 'woocommerce'
        ]
        
        page_text = soup.get_text().lower()
        ecommerce_signals = sum(1 for indicator in ecommerce_indicators if indicator in page_text)
        
        if ecommerce_signals >= 3:
            analysis['has_ecommerce'] = True
    
    def _detect_blog_signals(self, soup, analysis):
        """Detect blog/content site indicators"""
        blog_indicators = [
            'blog', 'article', 'post', 'news', 'read more',
            'published', 'author', 'category', 'tag'
        ]
        
        page_text = soup.get_text().lower()
        blog_signals = sum(1 for indicator in blog_indicators if indicator in page_text)
        
        if blog_signals >= 3:
            analysis['has_blog'] = True
    
    def _analyze_javascript_usage(self, soup, analysis):
        """Analyze JavaScript usage and complexity"""
        script_tags = soup.find_all('script')
        js_heavy_indicators = [
            'react', 'angular', 'vue', 'spa', 'bundle.js',
            'webpack', 'next.js', 'gatsby'
        ]
        
        script_content = ' '.join([script.get('src', '') + script.get_text() for script in script_tags]).lower()
        js_signals = sum(1 for indicator in js_heavy_indicators if indicator in script_content)
        
        if js_signals >= 2 or len(script_tags) > 10:
            analysis['javascript_heavy'] = True
    
    def _check_sitemap_existence(self, url, analysis):
        """Check for XML sitemap"""
        sitemap_urls = [
            urljoin(url, '/sitemap.xml'),
            urljoin(url, '/sitemap_index.xml'),
            urljoin(url, '/robots.txt')  # Check robots.txt for sitemap reference
        ]
        
        for sitemap_url in sitemap_urls:
            try:
                response = requests.get(sitemap_url, timeout=5)
                if response.status_code == 200:
                    if 'sitemap' in sitemap_url or 'sitemap' in response.text.lower():
                        analysis['has_sitemap'] = True
                        break
            except:
                continue
    
    def _estimate_site_size(self, url, analysis):
        """Estimate website size using various signals"""
        # Start with baseline based on CMS
        if analysis['cms_detected'] == 'wordpress':
            baseline = 50
        elif analysis['cms_detected'] == 'shopify':
            baseline = 100
        elif analysis['has_ecommerce']:
            baseline = 200
        else:
            baseline = 20
        
        # Adjust based on content signals
        if analysis['has_blog']:
            baseline *= 3
        if analysis['has_ecommerce']:
            baseline *= 2
        if analysis['has_sitemap']:
            baseline *= 1.5
        
        analysis['estimated_pages'] = int(baseline)
    
    def _generate_intelligent_recommendations(self, analysis):
        """Generate intelligent SEO recommendations based on analysis"""
        recommendations = []
        
        # Meta tag recommendations
        meta = analysis.get('meta_analysis', {})
        if 'title' in meta and not meta['title']['optimal']:
            if meta['title']['length'] < 30:
                recommendations.append("Extend page title to 30-60 characters for better SEO impact")
            elif meta['title']['length'] > 60:
                recommendations.append("Shorten page title to under 60 characters to prevent truncation")
        
        if 'description' in meta:
            if not meta['description']['optimal']:
                recommendations.append("Optimize meta description to 120-160 characters for better SERP display")
        else:
            recommendations.append("Add meta description for improved SERP appearance and click-through rates")
        
        if 'h1_tags' in meta and not meta['h1_tags']['optimal']:
            if meta['h1_tags']['count'] == 0:
                recommendations.append("Add H1 tag for better content structure and SEO")
            elif meta['h1_tags']['count'] > 1:
                recommendations.append("Use only one H1 tag per page for optimal SEO structure")
        
        # Content recommendations
        structure = analysis.get('structure_analysis', {})
        if structure.get('word_count', 0) < 300:
            recommendations.append("Increase page content to at least 300 words for better SEO value")
        
        if structure.get('images_without_alt', 0) > 0:
            recommendations.append(f"Add alt text to {structure['images_without_alt']} images for accessibility and SEO")
        
        # Platform-specific recommendations
        if analysis['cms_detected'] == 'wordpress':
            recommendations.extend([
                "Install and configure a comprehensive SEO plugin (Yoast or RankMath)",
                "Optimize WordPress performance with caching and image optimization",
                "Review and optimize URL structure (permalinks)"
            ])
        
        if analysis['has_ecommerce']:
            recommendations.extend([
                "Implement structured data markup for products",
                "Optimize product images with descriptive filenames and alt text",
                "Create SEO-optimized category and product page templates"
            ])
        
        if analysis['javascript_heavy']:
            recommendations.extend([
                "Implement server-side rendering for critical content",
                "Optimize JavaScript loading for better Core Web Vitals",
                "Ensure content is crawlable without JavaScript execution"
            ])
        
        analysis['recommendations'] = recommendations
    
    def generate_obsidian_markdown(self, analysis):
        """Generate comprehensive Obsidian-formatted markdown report"""
        domain = analysis['domain']
        timestamp = datetime.now()
        
        # Create filename with timestamp
        filename = f"SEO-Audit-{domain.replace('.', '-')}-{timestamp.strftime('%Y-%m-%d')}.md"
        filepath = os.path.join(self.seo_audits_folder, filename)
        
        with open(filepath, 'w') as f:
            # Obsidian metadata (frontmatter)
            f.write("---\n")
            f.write(f"type: seo-audit\n")
            f.write(f"domain: {domain}\n")
            f.write(f"audit-date: {timestamp.strftime('%Y-%m-%d')}\n")
            f.write(f"cms: {analysis['cms_detected'] or 'unknown'}\n")
            f.write(f"ecommerce: {analysis['has_ecommerce']}\n")
            f.write(f"blog: {analysis['has_blog']}\n")
            f.write(f"javascript-heavy: {analysis['javascript_heavy']}\n")
            f.write("tags:\n")
            f.write("  - seo-audit\n")
            f.write(f"  - {domain}\n")
            if analysis['cms_detected']:
                f.write(f"  - {analysis['cms_detected']}\n")
            if analysis['has_ecommerce']:
                f.write("  - ecommerce\n")
            if analysis['has_blog']:
                f.write("  - blog\n")
            f.write("---\n\n")
            
            # Main content
            f.write(f"# SEO Audit: {domain}\n\n")
            f.write(f"**Audit Date:** {timestamp.strftime('%B %d, %Y at %H:%M')}\n")
            f.write(f"**Website:** {analysis['url']}\n")
            f.write(f"**Analyzer:** Intelligent SEO Audit System\n\n")
            
            # Quick Stats Box
            f.write("## 📊 Quick Stats\n\n")
            f.write("| Metric | Value |\n")
            f.write("|--------|-------|\n")
            f.write(f"| **Platform** | {analysis['cms_detected'].title() if analysis['cms_detected'] else 'Unknown'} |\n")
            f.write(f"| **Estimated Pages** | ~{analysis['estimated_pages']:,} |\n")
            f.write(f"| **E-commerce** | {'✅ Yes' if analysis['has_ecommerce'] else '❌ No'} |\n")
            f.write(f"| **Blog/Content** | {'✅ Yes' if analysis['has_blog'] else '❌ No'} |\n")
            f.write(f"| **JS-Heavy** | {'⚠️ Yes' if analysis['javascript_heavy'] else '✅ No'} |\n")
            f.write(f"| **XML Sitemap** | {'✅ Found' if analysis['has_sitemap'] else '❌ Not Found'} |\n\n")
            
            # Executive Summary
            f.write("## 🎯 Executive Summary\n\n")
            self._write_executive_summary(f, analysis)
            
            # Technical Analysis
            f.write("## 🔧 Technical Analysis\n\n")
            self._write_technical_analysis(f, analysis)
            
            # Content Analysis
            f.write("## 📝 Content Analysis\n\n")
            self._write_content_analysis(f, analysis)
            
            # SEO Recommendations
            f.write("## 🚀 Priority Recommendations\n\n")
            self._write_recommendations(f, analysis)
            
            # Next Steps
            f.write("## 📋 Action Items\n\n")
            self._write_action_items(f, analysis)
            
            # Related Notes
            f.write("## 🔗 Related Notes\n\n")
            f.write("- [[SEO Strategy]]\n")
            f.write("- [[Content Marketing]]\n")
            f.write("- [[Technical SEO]]\n")
            if analysis['cms_detected']:
                f.write(f"- [[{analysis['cms_detected'].title()} Optimization]]\n")
            if analysis['has_ecommerce']:
                f.write("- [[E-commerce SEO]]\n")
            
        print(f"📋 Created Obsidian note: {filename}")
        print(f"💾 Saved to: {filepath}")
        
        return filepath
    
    def _write_executive_summary(self, f, analysis):
        """Write executive summary section"""
        domain = analysis['domain']
        
        f.write(f"**{domain}** is a ")
        if analysis['cms_detected']:
            f.write(f"**{analysis['cms_detected'].title()}**-powered ")
        
        if analysis['has_ecommerce'] and analysis['has_blog']:
            f.write("e-commerce and content website")
        elif analysis['has_ecommerce']:
            f.write("e-commerce website")
        elif analysis['has_blog']:
            f.write("content/blog website")
        else:
            f.write("business website")
        
        f.write(f" with approximately **{analysis['estimated_pages']:,} pages**.\n\n")
        
        # Key findings
        f.write("### Key Findings\n\n")
        
        if analysis['javascript_heavy']:
            f.write("- ⚠️ **JavaScript-heavy architecture** may impact SEO crawlability\n")
        
        if not analysis['has_sitemap']:
            f.write("- ❌ **No XML sitemap detected** - critical for search engine discovery\n")
        
        meta = analysis.get('meta_analysis', {})
        if 'title' in meta and not meta['title']['optimal']:
            f.write("- ⚠️ **Page title optimization needed** for better SERP performance\n")
        
        if 'description' in meta and not meta['description']['optimal']:
            f.write("- ⚠️ **Meta description optimization needed** for improved CTR\n")
        elif 'description' not in meta:
            f.write("- ❌ **Missing meta description** - crucial for SERP appearance\n")
        
        structure = analysis.get('structure_analysis', {})
        if structure.get('word_count', 0) < 300:
            f.write("- ⚠️ **Thin content detected** - consider expanding page content\n")
        
        f.write("\n")
    
    def _write_technical_analysis(self, f, analysis):
        """Write technical analysis section"""
        meta = analysis.get('meta_analysis', {})
        structure = analysis.get('structure_analysis', {})
        
        # Meta tags analysis
        f.write("### Meta Tags Analysis\n\n")
        
        if 'title' in meta:
            title_data = meta['title']
            status = "✅" if title_data['optimal'] else "⚠️"
            f.write(f"**Title Tag:** {status}\n")
            f.write(f"- Length: {title_data['length']} characters\n")
            f.write(f"- Text: \"{title_data['text']}\"\n")
            f.write(f"- Optimal: {title_data['optimal']} (30-60 chars recommended)\n\n")
        else:
            f.write("**Title Tag:** ❌ Not found\n\n")
        
        if 'description' in meta:
            desc_data = meta['description']
            status = "✅" if desc_data['optimal'] else "⚠️"
            f.write(f"**Meta Description:** {status}\n")
            f.write(f"- Length: {desc_data['length']} characters\n")
            f.write(f"- Text: \"{desc_data['text'][:100]}{'...' if len(desc_data['text']) > 100 else ''}\"\n")
            f.write(f"- Optimal: {desc_data['optimal']} (120-160 chars recommended)\n\n")
        else:
            f.write("**Meta Description:** ❌ Missing\n\n")
        
        if 'h1_tags' in meta:
            h1_data = meta['h1_tags']
            status = "✅" if h1_data['optimal'] else "⚠️"
            f.write(f"**H1 Tags:** {status}\n")
            f.write(f"- Count: {h1_data['count']} (1 recommended)\n")
            if h1_data['texts']:
                f.write(f"- Text(s): {', '.join(h1_data['texts'])}\n")
            f.write("\n")
        
        # Content structure
        f.write("### Content Structure\n\n")
        if structure:
            f.write(f"- **Word Count:** {structure.get('word_count', 'N/A')}\n")
            f.write(f"- **Content Quality:** {structure.get('content_quality', 'Unknown').title()}\n")
            f.write(f"- **Internal Links:** {structure.get('internal_links', 'N/A')}\n")
            f.write(f"- **External Links:** {structure.get('external_links', 'N/A')}\n")
            f.write(f"- **Images:** {structure.get('images', 'N/A')}\n")
            f.write(f"- **Images Without Alt Text:** {structure.get('images_without_alt', 'N/A')}\n\n")
    
    def _write_content_analysis(self, f, analysis):
        """Write content analysis section"""
        structure = analysis.get('structure_analysis', {})
        
        f.write("### Content Quality Assessment\n\n")
        
        word_count = structure.get('word_count', 0)
        if word_count > 0:
            if word_count >= 1000:
                f.write("✅ **Excellent content depth** - comprehensive content detected\n")
            elif word_count >= 500:
                f.write("✅ **Good content length** - solid foundation for SEO\n")
            elif word_count >= 300:
                f.write("⚠️ **Adequate content** - consider expanding for better SEO value\n")
            else:
                f.write("❌ **Thin content** - needs significant expansion for SEO impact\n")
        
        f.write("\n### Content Optimization Opportunities\n\n")
        
        images_without_alt = structure.get('images_without_alt', 0)
        if images_without_alt > 0:
            f.write(f"- Add alt text to {images_without_alt} images for accessibility and SEO\n")
        
        internal_links = structure.get('internal_links', 0)
        if internal_links < 3:
            f.write("- Increase internal linking to improve site architecture and user navigation\n")
        
        if analysis['has_ecommerce']:
            f.write("- Implement product schema markup for rich snippets\n")
            f.write("- Optimize product descriptions with target keywords\n")
        
        if analysis['has_blog']:
            f.write("- Develop content clusters around main topics\n")
            f.write("- Implement proper heading hierarchy (H1-H6)\n")
        
        f.write("\n")
    
    def _write_recommendations(self, f, analysis):
        """Write recommendations section"""
        recommendations = analysis.get('recommendations', [])
        
        f.write("### Immediate Actions (High Priority)\n\n")
        high_priority = [rec for rec in recommendations[:5]]  # First 5 as high priority
        
        for i, rec in enumerate(high_priority, 1):
            f.write(f"{i}. {rec}\n")
        
        f.write("\n### Medium Priority Actions\n\n")
        medium_priority = recommendations[5:] if len(recommendations) > 5 else []
        
        if medium_priority:
            for i, rec in enumerate(medium_priority, 1):
                f.write(f"{i}. {rec}\n")
        else:
            f.write("- Complete high priority actions first\n")
        
        f.write("\n### Platform-Specific Recommendations\n\n")
        
        if analysis['cms_detected'] == 'wordpress':
            f.write("**WordPress Optimization:**\n")
            f.write("- Install Yoast SEO or RankMath plugin\n")
            f.write("- Optimize images with compression plugins\n")
            f.write("- Implement caching for better performance\n")
            f.write("- Review and optimize permalink structure\n\n")
        
        if analysis['has_ecommerce']:
            f.write("**E-commerce SEO:**\n")
            f.write("- Implement product structured data\n")
            f.write("- Optimize category page SEO\n")
            f.write("- Create detailed product descriptions\n")
            f.write("- Implement customer review schema\n\n")
        
        if analysis['javascript_heavy']:
            f.write("**JavaScript Optimization:**\n")
            f.write("- Implement server-side rendering (SSR)\n")
            f.write("- Optimize JavaScript loading order\n")
            f.write("- Ensure content is crawlable without JS\n")
            f.write("- Monitor Core Web Vitals performance\n\n")
    
    def _write_action_items(self, f, analysis):
        """Write action items section"""
        f.write("### Week 1: Foundation\n")
        f.write("- [ ] Fix critical technical issues identified above\n")
        f.write("- [ ] Optimize title tags and meta descriptions\n")
        f.write("- [ ] Add missing alt text to images\n")
        if not analysis['has_sitemap']:
            f.write("- [ ] Create and submit XML sitemap\n")
        f.write("\n")
        
        f.write("### Week 2-3: Content Optimization\n")
        f.write("- [ ] Expand thin content pages\n")
        f.write("- [ ] Improve internal linking structure\n")
        f.write("- [ ] Optimize heading hierarchy\n")
        if analysis['has_blog']:
            f.write("- [ ] Develop content strategy and calendar\n")
        f.write("\n")
        
        f.write("### Week 4+: Advanced Optimization\n")
        f.write("- [ ] Implement structured data markup\n")
        f.write("- [ ] Optimize page loading speed\n")
        f.write("- [ ] Conduct competitor analysis\n")
        f.write("- [ ] Set up ongoing SEO monitoring\n")
        f.write("\n")
        
        f.write("### Ongoing Monitoring\n")
        f.write("- [ ] Weekly: Monitor keyword rankings\n")
        f.write("- [ ] Monthly: Analyze organic traffic trends\n")
        f.write("- [ ] Quarterly: Comprehensive SEO audit review\n\n")
    
    def run_intelligent_audit(self, url):
        """Main method to run complete intelligent SEO audit"""
        print("🚀 Starting Intelligent SEO Audit")
        print("=" * 50)
        print(f"🎯 Target URL: {url}")
        print(f"📝 Output: Obsidian Vault ({self.obsidian_vault_path})")
        
        # Step 1: Analyze website
        print("\n1️⃣  Analyzing website...")
        analysis = self.analyze_website(url)
        
        # Print analysis summary
        print(f"✅ Analysis complete:")
        print(f"   - Domain: {analysis['domain']}")
        print(f"   - Platform: {analysis['cms_detected'] or 'Unknown'}")
        print(f"   - Estimated pages: {analysis['estimated_pages']}")
        print(f"   - E-commerce: {analysis['has_ecommerce']}")
        print(f"   - Blog: {analysis['has_blog']}")
        print(f"   - JavaScript heavy: {analysis['javascript_heavy']}")
        print(f"   - Sitemap found: {analysis['has_sitemap']}")
        
        # Step 2: Generate Obsidian markdown
        print("\n2️⃣  Generating Obsidian markdown report...")
        markdown_file = self.generate_obsidian_markdown(analysis)
        
        # Final summary
        print("\n🎉 AUDIT COMPLETE!")
        print("=" * 50)
        print(f"📊 Website: {url}")
        print(f"📝 Report saved to Obsidian vault")
        print(f"💾 File: {os.path.basename(markdown_file)}")
        print(f"📁 Location: {markdown_file}")
        
        # Open in Obsidian if possible
        try:
            subprocess.run(['open', markdown_file])
            print(f"📂 Opened in default markdown editor")
        except:
            pass
        
        return True

def main():
    """Main function to run SEO audit"""
    if len(sys.argv) != 2:
        print("Usage: python3 intelligent_seo_analyzer.py <website_url>")
        print("Example: python3 intelligent_seo_analyzer.py example.com")
        sys.exit(1)
    
    url = sys.argv[1]
    
    # Initialize analyzer (will prompt for Obsidian vault setup if needed)
    analyzer = IntelligentSEOAnalyzer()
    
    # Run the audit
    analyzer.run_intelligent_audit(url)

if __name__ == "__main__":
    main() 