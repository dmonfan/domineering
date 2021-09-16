#rescale to 5x5x5

import random

def rand_3tuples(n, m):
	items = []
	for i in range(m):
		items.append((random.randint(0,n-2),random.randint(0,n-2),random.randint(0,n-2)))

	return items


def print_grid(elist, n):
	grid = ""
	for i in range(n):
		for j in range(n):
			for k in range(n):
				if (i,j,k) in elist:
					grid += "X "
				else:
					grid += "O "
			grid += "\n"
		grid += "\n"
	print(grid)

def place_domino(elist, m, dir):
	if(dir == 0):
		dirx = 1
		diry = 0
		dirz = 0
	if(dir == 1):
		dirx = 0
		diry = 1
		dirz = 0
	if(dir == 2):
		dirx = 0
		diry = 0
		dirz = 1
	if m[0] < 0 or m[0] > 8: #check if x coordinate out of bounds
		return
	if m[1] < 0 or m[1] > 8: #check if y coordinate out of bounds
		return
	if m[2] < 0 or m[2] > 8: #check if z coordinate out of bounds
		return	
	if m in elist:
		return
	if (m[0]+dirx,m[1]+diry,m[2]+dirz) in elist:
		return
	elist.append(m)
	elist.append((m[0]+dirx,m[1]+diry,m[2]+dirz))

elist = []
l = 5 # max length of grid
m = 10 # moves

ilistx = rand_3tuples(l,m)
ilisty = rand_3tuples(l,m)
ilistz = rand_3tuples(l,m)

print(ilistx)
print(ilisty)
print(ilistz)

#convention is at spot n fill n+1

for i in range(l):
	place_domino(elist,ilistx[i],0)
	place_domino(elist,ilisty[i],1)
	place_domino(elist,ilistz[i],2)
	print(elist)
	print_grid(elist, l)

n = int(len(elist)/2)
print(n)