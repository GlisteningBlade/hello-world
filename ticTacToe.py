class sq():
	def __init__(self,pos):
		self.state = ' '



for i in range(1,10):
	exec("s{} = sq({})".format(i,i))


posList = [s1,s2,s3,s4,s5,s6,s7,s8,s9]
posDict =  {'1' : s1,
			'2' : s2,
			'3' : s3,
			'4' : s4,
			'5' : s5,
			'6' : s6,
			'7' : s7,
			'8' : s8,
			'9' : s9}

lC = [s1,s4,s7]
mC = [s2,s5,s8]
rC = [s3,s6,s9]
tR = [s1,s2,s3]
mR = [s4,s5,s6]
bR = [s7,s8,s9]
lX = [s1,s5,s9]
rX = [s3,s5,s7]

from time import sleep

wins = [lC,mC,rC,tR,mR,bR,lX,rX]

def markx(pos):
	global mark1
	global mark2
	if pos.state == ' ':
		pos.state = mark1
	show()

def marko(pos):
	global mark1
	global mark2
	if pos.state == ' ':
		pos.state = mark2
	show()

def checkWin():
	global mark1
	global mark2
	for i in wins:
		if i[0].state == i[1].state and i[1].state == i[2].state:
			if i[1].state == mark1:
				p1win()
			if i[1].state == mark2:
				p2win()

from time import sleep

def show():
	print("1     ▌2     ▌3     ")
	print("   {}  █   {}  █   {}  ".format(s1.state, s2.state, s3.state))
	print("▄▄▄▄▄▄█▄▄▄▄▄▄█▄▄▄▄▄▄▄")
	print("4     ▌5     ▌6     ")
	print("   {}  █   {}  █   {}  ".format(s4.state ,s5.state, s6.state))
	print("▄▄▄▄▄▄█▄▄▄▄▄▄█▄▄▄▄▄▄▄")
	print("7     ▌8     ▌9     ")
	print("   {}  █   {}  █   {}  ".format(s7.state, s8.state, s9.state))
	print("      █      █     ")

def setup():
	global mark1
	global mark2
	for i in posList:
		i.state = ' '
	print("Player 1, please enter what symbol you'd like to use.")
	print("Please note that only the first character will be used.")
	mark1 = input("")
	print("")
	print("Player 2, please enter what symbol you'd like to use.")
	mark2 = input("")
	if len(mark1) == 0:
		mark1 = 'X'
	if len(mark2) == 0:
		mark2 = 'O'
	mark1 = mark1[0]
	mark2 = mark2[0]
	if mark1 == ' ' or len(mark1) == 0:
		mark1 = 'X'
	if mark2 == ' ' or mark2 == mark1 or len(mark2) == 0:
		if mark1 != 'O':
			mark2 = 'O'
		else:
			mark2 = 'X'
	p1turn()

def clearscreen():
	for i in range(1,201):
		print("\n")

def p1turn():
	sleep(3)
	clearscreen()

	global mark1
	global mark2
	print("{}'s turn.\n".format(mark1))
	isTie = True
	for i in posList:
		if i.state == ' ':
			isTie = False
	if isTie == True:
		tie()
	show()
	print("Which place would you like to mark?")
	p1Pos = input("")
	if len(p1Pos) == 0 or not(p1Pos in '1 2 3 4 5 6 7 8 9'.split()):
		print("Hey, you can't mark a space that's not on the board.")
		p1turn()
	else:
		p1Pos = posDict[p1Pos]
		if p1Pos.state == ' ':
			markx(p1Pos)
			checkWin()
			p2turn()
		else:
			print("You can't mark a spot that's already filled.")
			p1turn()

def p2turn():
	sleep(3)
	clearscreen()
	global mark1
	global mark2
	print("{}'s turn.\n".format(mark2))
	isTie = True
	for i in posList:
		if i.state == ' ':
			isTie = False
	if isTie == True:
		tie()
	show()
	print("Which place would you like to mark?")
	p2Pos = input("")
	if len(p2Pos) == 0 or not(p2Pos in '1 2 3 4 5 6 7 8 9'.split()):
		print("Hey, you can't mark a space that's not on the board.")
		p2turn()
	else:
		p2Pos = posDict[p2Pos]
		if p2Pos.state == ' ':
			marko(p2Pos)
			checkWin()
			p1turn()
		else:
			print("You can't mark a spot that's already filled.")
			p2turn()

def p1win():
	clearscreen()
	global mark1
	print("Player 1, {}, won!".format(mark1))
	print("Type QUIT to quit, or anything else to play again.")
	n = input("")
	if n != 'QUIT':
		setup()

def p2win():
	clearscreen()
	global mark2
	print("Player 2, {}, won!".format(mark2))
	print("Type QUIT to quit, or anything else to play again.")
	n = input("")
	if n != 'QUIT':
		setup()
def tie():
	sleep(1)
	clearscreen()
	show()
	print("It's a tie!")
	print("Type QUIT to quit, or anything else to play again.")
	n = input("")
	if n != 'QUIT':
		setup()

def showbegin():
		print("      █      █      ")
		print("   T  █   I  █   C  ")
		print("▄▄▄▄▄▄█▄▄▄▄▄▄█▄▄▄▄▄▄")
		print("      █      █      ")
		print("   T  █   A  █   C  ")
		print("▄▄▄▄▄▄█▄▄▄▄▄▄█▄▄▄▄▄▄")
		print("      █      █      ")
		print("   T  █   O  █   E  ")
		print("      █      █      ")



showbegin()
sleep(1)
setup()
