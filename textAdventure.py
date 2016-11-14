'''
Name: The Emerald Jungle
A Text Based Adventure Game

By Nicholas Strickland
'''


print("Do you want FAST or SLOW text scrolling?") # In this game, I use text scrolling
scrollspeed = input("")
if 'f' in scrollspeed or 'F' in scrollspeed:      # Here, they can choose whether it's faster or slower
	scrollspeed = 'FAST'
else:
	scrollspeed = 'SLOW'

print("Do you have any passwords?") # Additionally, I use a passcode system, similar to old games
passcode = input("")				# It makes it so you can return to a location if you've reached it
if len(passcode) == 0:
	passcode = ' '
elif passcode == 'WildWolf':
	location = 'jungle'
	inven = ['club','torch','wolf']

elif passcode == 'DeepDarkness':
	location = 'cave'
	inven = ['meat','club','torch']
	cookmeter = 0
else:
	location = 'start'

def show(inven): # This function just shows the inventory.
	txt("PACK")
	print("")
	for i in inven:
		print(str(i).title())
	print("")




def clearscreen():
	sleep(1.25)
	for i in range(1,201):
		print("")

def sinput(strings):   # This is used as an alternative to the input
	n = input(strings) # While an input() would cause an error if they entered nothing and you used .lower()
	if len(n) == 0:    # This would return an empty string
		n = ' '
	return n
from graphics import *
from random import choice

def ded(colorn): # This function is used for the death screens
	win = GraphWin('You died!',400,400) # IT basically just pops up a screen
	row = 4                             # Makes some cool colors
	col = 4                             # And pauses
	rowc = 400 / col
	colc = 400 / col
	for i in range(0,30):
		for i in range(0,row+1):
			for b in range(0,col+1):
				p1 = Point(i*rowc,b*colc)
				p2 = Point((i*rowc)+rowc,(b*colc)+colc)
				rect = Rectangle(p1,p2)
				if 'darkblue' in colorn: # Drowning
					rFill = choice(range(1,2))
					gFill = choice(range(1,2))
					bFill = choice(range(1,156))
	
				elif 'darkred' in colorn: # Stabbed
					rFill = choice(range(1,156))
					gFill = choice(range(1,2))
					bFill = choice(range(1,2))
	
				elif 'darkgreen' in colorn: # Poisoned
					rFill = choice(range(1,2))
					gFill = choice(range(1,156))
					bFill = choice(range(1,2))
	
				rectColor = color_rgb(rFill,gFill,bFill)
				rect.setFill(rectColor)
				rect.setOutline(rectColor)
				rect.draw(win)

# ded('darkblue')
# ded('darkred')    # These were used to test it at the start.
# ded('darkgreen')    Uncomment it to see them.

from time import sleep
clearscreen()
title1 = '''
████████╗██╗  ██╗███████╗
╚══██╔══╝██║  ██║██╔════╝ 
   ██║   ███████║█████╗
   ██║   ██╔══██║██╔══╝
   ██║   ██║  ██║███████╗
   ╚═╝   ╚═╝  ╚═╝╚══════╝''' # The title screen is broken into three parts, so it doesn't all print at once.

title2 = '''
███████╗███╗   ███╗███████╗██████╗  █████╗ ██╗     ██████╗
██╔════╝████╗ ████║██╔════╝██╔══██╗██╔══██╗██║     ██╔══██╗
█████╗  ██╔████╔██║█████╗  ██████╔╝███████║██║     ██║  ██║
██╔══╝  ██║╚██╔╝██║██╔══╝  ██╔══██╗██╔══██║██║     ██║  ██║
███████╗██║ ╚═╝ ██║███████╗██║  ██║██║  ██║███████╗██████╔╝
╚══════╝╚═╝     ╚═╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═════╝'''

title3 = '''
     ██╗██╗   ██╗███╗   ██╗ ██████╗ ██╗     ███████╗
     ██║██║   ██║████╗  ██║██╔════╝ ██║     ██╔════╝
     ██║██║   ██║██╔██╗ ██║██║  ███╗██║     █████╗
██   ██║██║   ██║██║╚██╗██║██║   ██║██║     ██╔══╝
╚█████╔╝╚██████╔╝██║ ╚████║╚██████╔╝███████╗███████╗
 ╚════╝  ╚═════╝ ╚═╝  ╚═══╝ ╚═════╝ ╚══════╝╚══════╝
'''
# This is the title screen used for the endings.
# It's different.
altTitle = ''' 
   ▄▄▄▄▀ ▄  █ ▄███▄                          
▀▀▀ █   █   █ █▀   ▀                         
    █   ██▀▀█ ██▄▄                           
   █    █   █ █▄   ▄▀                        
  ▀        █  ▀███▀                          
          ▀                                  
                                             
▄███▄   █▀▄▀█ ▄███▄   █▄▄▄▄ ██   █     ██▄   
█▀   ▀  █ █ █ █▀   ▀  █  ▄▀ █ █  █     █  █  
██▄▄    █ ▄ █ ██▄▄    █▀▀▌  █▄▄█ █     █   █ 
█▄   ▄▀ █   █ █▄   ▄▀ █  █  █  █ ███▄  █  █   
▀███▀      █  ▀███▀     █      █     ▀ ███▀  
          ▀            ▀      █              
                             ▀               
  ▄▄▄▄▄ ▄      ▄     ▄▀  █     ▄███▄         
▄▀  █    █      █  ▄▀    █     █▀   ▀        
    █ █   █ ██   █ █ ▀▄  █     ██▄▄          
 ▄ █  █   █ █ █  █ █   █ ███▄  █▄   ▄▀       
  ▀   █▄ ▄█ █  █ █  ███      ▀ ▀███▀         
       ▀▀▀  █   ██                           
                                             
'''
print("") 
# The Game Over screen.
# You only see this if you die.
gameOver = '''
  ▄████  ▄▄▄       ███▄ ▄███▓▓█████
 ██▒ ▀█▒▒████▄    ▓██▒▀█▀ ██▒▓█   ▀
▒██░▄▄▄░▒██  ▀█▄  ▓██    ▓██░▒███
░▓█  ██▓░██▄▄▄▄██ ▒██    ▒██ ▒▓█  ▄
░▒▓███▀▒ ▓█   ▓██▒▒██▒   ░██▒░▒████▒
 ░▒   ▒  ▒▒   ▓▒█░░ ▒░   ░  ░░░ ▒░ ░
  ░   ░   ▒   ▒▒ ░░  ░      ░ ░ ░  ░
░ ░   ░   ░   ▒   ░      ░      ░
      ░       ░  ░       ░      ░  ░

 ▒█████   ██▒   █▓▓█████  ██▀███
▒██▒  ██▒▓██░   █▒▓█   ▀ ▓██ ▒ ██▒
▒██░  ██▒ ▓██  █▒░▒███   ▓██ ░▄█ ▒
▒██   ██░  ▒██ █░░▒▓█  ▄ ▒██▀▀█▄
░ ████▓▒░   ▒▀█░  ░▒████▒░██▓ ▒██▒
░ ▒░▒░▒░    ░ ▐░  ░░ ▒░ ░░ ▒▓ ░▒▓░
  ░ ▒ ▒░    ░ ░░   ░ ░  ░  ░▒ ░ ▒░
░ ░ ░ ▒       ░░     ░     ░░   ░
    ░ ░        ░     ░  ░   ░
              ░
'''


# '''
# The basic story is this.
# You play as a guy lost in a jungle.
# Don't die.
# Escape!
# '''
#

def stxt(string1): # I never used this, but I made it anyways
	print(string1)
	sleep(0.75)

if 'F' in scrollspeed: # this is where that scroll speed comes in again


	def txt(string1):
		print(string1) # If they chose fast, it makes it so the delays for text scrolling is smaller
		sleep(0.75)

	def ltxt(string1):
		print(string1)
		sleep(1.5)

else:
	def txt(string1):
		print(string1)
		sleep(1.25)
					# If not, it makes the delay larger
	def ltxt(string1):
		print(string1)
		sleep(2.25)
	
if location == 'start':
	inven = []
	ltxt("This is my text adventure project for Computers and Connections.") # Instructions! 
	print("Objects you can interact with or actions you can perform are always")
	txt("shown in ALL CAPS.")
	txt("Also, you can type PACK to view your inventory.") # For most of the game, you can type in any item thta's in all caps
	n = input("Press Enter to begin..")					   # And you'll use it / interact with it / go there / etc.
	clearscreen()
	ltxt("Lost in a harsh environment, you must survive with only your wits.")
	ltxt("Welcome to...")
	stxt(title1)
	stxt(title2) # Title screen! it's neat
	stxt(title3)
	print("")
	n = input("Press enter to begin...")

	clearscreen()
	txt('')
	txt('You open your eyes to a canopy of branches.')
	txt('After stirring, a few animals scatter.') # This line is awful and should have never been written
	ltxt("You get up, and look around, finding yourself in a thick jungle.")
	ltxt("You have nothing but a backpack and the clothes on your back.")
	txt("There is a STICK on the ground. There's also an EXIT to your left.") # You pick up the stick, or you  just leave. Nothing else.
	action = input("")
	if len(action) == 0:
		action = ' '
	print("")
	if 'stick' in action.lower(): # This is how it tests what you wanted to do.
								  # It checks if the non case-sensitive keyword is anywhere in the input.
								  # If so, it carries out the associated action.
								  # Because of this, 'grab stick' does the same thing as 'pick up stick' or 'go a sit on the stick, then pick it up, then leave' 
		txt("You pick up the stick, then exit to your left.") # Speak calmly and carry a big stick. that's what I always say.
		inven.append('stick')

	else:
		txt("You decide to leave the stick behind and exit to your left.") # This one doesn't use a while loop.
	sleep(1)  															   # I use while to keep performing actions until they leave the location
	clearscreen()
	txt("After leaving the clearing you woke up in, you see what seems to be a camp.") 
	if not 'skipahead' in action:
		location = 'clearing'

	sleep(1)

if location == 'clearing':
	cookmeter = 0 # Keeps track of how much you cook the meat
while location == 'clearing':
	sleep(2)
	clearscreen()
	print("")
	if not 'meat' in inven: # IT only talks about the meat if you don't have it
		txt("There's a CAMPFIRE here, with some MEAT hanging above it.")
	else:
		txt("There's a CAMPFIRE here, perfect if you want to COOK something.")
	if not 'club' in inven:
		txt("Next to the CAMPFIRE, a CLUB lies on the ground.")
	txt("The PATH continues forward.")
	n = input("")
	print("")
	if len(n) == 0:
		n = ' '
	if 'pack' in n.lower():
		for item in inven:
			print(item.title())
		sleep(1.5)
	if 'campfire' in n.lower():
		if 'stick' in inven:
			txt("You light your stick on fire, helping you to see in the dense shrubbery.")
			inven.remove('stick')
			inven.append('torch')
		else:
			txt("You touch the fire. It's hot.")
	elif 'meat' in n.lower() and not 'meat' in inven:
		txt("You take the meat, putting it in your backpack.")
		txt("It will be useful if food is hard to find.")
		inven.append('meat')
	elif 'club' in n.lower() and not 'club' in inven:
		txt("You pick up the club, wielding it in your hand.")
		txt("It's well weighted.")
		inven.append('club')
	elif 'path' in n.lower():
		txt("You decide to leave on your way, heading further into the unknown.")

		location = 'spider'
	elif 'cook' in n.lower() and 'meat' in inven: # Cook the meat by typing COOK.
		txt("You decide to cook the meat.")
		if cookmeter == 0:
			txt("It's still a bit raw.")
		if cookmeter == 1:
			txt("It's now perfectly cooked.")
		if cookmeter == 2:
			txt("It's burnt a bit...")
		if cookmeter == 3:
			txt("It's quite burnt now.")
		if cookmeter > 3:
			txt("It's now burnt beyond recognition.") # Instead of making like twenty different comments, it just does the same thing if it's burnt
		cookmeter += 1
	clearscreen()

'''
Now's as good a time of any to talk about inventory.
It's a list with strings in it.
That's it.
'''

if location == 'spider':
	ltxt("Suddenly, a huge spider leaps out!")
	if 'club' in inven:
		txt("You use your club to smack it dead.")
	elif 'stick' in inven:
		txt("You kill it using your stick, breaking it in the process.")
		inven.remove('stick')
	elif 'torch' in inven:
		txt("You scare the spider away using your newly lit torch.")
		# You can evade the spider if you picked up LITERALLY ANYTHING*
		# 
		#
		#*besides the meat
	else:
		txt("With no weapons to defend yourself, the spider lunges and bites...")
		txt("Its deadly venom kills you within minutes.")
		print("")
		sleep(1)
		ded('darkgreen') # First death possible.
		print(gameOver)  # If you get this, it's impressive.
		print("")        # you've got to avoid picking up pretty much anything
		n = input("Press Enter to quit...")
		quit()
while location == 'spider':
	sleep(2)
	clearscreen() 
	txt("After fighting away the spider, you look ahead to see a large CAVE.")
	txt("Additionally, there seems to be a VILLAGE to the right.") # Pro tip: Don't go to the village.
	n = input("")												   # They murder you.
	if 'pack' in n.lower():
		txt("INVENTORY")
		for i in inven:
			txt(i)
	elif 'cave' in n.lower():
		ltxt("You enter the dark cave...")
		location = 'cave'
	elif 'village' in n.lower():
		ltxt("You decide to head towards the village...")
		print("")
		txt("Suddenly, the inhabitants leap out, weapons drawn!")
		txt("Before you can react, one of them runs you through with his blade...")
		txt("Their village is safe for another day.")
		print("")
		ded('darkred')
		txt(gameOver)
		input("Press Enter to quit...")
		quit()

while location == 'cave':
	sleep(2)
	clearscreen()
	if not 'torch' in inven:
		txt("The cave is extremely dark...")
		txt("It's quite hard to see...")
		txt("Stumbling along in the darkness, you go along an unknown passage...")
		location = 'caveleft'
	else:
		txt("Using your new torch, you can easily see through the cave.")
		txt("Use the password DeepDark to skip to this location next time.")
		txt("There seems to be multiple paths, on on the LEFT and one on the RIGHT.")
		n = sinput("")
		if 'left' in n.lower():
			txt("You decide to go along the left path.")
			location = 'caveleft'
		if 'right' in n.lower():
			txt("You decide to head along the right path.")
			location = 'caveright'
		elif 'pack' in n.lower():
			print("INVENTORY")
			for i in inven:
				print(i.title())

print("")
if location == 'caveleft':
	sleep(1)
	print("")
	txt("Eventually, after heading along the path, you find an exit.")
	txt("To your surprise, a city is in the distance!")
	txt("You finally have found a way back to civilization...")
	txt("You got the normal ending.") # Normal ending!
	# Normal Ending: survive, but don't get anything
	txt("You say your last goodbye to...")
	txt(altTitle)
	n = input("Press ENTER to Exit")
	quit()
	


while location == 'caveright':
	sleep(1)

	clearscreen()
	txt("The right path leads to a large room in the cave.")
	txt("There is a small LAKE to your left, and the CAVE continues forward.")
	what = sinput("")
	if 'pack' in what.lower():
		txt("PACK")
		for i in inven:
			print(i)
		sleep(0.5)
	elif 'lake' in what.lower():
		txt("You decide to take a swim in the lake...")
		txt("Suddenly, a cold hand grabs your foot from below!")
		txt("You sink into the icy depths...")
		ded('darkblue')
		txt(gameOver)
		input("Press ENTER to quit.")
		quit()
	elif 'cave' in what.lower():
		txt("You decide to head further into the depths of the cave...")
		txt("As you head further in, the cave grows narrower.")
		txt("However, soon, you see a light!")
		txt("You head outside of the cave.")
		location = 'jungle'
seenWolf = 0


while location == 'jungle':
	sleep(1.5)
	clearscreen()
	if not 'wolf' in inven:
		txt("Standing outside of the cave, you see a hungry-looking WOLF a distance away.")
	if not 'spear' in inven:
		txt("There's a SPEAR nearby, along with a PATH deeper into the bush.")
	else:
		txt("The PATH leads deeper into the jungle...")
	what = sinput("")
	if 'pack' in what.lower():
		txt("PACK")
		for i in inven:
			print(i)
		sleep(0.5)
	elif 'wolf' in what.lower() and not 'wolf' in inven:
		if 'meat' in inven:
			txt("You approach the wolf with some tasty meat.")
			if cookmeter == 2 or cookmeter == 3:
				txt("The wolf eats it, happily. You have earned a friend.")
				txt("Use WildWolf to return to this spot if you play again.")
				inven.append('wolf')
			else:
				txt("The wolf eats the meat, but finds it disgusting.")
				txt("It runs away.")
			inven.remove('meat')
		
		elif seenWolf == 0:
			txt("The wolf seems quite hungry.")
			txt("If you don't have any food, I would stay away.")
			seenWolf = 1
		elif seenWolf == 1:
			txt("You decide to go to the wolf anyways.")
			txt("Starving, it goes for the only meat in sight...")
			txt("You!")
			ded('darkred')
			print(gameOver)
			input("Press enter to quit...")
			quit()	
	elif 'spear' in what.lower() and not 'spear' in inven:
		txt("You decide to go and grab the spear.")
		if 'club' in inven:
			txt("Unfortunately, it is too heavy to carry along with your club.")
			txt("Which do you take?")
			wpn = sinput("")
			if 'spear' in wpn.lower():
				txt("You decide to take the spear and leave the club behind.")
				inven.remove('club')
				inven.append('spear')
			else:
				txt("You decide to leave the spear behind, keeping the club.")
		else:
			txt("You pick it up, storing it with your other items.")
			inven.append('spear')
	elif 'path' in what.lower():
		txt("You head through the thick foliage..")
		txt("The path leads onto a beach!")
		txt("You must be on the edge of an island...")
		location = 'beach'

while location == 'beach':
	sleep(2)
	clearscreen()
	txt("There's a small CRATE near the shore...")
	txt("There's also a small BOAT nearby!")
	wat = sinput("")
	print("")
	if 'pack' in wat.lower():
		show(inven)

	elif 'crate' in wat.lower():
		if not 'map' in inven:
			txt("Investigating the crate, there seems to be a small map inside.")
			txt("Maybe it could lead to treasure...")
			txt("Unfortunately, it leads off of the island. You take it anyway.")
			inven.append('map')
		else:
			txt("The crate is empty..")
			txt("There was a map earlier, but you took it.")
	elif 'boat' in wat.lower():
		txt("You decide to take the boat and set off from the island.")
		if not 'map' in inven:
			txt("With no idea of where to go, you simply set off and hope to see land.")
			txt("After many days, you eventually find an island with civilization.")
			txt("You have survived, though you are a shadow of the human you used to be...")
			txt("You have escaped...")
			txt(altTitle)
			print("You got the bad ending.")
			input("Press enter to quit...")
			quit()
		else:
			txt("Following the map, you find the island where the treasure is supposedly buried.")
			txt("You finally find the marked spot, braving dangers far more dangerous than any before.")
			if not 'wolf' in inven:
				txt("Unfortunately, after finding it, you have no way to dig to the chest.")
				txt("Despairing, you eventually use the boat to return home.")
				txt("You say goodbye to...")
				txt(altTitle)
				print("You  got the normal ending.")
				input("Press enter to quit...")
				quit()
			else:
				txt("After finding the treasure, you, with the help of your trusty wolf friend, dig up the treasure.")
				txt("Inside are the most valuable treasures you've ever seen!")
				txt("Taking the chest with you, you use the boat to go home, richer and happier than ever before..")
				txt("You say goodbye to...")
				print(altTitle)
				print("You got the good ending!")
				input("Press enter to quit.")
				quit()

print("This should never show up.")
print("If it does, it's a problem.")
input("")
p = txt






	
	
	
