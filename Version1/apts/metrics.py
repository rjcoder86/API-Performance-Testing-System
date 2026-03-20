# apts/metrics.py

# apts/metrics.py

from collections import Counter
import statistics

from collections import Counter
import statistics


def calculate_metrics(results):
    total_requests = len(results)
    success_count = sum(1 for r in results if r["success"])

    # 🔥 Group by error type
    error_types = [r.get("error_type", "UNKNOWN") for r in results if not r["success"]]
    error_type_counts = Counter(error_types)

    # 🔥 Also keep detailed messages (optional)
    error_messages = [r.get("error") for r in results if not r["success"]]
    error_message_counts = Counter(error_messages)

    if success_count == 0:
        return {
            "total_requests": total_requests,
            "success_rate": 0,
            "avg_time": None,
            "min_time": None,
            "max_time": None,
            "all_failed": True,
            "error_types": error_type_counts,
            "error_messages": error_message_counts
        }

    response_times = [r["response_time"] for r in results if r["success"]]

    return {
        "total_requests": total_requests,
        "success_rate": (success_count / total_requests) * 100,
        "avg_time": statistics.mean(response_times),
        "min_time": min(response_times),
        "max_time": max(response_times),
        "all_failed": False,
        "error_types": error_type_counts,
        "error_messages": error_message_counts
    }


def rate_performance(metrics):
    if metrics["all_failed"]:
        return "API Unreachable ❌"

    avg_time = metrics["avg_time"]
    success_rate = metrics["success_rate"]

    if success_rate < 50:
        return "Unstable API ⚠️"

    if avg_time < 0.2:
        return "Excellent 🚀"
    elif avg_time < 0.5:
        return "Good 👍"
    elif avg_time < 1:
        return "Moderate ⚡"
    else:
        return "Poor 🐢"