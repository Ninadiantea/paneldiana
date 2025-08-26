#!/usr/bin/env python3
"""
Test script untuk verifikasi handling message length
"""

def test_truncate_message():
    """Test truncate_message function"""
    from telegram_bot import truncate_message, split_long_message
    
    print("🧪 Testing Message Length Handling")
    print("=" * 40)
    
    # Test short message
    short_msg = "Hello World"
    result = truncate_message(short_msg)
    print(f"Short message: {len(short_msg)} chars -> {len(result)} chars")
    print(f"Result: {result}")
    
    # Test long message
    long_msg = "A" * 5000
    result = truncate_message(long_msg)
    print(f"Long message: {len(long_msg)} chars -> {len(result)} chars")
    print(f"Result ends with: ...{result[-10:]}")
    
    # Test split message
    long_msg_with_newlines = "Line 1\n" * 1000
    parts = split_long_message(long_msg_with_newlines)
    print(f"Split message into {len(parts)} parts")
    for i, part in enumerate(parts[:3]):
        print(f"Part {i+1}: {len(part)} chars")
    
    print("\n✅ Message length handling tests completed")

if __name__ == "__main__":
    test_truncate_message()