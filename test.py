import requests

#Ausrtria NES
# api_key = '2c8301ed15984ac1838cae030b1bb981'
# request_msg = f'https://newsapi.org/v2/top-headlines?country=at&apiKey={api_key}'

# response = requests.get(request_msg).json()
# articles = response['articles']

# print(articles)

# for a in articles:
#     print(a['title'])
#     print(a['content'])

stop = 'Finanzamt'

allStops = requests.get("https://smartinfo.ivb.at/api/JSON/STOPS").json()

for s in allStops:
    if s['stop']['name'] == stop:
        id = s['stop']['uid']

departures = requests.get(f"https://smartinfo.ivb.at/api/JSON/PASSAGE?stopID={id}").json()

for d in departures:
    print(d)

