# 🚀 Obsidian SEO Analyzer

**Transform your SEO workflow with intelligent analysis directly into your Obsidian vault**

## 📋 Overview

The Obsidian SEO Analyzer is a streamlined, intelligent SEO audit system that generates comprehensive markdown reports directly into your Obsidian vault. No CSV exports, no API dependencies, no complex setups—just intelligent analysis that flows seamlessly into your note-taking workflow.

## ✨ Key Features

- **🤖 Intelligent Website Analysis**: Automatic CMS detection, content analysis, and SEO scoring
- **📝 Direct Obsidian Integration**: Reports saved directly to your vault as formatted markdown
- **🎯 Zero Configuration**: No API keys, no account setups, just install and run
- **📊 Comprehensive Reports**: Executive summaries, technical analysis, and actionable recommendations
- **🔧 Platform-Aware**: Customized recommendations based on detected CMS (WordPress, Shopify, React, etc.)
- **⚡ Fast & Efficient**: Single-command operation with intelligent defaults

## 🚀 Quick Start

### 1. Setup (One-time)
```bash
# Run the setup script
python3 setup_obsidian_seo.py
```

### 2. Run Your First Audit
```bash
# Method 1: Direct command
python3 obsidian_seo_analyzer.py example.com

# Method 2: Using the helper script
./run_seo_audit.sh example.com
```

### 3. Find Your Report
The system will automatically:
- Detect or prompt for your Obsidian vault location
- Create a "SEO Audits" folder in your vault
- Save the comprehensive report as a markdown file
- Organize reports by domain and date

## 📁 Report Structure

Each SEO audit generates a beautifully formatted markdown report with:

### 🎯 Executive Summary
- Overall SEO health score
- Key findings and priorities
- Business impact assessment

### 🔧 Technical Analysis
- **Meta Tags**: Title tags, descriptions, H1 analysis
- **Content Structure**: Word count, quality assessment, link analysis
- **Platform Detection**: CMS identification and specific recommendations

### 📊 Content Analysis
- Content depth and quality evaluation
- Image optimization opportunities
- Internal linking assessment

### 🎯 Action-Oriented Recommendations
- **Immediate Actions** (High Priority)
- **Medium Priority** improvements
- **Platform-Specific** optimizations

### 📅 Implementation Roadmap
- Week 1: Foundation fixes
- Week 2-3: Content optimization
- Week 4+: Advanced improvements
- Ongoing monitoring checklist

## 🎛️ Advanced Usage

### Custom Obsidian Vault Path
```python
from obsidian_seo_analyzer import ObsidianSEOAnalyzer

# Specify custom vault path
analyzer = ObsidianSEOAnalyzer("/path/to/your/obsidian/vault")
analyzer.run_intelligent_audit("example.com")
```

### Batch Processing Multiple Sites
```bash
# Create a simple batch script
for site in example.com client1.com client2.com; do
    echo "Auditing $site..."
    python3 obsidian_seo_analyzer.py "$site"
done
```

## 🔍 What Gets Analyzed

### Automatic Detection
- **CMS Platforms**: WordPress, Shopify, React, Squarespace, and more
- **E-commerce Signals**: Shopping carts, product pages, checkout flows
- **Blog Presence**: Content management, posting patterns
- **JavaScript Usage**: SPA detection, rendering requirements

### SEO Elements
- Title tags and meta descriptions
- Header structure (H1-H6)
- Content depth and quality
- Internal/external linking
- Image optimization
- Sitemap presence
- Mobile responsiveness indicators

### Technical Analysis
- Page structure assessment
- Loading performance indicators
- Crawlability evaluation
- Schema markup detection

## 📂 File Organization

Your Obsidian vault will be organized as:
```
📁 Your Obsidian Vault/
└── 📁 SEO Audits/
    ├── 📄 example.com_SEO_Audit_2024-01-15.md
    ├── 📄 client-site.com_SEO_Audit_2024-01-16.md
    └── 📄 another-domain.com_SEO_Audit_2024-01-17.md
```

## 🔧 Customization Options

### Vault Location Setup
On first run, the system will guide you through:
1. Auto-detection of common Obsidian locations
2. Custom path specification
3. Desktop fallback option

### Report Customization
The system generates reports optimized for:
- **Obsidian linking**: Proper markdown formatting
- **Mobile viewing**: Clean, responsive layout
- **Action tracking**: Checkbox lists for task management
- **Visual clarity**: Emojis and formatting for quick scanning

## 🎯 Perfect For

- **SEO Consultants**: Client audit workflows
- **Digital Agencies**: Streamlined reporting
- **Content Creators**: Website optimization
- **Small Business Owners**: DIY SEO insights
- **Web Developers**: Technical SEO validation

## 🆚 Why Choose This Over Screaming Frog?

| Feature | Obsidian SEO Analyzer | Screaming Frog |
|---------|----------------------|----------------|
| **Setup Time** | < 1 minute | 15-30 minutes |
| **Learning Curve** | Minimal | Steep |
| **Output Format** | Obsidian markdown | CSV exports |
| **Automation** | Fully automated | Manual configuration |
| **Cost** | Free | Paid for full features |
| **Integration** | Direct to notes | External tools needed |

## 🛠️ System Requirements

- **Python 3.7+**
- **Internet connection** (for website analysis)
- **Optional**: Obsidian app for enhanced experience

## 📞 Support & Troubleshooting

### Common Issues

**"No module named 'requests'"**
```bash
pip3 install requests beautifulsoup4
```

**"Permission denied"**
```bash
chmod +x run_seo_audit.sh
```

**"Obsidian vault not found"**
- The system will prompt you to specify your vault location
- You can also save reports to Desktop as fallback

### Getting Help
The system includes extensive error handling and user guidance. Most issues are resolved through the interactive prompts during setup.

## 🎉 Success Stories

Transform your SEO workflow from:
- ❌ Manual Screaming Frog configuration
- ❌ CSV export management
- ❌ Report compilation in separate tools
- ❌ Client delivery complexity

To:
- ✅ One-command intelligent analysis
- ✅ Automatic Obsidian integration
- ✅ Professional markdown reports
- ✅ Instant client sharing

---

**Ready to revolutionize your SEO workflow?** 

Run `python3 setup_obsidian_seo.py` to get started in under a minute! 🚀 