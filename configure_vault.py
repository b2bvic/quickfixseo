#!/usr/bin/env python3
"""
Quick vault configuration script
"""

import os
import json

def main():
    print("🔧 CONFIGURE OBSIDIAN VAULT")
    print("=" * 40)
    
    vault_path = input("Enter your Obsidian vault path: ").strip()
    
    # Handle relative paths and expand user home
    if vault_path.startswith('~'):
        vault_path = os.path.expanduser(vault_path)
    elif not vault_path.startswith('/'):
        # Relative path - try from home directory
        vault_path = os.path.expanduser(f"~/{vault_path}")
    
    if os.path.exists(vault_path):
        config_file = os.path.expanduser("~/.obsidian_seo_config.json")
        config = {'obsidian_vault_path': vault_path}
        
        with open(config_file, 'w') as f:
            json.dump(config, f, indent=2)
        
        print(f"✅ Configured vault: {vault_path}")
        print(f"💾 Saved to: {config_file}")
        print("🚀 You can now run: python3 obsidian_seo_analyzer.py <website>")
    else:
        print(f"❌ Path doesn't exist: {vault_path}")

if __name__ == "__main__":
    main() 