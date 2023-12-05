# Fix My Code

👉 Try and fix this code which is *full* of errors.

*First, delete any other code in your `main.py` file. Copy each code snippet below into `main.py` by clicking the copy icon in the top right of each code box. Then, hit `run` and see what errors occur. Fix the errors and press `run` again until you are error free. Click on the `👀 Answer` to compare your code to the correct code.*

```python
import requests, json, os

newsKey = os.environ['newsapi']
country = "us"

url = f"https://newsapi/v2/top-headlines?country={country}&apiKey={newsKey}"

result = requests.get(url)
data = result()

for article in data['articles']:
  print(article['title'])
  print(article['url'])
  print(article['content'])
```
<details> <summary> 👀 Answer </summary>

```python
import requests, json, os

newsKey = os.environ['newsapi']
country = "us"

url = f"https://newsapi.org/v2/top-headlines?country={country}&apiKey={newsKey}" # Typo in the URL

result = requests.get(url)
data = result.json()# Didn't format the data as json

for article in data['articles']:
  print(article['title'])
  print(article['url'])
  print(article['content'])
```
</details>