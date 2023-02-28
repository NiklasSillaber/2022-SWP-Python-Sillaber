import requests

api_key = '2c8301ed15984ac1838cae030b1bb981'
request_msg = f'https://newsapi.org/v2/top-headlines?country=at&apiKey={api_key}'

response = requests.get(request_msg).json()
articles = response['articles']

print(articles)

for a in articles:
    print(a['title'])
    print(a['content'])

