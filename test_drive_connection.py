#!/usr/bin/env python3
"""
Test Google Drive Connection
Verifies that the Google Drive API is set up correctly
"""

import os
import sys
from datetime import datetime

# Add the current directory to the path so we can import our crawler
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

try:
    from intelligent_crawler import IntelligentCrawler
except ImportError as e:
    print(f"❌ Error importing intelligent_crawler: {e}")
    print("Make sure all dependencies are installed: pip install -r requirements.txt")
    sys.exit(1)

def test_authentication():
    """Test Google Drive authentication"""
    print("🔐 Testing Google Drive authentication...")
    
    crawler = IntelligentCrawler()
    
    try:
        success = crawler.authenticate_google_drive()
        if success:
            print("✅ Authentication successful!")
            return True
        else:
            print("❌ Authentication failed!")
            return False
    except Exception as e:
        print(f"❌ Authentication error: {str(e)}")
        return False

def test_shared_drive_access():
    """Test access to shared drives"""
    print("📁 Testing shared drive access...")
    
    crawler = IntelligentCrawler()
    
    try:
        # First authenticate
        if not crawler.authenticate_google_drive():
            print("❌ Cannot test shared drive - authentication failed")
            return False
        
        # Then try to find shared drive
        drive_id = crawler.find_shared_drive()
        if drive_id:
            print("✅ Shared drive access successful!")
            return True
        else:
            print("❌ No shared drives found or access denied")
            return False
    except Exception as e:
        print(f"❌ Shared drive error: {str(e)}")
        return False

def test_folder_creation():
    """Test creating folders in shared drive"""
    print("📂 Testing folder creation...")
    
    crawler = IntelligentCrawler()
    
    try:
        # Authenticate and get shared drive
        if not crawler.authenticate_google_drive():
            print("❌ Cannot test folder creation - authentication failed")
            return False
        
        if not crawler.find_shared_drive():
            print("❌ Cannot test folder creation - no shared drive found")
            return False
        
        # Try to create test folder structure
        test_client = "TEST_CLIENT_DELETE_ME"
        test_timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        
        folder_id = crawler.create_drive_folder_structure(test_client, test_timestamp)
        
        if folder_id:
            print("✅ Folder creation successful!")
            print(f"   Created: {test_client}/Audit_{test_timestamp}")
            print("   You can delete this test folder from Google Drive")
            return True
        else:
            print("❌ Folder creation failed!")
            return False
            
    except Exception as e:
        print(f"❌ Folder creation error: {str(e)}")
        return False

def test_website_analysis():
    """Test website analysis functionality"""
    print("🔍 Testing website analysis...")
    
    crawler = IntelligentCrawler()
    test_url = "https://example.com"
    
    try:
        analysis = crawler.analyze_website(test_url)
        
        if analysis and analysis.get('domain'):
            print("✅ Website analysis successful!")
            print(f"   Domain: {analysis['domain']}")
            print(f"   CMS detected: {analysis.get('cms_detected', 'None')}")
            print(f"   Has sitemap: {analysis.get('has_sitemap', False)}")
            print(f"   Estimated pages: {analysis.get('estimated_pages', 0)}")
            return True
        else:
            print("❌ Website analysis failed!")
            return False
            
    except Exception as e:
        print(f"❌ Website analysis error: {str(e)}")
        return False

def run_all_tests():
    """Run all tests in sequence"""
    print("🧪 Running Google Drive Integration Tests")
    print("=" * 50)
    print()
    
    tests = [
        ("Authentication", test_authentication),
        ("Shared Drive Access", test_shared_drive_access),
        ("Folder Creation", test_folder_creation),
        ("Website Analysis", test_website_analysis)
    ]
    
    results = {}
    
    for test_name, test_func in tests:
        print(f"\n🔬 Test: {test_name}")
        print("-" * 30)
        
        try:
            results[test_name] = test_func()
        except Exception as e:
            print(f"❌ Test failed with exception: {str(e)}")
            results[test_name] = False
        
        print()
    
    # Summary
    print("📊 Test Results Summary")
    print("=" * 50)
    
    passed = sum(results.values())
    total = len(results)
    
    for test_name, result in results.items():
        status = "✅ PASS" if result else "❌ FAIL"
        print(f"{test_name:<20} {status}")
    
    print()
    print(f"Overall: {passed}/{total} tests passed")
    
    if passed == total:
        print("🎉 All tests passed! Your setup is ready.")
        print()
        print("You can now run:")
        print("python intelligent_crawler.py https://example.com")
    else:
        print("❌ Some tests failed. Please check the setup:")
        print("python setup_google_drive.py")
    
    return passed == total

def main():
    if len(sys.argv) > 1 and sys.argv[1] == "--quick":
        # Quick test - just authentication and shared drive
        print("🚀 Quick Connection Test")
        print("=" * 30)
        
        auth_ok = test_authentication()
        if auth_ok:
            drive_ok = test_shared_drive_access()
            if drive_ok:
                print("\n✅ Quick test passed! Connection is working.")
            else:
                print("\n❌ Quick test failed! Check shared drive access.")
        else:
            print("\n❌ Quick test failed! Check authentication setup.")
    else:
        # Full test suite
        run_all_tests()

if __name__ == "__main__":
    main() 