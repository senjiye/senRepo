import sys

letter = "BGC"
order = ["BCG", "BGC", "CBG", "CGB", "GBC", "GCB"]

input_str = sys.stdin.read()
for line in input_str.split("\n")[:-1]:
	a = list(map(int,line.split()))
	bin1 = a[0:3]
	sbin1 = sum(bin1)
	bin2 = a[3:6]
	sbin2 = sum(bin2)
	bin3 = a[6:9]
	sbin3 = sum(bin3)
	stotal = sbin1 + sbin2 + sbin3
	
	min = stotal
	form = "GCB"
	for i in range(3):
		s = stotal - bin1[(i)%3] - bin3[(i+2)%3] - bin2[(i+1)%3]
		if s == min:
			aux = letter[i] + letter[(i+1)%3] + letter[(i+2)%3]
			if order.index(aux) < order.index(form):
				form = aux
		if s < min:
			min = s 
			form = letter[i] + letter[(i+1)%3] + letter[(i+2)%3]
			
		s = stotal - bin1[(i)%3] - bin3[(i+1)%3] - bin2[(i+2)%3]
		if s == min:
			aux = letter[i] + letter[(i+2)%3] + letter[(i+1)%3]
			if order.index(aux) < order.index(form):
				form = aux
		if s < min:
			min = s 
			form = letter[i] + letter[(i+2)%3] + letter[(i+1)%3]


	print("%s %d" %(form, min))
	


