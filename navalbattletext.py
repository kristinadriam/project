import random

# field
size = 12
field = []
sum = 0

for i in range(size):
	field.append([])
	for j in range(size):
		field[i].append(0)		

# function
def ship_one(x,y):
	field[x].pop(y)
	field[x].insert(y,1)	
	
def ship_two(x,y,c,d):
	ship_one(x,y)
	ship_one(x+c,y+d)	
	
def ship_three(x,y,c,d):
	ship_two(x,y,c,d)
	ship_one(x+2*c,y+2*d) 
	
def ship_four(x,y,c,d):
	ship_three(x,y,c,d)
	ship_one(x+3*c,y+3*d) 	
		
def check(x,y):
	if field[x-1][y-1] == 0 and field[x-1][y] == 0 and field[x-1][y+1] == 0 and field[x][y-1] == 0 and field[x][y] == 0 and field[x][y+1] == 0 and field[x+1][y-1] == 0 and field[x+1][y] == 0 and field[x+1][y+1] == 0:
		a = 1
	else:
		a = 0
	return a
	
def print_board():
	for i in range(1,size-1):
		for j in range(1,size-1):
			if field[i][j] == 0:
				print('□', end=' ')
			elif field[i][j] == 1:
				print('■', end=' ')	
			elif field[i][j] == 2:
				print('•', end=' ')		
			else:
				print('x', end=' ')			
		print()	
	print()					


# 4 deck
c = random.randint(0,1)
if c == 0:
	a = random.randint(1,7)
	b = random.randint(1,10)
	ship_four(a,b,1,0)
elif c == 1:
	a = random.randint(1,10)
	b = random.randint(1,7)
	ship_four(a,b,0,1)		
		
# 3 deck
for i in range(2):
	test = 0
	a = 0
	b = 0
	c = random.randint(0,1)
	while test != 1:
		if c == 0: 
			a = random.randint(1,8)
			b = random.randint(1,10)	
			if check(a,b) == 1 and check(a+1,b) == 1 and check(a+2,b) == 1:
				ship_three(a,b,1,0)
				test = 1
		elif c == 1:
			a = random.randint(1,10)
			b = random.randint(1,8)	
			if check(a,b) == 1 and check(a,b+1) == 1 and check(a,b+2) == 1:
				ship_three(a,b,0,1)
				test = 1

# 2 deck
for i in range(3):
	test = 0
	a = 0
	b = 0
	c = random.randint(0,1)
	while test != 1:
		if c == 0: 
			a = random.randint(1,9)
			b = random.randint(1,10)	
			if check(a,b) == 1 and check(a+1,b) == 1:
				ship_two(a,b,1,0)
				test = 1
		elif c == 1:
			a = random.randint(1,10)
			b = random.randint(1,9)	
			if check(a,b) == 1 and check(a,b+1) == 1:
				ship_two(a,b,0,1)
				test = 1

# 1 deck
for i in range(4):
	test = 0
	a = 0
	b = 0
	while test != 1:
		a = random.randint(1,10)
		b = random.randint(1,10)	
		if check(a,b) == 1:
			ship_one(a,b)
			test = 1

# check
for i in range(1,size-1):
	for j in range(1,size-1):
		if field[i][j] == 0:
			print('□', end=' ')
		elif field[i][j] == 1:
			print('■', end=' ')	
		else:
			print('x', end=' ')			
	print()	
print()

a, b = map(int, input().split())

if field[a][b] == 0:
	field[a][b] = 2
	print_board()
elif field[a][b] == 1:
	field[a][b] = 3	
	print_board()
