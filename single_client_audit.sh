#!/bin/bash
#
# Single Client Screaming Frog Audit Script
# Quick audit for one client with dated folder structure
#

# Check if URL is provided as argument
if [ $# -eq 0 ]; then
    echo "🕷️  Single Client Screaming Frog Audit"
    echo ""
    echo "Usage: ./single_client_audit.sh <website_url>"
    echo "Example: ./single_client_audit.sh https://example.com"
    echo ""
    exit 1
fi

# Get the website URL from command line argument
CLIENT_URL="$1"
AUDIT_PARENT_DIR="$HOME/Documents/Client_Audits"

# Get current date for folder naming
TODAY=$(date +%Y-%m-%d)
TIMESTAMP=$(date +%Y-%m-%d_%H-%M-%S)

echo "🕷️  Starting Single Client Audit"
echo "🎯 Website: $CLIENT_URL"
echo "📅 Date: $TODAY"
echo "================================================="

# Set the direct path to Screaming Frog
SCREAMINGFROG_PATH="/Applications/Screaming Frog SEO Spider.app/Contents/MacOS/ScreamingFrogSEOSpiderLauncher"

# Check if Screaming Frog is available
if [ ! -f "$SCREAMINGFROG_PATH" ]; then
    echo "❌ ERROR: Screaming Frog not found at expected location!"
    echo "Please make sure Screaming Frog SEO Spider is installed in Applications folder."
    exit 1
fi

# Extract domain name for folder naming
DOMAIN=$(echo "$CLIENT_URL" | sed -E 's|https?://||' | sed -E 's|www\.||' | sed -E 's|/.*||' | sed -E 's|\.|_|g')

# Create folder structure
CLIENT_DIR="$AUDIT_PARENT_DIR/$DOMAIN"
OUTPUT_DIR="$CLIENT_DIR/$TODAY"

echo ""
echo "📁 Client folder: $CLIENT_DIR"
echo "📂 Output folder: $OUTPUT_DIR"
echo ""

# Create the directory structure
mkdir -p "$OUTPUT_DIR"

# Run the crawl
echo "⏳ Starting crawl for $CLIENT_URL..."
echo "This may take several minutes depending on site size..."
echo ""

"$SCREAMINGFROG_PATH" --crawl "$CLIENT_URL" \
              --headless \
              --output-folder "$OUTPUT_DIR" \
              --export-format csv \
              --save-crawl

# Check if crawl was successful
if [ $? -eq 0 ]; then
    echo ""
    echo "✅ SUCCESS: Crawl completed!"
    echo "📊 Results saved to: $OUTPUT_DIR"
    
    # Create a summary file
    echo "Single Client Crawl Summary" > "$OUTPUT_DIR/crawl_info.txt"
    echo "===========================" >> "$OUTPUT_DIR/crawl_info.txt"
    echo "Website: $CLIENT_URL" >> "$OUTPUT_DIR/crawl_info.txt"
    echo "Date: $TODAY" >> "$OUTPUT_DIR/crawl_info.txt"
    echo "Timestamp: $TIMESTAMP" >> "$OUTPUT_DIR/crawl_info.txt"
    echo "Output Directory: $OUTPUT_DIR" >> "$OUTPUT_DIR/crawl_info.txt"
    
    # List the generated files
    echo ""
    echo "📋 Generated files:"
    ls -la "$OUTPUT_DIR" | grep -E '\.(csv|seospider)$'
    
    echo ""
    echo "🎉 Audit complete! You can find all results in:"
    echo "   $OUTPUT_DIR"
    
else
    echo ""
    echo "❌ ERROR: Crawl failed for $CLIENT_URL"
    exit 1
fi 