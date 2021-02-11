import requests
import random
  
def display(link):
  response = requests.get(link, stream=True)
  l = []
  for i in response.iter_lines():
    t = i.decode("utf-8")
    l.append(t)
  u = len(l)
  if (u>=335):
    m = 30
  else:
    m = 15
  for w in random.sample(l,m):
    print(w)
  
  
  
if __name__ == "__main__":
  url1 = "https://raw.githubusercontent.com/akash100507/lists/master/words1.txt"
  print("List1")
  display(url1)
  url2 = "https://raw.githubusercontent.com/akash100507/lists/master/words2.txt"
  print("List2")
  display(url2)
  url3 = "https://raw.githubusercontent.com/akash100507/lists/master/words3.txt"
  print("List3")
  display(url3)
  url4 = "https://raw.githubusercontent.com/akash100507/lists/master/words4.txt"
  print("List4")
  display(url4)
  url5 = "https://raw.githubusercontent.com/akash100507/lists/master/word_undo.txt"
  print("List5")
  display(url5)
