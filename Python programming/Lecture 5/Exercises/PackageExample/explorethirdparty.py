import requests


def main():
    fetch_url = "https://jsonplaceholder.typicode.com/posts"
    request = requests.get(fetch_url)
    text = request.json()
    print(text)

if __name__ == "__main__":
    main()
