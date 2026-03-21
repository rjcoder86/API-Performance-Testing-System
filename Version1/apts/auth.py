# apts/auth.py

import requests


def get_token(login_url, credentials, token_field="access"):
    try:

        response = requests.post(login_url, json=credentials)

        if response.status_code != 200:
            print(f"❌ Login failed with status {response.status_code}")
            print(response.text)
            return None

        data = response.json()
        if not token_field:
            token_field = "access"

        #test the response to find the token field
        token = data.get('data').get(token_field)

        if not token:
            print("❌ Token not found in response")
            print("Response:", data)
            return None

        print("✅ Login successful. Token fetched.")
        return token

    except Exception as e:
        print("❌ Login error:", str(e))
        return None