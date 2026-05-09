import requests

def get_posts(user_id):
    try:
        response = requests.get(
            "https://jsonplaceholder.typicode.com/posts",
            params={"userId": user_id},
            timeout=10
        )
        response.raise_for_status()
        return response.json()

    except requests.exceptions.Timeout:
        print("Request timed out. Server took too long to respond.")
        return []
    except requests.exceptions.ConnectionError:
        print("Could not connect. Check your internet connection.")
        return []
    except requests.exceptions.HTTPError as e:
        print(f"HTTP error: {e.response.status_code}")
        return []
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
        return []

posts = get_posts(1)
print(f"Found {len(posts)} posts")