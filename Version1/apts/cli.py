# apts/cli.py

import json
import argparse
from .load_tester import run_load_test
from .metrics import calculate_metrics, rate_performance
from .report import generate_report
from apts.auth import get_token

def main():
    parser = argparse.ArgumentParser(description="APTS - API Performance Testing System")

    parser.add_argument("--token", help="Bearer token for authentication")
    parser.add_argument("--url", required=True, help="API endpoint URL")
    parser.add_argument("--method", default="GET", help="HTTP method (GET, POST, PUT, DELETE)")
    parser.add_argument("--data", help="Request body (JSON string)")
    parser.add_argument("--header", action="append", help="Custom headers (key:value)")
    parser.add_argument("--requests", type=int, default=1, help="Total number of requests")
    parser.add_argument("--concurrency", type=int, default=1, help="Number of concurrent workers")

    parser.add_argument("--login-url", help="Login API URL")
    parser.add_argument("--credentials", help="Request body (JSON string)")
    parser.add_argument("--token-field", help="Token field in login response")
    
    args = parser.parse_args()

    headers = {}

    # 🔥 Priority 1: Direct token
    if args.token:
        headers["Authorization"] = f"Bearer {args.token}"

    # 🔥 Priority 2: Auto login
    elif args.login_url and args.credentials:
        print("\n🔐 Performing auto login...")

    if args.credentials:
        try:
            credentials = json.loads(args.credentials)  # ✅ THIS IS KEY
        except json.JSONDecodeError:
            print("❌ Invalid JSON format in --credentials")
            return
        
        token = get_token(
            login_url=args.login_url,
            credentials=credentials,
            token_field=args.token_field
        )

        if not token:
            print("❌ Cannot proceed without token")
            return

        headers["Authorization"] = f"Bearer {token}"

    # 🔥 No auth
    else:
        print("\n⚠️ No authentication provided")

    # Custom headers
    if args.header:
        for h in args.header:
            key, value = h.split(":", 1)
            headers[key.strip()] = value.strip()

    data = None
    if args.data:
        try:
            data = json.loads(args.data)
        except json.JSONDecodeError:
            print("❌ Invalid JSON format in --data")
            return
    
        
    auth_type = "None"

    if args.token:
        auth_type = "Token (Manual)"
    elif args.login_url:
        auth_type = "Auto Login"

    # 🔥 NEW: Print execution details
    print("\n🚀 Starting API Test...")
    print("-" * 40)
    print(f"Endpoint        : {args.url}")
    print(f"Method          : {args.method.upper()}")
    print(f"Request Body    : {args.data if args.data else 'None'}")
    print(f"Total Requests  : {args.requests}")
    print(f"Concurrency     : {args.concurrency}")
    print(f"Authentication  : {auth_type}")
    print("-" * 40)

    # Run test
    results = run_load_test(
        url=args.url,
        total_requests=args.requests,
        concurrency=args.concurrency,
        headers=headers,
        method=args.method,
        data=data
    )

    print("\n⏳ Test completed. Generating report...\n")

    metrics = calculate_metrics(results)
    rating = rate_performance(metrics)

    generate_report(args.url, metrics, rating)