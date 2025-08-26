#!/usr/bin/env python3
"""
Test script untuk debug paket XUT
"""

import json
import os
from paket_xut import get_package_xut
from api_request import get_family

def test_packages():
    """Test loading packages"""
    print("🧪 Testing Package Loading")
    print("=" * 40)
    
    # Check if tokens.json exists
    if not os.path.exists("tokens.json"):
        print("❌ tokens.json tidak ditemukan!")
        print("💡 Silakan login terlebih dahulu dengan CLI")
        return
    
    # Load tokens
    try:
        with open("tokens.json", "r", encoding="utf8") as f:
            tokens = json.load(f)
        print("✅ Tokens loaded successfully")
        print(f"📋 Token keys: {list(tokens.keys())}")
    except Exception as e:
        print(f"❌ Error loading tokens: {e}")
        return
    
    # Test get_family directly
    print("\n🔍 Testing get_family...")
    try:
        family_data = get_family(tokens, "08a3b1e6-8e78-4e45-a540-b40f06871cfe")
        if family_data:
            print("✅ get_family successful")
            print(f"📋 Family data keys: {list(family_data.keys())}")
            
            if "package_variants" in family_data:
                variants = family_data["package_variants"]
                print(f"📦 Found {len(variants)} package variants")
                
                for i, variant in enumerate(variants):
                    print(f"  Variant {i+1}: {variant.get('name', 'Unknown')}")
                    if "package_options" in variant:
                        options = variant["package_options"]
                        print(f"    Options: {len(options)}")
                        for option in options:
                            print(f"      - {option.get('name', 'Unknown')} (Rp {option.get('price', 0):,})")
            else:
                print("❌ No package_variants found in response")
        else:
            print("❌ get_family returned None")
    except Exception as e:
        print(f"❌ Error in get_family: {e}")
    
    # Test get_package_xut
    print("\n🔍 Testing get_package_xut...")
    try:
        packages = get_package_xut(tokens)
        print(f"📦 Found {len(packages)} packages")
        
        if packages:
            print("✅ Packages found:")
            for package in packages:
                print(f"  {package['number']}. {package['name']} - Rp {package['price']:,}")
        else:
            print("❌ No packages found")
    except Exception as e:
        print(f"❌ Error in get_package_xut: {e}")

if __name__ == "__main__":
    test_packages()