import requests

url = "https://jsonplaceholder.typicode.com/posts"
payload = {
    "title": "Learn APIs",
    "body": "POST example with requests",
    "userId": 1
}

response = requests.post(url, json=payload)
print("Status Code:", response.status_code)
print("Response JSON:", response.json())