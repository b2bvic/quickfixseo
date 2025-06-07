#!/bin/bash
#
# Screaming Frog Client Audit Script
# Each client gets their own folder, each crawl gets a dated subfolder
#

# --- CUSTOMIZE THIS SECTION ---
# Add your client websites here (one per line)
CLIENTS=(
  "https://example-client1.com"
  "https://example-client2.com"
  "https://example-client3.com"
)

# Main directory for all client audits
AUDIT_PARENT_DIR="$HOME/Documents/Client_Audits"

# Optional: Path to your standard configuration file
# Create this first in Screaming Frog app, then save it to ~/Documents/SF-Configs/
# STANDARD_CONFIG="$HOME/Documents/SF-Configs/Standard_Config.seospiderconfig"
# --- END CUSTOMIZATION ---

# Get current date for folder naming (format: 2025-06-07)
TODAY=$(date +%Y-%m-%d)
TIMESTAMP=$(date +%Y-%m-%d_%H-%M-%S)

echo "🕷️  Starting Screaming Frog Client Audits"
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

# Loop through each client
for client in "${CLIENTS[@]}"; do
    # Skip empty lines or comments
    if [[ -z "$client" || "$client" == \#* ]]; then
        continue
    fi
    
    # Extract domain name for folder naming
    DOMAIN=$(echo "$client" | sed -E 's|https?://||' | sed -E 's|www\.||' | sed -E 's|/.*||' | sed -E 's|\.|_|g')
    
    # Create client folder structure: ~/Documents/Client_Audits/client_com/2025-06-07/
    CLIENT_DIR="$AUDIT_PARENT_DIR/$DOMAIN"
    OUTPUT_DIR="$CLIENT_DIR/$TODAY"
    
    echo ""
    echo "🎯 CRAWLING: $client"
    echo "📁 Client folder: $CLIENT_DIR"
    echo "📂 Output folder: $OUTPUT_DIR"
    
    # Create the directory structure
    mkdir -p "$OUTPUT_DIR"
    
    # Basic crawl command (modify as needed)
    echo "⏳ Starting crawl..."
    "$SCREAMINGFROG_PATH" --crawl "$client" \
                  --headless \
                  --output-folder "$OUTPUT_DIR" \
                  --export-format csv \
                  --save-crawl
    
    # Check if crawl was successful
    if [ $? -eq 0 ]; then
        echo "✅ SUCCESS: Crawl completed for $client"
        echo "📊 Results saved to: $OUTPUT_DIR"
        
        # Create a summary file
        echo "Crawl Summary" > "$OUTPUT_DIR/crawl_info.txt"
        echo "=============" >> "$OUTPUT_DIR/crawl_info.txt"
        echo "Website: $client" >> "$OUTPUT_DIR/crawl_info.txt"
        echo "Date: $TODAY" >> "$OUTPUT_DIR/crawl_info.txt"
        echo "Timestamp: $TIMESTAMP" >> "$OUTPUT_DIR/crawl_info.txt"
        echo "Output Directory: $OUTPUT_DIR" >> "$OUTPUT_DIR/crawl_info.txt"
        
    else
        echo "❌ ERROR: Crawl failed for $client"
    fi
    
    echo "-------------------------------------------------"
done

echo ""
echo "🎉 All client audits completed!"
echo "📁 Results are organized in: $AUDIT_PARENT_DIR"
echo ""
echo "Each client has their own folder with dated subfolders:"
echo "   Client_Audits/"
echo "   ├── client1_com/"
echo "   │   └── $TODAY/"
echo "   ├── client2_com/"
echo "   │   └── $TODAY/"
echo "   └── ..." 