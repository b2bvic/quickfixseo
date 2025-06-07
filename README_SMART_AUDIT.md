# 🕷️ Smart SEO Audit System

An intelligent Screaming Frog crawler that automatically analyzes websites, sets optimal parameters, and uploads results directly to Google Drive with organized folder structure.

## ✨ Features

- **🧠 Intelligent Parameter Detection**: Automatically analyzes website structure and sets optimal crawl parameters
- **🔍 Website Analysis**: Detects CMS, e-commerce, blog, JavaScript usage, and more
- **📊 CSV Export**: All results in CSV format for easy analysis
- **☁️ Google Drive Integration**: Direct upload to victor@scalewithsearch.com workspace
- **📁 Organized Structure**: `Shared Drive > Client Folder > Audit Folder`
- **📅 Timestamped Files**: `YYYY-MM-DD_HH-MM-SS_filename.csv`
- **🚀 One-Command Execution**: Just input a URL and everything is handled automatically

## 🚀 Quick Start

1. **Setup Google Drive API** (one-time setup):
   ```bash
   ./smart_audit.sh --setup
   ```

2. **Test Connection**:
   ```bash
   ./smart_audit.sh --test
   ```

3. **Run Your First Audit**:
   ```bash
   ./smart_audit.sh https://example.com
   ```

## 📋 Requirements

- **macOS** (tested on macOS 24.5.0)
- **Screaming Frog SEO Spider** (licensed version recommended)
- **Python 3.7+**
- **Google Workspace Account** with Drive access
- **Internet Connection**

## 🔧 Installation & Setup

### Step 1: Install Dependencies

```bash
# Install Python dependencies
pip install -r requirements.txt
```

### Step 2: Configure Google Drive API

1. **Run the setup wizard**:
   ```bash
   ./smart_audit.sh --setup
   ```

2. **Follow the instructions to**:
   - Create Google Cloud Project
   - Enable Google Drive API
   - Create OAuth2 credentials
   - Download `credentials.json`

3. **Verify setup**:
   ```bash
   ./smart_audit.sh --test
   ```

### Step 3: Make Scripts Executable

```bash
chmod +x smart_audit.sh
```

## 🎯 Usage

### Basic Usage

```bash
# Audit a website
./smart_audit.sh https://scalewithsearch.com

# Works with or without https://
./smart_audit.sh example.com
```

### Advanced Options

```bash
# Show help
./smart_audit.sh --help

# Setup Google Drive API
./smart_audit.sh --setup

# Test connection (full test)
./smart_audit.sh --test

# Quick connection test
./smart_audit.sh --test-quick
```

## 🧠 Intelligent Features

### Automatic Website Analysis

The system analyzes each website to determine:

- **CMS Detection**: WordPress, Shopify, Wix, Squarespace, etc.
- **Site Type**: E-commerce, blog, corporate, etc.
- **Technical Stack**: React, JavaScript-heavy sites
- **Size Estimation**: From sitemaps and structure
- **Special Features**: Multilingual, forms, etc.

### Smart Parameter Setting

Based on analysis, the system automatically configures:

- **Crawl Limits**: Adjusted based on site size
- **JavaScript Rendering**: For JS-heavy sites
- **Image Crawling**: For e-commerce sites
- **Form Crawling**: For complex sites
- **Sitemap Usage**: When available
- **Export Formats**: Always CSV for consistency

### Example Analysis Output

```
✅ Analysis complete:
   - Domain: scalewithsearch.com
   - CMS: wordpress
   - Estimated pages: 1,245
   - Has sitemap: true
   - E-commerce: false
   - JavaScript heavy: false
   - Crawl limit: 10,000
```

## 📁 Google Drive Organization

Files are automatically organized in Google Drive:

```
Shared Drive (victor@scalewithsearch.com)
├── scalewithsearch_com/
│   ├── Audit_2024-01-15_14-30-25/
│   │   ├── 2024-01-15_14-30-25_all_inlinks.csv
│   │   ├── 2024-01-15_14-30-25_all_outlinks.csv
│   │   ├── 2024-01-15_14-30-25_internal_html.csv
│   │   ├── 2024-01-15_14-30-25_images.csv
│   │   └── 2024-01-15_14-30-25_crawl.seospider
│   └── Audit_2024-01-20_09-15-42/
│       └── ...
└── example_com/
    └── Audit_2024-01-15_16-45-10/
        └── ...
```

## 🔍 Output Files

Each audit generates these CSV files:

- **`internal_html.csv`**: All internal HTML pages
- **`external_links.csv`**: External links found
- **`images.csv`**: Image analysis
- **`javascript.csv`**: JavaScript files
- **`stylesheets.csv`**: CSS files
- **`all_inlinks.csv`**: Inbound link analysis
- **`all_outlinks.csv`**: Outbound link analysis
- **`redirects.csv`**: Redirect chains
- **`page_titles.csv`**: Title tag analysis
- **`meta_description.csv`**: Meta description analysis
- **`h1.csv`**: H1 tag analysis
- **`h2.csv`**: H2 tag analysis
- **`crawl.seospider`**: Native Screaming Frog file

## ⚡ Performance

### Crawl Speed Optimization

- **Small sites (< 1,000 pages)**: ~2-5 minutes
- **Medium sites (1,000-10,000 pages)**: ~10-30 minutes  
- **Large sites (10,000+ pages)**: ~30-60 minutes

### Smart Limits

- **Default limit**: 10,000 pages
- **Large sites**: 25,000 pages
- **Enterprise sites**: 50,000 pages
- **Timeout**: 1 hour maximum

## 🛠️ Troubleshooting

### Common Issues

1. **"Google Drive credentials not found"**
   ```bash
   ./smart_audit.sh --setup
   # Follow the Google Drive API setup instructions
   ```

2. **"Screaming Frog not found"**
   - Install Screaming Frog SEO Spider from official website
   - Ensure it's in `/Applications/` folder

3. **"Authentication failed"**
   ```bash
   ./smart_audit.sh --test
   # Follow authentication prompts
   ```

4. **"No shared drives found"**
   - Ensure victor@scalewithsearch.com has shared drive access
   - Check Google Workspace permissions

### Debug Mode

For detailed debugging:

```bash
python intelligent_crawler.py https://example.com
```

### Log Files

Check these locations for logs:
- Screaming Frog logs: `~/Library/Application Support/Screaming Frog SEO Spider/`
- Python errors: Terminal output
- Google API errors: `token.json` issues

## 🔒 Security & Privacy

- **Credentials**: Stored locally in `credentials.json` and `token.json`
- **Data**: Only crawls public website data
- **Upload**: Direct to specified Google Workspace account
- **Cleanup**: Temporary files automatically removed

## 📈 Scaling for Agencies

### Bulk Processing

For multiple clients, you can run:

```bash
# Create a client list
echo "client1.com" > clients.txt
echo "client2.com" >> clients.txt

# Process each client
while read client; do
    ./smart_audit.sh "$client"
    sleep 60  # Wait between audits
done < clients.txt
```

### Team Workflow

1. **Account Setup**: Each team member needs Google Drive access
2. **Shared Credentials**: Use same `credentials.json` for team
3. **Folder Organization**: Each client gets own folder automatically
4. **Audit History**: All audits timestamped and preserved

## 🔄 Updates & Maintenance

### Updating Dependencies

```bash
pip install --upgrade -r requirements.txt
```

### Updating Screaming Frog

1. Download latest version from official website
2. Replace existing installation
3. Test with: `./smart_audit.sh --test-quick`

## 📞 Support

### Getting Help

1. **Check logs**: Review terminal output for errors
2. **Test components**: Use `--test` flag to isolate issues
3. **Verify setup**: Re-run `--setup` if needed

### Common Solutions

- **Rate limits**: Wait and retry
- **Large sites**: May need manual parameter adjustment
- **Network issues**: Check internet connection
- **Permission errors**: Verify Google Drive access

## 🎉 Success Metrics

After setup, you should see:

- ✅ Automated parameter detection
- ✅ Consistent CSV exports
- ✅ Organized Google Drive structure
- ✅ Timestamped audit history
- ✅ One-command operation

**Ready to transform your SEO audit workflow!** 🚀 