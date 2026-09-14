import requests
import time

def check_website(url):
    try:
        start_time = time.time()
        response = requests.get(url, timeout=10)
        end_time = time.time()
        response_time = round((end_time - start_time) * 1000, 2)  # in ms

        status_code = response.status_code

        if 200 <= status_code < 400:
            status = "✅ Website is UP and running!"
        elif 400 <= status_code < 500:
            status = "⚠️ Client Error (4xx)"
        elif 500 <= status_code < 600:
            status = "❌ Server Error (5xx)"
        else:
            status = "❓ Unknown Status"

        print("\n=== Website Status Checker ===")
        print(f"URL           : {url}")
        print(f"Status Code   : {status_code}")
        print(f"Status        : {status}")
        print(f"Response Time : {response_time} ms")

    except requests.exceptions.RequestException as e:
        print("\n=== Website Status Checker ===")
        print(f"URL           : {url}")
        print("Status        : ❌ Website is DOWN or not reachable!")
        print(f"Error         : {e}")

if __name__ == "__main__":
    website = input("Enter website URL (e.g., https://www.google.com): ").strip()
    if not website.startswith("http://") and not website.startswith("https://"):
        website = "https://" + website
    check_website(website)
