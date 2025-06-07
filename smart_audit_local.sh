#!/bin/bash
#
# Smart SEO Audit Script - Local Version
# Intelligent Screaming Frog crawler that saves locally for manual upload
#

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Function to print colored output
print_status() {
    echo -e "${GREEN}✅ $1${NC}"
}

print_error() {
    echo -e "${RED}❌ $1${NC}"
}

print_warning() {
    echo -e "${YELLOW}⚠️  $1${NC}"
}

print_info() {
    echo -e "${BLUE}ℹ️  $1${NC}"
}

# Function to check if Python 3 is available
check_python() {
    if command -v python3 &> /dev/null; then
        return 0
    elif command -v python &> /dev/null; then
        # Check if python is actually python3
        python_version=$(python --version 2>&1)
        if [[ $python_version == *"Python 3"* ]]; then
            return 0
        fi
    fi
    return 1
}

# Function to get the correct Python command
get_python_cmd() {
    if command -v python3 &> /dev/null; then
        echo "python3"
    else
        echo "python"
    fi
}

# Main script
main() {
    echo "🕷️  Smart SEO Audit - Local Version"
    echo "=================================================="
    echo ""
    
    # Check if URL is provided
    if [ $# -eq 0 ]; then
        echo "Usage: $0 <website_url>"
        echo ""
        echo "Examples:"
        echo "  $0 https://example.com"
        echo "  $0 example.com"
        echo ""
        echo "Features:"
        echo "• 🧠 Intelligent parameter detection"
        echo "• 🔍 Automatic website analysis"
        echo "• 📊 CSV export format"
        echo "• 💾 Local organized storage"
        echo "• 📁 Ready for manual upload structure"
        echo "• 📅 Timestamped audit files"
        echo "• 📂 Auto-opens results in Finder"
        echo ""
        exit 1
    fi
    
    URL="$1"
    
    # Add https:// if not present
    if [[ ! "$URL" =~ ^https?:// ]]; then
        URL="https://$URL"
        print_info "Added https:// prefix: $URL"
    fi
    
    echo "🎯 Target URL: $URL"
    echo ""
    
    # Check Python installation
    print_info "Checking Python installation..."
    if ! check_python; then
        print_error "Python 3 is required but not found!"
        print_info "Please install Python 3: https://www.python.org/downloads/"
        exit 1
    fi
    
    PYTHON_CMD=$(get_python_cmd)
    print_status "Python 3 found: $PYTHON_CMD"
    
    # Check if basic requirements are installed
    print_info "Checking dependencies..."
    if ! $PYTHON_CMD -c "import requests, bs4" &> /dev/null; then
        print_warning "Required dependencies not found!"
        print_info "Installing basic dependencies..."
        
        $PYTHON_CMD -m pip install requests beautifulsoup4
        if [ $? -ne 0 ]; then
            print_error "Failed to install dependencies!"
            print_info "Try running: pip install requests beautifulsoup4"
            exit 1
        fi
        print_status "Dependencies installed successfully"
    else
        print_status "Dependencies are installed"
    fi
    
    # Check if Screaming Frog is available
    SCREAMINGFROG_PATH="/Applications/Screaming Frog SEO Spider.app/Contents/MacOS/ScreamingFrogSEOSpiderLauncher"
    if [ ! -f "$SCREAMINGFROG_PATH" ]; then
        print_error "Screaming Frog SEO Spider not found!"
        print_info "Please install Screaming Frog from: https://www.screamingfrog.co.uk/"
        exit 1
    fi
    
    print_status "Screaming Frog SEO Spider found"
    echo ""
    
    # Run the intelligent crawler
    print_info "Starting intelligent SEO audit (local version)..."
    echo ""
    
    $PYTHON_CMD intelligent_crawler_local.py "$URL"
    
    # Check if the crawl was successful
    if [ $? -eq 0 ]; then
        echo ""
        print_status "Smart audit completed successfully! 🎉"
        print_info "Files are organized and ready for manual upload"
        print_info "Check your Desktop/SEO_Audits folder"
    else
        echo ""
        print_error "Smart audit failed!"
        print_info "Check the error messages above for troubleshooting"
        exit 1
    fi
}

# Help function
show_help() {
    echo "🕷️  Smart SEO Audit Script - Local Version"
    echo ""
    echo "USAGE:"
    echo "  $0 <website_url>              Run smart audit locally"
    echo "  $0 --help                     Show this help"
    echo ""
    echo "FEATURES:"
    echo "• Intelligent crawl parameter detection"
    echo "• Automatic website structure analysis"
    echo "• CSV format export"
    echo "• Local organized storage (Desktop/SEO_Audits)"
    echo "• Folder structure: Client_Name > Audit_YYYY-MM-DD_HH-MM-SS"
    echo "• Timestamped file names"
    echo "• Audit summary with upload instructions"
    echo "• Auto-opens results folder in Finder"
    echo ""
    echo "OUTPUT LOCATION:"
    echo "  ~/Desktop/SEO_Audits/client_name/Audit_YYYY-MM-DD_HH-MM-SS/"
    echo ""
    echo "EXAMPLES:"
    echo "  $0 https://scalewithsearch.com"
    echo "  $0 example.com"
    echo ""
    echo "MANUAL UPLOAD:"
    echo "After audit completion:"
    echo "1. Results folder opens automatically in Finder"
    echo "2. Drag and drop files to Google Drive"
    echo "3. Follow folder structure in audit summary"
    echo ""
    echo "NO GOOGLE DRIVE SETUP REQUIRED!"
    echo "Perfect for when you prefer manual control over uploads."
}

# Handle command line arguments
case "${1:-}" in
    --help|-h)
        show_help
        ;;
    "")
        show_help
        exit 1
        ;;
    *)
        main "$@"
        ;;
esac 