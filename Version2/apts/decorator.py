# version2/apts/profiler/decorator.py

import time
from django.db import connection


def apts_profile(func):
    def wrapper(*args, **kwargs):

        # Reset query log (important)
        connection.queries_log.clear()

        start_time = time.perf_counter()

        response = func(*args, **kwargs)

        end_time = time.perf_counter()

        queries = connection.queries

        total_time = end_time - start_time
        total_queries = len(queries)

        # Pass to analyzer
        from .analyzer import analyze_queries
        report = analyze_queries(queries, total_time, response)

        from .report import print_report
        print_report(report)

        return response

    return wrapper