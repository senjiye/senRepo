import math
import sys

line = "smth"
ts = []
while (line != ""):
	try:
		ts.append([int(x) for x in input().split()])
			
	except EOFError:
		line = ""
m = 0

for i in ts:
	if m < i[2]:
		m = i[2]

soil = [0] * (m+1)

for i in ts:
	for j in range(i[0],i[2]):
		if soil[j] < i[1]:
			soil[j] = i[1]
			

pv = 0
for i in range(1,m):
	if soil[i] != pv:
		print("%d %d"%(i, soil[i]),end=" ")
		pv = soil[i]
print("%d %d"%(m, 0))

