import requests
import random

def display(l):
	# h = []
	# for i in l:
	# 	t = i.decode("utf-8")
	# 	h.append(t)
	# u = len(h)
	m = 5
	for w in random.sample(l,m):
		print(w)

	
with open('E:\lists\sample.txt') as f:
	lines = f.read().splitlines()

print(lines)
display(lines)
