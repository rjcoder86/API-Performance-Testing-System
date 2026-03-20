# apts/request_sender.py

import requests
import time

# apts/request_sender.py

def extract_error_message(response, default_msg):
    try:
        if response.headers.get("Content-Type", "").startswith("application/json"):
            data = response.json()

            # Try common keys
            for key in ["message", "error", "detail", "msg"]:
                if key in data and data[key]:
                    return data[key]

    except Exception:
        pass

    return default_msg


import requests
import time


def send_request(url, headers=None, method="GET", data=None, timeout=10):

    start_time = time.perf_counter()

    try:
        response = requests.request(
            method=method.upper(),
            url=url,
            headers=headers,
            json=data,
            timeout=timeout
        )

        end_time = time.perf_counter()

        success = 200 <= response.status_code < 300

        error_msg = None
        error_type = None

        if not success:
            error_type = f"HTTP_{response.status_code}"
            error_msg = extract_error_message(response, f"HTTP {response.status_code}")

        return {
            "status_code": response.status_code,
            "response_time": end_time - start_time,
            "response_size": len(response.content),
            "success": success,
            "error": error_msg,
            "error_type": error_type
        }

    except requests.exceptions.Timeout:
        return {
            "status_code": None,
            "response_time": 0,
            "response_size": 0,
            "success": False,
            "error": "Request Timeout",
            "error_type": "TIMEOUT"
        }

    except requests.exceptions.ConnectionError:
        return {
            "status_code": None,
            "response_time": 0,
            "response_size": 0,
            "success": False,
            "error": "Connection Error",
            "error_type": "CONNECTION_ERROR"
        }

    except Exception as e:
        return {
            "status_code": None,
            "response_time": 0,
            "response_size": 0,
            "success": False,
            "error": str(e),
            "error_type": "UNKNOWN_ERROR"
        }