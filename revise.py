import requests
import random
  
def display(link):
  response = requests.get(link, stream=True)
  l = []
  for i in response.iter_lines():
    t = i.decode("utf-8")
    l.append(t)
  u = len(l)
  m = 75
  for w in random.sample(l,m):
    print(w)
    
if __name__ == "__main__":
  
  for j in range(1,4):
    url = "https://raw.githubusercontent.com/akash100507/lists/master/sets/lists"+str(j)+".txt"
    print("List "+str(j))
    display(url)
    print("\n\n\n------------------------------------\n\n")
