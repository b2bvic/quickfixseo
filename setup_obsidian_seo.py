#!/usr/bin/env python3
"""
Setup script for Obsidian SEO Analyzer
Installs dependencies and guides first-time setup
"""

import os
import sys
import subprocess

def install_dependencies():
    """Install required Python packages"""
    print("📦 Installing required dependencies...")
    
    try:
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', 
                              'requests', 'beautifulsoup4', 'pathlib'])
        print("✅ Dependencies installed successfully!")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Error installing dependencies: {e}")
        return False

def check_obsidian():
    """Check if Obsidian is available and guide setup"""
    print("\n🔍 Checking for Obsidian...")
    
    # Common Obsidian vault locations
    common_paths = [
        os.path.expanduser("~/Documents/Obsidian Vault"),
        os.path.expanduser("~/Obsidian"),
        os.path.expanduser("~/Documents/Notes"),
        os.path.expanduser("~/Desktop/Obsidian")
    ]
    
    found_vaults = []
    for path in common_paths:
        if os.path.exists(path):
            found_vaults.append(path)
    
    if found_vaults:
        print(f"✅ Found {len(found_vaults)} potential Obsidian vault(s):")
        for vault in found_vaults:
            print(f"   - {vault}")
    else:
        print("ℹ️  No common Obsidian vaults found.")
        print("   The analyzer will prompt you to set up your vault location on first run.")
    
    return True

def create_sample_run_script():
    """Create a sample run script"""
    script_content = '''#!/bin/bash
# Sample script to run Obsidian SEO Analyzer
# Usage: ./run_seo_audit.sh example.com

if [ $# -eq 0 ]; then
    echo "Usage: $0 <website_url>"
    echo "Example: $0 example.com"
    exit 1
fi

echo "🚀 Running SEO audit for: $1"
python3 obsidian_seo_analyzer.py "$1"
'''
    
    with open('run_seo_audit.sh', 'w') as f:
        f.write(script_content)
    
    # Make executable
    os.chmod('run_seo_audit.sh', 0o755)
    print("✅ Created run_seo_audit.sh script")

def main():
    print("🔧 OBSIDIAN SEO ANALYZER SETUP")
    print("=" * 50)
    
    # Install dependencies
    if not install_dependencies():
        sys.exit(1)
    
    # Check Obsidian setup
    check_obsidian()
    
    # Create helper script
    create_sample_run_script()
    
    print("\n🎉 SETUP COMPLETE!")
    print("=" * 50)
    print("Your Obsidian SEO Analyzer is ready to use!")
    print("\n📋 Quick Start:")
    print("1. Run: python3 obsidian_seo_analyzer.py example.com")
    print("2. Or use: ./run_seo_audit.sh example.com")
    print("\n📝 Features:")
    print("• Intelligent website analysis")
    print("• Automatic CMS detection")
    print("• SEO recommendations")
    print("• Direct Obsidian vault integration")
    print("• No API keys required")
    print("• Markdown-formatted reports")
    
    print("\n🚀 Ready to audit your first website?")
    test_url = input("Enter a website to test (or press Enter to skip): ").strip()
    
    if test_url:
        print(f"\n🎯 Running test audit for: {test_url}")
        try:
            subprocess.run([sys.executable, 'obsidian_seo_analyzer.py', test_url])
        except KeyboardInterrupt:
            print("\n👋 Setup complete! Run the analyzer anytime with your target URL.")

if __name__ == "__main__":
    main() 