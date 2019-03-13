import math
import sys

line = "smth"
def fit(c1, c2):
	co1 = list(map(int,c1[:]))
	co2 = list(map(int,c2[:]))
	for i in range(len(c1)):
		if min(co1) < min(co2):
			co1.remove(min(co1))
			co2.remove(min(co2))
		else:
			return False
	return True

	
while (line != ""):
	try:
		line = input()
		n, l = line.split()
		n = int(n)
		l = int(l)
		cubes = []
		orden = []
		tails = []
		nex = []
		weight = []
		for i in range(n):
			nex.append(0)
			tails.append([])
			weight.append(1)
		num = 0
		for i in range(n):
			cubes.append(input().split())
		for i in range(n):
			for j in range(n):
				if fit(cubes[i],cubes[j]):
					tails[i].append(j)

		itera = 1
		for asdasd in range(n):
			#print (itera)
			for i in range(n):
				if len(tails[i]) == itera:
			#		print(tails[i])
					for w in tails[i]:
						if((weight[w]+1)>weight[i]):
							weight[i] = (weight[w]+1)
							nex[i] = w
			itera = itera + 1
		if n > 0:
			print(max(weight))
			pos = weight.index(max(weight))
			print(pos+1,end=" ")
			for i in range(max(weight)-2):
				print (nex[pos]+1, end=" ")
				pos = nex[pos]
			if (max(weight)) != 1:
				print (nex[pos]+1)
		else:
			print(1)
			print(1)
		
	except EOFError:
		line = ""

