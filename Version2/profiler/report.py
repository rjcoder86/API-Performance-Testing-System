
def print_report(report):
    print("\n🔍 APTS Profiling Report")
    print("-" * 40)

    print(f"Execution Time : {report['total_time']:.4f} sec")
    print(f"DB Queries     : {report['total_queries']}")
    print(f"Response Size  : {report['response_size']} bytes")

    print(f"\nSlow Queries   : {len(report['slow_queries'])}")
    print(f"Repeated Query : {len(report['repeated_queries'])}")

    if report["issues"]:
        print("\n⚠️ Issues Found:")
        for issue in report["issues"]:
            print(f"- {issue}")

    if report["suggestions"]:
        print("\n💡 Suggestions:")
        for s in report["suggestions"]:
            print(f"- {s}")

    print("-" * 40)