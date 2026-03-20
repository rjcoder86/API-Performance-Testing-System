# apts/load_tester.py

from concurrent.futures import ThreadPoolExecutor, as_completed
from .request_sender import send_request


def run_load_test(url, total_requests, concurrency, headers=None, method="GET", data=None):

    results = []

    with ThreadPoolExecutor(max_workers=concurrency) as executor:

        futures = [
            executor.submit(send_request, url, headers, method, data)
            for _ in range(total_requests)
        ]

        for future in as_completed(futures):
            results.append(future.result())

    return results