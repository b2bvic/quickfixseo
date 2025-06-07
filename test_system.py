#!/usr/bin/env python3
"""
System Test Script for QuickFixSEO
A product of Scale With Search (https://scalewithsearch.com)
Created by Victor Valentine Romo (@b2bvic)

Tests all major components to ensure everything is working correctly.
"""

import sys
import os
from pathlib import Path

def test_imports():
    """Test all required module imports"""
    print("🧪 Testing module imports...")
    
    try:
        import requests
        import bs4
        import urllib3
        import textstat
        from dotenv import load_dotenv
        from google.auth.transport.requests import Request
        from googleapiclient.discovery import build
        print("✅ All required modules imported successfully")
        return True
    except ImportError as e:
        print(f"❌ Import error: {e}")
        return False

def test_main_modules():
    """Test main SEO audit modules"""
    print("\n🧪 Testing main modules...")
    
    try:
        import obsidian_seo_crawler
        import intelligent_crawler
        import intelligent_crawler_local
        import setup_dev
        print("✅ All main modules imported successfully")
        return True
    except ImportError as e:
        print(f"❌ Main module import error: {e}")
        return False

def test_configuration():
    """Test configuration files"""
    print("\n🧪 Testing configuration...")
    
    try:
        import dev_config
        dev_config.validate_dev_config()
        print("✅ Configuration validated")
        return True
    except Exception as e:
        print(f"❌ Configuration error: {e}")
        return False

def test_shell_scripts():
    """Test shell script syntax"""
    print("\n🧪 Testing shell scripts...")
    
    scripts = [
        'smart_audit.sh',
        'smart_audit_local.sh',
        'run_seo_audit.sh',
        'run_client_audits.sh',
        'single_client_audit.sh'
    ]
    
    all_good = True
    for script in scripts:
        if Path(script).exists():
            # Test syntax with bash -n
            result = os.system(f"bash -n {script}")
            if result == 0:
                print(f"✅ {script} syntax OK")
            else:
                print(f"❌ {script} syntax error")
                all_good = False
        else:
            print(f"⚠️  {script} not found")
    
    return all_good

def test_permissions():
    """Test file permissions"""
    print("\n🧪 Testing file permissions...")
    
    scripts = ['smart_audit.sh', 'smart_audit_local.sh', 'run_seo_audit.sh']
    all_good = True
    
    for script in scripts:
        if Path(script).exists():
            if os.access(script, os.X_OK):
                print(f"✅ {script} is executable")
            else:
                print(f"❌ {script} is not executable")
                all_good = False
    
    return all_good

def main():
    """Run all tests"""
    print("🚀 QuickFixSEO System Test")
    print("=" * 50)
    
    tests = [
        test_imports,
        test_main_modules,
        test_configuration,
        test_shell_scripts,
        test_permissions
    ]
    
    results = []
    for test in tests:
        results.append(test())
    
    print("\n" + "=" * 50)
    print("📊 Test Results:")
    
    passed = sum(results)
    total = len(results)
    
    if passed == total:
        print(f"🎉 All tests passed! ({passed}/{total})")
        print("\n✅ Your QuickFixSEO system is ready to use!")
        return 0
    else:
        print(f"⚠️  {passed}/{total} tests passed")
        print(f"❌ {total - passed} tests failed")
        print("\n🔧 Please fix the issues above before using the system.")
        return 1

if __name__ == "__main__":
    sys.exit(main()) 