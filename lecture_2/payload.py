import requests

url = "https://jsonplaceholder.typicode.com/posts"
# payload 1
payload = {
    "title": "Learn APIs",
    "body": "POST example with requests",
    "userId": 1
}
# payload 2
payload = [
    {
        "title": "Person 1",
        "body": "POST example with requests",
        "userId": 1
    },
    {
        "title": "Person 2",
        "body": "POST example with requests",
        "userId": 2
    },
    {
        "title": "Person 3",
        "body": "POST example with requests",
        "userId": 3
    }
]

response = requests.post(url, json=payload)
print("Status Code:", response.status_code)
print("Response Status:", response.status_code)
print("Response JSON:", response.json())