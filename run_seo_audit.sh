#!/bin/bash
# Sample script to run Obsidian SEO Analyzer
# Usage: ./run_seo_audit.sh example.com

if [ $# -eq 0 ]; then
    echo "Usage: $0 <website_url>"
    echo "Example: $0 example.com"
    exit 1
fi

echo "🚀 Running SEO audit for: $1"
python3 obsidian_seo_analyzer.py "$1"
