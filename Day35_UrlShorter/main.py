import requests

API_URL = "https://tinyurl.com/api-create.php"

def shorten_url(long_url):
    try:
        params = {'url': long_url}
        response = requests.get(API_URL, params=params)
        response.raise_for_status()  # Raise error for bad status codes
        short_url = response.text
        return short_url
    except requests.exceptions.RequestException as e:
        return f"Error: {e}"

def main():
    print("=== URL Shortener ===")
    long_url = input("Enter a long URL: ").strip()
    if not (long_url.startswith('http://') or long_url.startswith('https://')):
        print("✘ Invalid URL! Please enter a valid URL starting with http:// or https://")
        return

    print("\nShortening URL, please wait...")
    short_url = shorten_url(long_url)

    if short_url.startswith("http"):
        print(f"✔ Short URL: {short_url}")
        print(f"🔗 Long URL : {long_url}")
    else:
        print(f"✘ {short_url}")

if __name__ == "__main__":
    main()
