#!/usr/bin/env python3
"""
License Management System for QuickFixSEO
A product of Scale With Search (https://scalewithsearch.com)
Created by Victor Valentine Romo (@b2bvic)

This module handles feature restrictions based on license tier.
"""

import os
import json
from pathlib import Path
from enum import Enum
from typing import Dict, List, Optional

class LicenseTier(Enum):
    FREE = "free"
    PROFESSIONAL = "professional"
    ENTERPRISE = "enterprise"
    LIFETIME = "lifetime"

class LicenseManager:
    """Manages license validation and feature restrictions"""
    
    def __init__(self):
        self.license_file = Path.home() / ".auto_seo_license"
        self.current_tier = self._detect_license_tier()
        
    def _detect_license_tier(self) -> LicenseTier:
        """Detect the current license tier"""
        
        # Check for license file
        if self.license_file.exists():
            try:
                with open(self.license_file, 'r') as f:
                    license_data = json.load(f)
                    tier = license_data.get('tier', 'free').lower()
                    
                    # Check subscription expiry
                    if tier in ['professional', 'pro', 'enterprise', 'ent']:
                        expiry = license_data.get('expires_at')
                        if expiry:
                            from datetime import datetime
                            expiry_date = datetime.fromisoformat(expiry)
                            if datetime.now() > expiry_date:
                                print(f"⚠️  Subscription expired on {expiry_date.strftime('%Y-%m-%d')}")
                                print(f"🔄 Renew at: https://your-site.com/billing")
                                return LicenseTier.FREE
                    
                    if tier in ['professional', 'pro']:
                        return LicenseTier.PROFESSIONAL
                    elif tier in ['enterprise', 'ent']:
                        return LicenseTier.ENTERPRISE
                    elif tier in ['lifetime', 'life']:
                        return LicenseTier.LIFETIME
            except Exception as e:
                print(f"⚠️  Could not read license file: {e}")
        
        # Check environment variable
        env_license = os.getenv('AUTO_SEO_LICENSE', '').lower()
        if env_license in ['professional', 'pro']:
            return LicenseTier.PROFESSIONAL
        elif env_license in ['enterprise', 'ent']:
            return LicenseTier.ENTERPRISE
        elif env_license in ['lifetime', 'life']:
            return LicenseTier.LIFETIME
            
        # Default to free
        return LicenseTier.FREE
    
    def get_max_pages(self) -> Optional[int]:
        """Get maximum pages allowed for current license"""
        limits = {
            LicenseTier.FREE: 25,
            LicenseTier.PROFESSIONAL: None,  # Unlimited
            LicenseTier.ENTERPRISE: None,    # Unlimited
            LicenseTier.LIFETIME: None,      # Unlimited
        }
        return limits[self.current_tier]
    
    def is_multithreading_enabled(self) -> bool:
        """Check if multithreaded crawling is allowed"""
        return self.current_tier in [LicenseTier.PROFESSIONAL, LicenseTier.ENTERPRISE, LicenseTier.LIFETIME]
    
    def get_max_concurrent_requests(self) -> int:
        """Get maximum concurrent requests allowed"""
        limits = {
            LicenseTier.FREE: 1,           # Single-threaded
            LicenseTier.PROFESSIONAL: 10,  # Fast crawling
            LicenseTier.ENTERPRISE: 20,    # Fastest crawling
            LicenseTier.LIFETIME: 15,      # Premium but not enterprise-level
        }
        return limits[self.current_tier]
    
    def get_crawl_delay(self) -> float:
        """Get delay between requests in seconds"""
        delays = {
            LicenseTier.FREE: 1.0,         # Slow and respectful
            LicenseTier.PROFESSIONAL: 0.1, # Fast
            LicenseTier.ENTERPRISE: 0.05,  # Fastest
            LicenseTier.LIFETIME: 0.1,     # Same as professional
        }
        return delays[self.current_tier]
    
    def is_feature_enabled(self, feature: str) -> bool:
        """Check if a specific feature is enabled for current license"""
        
        # Free tier features
        free_features = {
            "basic_seo_analysis",
            "title_analysis", 
            "meta_description_analysis",
            "heading_structure",
            "image_alt_text",
            "basic_content_quality",
            "basic_technical_seo",
            "basic_reporting",
        }
        
        # Professional tier features (includes all free features)
        pro_features = free_features | {
            "multithreaded_crawling",
            "unlimited_pages",
            "advanced_reporting",
            "advanced_content_analysis",
            "performance_monitoring",
            "schema_validation",
            "competitive_analysis",
        }
        
        # Enterprise tier features (includes all pro features)
        enterprise_features = pro_features | {
            "api_access",
            "webhook_integrations",
            "team_collaboration",
            "white_label_reports",
            "priority_support",
            "custom_integrations",
        }
        
        # Lifetime features (same as professional)
        lifetime_features = pro_features.copy()
        
        feature_sets = {
            LicenseTier.FREE: free_features,
            LicenseTier.PROFESSIONAL: pro_features,
            LicenseTier.ENTERPRISE: enterprise_features,
            LicenseTier.LIFETIME: lifetime_features,
        }
        
        return feature in feature_sets[self.current_tier]
    
    def require_feature(self, feature: str, action_name: str = "this action"):
        """Raise an exception if feature is not available in current license"""
        if not self.is_feature_enabled(feature):
            tier_name = self.current_tier.value.title()
            raise LicenseError(
                f"🔒 {action_name.title()} requires a Professional or Enterprise license.\n"
                f"Current license: {tier_name}\n"
                f"Upgrade at: https://your-website.com/pricing"
            )
    
    def get_license_info(self) -> Dict:
        """Get current license information"""
        return {
            "tier": self.current_tier.value,
            "tier_display": self.current_tier.value.title(),
            "max_pages": self.get_max_pages(),
            "multithreading": self.is_multithreading_enabled(),
            "max_concurrent": self.get_max_concurrent_requests(),
            "crawl_delay": self.get_crawl_delay(),
        }
    
    def print_license_status(self):
        """Print current license status"""
        info = self.get_license_info()
        
        print(f"📄 QuickFixSEO License Status")
        print(f"   Tier: {info['tier_display']}")
        print(f"   Max Pages: {'Unlimited' if info['max_pages'] is None else info['max_pages']}")
        print(f"   Multithreading: {'✅ Enabled' if info['multithreading'] else '❌ Disabled'}")
        print(f"   Concurrent Requests: {info['max_concurrent']}")
        print(f"   Crawl Delay: {info['crawl_delay']}s")
        
        if self.current_tier == LicenseTier.FREE:
            print(f"\n💡 Upgrade options:")
            print(f"   📅 Professional: $19/month or $199/year")
            print(f"   🏢 Enterprise: $49/month or $499/year") 
            print(f"   💎 Lifetime: $999 one-time (no subscriptions)")
            print(f"   🚀 Benefits: 10x faster crawling, unlimited pages, advanced reports")
            print(f"   🎯 Start free trial: https://your-website.com/pricing")

class LicenseError(Exception):
    """Exception raised when a feature requires a higher license tier"""
    pass

# Global license manager instance
license_manager = LicenseManager()

# Convenience functions
def get_max_pages() -> Optional[int]:
    """Get maximum pages allowed for current license"""
    return license_manager.get_max_pages()

def is_multithreading_enabled() -> bool:
    """Check if multithreaded crawling is allowed"""
    return license_manager.is_multithreading_enabled()

def require_pro_feature(feature: str, action_name: str = "this action"):
    """Require a professional feature or raise LicenseError"""
    license_manager.require_feature(feature, action_name)

def is_feature_enabled(feature: str) -> bool:
    """Check if a feature is enabled for current license"""
    return license_manager.is_feature_enabled(feature)

# Example usage functions
def crawl_with_license_check(url: str, max_pages: int = None):
    """Example crawling function with license restrictions"""
    
    # Check page limit
    license_limit = get_max_pages()
    if license_limit is not None and max_pages and max_pages > license_limit:
        print(f"🔒 Page limit exceeded. Free tier allows up to {license_limit} pages.")
        print(f"   Requested: {max_pages}, Limiting to: {license_limit}")
        max_pages = license_limit
    
    # Check multithreading
    if not is_multithreading_enabled():
        print(f"🔒 Single-threaded crawling (Free tier)")
        print(f"   Upgrade to Professional for 5-10x faster multithreaded crawling")
    
    # Proceed with crawling...
    print(f"🕷️  Crawling {url} with {max_pages or 'unlimited'} pages...")
    
def generate_advanced_report():
    """Example advanced reporting function"""
    try:
        require_pro_feature("advanced_reporting", "advanced report generation")
        print("📊 Generating advanced report with charts and insights...")
        # Advanced reporting logic here
    except LicenseError as e:
        print(str(e))
        print("📝 Generating basic report instead...")
        # Basic reporting logic here

if __name__ == "__main__":
    # Demo the license system
    license_manager.print_license_status()
    
    print(f"\n🧪 Testing license restrictions...")
    
    # Test page limits
    crawl_with_license_check("example.com", 100)
    
    # Test advanced features
    generate_advanced_report() 