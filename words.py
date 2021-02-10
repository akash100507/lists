import requests
import random
  
def display(link):
  response = requests.get(link, stream=True)
  l = []
  for i in response.iter_lines():
    t = i.decode("utf-8")
    l.append(t)
  print(len(l))
  for w in random.sample(l,10):
    print(w)
  
  
  
if __name__ == "__main__":
  url1 = "https://raw.githubusercontent.com/akash100507/lists/main/words1.txt"
  print("List1")
  display(url1)
  url2 = "https://raw.githubusercontent.com/akash100507/lists/main/words2.txt"
  print("List2")
  display(url2)
