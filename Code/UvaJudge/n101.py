#n101

n = int(input())
a = ""
l = []
pos = []
for i in range(n):
	l.append([i])
	pos.append(i)

while a!="quit":
	a = input()
	if a!="quit" :
		s,f,m,t = a.split()
		f = int(f)
		t = int(t)
		if f != t and pos[f] != pos[t]:
			if m == "over":
				#move over
				if s == "move":
					while l[pos[f]][-1] != f:
						n = l[pos[f]].pop()
						l[n].insert(0,n)
						pos[n] = n
					l[pos[f]].remove(f)
					l[pos[t]].append(f)
					pos[f] = pos[t]
				#pile over
				else:
					aux = l[pos[f]].index(f)
					aux2 = l[pos[t]].index(t)
					auxmatrix = list(l[pos[f]][aux:])
					for i in auxmatrix:
						l[pos[t]].append(i)
					for i in auxmatrix:
						l[pos[f]].remove(i)
					for i in auxmatrix:
						pos[i] = pos[t]
			else:
				#move onto
				if s == "move":
					while l[pos[f]][-1] != f:
						n = l[pos[f]].pop()
						l[n].insert(0,n)
						pos[n] = n
					while l[pos[t]][-1] != t:
						n = l[pos[t]].pop()
						l[n].insert(0,n)
						pos[n] = n
					l[pos[f]].remove(f)
					l[pos[t]].append(f)
					pos[f] = pos[t]
				#pile onto
				else:
					while l[pos[t]][-1] != t:
						n = l[pos[t]].pop()
						l[n].insert(0,n)
						pos[n] = n
					aux = l[pos[f]].index(f)
					auxmatrix = list(l[pos[f]][aux:])
					for i in auxmatrix:
						l[pos[f]].remove(i)
					for i in auxmatrix:
						l[pos[t]].append(i)
						pos[i] = pos[t]
					
			
	
iter = 0
for i in l:
	print(iter, end="")
	print(":", end="")
	for ii in i:
		print(" ", end="")
		print(ii, end="")
	print()	
	iter = iter + 1




