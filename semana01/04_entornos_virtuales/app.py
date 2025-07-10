import requests
from pprint import pprint

def main():
    response = requests.get("https://jsonplaceholder.typicode.com/users")
    json = response.json()

    for user in json:
        if user["id"] == 2:
            break
        pprint(user)


if __name__ == "__main__":
    main()