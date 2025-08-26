#!/usr/bin/env python3
"""
Debug script untuk test bot functionality
"""

import json
import logging
from telegram_bot import user_data, user_states, load_token

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def debug_bot_state():
    """Debug bot state"""
    print("🔍 Debug Bot State")
    print("=" * 40)
    
    print(f"📊 User data count: {len(user_data)}")
    print(f"📊 User states count: {len(user_states)}")
    
    for user_id, data in user_data.items():
        print(f"\n👤 User {user_id}:")
        print(f"  Login status: {data.get('is_logged_in', False)}")
        print(f"  Phone: {data.get('phone_number', 'None')}")
        print(f"  Balance: {data.get('balance', 'None')}")
        print(f"  Has tokens: {bool(data.get('tokens'))}")
        
        if data.get('tokens'):
            token_keys = list(data['tokens'].keys())
            print(f"  Token keys: {token_keys}")

def test_load_token():
    """Test load_token function"""
    print("\n🔍 Testing load_token...")
    try:
        result = load_token()
        if result:
            print("✅ load_token successful")
            print(f"📋 Result keys: {list(result.keys())}")
            return result
        else:
            print("❌ load_token returned None")
            return None
    except Exception as e:
        print(f"❌ Error in load_token: {e}")
        return None

def simulate_package_request(user_info):
    """Simulate package request"""
    print("\n🔍 Simulating package request...")
    
    if not user_info.get("is_logged_in"):
        print("❌ User not logged in")
        return
    
    if not user_info.get("tokens"):
        print("❌ No tokens available")
        return
    
    print("✅ User logged in and has tokens")
    print("📦 This would trigger get_package_xut()")
    print("💡 Check the logs when you click 'Paket XUT' in bot")

if __name__ == "__main__":
    debug_bot_state()
    user_info = test_load_token()
    if user_info:
        simulate_package_request(user_info)
    
    print("\n💡 Tips untuk debug:")
    print("1. Jalankan bot: python3 run_bot.py")
    print("2. Login dengan bot")
    print("3. Coba klik 'Paket XUT'")
    print("4. Cek log output untuk error details")
    print("5. Atau jalankan: python3 test_packages.py (setelah login)")