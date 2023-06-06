import random
import threading
import time

import requests


def send_logs():
    url = "http://localhost:5050/api/v1/logs"

    payload = {
        "id": random.randint(100000, 9999999),
        "unix_ts": int(time.time()),
        "user_id": random.randint(100000, 999999),
        "event_name": random.choice(["login", "logout"])
    }

    while True:
        try:
            response = requests.post(url, json=payload)
            if response.status_code == 204:
                print("Log sent successfully")
            else:
                print(f"Failed to send log. Status Code: {response.status_code}")
        except requests.exceptions.RequestException as e:
            print(f"Error occurred while sending log: {e}")

        # Sleep for 1 millisecond to achieve 1,000 requests per second
        time.sleep(0.001)


# Start firing requests in the background
if __name__ == "__main__":
    for _ in range(1000):
        threading.Thread(target=send_logs).start()
