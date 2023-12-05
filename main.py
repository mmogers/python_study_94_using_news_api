import os, requests, json


news = os.environ['newsapi']
country = "us"

organization = os.environ['organizationid']


url = f"https://newsapi.org/v2/top-headlines?country={country}&apiKey={news}" 

result = requests.get(url)
data = result.json()

counter = 0
for article in data['articles']:
  counter += 1
  if counter > 5:
    break
  title = article['title']
  
  print(f"""{counter} : {title}""")
  print()
  if article['description']:
    print(article['description'])
    print()
    
  

#prompt = "Who is the most handsome bald man?"
#response = openai.Completion.create(model="text-davinci-002", #prompt=prompt, temperature=0, max_tokens=6)
#print(response["choices"][0]["text"].strip())