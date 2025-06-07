#!/usr/bin/env python3
"""
Example subscription management for QuickFixSEO

This demonstrates how to create and manage subscription licenses.
"""

import json
from datetime import datetime, timedelta
from pathlib import Path

def create_subscription_license(tier: str, duration_months: int = 12):
    """Create a subscription license file"""
    
    license_file = Path.home() / ".auto_seo_license"
    
    # Calculate expiry date
    expires_at = datetime.now() + timedelta(days=duration_months * 30)
    
    license_data = {
        "tier": tier,
        "type": "subscription",
        "created_at": datetime.now().isoformat(),
        "expires_at": expires_at.isoformat(),
        "auto_renew": True,
        "customer_id": "cust_example123",
        "subscription_id": "sub_example456"
    }
    
    with open(license_file, 'w') as f:
        json.dump(license_data, f, indent=2)
    
    print(f"✅ Created {tier} subscription license")
    print(f"   Expires: {expires_at.strftime('%Y-%m-%d')}")
    print(f"   File: {license_file}")

def create_lifetime_license():
    """Create a lifetime license file"""
    
    license_file = Path.home() / ".auto_seo_license"
    
    license_data = {
        "tier": "lifetime",
        "type": "lifetime",
        "created_at": datetime.now().isoformat(),
        "expires_at": None,  # Never expires
        "customer_id": "cust_lifetime789",
        "license_key": "LIFE-XXXX-XXXX-XXXX"
    }
    
    with open(license_file, 'w') as f:
        json.dump(license_data, f, indent=2)
    
    print(f"✅ Created lifetime license")
    print(f"   Never expires")
    print(f"   File: {license_file}")

def create_trial_license(tier: str, trial_days: int = 7):
    """Create a trial license"""
    
    license_file = Path.home() / ".auto_seo_license"
    
    expires_at = datetime.now() + timedelta(days=trial_days)
    
    license_data = {
        "tier": tier,
        "type": "trial",
        "created_at": datetime.now().isoformat(),
        "expires_at": expires_at.isoformat(),
        "trial_days": trial_days,
        "email": "user@example.com"
    }
    
    with open(license_file, 'w') as f:
        json.dump(license_data, f, indent=2)
    
    print(f"✅ Created {trial_days}-day {tier} trial")
    print(f"   Expires: {expires_at.strftime('%Y-%m-%d')}")

def simulate_expired_subscription():
    """Create an expired subscription to test expiry handling"""
    
    license_file = Path.home() / ".auto_seo_license"
    
    # Create subscription that expired yesterday
    expires_at = datetime.now() - timedelta(days=1)
    
    license_data = {
        "tier": "professional",
        "type": "subscription",
        "created_at": (datetime.now() - timedelta(days=365)).isoformat(),
        "expires_at": expires_at.isoformat(),
        "auto_renew": False,  # Renewal failed
        "customer_id": "cust_expired123"
    }
    
    with open(license_file, 'w') as f:
        json.dump(license_data, f, indent=2)
    
    print(f"⚠️  Created expired subscription for testing")
    print(f"   Expired: {expires_at.strftime('%Y-%m-%d')}")

def check_license_status():
    """Check current license status"""
    from license_manager import license_manager
    license_manager.print_license_status()

def main():
    """Demo subscription management"""
    
    print("🎯 QuickFixSEO Subscription Management Demo\n")
    
    while True:
        print("Choose an option:")
        print("1. Create Professional subscription (1 year)")
        print("2. Create Enterprise subscription (1 year)")
        print("3. Create Lifetime license")
        print("4. Create Professional trial (7 days)")
        print("5. Simulate expired subscription")
        print("6. Check current license status")
        print("7. Remove license file")
        print("0. Exit")
        
        choice = input("\nEnter choice (0-7): ").strip()
        
        if choice == "1":
            create_subscription_license("professional", 12)
        elif choice == "2":
            create_subscription_license("enterprise", 12)
        elif choice == "3":
            create_lifetime_license()
        elif choice == "4":
            create_trial_license("professional", 7)
        elif choice == "5":
            simulate_expired_subscription()
        elif choice == "6":
            check_license_status()
        elif choice == "7":
            license_file = Path.home() / ".auto_seo_license"
            if license_file.exists():
                license_file.unlink()
                print("✅ License file removed")
            else:
                print("⚠️  No license file found")
        elif choice == "0":
            break
        else:
            print("❌ Invalid choice")
        
        print()

if __name__ == "__main__":
    main() 