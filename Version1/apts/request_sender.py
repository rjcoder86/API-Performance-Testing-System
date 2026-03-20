# apts/request_sender.py

import requests
import time


def send_request(url: str, headers=None, timeout=10):

    start_time = time.perf_counter()

    try:
        response = requests.get(url, headers=headers, timeout=timeout)

        end_time = time.perf_counter()

        success = 200 <= response.status_code < 300

        return {
            "status_code": response.status_code,
            "response_time": end_time - start_time,
            "response_size": len(response.content),
            "success": success,
        }

    except requests.RequestException as e:

        end_time = time.perf_counter()

        return {
            "status_code": None,
            "response_time": end_time - start_time,
            "response_size": 0,
            "success": False,
            "error": str(e)
        }