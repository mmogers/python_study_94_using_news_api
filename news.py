import requests, json, os

newsKey = os.environ['newsapi']
country = "us"

url = f"https://newsapi.org/v2/top-headlines?country={country}&apiKey={newsKey}"

result = requests.get(url)
data = result.json()
# print(json.dumps(data, indent=2))

for article in data['articles']:
  print(article['title'])
  print(article['url'])
  print(article['content'])
  

