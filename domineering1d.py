elist = []
l = 10; #max length of list

ilist = [0,3,-1,0,2,10,2,4,6,8,'q']

#convention is at spot n fill n+1

for m in ilist:
	if m == 'q':
		break
	if m < 0 or m > 8:
		continue
	if m in elist:
		continue
	if (m+1) in elist:
		continue
	elist.append(m)
	elist.append(m+1)
	print(elist)

n = int(len(elist)/2)
print(n)