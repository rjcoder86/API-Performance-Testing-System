# apts/cli.py

import argparse
from .load_tester import run_load_test
from .metrics import calculate_metrics, rate_performance
from .report import generate_report


def main():
    breakpoint()
    parser = argparse.ArgumentParser(description="APTS - API Performance Testing System")
    parser.add_argument("--token", help="Bearer token for authentication")
    parser.add_argument("--url", required=True, help="API endpoint URL")
    parser.add_argument("--requests", type=int, default=1, help="Total number of requests")
    parser.add_argument("--concurrency", type=int, default=1, help="Number of concurrent workers")

    args = parser.parse_args()
    headers = {}

    if args.token:
        headers["Authorization"] = f"Bearer {args.token}"

    results = run_load_test(args.url, args.requests, args.concurrency, headers)


    metrics = calculate_metrics(results)
    rating = rate_performance(metrics)

    generate_report(args.url, metrics, rating)
