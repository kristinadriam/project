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
def ship_one(x,y,z):
	field[x].pop(y)
	field[x].insert(y,z)	
	
def ship_two(x,y,z,c,d):
	ship_one(x,y,z)
	ship_one(x+c,y+d,z)	
	
def ship_three(x,y,z,c,d):
	ship_two(x,y,z,c,d)
	ship_one(x+2*c,y+2*d,z) 
	
def ship_four(x,y,z,c,d):
	ship_three(x,y,z,c,d)
	ship_one(x+3*c,y+3*d,z) 	
		
def check(x,y):
	if field[x-1][y-1] == 0 and field[x-1][y] == 0 and field[x-1][y+1] == 0 and field[x][y-1] == 0 and field[x][y] == 0 and field[x][y+1] == 0 and field[x+1][y-1] == 0 and field[x+1][y] == 0 and field[x+1][y+1] == 0:
		a = 1
	else:
		a = 0
	return a
	
def print_board():
	for i in range(1,size-1):
		for j in range(1,size-1):
			if field[i][j] == 5:
				print('x', end=' ')	
			elif field[i][j] == 10:
				print('•', end=' ')		
			else:
				print('□', end=' ')				
		print()	
	print()					


# 4 deck
c = random.randint(0,1)
if c == 0:
	a = random.randint(1,7)
	b = random.randint(1,10)
	ship_four(a,b,4,1,0)
elif c == 1:
	a = random.randint(1,10)
	b = random.randint(1,7)
	ship_four(a,b,4,0,1)		
		
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
				ship_three(a,b,3,1,0)
				test = 1
		elif c == 1:
			a = random.randint(1,10)
			b = random.randint(1,8)	
			if check(a,b) == 1 and check(a,b+1) == 1 and check(a,b+2) == 1:
				ship_three(a,b,3,0,1)
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
				ship_two(a,b,2,1,0)
				test = 1
		elif c == 1:
			a = random.randint(1,10)
			b = random.randint(1,9)	
			if check(a,b) == 1 and check(a,b+1) == 1:
				ship_two(a,b,2,0,1)
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
			ship_one(a,b,1)
			test = 1

# check
print_board()
while a != 0:
	s, t = map(int, input().split())
	
	if field[s][t] == 0:
		field[s][t] = 10
	elif field[s][t] == 1:
		field[s][t] = 5
		print('Ты попал(а) в однопалубный корабль')
	elif field[s][t] == 2:
		field[s][t] = 5
		print('Ты попал(а) в двухпалубный корабль')
	elif field[s][t] == 3:
		field[s][t] = 5
		print('Ты попал(а) в трёхпалубный корабль')
	elif field[s][t] == 4:
		field[s][t] = 5
		print('Ты попал(а) в четырёхпалубный корабль')	
		
	print_board()					
