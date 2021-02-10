import requests
import random
url = "https://raw.githubusercontent.com/akash100507/lists/main/words.txt"

response = requests.get(url, stream=True)

l = []

for i in response.iter_lines():
  t = i.decode("utf-8")
  l.append(t)
  

#print(l)
print(len(l))

for w in random.sample(l,10):
  print(w)
