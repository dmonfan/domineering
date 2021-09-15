def print_grid(elist):
	grid = ""
	for i in range(10):
		for j in range(10):
			if (i,j) in elist:
				grid += "X "
			else:
				grid += "O "
		grid += "\n"
	print(grid)

def place_domino(elist, m, dir):
	if(dir == 0):
		dirx = 1
		diry = 0
	if(dir == 1):
		dirx = 0
		diry = 1
	if m[0] < 0 or m[0] > 8: #check if x coordinate out of bounds
		return
	if m[1] < 0 or m[1] > 8: #check if y coordinate out of bounds
		return 	
	if m in elist:
		return
	if (m[0]+dirx,m[1]+diry) in elist:
		return
	elist.append(m)
	elist.append((m[0]+dirx,m[1]+diry))

elist = []
l = 10; #max length of grid

ilistx = [(0,4),(3,7),(1,1),(0,7),(2,4),(9,6),(2,3),(4,4),(6,6),(8,3)]
ilisty = [(1,2),(4,2),(4,7),(2,7),(2,4),(6,8),(1,7),(0,0),(5,2),(5,1)]

#convention is at spot n fill n+1

for i in range(l):
	place_domino(elist,ilistx[i],0)
	place_domino(elist,ilisty[i],1)
	print_grid(elist)

n = int(len(elist)/2)
print(n)