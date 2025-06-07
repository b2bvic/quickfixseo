#!/bin/bash
#
# Smart SEO Audit Script
# Wrapper for the intelligent Python crawler with Google Drive integration
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
    echo "🕷️  Smart SEO Audit with Google Drive Integration"
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
        echo "• ☁️  Direct Google Drive upload"
        echo "• 📁 Organized folder structure"
        echo "• 📅 Timestamped audit files"
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
    
    # Check if requirements are installed
    print_info "Checking dependencies..."
    if ! $PYTHON_CMD -c "import google.auth" &> /dev/null; then
        print_warning "Google API dependencies not found!"
        print_info "Installing dependencies..."
        
        if [ -f "requirements.txt" ]; then
            $PYTHON_CMD -m pip install -r requirements.txt
            if [ $? -ne 0 ]; then
                print_error "Failed to install dependencies!"
                print_info "Try running: pip install -r requirements.txt"
                exit 1
            fi
            print_status "Dependencies installed successfully"
        else
            print_error "requirements.txt not found!"
            exit 1
        fi
    else
        print_status "Dependencies are installed"
    fi
    
    # Check if credentials are set up
    if [ ! -f "credentials.json" ]; then
        print_error "Google Drive credentials not found!"
        print_info "Please set up Google Drive API credentials first:"
        print_info "$PYTHON_CMD setup_google_drive.py"
        exit 1
    fi
    
    print_status "Google Drive credentials found"
    echo ""
    
    # Run the intelligent crawler
    print_info "Starting intelligent SEO audit..."
    echo ""
    
    $PYTHON_CMD intelligent_crawler.py "$URL"
    
    # Check if the crawl was successful
    if [ $? -eq 0 ]; then
        echo ""
        print_status "Smart audit completed successfully! 🎉"
        print_info "Check Google Drive for your organized audit results"
    else
        echo ""
        print_error "Smart audit failed!"
        print_info "Check the error messages above for troubleshooting"
        exit 1
    fi
}

# Help function
show_help() {
    echo "🕷️  Smart SEO Audit Script"
    echo ""
    echo "USAGE:"
    echo "  $0 <website_url>              Run smart audit"
    echo "  $0 --setup                    Show setup instructions"
    echo "  $0 --test                     Test Google Drive connection"
    echo "  $0 --test-quick               Quick connection test"
    echo "  $0 --help                     Show this help"
    echo ""
    echo "FEATURES:"
    echo "• Intelligent crawl parameter detection"
    echo "• Automatic website structure analysis"
    echo "• CSV format export"
    echo "• Direct Google Drive upload"
    echo "• Organized folder structure: Client > Audit_YYYY-MM-DD_HH-MM-SS"
    echo "• Timestamped file names"
    echo ""
    echo "EXAMPLES:"
    echo "  $0 https://scalewithsearch.com"
    echo "  $0 example.com"
    echo ""
    echo "SETUP:"
    echo "1. Run: $0 --setup"
    echo "2. Follow the Google Drive API setup instructions"
    echo "3. Run: $0 --test"
    echo "4. Start auditing: $0 <your-website>"
}

# Handle command line arguments
case "${1:-}" in
    --help|-h)
        show_help
        ;;
    --setup)
        PYTHON_CMD=$(get_python_cmd)
        $PYTHON_CMD setup_google_drive.py
        ;;
    --test)
        PYTHON_CMD=$(get_python_cmd)
        $PYTHON_CMD test_drive_connection.py
        ;;
    --test-quick)
        PYTHON_CMD=$(get_python_cmd)
        $PYTHON_CMD test_drive_connection.py --quick
        ;;
    "")
        show_help
        exit 1
        ;;
    *)
        main "$@"
        ;;
esac 