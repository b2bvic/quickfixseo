#!/usr/bin/env python3
"""
Advanced SEO Audit System - Enterprise Edition
Features:
- AI-powered content quality analysis
- Mobile-first indexing optimization
- Competitive positioning analysis
- Advanced schema markup detection
- Page experience signals monitoring
- Core Web Vitals tracking
"""

import sys
import os
from obsidian_seo_crawler import ComprehensiveSEOCrawler

def main():
    print("🚀 Advanced SEO Audit System - Enterprise Edition")
    print("=" * 60)
    print("🧠 AI-Powered Content Analysis")
    print("📱 Mobile-First Indexing Optimization")
    print("🏆 Competitive Positioning Analysis")
    print("🔍 Advanced Schema Markup Detection")
    print("⚡ Page Experience Signals Monitoring")
    print("📊 Core Web Vitals Tracking")
    print("=" * 60)
    
    if len(sys.argv) != 2:
        print("\nUsage: python3 advanced_seo_audit.py <website_url>")
        print("\nExamples:")
        print("  python3 advanced_seo_audit.py https://example.com")
        print("  python3 advanced_seo_audit.py example.com")
        print("\nFeatures:")
        print("• 🧠 Content quality scoring with readability analysis")
        print("• 📱 Mobile-first indexing compliance checks")
        print("• 🏆 Competitive benchmarking and positioning")
        print("• 🔍 Intelligent schema markup recommendations")
        print("• ⚡ Page experience signals analysis")
        print("• 📊 Advanced performance metrics")
        print("• 🎯 AI-powered optimization recommendations")
        sys.exit(1)
    
    url = sys.argv[1]
    
    # Add https:// if not present
    if not url.startswith(('http://', 'https://')):
        url = 'https://' + url
    
    print(f"\n🎯 Target Website: {url}")
    print(f"🔍 Analysis Mode: Enterprise-Level Comprehensive Audit")
    
    # Initialize the advanced crawler
    try:
        crawler = ComprehensiveSEOCrawler()
        print(f"📁 Reports will be saved to: {crawler.seo_audits_folder}")
        
        # Run comprehensive analysis with all advanced features
        print(f"\n🚀 Starting advanced SEO analysis...")
        print("   This includes:")
        print("   • Technical infrastructure analysis")
        print("   • Content quality assessment with AI scoring")
        print("   • Mobile-first indexing compliance")
        print("   • Schema markup intelligence")
        print("   • Competitive positioning analysis")
        print("   • Page experience signals monitoring")
        
        analysis = crawler.comprehensive_analysis(url)
        
        # Generate the enhanced report
        print(f"\n📊 Generating enterprise-level audit report...")
        crawler.generate_comprehensive_markdown(analysis)
        
        print(f"\n✅ Advanced SEO audit completed successfully!")
        print(f"📄 Report saved to: {crawler.seo_audits_folder}")
        
        # Display key insights
        print(f"\n🔍 Key Insights:")
        print(f"   • Pages analyzed: {analysis.get('total_pages', 'N/A')}")
        if 'seo_issues' in analysis:
            print(f"   • SEO issues found: {len(analysis['seo_issues'])}")
        else:
            print(f"   • SEO issues found: Analysis in progress")
        
        if 'competitive_analysis' in analysis:
            comp_score = analysis['competitive_analysis']['competitive_score']
            print(f"   • Competitive score: {comp_score:.1f}/100")
            
            if comp_score >= 80:
                print(f"   • 🏆 Excellent competitive positioning")
            elif comp_score >= 60:
                print(f"   • 📊 Good foundation with improvement opportunities")
            else:
                print(f"   • 🚀 High potential for ranking improvements")
        
        # Advanced recommendations
        if analysis.get('recommendations'):
            print(f"\n🎯 Top Recommendations:")
            for i, rec in enumerate(analysis['recommendations'][:3], 1):
                print(f"   {i}. {rec}")
        
        print(f"\n📈 Next Steps:")
        print(f"   1. Review the detailed audit report in your Obsidian vault")
        print(f"   2. Prioritize critical issues for immediate attention")
        print(f"   3. Implement mobile-first optimizations")
        print(f"   4. Enhance content quality based on AI analysis")
        print(f"   5. Monitor competitive positioning improvements")
        
    except Exception as e:
        print(f"\n❌ Error during advanced analysis: {str(e)}")
        print(f"💡 Troubleshooting tips:")
        print(f"   • Ensure the website is accessible")
        print(f"   • Check your internet connection")
        print(f"   • Verify the URL is correct")
        print(f"   • Install required dependencies: pip install -r requirements.txt")
        sys.exit(1)

if __name__ == "__main__":
    main() 