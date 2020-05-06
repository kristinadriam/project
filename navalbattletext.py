import random

# необходимые значения
size = 12
field = []
shots = 0
killed = 0
n = 50

#Выносим в отдельное место все те символы, что используются для рисования
# проще поменять символ и не нужно помнить где какой
#пример
DEAD_SHIP = 'x'

# инструкция
print('Привет!')
print()
print('Ты попал во всем известную с детства игру "Морской бой"! Правила просты: "выбей" 10 кораблей (один четырёхпалубный, два трёхпалубных, три двухпалубных и четыре однопалубных) – и ты победил. Но не забывай, что количество ходов ограничено – их всего 50. Так что следи за этим, иначе, увы, проиграешь. Но гарантирую, что тебе этого числа хватит сполна :)')
print('Чтобы начать играть, введи координаты в формате буква (заглавная, кириллица)-пробел-число.')
print()
print('Вот некоторые обозначения, которые тебе могут встретиться:')
print('□ – пустая клетка.')
print('• – промах, совершённый этим ходом.')
print('• – промах, совершённый несколько ходов назад.')
print('✶ – "убитый" этим ходом корабль или его часть.')
print(DEAD_SHIP, '– "убитый" несколько ходов назад корабль или его часть.')
print()
print('Удачи, игрок!')


#можно подкрашивать текст, например место взрыва, ибо так веселее!
print("\033[31m {}" .format("красненький текст"))
print("печатаем что-то")
print("\033[30m {}" .format("а тут он обратно черным стал"))
print()

# поле
for i in range(size):
	field.append([])
	for j in range(size):
		field[i].append(0)		

# полезные функции: установка кораблей
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

# полезные функции: проверка и вывод доски
def print_board():
	print(' ', end='  ')
	letters = ['А','Б','В','Г','Д','Е','Ж','З','И','К']
	for i in letters:
		print(i, end=' ')	
	print()
	for i in range(1,size-2):
		print(i, end='  ')
		for j in range(1,size-1):
			if field[i][j] == 5:
				print('✶', end=' ')
				field[i].pop(j)
				field[i].insert(j,6)
			elif field[i][j] == 6:
				print(DEAD_SHIP, end=' ')
			elif field[i][j] == 11:
				print('◎', end=' ')
				field[i].pop(j)
				field[i].insert(j,10)
			elif field[i][j] == 10:
				print('•', end=' ')		
			else:
				print('□', end=' ')				
		print()
	print(size-2, end=' ')
	for j in range(1,size-1):
		i = 10
		if field[i][j] == 5:
			print('✶', end=' ')
			field[i].pop(j)
			field[i].insert(j,6)
		elif field[i][j] == 6:
			print(DEAD_SHIP, end=' ')
		elif field[i][j] == 11:
			print('◎', end=' ')
			field[i].pop(j)
			field[i].insert(j,10)
		elif field[i][j] == 10:
			print('•', end=' ')		
		else:
			print('□', end=' ')							
	print()			
	print()			


def shot(l):
	global shots, killed
	shots = shots + 1
	field[s][t] = l
	killed += 1
	print()
	print('Ты попал(а).')


# установка 4-палубного корабля
c = random.randint(0,1)

if c == 0:
	a = random.randint(1,7)
	b = random.randint(1,10)
	ship_four(a,b,4,1,0)
elif c == 1:
	a = random.randint(1,10)
	b = random.randint(1,7)
	ship_four(a,b,4,0,1)		
		
# установка 3-палубных кораблей
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

# установка 2-палубных кораблей
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

# установка 1-палубных кораблей
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

# проверка и вывод доски
print_board()

while killed != 20 or shots != n:
	letters = ['А','Б','В','Г','Д','Е','Ж','З','И','К']
	print('Координаты следующего выстрела:')
	try:
		t, s = input().split()
		s = int(s)
		t = int(letters.index(t)) + 1
	except ValueError:
		print('Ты что-то не то ввёл.')
		print()
		continue

	if field[s][t] == 0:
		shots = shots + 1
		field[s][t] = 11
	elif field[s][t] == 1:
		shot(5)
	elif field[s][t] == 2:
		shot(5)
	elif field[s][t] == 3:
		shot(5)
	elif field[s][t] == 4:
		shot(5)
	else:
		print('Упс, сюда ты уже стрелял(а).')
		print()
	print()		
	print_board()
	print('Осталось ' + str(n-shots) + ' выстрелов из ' + str(n) + '.')
	print('———————————————————————————')
	print()
	
# конец игры	
if shots == n and killed != 20:
	print('Ты проиграл(а).')
elif int(killed) == 20:
	print('Ты выиграл(а)!')
