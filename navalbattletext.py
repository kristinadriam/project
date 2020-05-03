import random

# fields
size = 10
field1 = []
field2 = []

for i in range(size):
	field1.append([])
	for j in range(size):
		field1[i].append(0)		
		
		
for i in range(size):
	field2.append([])
	for j in range(size):
		field2[i].append([0, 0])		

# function
def ship_one():
	field1[a].pop(b)
	field1[a].insert(b,1)	
	return
	
def ship_two(x,y):
	ship_one()
	field1[a+x].pop(b+y)
	field1[a+x].insert(b+y,1)
	return 	
	
def ship_three(x,y):
	for i in range(0,3):
		field1[a+x*i].pop(b+y*i)
		field1[a+x*i].insert(b+y*i,1)	 	
		
# 4 deck
c = random.randint(0,1)
d = random.randint(1,2)
e = (-1)**d
if c == 0:
	a = random.randint(3,6)
	b = random.randint(0,9)
	for i in range(1,4):
		field1[a+e*i].pop(b)
		field1[a+e*i].insert(b,1)
elif c == 1:
	a = random.randint(0,9)
	b = random.randint(3,6)
	for i in range(1,4):
		field1[a].pop(b+e*i)
		field1[a].insert(b+e*i,1)	
field1[a].pop(b)
field1[a].insert(b, 1)	

# 3 deck
for i in range(2):
	a = random.randint(0,7)
	b = random.randint(0,7)	
	c = random.randint(0,1)
	while field1[a][b] != 1:
		if c == 0: 
			a = random.randint(0,7)
			b = random.randint(0,9)	
			if field1[a][b] == 0:
				# крайние точки
				if (b == 0 or b == 9) and a == 0 and field1[a+1][b] == 0 and field1[a+2][b] == 0 and field1[a+3][b] == 0 and field1[a][b+1-2*b//9] == 0 and field1[a+1][b+1-2*b//9] == 0 and field1[a+2][b+1-2*b//9] == 0 and field1[a+3][b+1-2*b//9] == 0:
					ship_three(1,0)
				elif (b == 0 or b == 9) and a == 7 and field1[a-1][b] == 0 and field1[a+1][b] == 0 and field1[a+2][b] == 0 and field1[a-1][b+1-2*b//9] == 0 and field1[a][b+1-2*b//9] == 0 and field1[a+1][b+1-2*b//9] == 0 and field1[a+2][b+1-2*b//9] == 0:
					ship_three(1,0)
				# края	
				elif (a == 7 or a == 0) and b != 0 and b != 9 and field1[a][b-1] == 0 and field1[a+1][b-1] == 0 and field1[a+2][b-1] == 0 and field1[a+1][b] == 0 and field1[a+2][b] == 0 and field1[a][b+1] == 0 and field1[a+1][b+1] == 0 and field1[a+2][b+1] == 0 and field1[a+3-4*a//8][b-1] == 0 and field1[a+3-4*a//8][b] == 0 and field1[a+3-4*a//8][b+1] == 0:
					ship_three(1,0)
				elif (b == 0 or b == 9) and a != 0 and a != 9 and field1[a-1][b] == 0 and field1[a+1][b] == 0 and field1[a+2][b] == 0 and field1[a+3][b] == 0 and field1[a-1][b+1-2*b//9] == 0 and field1[a][b+1-2*b//9] == 0 and field1[a+1][b+1-2*b//9] == 0 and field1[a+2][b+1-2*b//9] == 0 and field1[a+3][b+1-2*b//9] == 0:
					ship_three(1,0)
				# другое
				elif a != 0 and a != 8 and b != 9 and b != 0 and field1[a-1][b-1] == 0 and field1[a][b-1] == 0 and field1[a+1][b-1] == 0 and field1[a+2][b-1] == 0 and field1[a+3][b-1] == 0 and field1[a-1][b] == 0 and field1[a+1][b] == 0 and field1[a+2][b] == 0 and field1[a+3][b] == 0 and field1[a-1][b+1] == 0 and field1[a][b+1] == 0 and field1[a+1][b+1] == 0 and field1[a+2][b+1] == 0 and field1[a+3][b+1] == 0:
					ship_two(1,0)
		elif c == 1:
			a = random.randint(0,9)
			b = random.randint(0,7)	
			if field1[a][b] == 0:
				# крайние точки	
				if (a == 0 or a == 9) and b == 0 and field1[a][b+1] == 0 and field1[a][b+2] == 0 and field1[a][b+3] == 0 and field1[a+1-2*a//9][b] == 0 and field1[a+1-2*a//9][b+1] == 0 and field1[a+1-2*a//9][b+2] == 0 and field1[a+1-2*a//9][b+3] == 0:
					ship_two(0,1)
				elif (a == 0 or a == 9) and b == 7 and field1[a][b-1] == 0 and field1[a][b+1] == 0 and field1[a][b+2] == 0 and field1[a+1-2*a//9][b-1] == 0 and field1[a+1-2*a//9][b] == 0 and field1[a+1-2*a//9][b+1] == 0 and field1[a+1-2*a//9][b+2] == 0:
					ship_two(0,1)
				# края	
				elif (a == 9 or a == 0) and b != 0 and b != 7 and field1[a][b-1] == 0 and field1[a][b+1] == 0 and field1[a][b+2] == 0 and field1[a][b+3] == 0 and field1[a+1-2*a//9][b-1] == 0 and field1[a+1-2*a//9][b] == 0 and field1[a+1-2*a//9][b+1] == 0 and field1[a+1-2*a//9][b+2] == 0 and field1[a+1-2*a//9][b+3] == 0:
					ship_two(0,1)
				elif (b == 8 or b == 0) and a != 0 and a != 9 and field1[a-1][b] == 0 and field1[a+1][b] == 0 and field1[a-1][b+1] == 0 and field1[a][b+1] == 0 and field1[a+1][b+1] == 0 and field1[a-1][b+2] == 0 and field1[a][b+2] == 0 and field1[a+1][b+2] == 0 and field1[a-1][b+3-4*b//9] == 0 and field1[a][b+3-4*b//9] == 0 and field1[a+1][b+3-4*b//9] == 0:
					ship_two(0,1)
				# другое
				elif a != 0 and a != 9 and b != 7 and b != 0 and field1[a-1][b-1] == 0 and field1[a-1][b] == 0 and field1[a-1][b+1] == 0 and field1[a-1][b+2] == 0 and field1[a-1][b+3] == 0 and field1[a][b-1] == 0 and field1[a][b+1] == 0 and field1[a][b+2] == 0 and field1[a][b+3] == 0 and field1[a+1][b-1] == 0 and field1[a+1][b] == 0 and field1[a+1][b+1] == 0 and field1[a+1][b+2] == 0 and field1[a+1][b+3] == 0:
					ship_two(0,1)	

# 2 deck
for i in range(3):
	a = random.randint(0,8)
	b = random.randint(0,8)	
	c = random.randint(0,1)
	while field1[a][b] != 1:
		if c == 0: 
			a = random.randint(0,8)
			b = random.randint(0,9)	
			if field1[a][b] == 0:
				# крайние точки
				if (b == 0 or b == 9) and a == 0 and field1[a+1][b] == 0 and field1[a+2][b] == 0 and field1[a][b+1-2*b//9] == 0 and field1[a+1][b+1-2*b//9] == 0 and field1[a+2][b+1-2*b//9] == 0:
					ship_two(1,0)
				elif (b == 0 or b == 9) and a == 8 and field1[a-1][b] == 0 and field1[a+1][b] == 0 and field1[a-1][b+1-2*b//9] == 0 and field1[a][b+1-2*b//9] == 0 and field1[a+1][b+1-2*b//9] == 0:
					ship_two(1,0)
				# края	
				elif (a == 8 or a == 0) and b != 0 and b != 9 and field1[a][b-1] == 0 and field1[a+1][b-1] == 0 and field1[a+1][b] == 0 and field1[a][b+1] == 0 and field1[a+1][b+1] == 0 and field1[a+2-3*a//8][b-1] == 0 and field1[a+2-3*a//8][b] == 0 and field1[a+2-3*a//8][b+1] == 0:
					ship_two(1,0)
				elif (b == 0 or b == 9) and a != 0 and a != 8 and field1[a-1][b] == 0 and field1[a+1][b] == 0 and field1[a+2][b] == 0 and field1[a-1][b+1-2*b//9] == 0 and field1[a][b+1-2*b//9] == 0 and field1[a+1][b+1-2*b//9] == 0 and field1[a+2][b+1-2*b//9] == 0:
					ship_two(1,0)
				# другое
				elif a != 0 and a != 8 and b != 9 and b != 0 and field1[a-1][b-1] == 0 and field1[a][b-1] == 0 and field1[a+1][b-1] == 0 and field1[a+2][b-1] == 0 and field1[a-1][b] == 0 and field1[a+1][b] == 0 and field1[a+2][b] == 0 and field1[a-1][b+1] == 0 and field1[a][b+1] == 0 and field1[a+1][b+1] == 0 and field1[a+2][b+1] == 0:
					ship_two(1,0)
		elif c == 1:
			a = random.randint(0,9)
			b = random.randint(0,8)	
			if field1[a][b] == 0:
				# крайние точки	
				if (a == 0 or a == 9) and b == 0 and field1[a][b+1] == 0 and field1[a][b+2] == 0 and field1[a+1-2*a//9][b] == 0 and field1[a+1-2*a//9][b+1] == 0 and field1[a+1-2*a//9][b+2] == 0:
					ship_two(0,1)
				elif (a == 0 or a == 9) and b == 8 and field1[a][b-1] == 0 and field1[a][b+1] == 0 and field1[a+1-2*a//9][b-1] == 0 and field1[a+1-2*a//9][b] == 0 and field1[a+1-2*a//9][b+1] == 0:
					ship_two(0,1)
				# края	
				elif (a == 9 or a == 0) and b != 0 and b != 8 and field1[a][b-1] == 0 and field1[a][b+1] == 0 and field1[a][b+2] == 0 and field1[a+1-2*a//9][b-1] == 0 and field1[a+1-2*a//9][b] == 0 and field1[a+1-2*a//9][b+1] == 0 and field1[a+1-2*a//9][b+2] == 0:
					ship_two(0,1)
				elif (b == 8 or b == 0) and a != 0 and a != 9 and field1[a-1][b] == 0 and field1[a+1][b] == 0 and field1[a-1][b+1] == 0 and field1[a][b+1] == 0 and field1[a+1][b+1] == 0 and field1[a-1][b+2-3*b//9] == 0 and field1[a][b+2-3*b//9] == 0 and field1[a+1][b+2-3*b//9] == 0:
					ship_two(0,1)
				# другое
				elif a != 0 and a != 9 and b != 8 and b != 0 and field1[a-1][b-1] == 0 and field1[a-1][b] == 0 and field1[a-1][b+1] == 0 and field1[a-1][b+2] == 0 and field1[a][b-1] == 0 and field1[a][b+1] == 0 and field1[a][b+2] == 0 and field1[a+1][b-1] == 0 and field1[a+1][b] == 0 and field1[a+1][b+1] == 0 and field1[a+1][b+2] == 0:
					ship_two(0,1)	
						
# 1 deck
for i in range(4):
	a = random.randint(0,9)
	b = random.randint(0,9)
	while field1[a][b] != 1:
		a = random.randint(0,9)
		b = random.randint(0,9)
		if field1[a][b] == 0:
			if a != 0 and a != 9 and b != 0 and b != 9 and field1[a-1][b-1] == 0 and field1[a-1][b] == 0 and field1[a-1][b+1] == 0 and field1[a][b-1] == 0 and field1[a][b+1] == 0 and field1[a+1][b-1] and field1[a+1][b] == 0 and field1[a+1][b+1] == 0:
				ship_one()	
			# крайние точки 	
			elif a == 0 and (b == 0 or b == 9) and field1[a+1][b] == 0 and field1[a][b+1-2*b//9] == 0 and field1[a+1][b+1-2*b//9] == 0:
				ship_one()		
			elif a == 9 and (b == 0 or b == 9) and field1[a-1][b] == 0 and field1[a][b+1-2*b//9] == 0 and field1[a-1][b+1-2*b//9] == 0:
				ship_one()	
			# края				
			elif (a == 0 or a == 9) and b != 0 and b != 9 and field1[a][b-1] == 0 and field1[a][b+1] == 0 and field1[a+1-2*a//9][b+1] == 0 and field1[a+1-2*a//9][b] == 0 and field1[a+1-2*a//9][b-1] == 0:
				ship_one()						
			elif (b == 0 or b == 9) and a != 0 and a != 9 and field1[a-1][b] == 0 and field1[a+1][b] == 0 and field1[a-1][b+1-2*b//9] == 0 and field1[a][b+1-2*b//9] == 0 and field1[a+1][b+1-2*b//9] == 0:
				ship_one()	
											
# check
for i in range(size):
	for j in range(size):
		if field1[i][j] == 0:
			print('□', end=' ')
		elif field1[i][j] == 1:
			print('■', end=' ')	
		else:
			print('x', end=' ')			
	print()	
print()


