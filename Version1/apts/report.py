# apts/report.py

# apts/report.py

def generate_report(url, metrics, rating):
    print("\nAPI Performance Report")
    print("-" * 30)
    print(f"URL: {url}")
    print(f"Total Requests: {metrics['total_requests']}")
    print(f"Success Rate: {metrics['success_rate']:.2f}%")

    # 🔥 WHY API FAILING
    if metrics.get("error_types"):
        print("\nWhy API is failing:")
        for err_type, count in metrics["error_types"].items():
            print(f"{err_type}: {count} requests")

    # 🔥 Optional detailed messages
    if metrics.get("error_messages"):
        print("\nError Details (sample):")
        for msg, count in list(metrics["error_messages"].items())[:3]:
            print(f"{msg} ({count})")

    if metrics["all_failed"]:
        print("\nERROR: All requests failed.")
        print(f"Performance Rating: {rating}")
        print("-" * 30)
        return

    print(f"\nAverage Response Time: {metrics['avg_time']:.4f} sec")
    print(f"Min Response Time: {metrics['min_time']:.4f} sec")
    print(f"Max Response Time: {metrics['max_time']:.4f} sec")
    print(f"Performance Rating: {rating}")
    print("-" * 30)