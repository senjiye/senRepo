import math
import sys

def getMinGrade(x):
	n = 2
	m = 99
	if x == 1:
		m = 1
	while(x>1):
		c = 0
		while(x%n!=0):
			n+=1
		while(x%n==0):
			x = x/n
			c +=1
		if (m > c):
			m = c
	return m


line = "smth"

while (line != ""):
	try:
		
		x, y = [int(x) for x in input().split()]
		if (x == y) and (y == 0):
			line = ""
		else:
			if (y != 1):
				i = getMinGrade(x)
				j = getMinGrade(y)
				n = int(min(i,j))
				while(int(math.ceil(pow(x,1/n)))-1 != int(math.ceil(pow(y,1/n)))):
					n = int(n/2)
				nValue = int(round(pow(y,1/n)))
				tHeight = y
				tCats = 0
				cats = 1
				for i in range(n):
					tCats += cats
					tHeight += x*cats
					#print(cats)
					#print(x)
					cats = cats*nValue
					x = x/(nValue+1)
				print(tCats, int(tHeight))
			else:
				tHeight = x
				tCats = 0
				cats = 1
				n = getMinGrade(x)
				if x == 1:
					print(0, x)
				else:
					for i in range(n):
						tCats += cats
						x = x/2
						tHeight += x
					print(tCats, int(tHeight))
			
	except EOFError:
		line = ""





