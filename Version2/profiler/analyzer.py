def analyze_queries(queries, total_time, response):

    slow_queries = []
    duplicate_queries = {}

    for q in queries:
        query_time = float(q.get("time", 0))

        # 🔴 Slow query detection
        if query_time > 0.1:
            slow_queries.append(q)

        # 🔴 Duplicate query detection (N+1 heuristic)
        sql = q.get("sql")

        if sql in duplicate_queries:
            duplicate_queries[sql] += 1
        else:
            duplicate_queries[sql] = 1

    # 🔥 Find repeated queries
    repeated_queries = {
        k: v for k, v in duplicate_queries.items() if v > 5
    }
    
    issues = []
    suggestions = []

    if len(queries) > 20:
        issues.append("High number of DB queries")
        suggestions.append("Use select_related / prefetch_related")

    if len(repeated_queries) > 0:
        issues.append("Possible N+1 query problem")
        suggestions.append("Optimize ORM queries to avoid repeated DB hits")

    if len(slow_queries) > 0:
        issues.append("Slow queries detected")
        suggestions.append("Add indexing or optimize SQL queries")

    return {
        "total_time": total_time,
        "total_queries": len(queries),
        "slow_queries": slow_queries,
        "repeated_queries": repeated_queries,
        "response_size": len(response.content) if hasattr(response, "content") else 0,
        "issues": issues,
        "suggestions": suggestions
    }