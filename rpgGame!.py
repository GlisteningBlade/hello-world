intro = '''
# RPG Enemy Game?
# Not sure if this will work.

# I think the best way to have a square grid is to have a list of lists
# Each list in the list is a row, with each item a square
# Each square is in a column

# Update (12:25 11/10/2016)
# I got the element system to work.
# And probably the enemy system
#
# Update (16:30 11/10/2016)
# Yes, the enemy system works
# And the player system probably works.
#
# Update (21:50 11/11/2016)
# Player system works.
# 3 Types of Armor (Armor, Helmet, Shield)
# Armors have defense and an element
# Helmets have defense and an ability
# Shields just have defense
#
# The equipping system now works, along with the inventory system.
#
# Update (8:45 11/12/2016)
# The ability system now works, yesss
# You can  equip a helmet with an ability and run it using self.abi
# It's good.
#
#
#
'''
class elmnt():
	def __init__(self,Adv,dAdv,name):
		self.name = name
		self.Adv = Adv
		self.dAdv = dAdv
	def mult(self,item):
		if item in self.Adv:
			return 1.5
		elif item in self.dAdv:
			return 0.75
		else:
			return 1

from random import choice
from random import normalvariate
def good(item):
		return normalvariate(item,1.5)
Fire = elmnt([],[],'Fire')
Grass = elmnt([],[],'Grass')
Water = elmnt([],[],'Water')
Dark = elmnt([],[],'Dark')
Light = elmnt([],[],'Light')

Fire.Adv.append(Grass)
Fire.dAdv.append(Water)

Grass.Adv.append(Water)
Grass.dAdv.append(Fire)

Water.Adv.append(Fire)
Water.dAdv.append(Grass)

Dark.Adv.append(Light)
Dark.dAdv.append(Light)

Light.Adv.append(Dark)
Light.dAdv.append(Dark)

class weapon():
	def __init__(self,dmg,element,name):
		self.element = element
		self.dmg = dmg
		self.name = name
	def atk(self,foe):
		atkDmg = good(self.dmg)
		damage = round((atkDmg*self.element.mult(foe.element)),0)
		isCrit = (choice(range(1,20))) == 1
		if isCrit:
			damage = damage * 2
			print("Critical Hit!")
		if damage >= foe.health:
			damage = foe.health
		damage = int(damage)

		txt("You attacked and dealt {} damage!".format(damage))
		foe.health -= damage

class enemy():
	def __init__(self,maxhealth,element,dmg,name,exp):
		self.maxhealth = maxhealth
		self.health = int(self.maxhealth)
		self.element = element
		self.name = name
		self.dmg = dmg
		self.exp = exp
	def atk(self,player):
		atkDmg = good(self.dmg)
		atkDmg = round(atkDmg,0)
		try:
			atkDmg = int(atkDmg * self.element.mult(player.inven[A].element)) - player.defence() // 4
		except AttributeError:
			atkDmg = int(atkDmg) - player.defence() // 4

		if atkDmg >= player.health:
			atkDmg = int(player.health)

		txt("{} attacked you and did {} damage!".format(self.name,atkDmg))
		player.health -= atkDmg


fireDagger = weapon(10,Fire,'Fire Dagger')
orc = enemy(50,Grass,10,'Orc',5)
sword = weapon(15,Grass,'Basic Sword')
waterGun = weapon(8,Water,'Water Gun')
dl = enemy(500,Dark,10,'Dark Lord of Evil',5)

maxHealth = 50

import sys
import time

def txt(string):
	for char in string:
		if char == '\n':
			time.sleep(0.5)
		sys.stdout.write(char)
		sys.stdout.flush()
		if char != '\n':
			time.sleep(.05)
		sys.stdout.flush()
	sys.stdout.write('\n')

class character():
	def __init__(self,maxHealth,inven,mAp):
		self.maxHealth = maxHealth
		self.health = int(maxHealth)
		self.inven = inven
		self.mAp = mAp
		self.Ap = int(mAp)
	def equip(self,item):
		if item in self.inven[P]:
			if type(item) is weapon:
				self.inven[P].remove(item)
				self.inven[P].append(self.inven[W])
				self.inven[W] = item
			if type(item) is helmet:
				self.inven[P].remove(item)
				self.inven[P].append(self.inven[H])
				self.inven[H] = item
			if type(item) is armor:
				self.inven[P].remove(item)
				self.inven[P].append(self.inven[A])
				self.inven[A] = item
			if type(item) is shield:
				self.inven[P].remove(item)
				self.inven[P].append(self.inven[S])
				self.inven[S] = item
			else:
				return None
	def pickup(self,item):
		if not(item in self.inven[P]):
			self.inven[P].append(item)
	def atk(self,foe):
		self.inven[W].atk(foe)
	def abi(self,foe):
		try:
			if self.Ap > 0:
				self.inven[H].ab(self,foe)
				self.Ap -= 1
			else:
				txt("No AP remaining!")
		except AttributeError:
			txt("No helmet equipped!")
		except TypeError:
			txt("The currently equipped helmet has no ability.")
	def defence(self):
		d = 0
		for i in [self.inven[A],self.inven[H],self.inven[S]]:
			if type(i) != type(None):
				d += i.defense
		return d
	def gap(self):
		self.Ap = self.mAp;
class armor():
	def __init__(self,defense,element):
		self.defense = defense
		self.element = element

class helmet():
	def __init__(self,defense,ability):
		self.defense = defense
		self.ability = ability
	def ab(self,person,foe):
		exec(self.ability)




# List of abilities!
# For all of these, person refers to the user
# Foe refers to the enem
heal = '''
healed = (person.maxHealth - person.health) // 2
healed = int(good(healed))
if healed <= 0:
    healed = (person.maxHealth - person.health)
if healed > (person.maxHealth - person.health):
	healed = person.maxHealth - person.health
if healed != 0:
	txt("You recovered {} health!".format(healed))
else:
	txt("You are already at full health!")
person.health += healed
'''
doublestrike = '''
print("You used Double Strike!")
w = int(person.inven[W].dmg)
person.inven[W].dmg *= 0.75
person.inven[W].atk(foe)
print("")
person.inven[W].atk(foe)
person.inven[W].dmg = int(w)
'''
elemental = '''
elnames = {Fire : 'Fire', Water : 'Water', Grass : 'Grass', Dark : 'Dark', Light : 'Light'}
print("You used Elemental Strike!")
w = person.inven[W].element
for i in [Fire,Dark,Light,Grass,Water]:
	if foe.element in i.Adv:
		person.inven[W].element = i
print("Changed to {} element!".format(elnames[person.inven[W].element]))
person.inven[W].atk(foe)
person.inven[W].element = w
'''

bloodstrike = '''
txt("You used Blood Strike!")
n = foe.health
person.atk(foe)
healed = n - foe.health
healed = int(healed // 2)
if healed > person.maxHealth - person.health:
    healed = person.maxHealth - person.health
person.health += healed
txt("You recovered {} health!".format(healed))
'''


# End list of abilities


class shield():
	def __init__(self,defense):
		self.defense = defense

global inventory

H = 'Helmet'
A = 'Armor'
S = 'Shield'
W = 'Weapon'
P = 'Pack'
inventory = {H : None, A : None, S : None, W : fireDagger, P : []}

hero = character(1000,inventory,5)

exec('''
print("Wow, this is neat!")
print(6 ** 6)
''')

def battle(person,foe):
	if foe.name[0].upper() in ['A','E','I','O','U']:
		article = 'an'
	else:
		article = 'a'
	txt("You come face to face with {} {}!\n".format(article,foe.name))
	while person.health > 0 and foe.health > 0:
		d = person.defence()
		time.sleep(4)
		for i in range(1,31):
			print('\n')
			time.sleep(0.05)
		txt("Health : {} / {}\n".format(person.health,person.maxHealth))
		txt("AP	 : {} / {}\n".format(person.Ap,person.mAp))
		action = input('''\n''')
		exec(action)
		foe.atk(person)
	if person.health <= 0:
		txt("You died!")
		time.sleep(2)
	elif foe.health <= 0:
		txt("You won!")




robe = helmet(10,heal)

horned = helmet(10,bloodstrike)
hero.pickup(horned)
hero.equip(horned)

god = weapon(50,Light,'Great Blade of Glory')
hero.pickup(god)
hero.equip(god)

battle(hero,dl)

battle(hero,orc)
