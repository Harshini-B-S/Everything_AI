import requests

url = "https://jsonplaceholder.typicode.com/users/1"

try:
    response = requests.get(url, timeout=10)

    print("Status code:", response.status_code)

    response.raise_for_status()

    user = response.json()

    print("Name:", user.get("name", "Unknown"))
    print("Email:", user.get("email", "Unknown"))

except requests.exceptions.RequestException as error:
    print("API request failed:", error)