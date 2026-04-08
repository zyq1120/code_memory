#!/usr/bin/env python
"""微信 MCP 测试工具"""
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from server import send_message_to_current, send_message_to_contact, get_wechat_status


def test_send(message):
    print(f"\n=== Test: Send Message ===")
    print(f"Message: {message}")
    success, err = send_message_to_current(message)
    if success:
        print(f"[OK] Sent: {message}")
    else:
        print(f"[ERROR] {err}")
    return success, err


def test_send_to_contact(contact_name, message):
    print(f"\n=== Test: Send to Contact ===")
    print(f"Contact: {contact_name}")
    print(f"Message: {message}")
    success, err = send_message_to_contact(contact_name, message)
    if success:
        print(f"[OK] Sent to {contact_name}: {message}")
    else:
        print(f"[ERROR] {err}")
    return success, err


def test_status():
    print(f"\n=== Test: WeChat Status ===")
    status = get_wechat_status()
    print(json.dumps(status, ensure_ascii=False, indent=2))
    return status


def main():
    import argparse
    parser = argparse.ArgumentParser(description="WeChat MCP Test")
    parser.add_argument("action", choices=["send", "send-to", "status"], help="Action")
    parser.add_argument("--message", "-m", help="Message")
    parser.add_argument("--contact", "-c", help="Contact name")
    
    args = parser.parse_args()
    
    if args.action == "send":
        if not args.message:
            print("Error: Need --message")
            return
        test_send(args.message)
    
    elif args.action == "send-to":
        if not args.message or not args.contact:
            print("Error: Need --message and --contact")
            return
        test_send_to_contact(args.contact, args.message)
    
    elif args.action == "status":
        test_status()


if __name__ == "__main__":
    import json
    main()
