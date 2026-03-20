# apts/report.py

def generate_report(url, metrics, rating):
    print("\nAPI Performance Report")
    print("-" * 30)
    print(f"URL: {url}")
    print(f"Total Requests: {metrics['total_requests']}")
    print(f"Success Rate: {metrics['success_rate']:.2f}%")
    breakpoint()
    if metrics["all_failed"]:
        print("\nERROR: All requests failed. API may be down or unreachable.")
        print(f"Performance Rating: {rating}")
        print("-" * 30)
        return

    print(f"Average Response Time: {metrics['avg_time']:.4f} sec")
    print(f"Min Response Time: {metrics['min_time']:.4f} sec")
    print(f"Max Response Time: {metrics['max_time']:.4f} sec")
    print(f"Performance Rating: {rating}")
    print("-" * 30)