from graphics import *
from random import choice

def avg(list1):
	return sum(list1) / len(list1)

print("Type HELP for help, or anything else to begin.")
wants = input("")
if wants == 'HELP':
	print("Available Palletes:\nred, blue, green\ndarkred, darkblue, darkgreen\npalered, paleblue, palegreen\nrainbow,pastels,gray,spiderman")
else:
	print("")
print("")
def tileFill():
	print("")
	print("What screen size do you want? (minimum 200)")
	scrSize = int(input(""))
	if scrSize < 200:
		scrSize = 200

	print("What color scheme do you want?")
	colRange = input("")

	print("How many rows of rectangles to generate?")
	rows = int(input(""))
	rowC = scrSize/rows
	print("And how many columns?")
	col = int(input(""))
	colC = scrSize/col
	print("Would you like to have some extra flair added?")
	flair = input("")
	if 'yes' in flair:
		print("Type Small, Medium, or type Large?")
		flair = input("")
		if 'SMALL' in flair.upper():
			flair = 'small'
		elif 'MEDIUM' in flair.upper():
			flair = 'medium'
	else:
		flair = 'no'
	win = GraphWin('Filling', scrSize, scrSize)
	idk = []
	for b in range(0,rows+1):
		idk.append(b)
	idk.reverse()
	while True:
		for b in idk:
			for i in range(0,col + 1):
				p1 = Point(colC*i,rowC*b)
				p2 = Point((colC*i)+colC,(rowC*b)+rowC)

				if flair == 'small':
					rad = min(colC,rowC)
				elif flair == 'medium':
					rad = avg([colC,rowC])
				else:
					rad = max(colC,rowC)
				circ = Circle(p2,rad)
				rect = Rectangle(p1,p2)
				if 'ween' in colRange:
					which = choice([0,1])
					if which == 0:
						rFill = choice(range(1,50))
						gFill = rFill
						bFill = gFill
						rcFill = choice(range(1,50))
						gcFill = rcFill
						bcFill = gcFill
					else:
						rFill = choice(range(240,256))
						gFill = choice(range(70,160))
						bFill = choice(range(1,2))
						rcFill = choice(range(240,256))
						gcFill = choice(range(70,160))
						bcFill = choice(range(1,2))
				elif 'darkred' in colRange:
					rFill = choice(range(1,156))
					gFill = choice(range(1,2))
					bFill = choice(range(1,2))
					rcFill = choice(range(1,156))
					gcFill = choice(range(1,2))
					bcFill = choice(range(1,2))
				elif 'darkblue' in colRange:
					rFill = choice(range(1,2))
					gFill = choice(range(1,2))
					bFill = choice(range(1,156))
					rcFill = choice(range(1,2))
					gcFill = choice(range(1,2))
					bcFill = choice(range(1,156))
				elif 'darkgreen' in colRange:
					rFill = choice(range(1,2))
					gFill = choice(range(1,156))
					bFill = choice(range(1,2))
					rcFill = choice(range(1,2))
					gcFill = choice(range(1,156))
					bcFill = choice(range(1,2))
				elif 'bw' in colRange:
					rFill = choice([0,255])
					gFill = rFill
					bFill = gFill;
					rcFill = choice([0,255])
					gcFill = rcFill
					bcFill = gcFill
				elif 'palered' in colRange:
					rFill = choice(range(245,256))
					gFill = choice(range(153,204))
					bFill = gFill
					rcFill = choice(range(245,256))
					gcFill = choice(range(153,204))
					bcFill = gcFill
				elif 'paleblue' in colRange:
					rFill = choice(range(154,204))
					gFill = rFill
					bFill = choice(range(245,256))
					rcFill = choice(range(154,204))
					gcFill = rcFill
					bcFill = choice(range(245,256))
				elif 'palegreen' in colRange:
					rFill = choice(range(153,204))
					gFill = choice(range(245,256))
					bFill = rFill
					rcFill = choice(range(153,204))
					gcFill = choice(range(245,256))
					bcFill = rcFill
				elif 'gray' in colRange:
					rFill = choice(range(1,256))
					gFill = rFill
					bFill = gFill
					rcFill = choice(range(1,256))
					gcFill = rcFill
					bcFill = gcFill
				elif 'crt2' in colRange:
					rFill = choice([0,128,255])
					gFill = choice([0,128,255])
					bFill = choice([0,128,255])
					rcFill = choice([0,128,255])
					gcFill = choice([0,128,255])
					bcFill = choice([0,128,255])
				elif 'crt' in colRange:
					rFill = choice([0,255])
					gFill = choice([0,255])
					bFill = choice([0,255])
					rcFill = choice([0,255])
					gcFill = choice([0,255])
					bcFill = choice([0,255])
				elif 'orange' in colRange:
					rFill = choice(range(240,256))
					gFill = choice(range(70,160))
					bFill = choice(range(1,2))
					rcFill = choice(range(240,256))
					gcFill = choice(range(70,160))
					bcFill = choice(range(1,2))
				elif 'fall' in colRange:
					rFill = choice(range(200,256))
					gFill = choice(range(70,160))
					bFill = choice(range(1,2))
					rcFill = choice(range(200,256))
					gcFill = choice(range(70,160))
					bcFill = choice(range(1,2))
				elif 'pastels' in colRange:
					rFill = choice(range(200,256))
					gFill = choice(range(200,256))
					bFill = choice(range(200,256))
					rcFill = choice(range(200,256))
					gcFill = choice(range(200,256))
					bcFill = choice(range(200,256))
				elif 'spiderman' in colRange:
					which = choice([1,0])
					if which == 1:
						rFill = choice(range(150,256))
						gFill = choice(range(1,6))
						bFill = choice(range(1,6))
						rcFill = choice(range(150,256))
						gcFill = choice(range(1,6))
						bcFill = choice(range(1,6))
					else:
						rFill = choice(range(1,6))
						gFill = choice(range(1,6))
						bFill = choice(range(150,256))
						rcFill = choice(range(1,6))
						gcFill = choice(range(1,6))
						bcFill = choice(range(150,256))
				elif 'christmas' in colRange:
					which = choice([1,1,1,1,1,0,0,0,0,0,2])
					if which == 1:
						rFill = choice(range(150,256))
						gFill = choice(range(1,6))
						bFill = choice(range(1,6))
						rcFill = choice(range(150,256))
						gcFill = choice(range(1,6))
						bcFill = choice(range(1,6))
	
					if which == 0:
						rFill = choice(range(1,6))
						gFill = choice(range(150,256))
						bFill = choice(range(1,6))
						rcFill = choice(range(1,6))
						gcFill = choice(range(150,256))
						bcFill = choice(range(1,6))
					if which == 2:
						rFill = 254
						gFill = 254
						bFill = 254
						rcFill = 254
						gcFill = 254
						bcFill = 254
				elif 'red' in colRange:
					rFill = choice(range(150,256))
					gFill = choice(range(1,6))
					bFill = choice(range(1,6))
					rcFill = choice(range(150,256))
					gcFill = choice(range(1,6))
					bcFill = choice(range(1,6))
				elif 'blue' in colRange:
					rFill = choice(range(1,6))
					gFill = choice(range(1,6))
					bFill = choice(range(150,256))
					rcFill = choice(range(1,6))
					gcFill = choice(range(1,6))
					bcFill = choice(range(150,256))
				elif 'green' in colRange:
					rFill = choice(range(1,6))
					gFill = choice(range(150,256))
					bFill = choice(range(1,6))
					rcFill = choice(range(1,6))
					gcFill = choice(range(150,256))
					bcFill = choice(range(1,6))
				else:
					rFill = choice(range(1,256))
					gFill = choice(range(1,256))
					bFill = choice(range(1,256))
					rcFill = choice(range(1,256))
					gcFill = choice(range(1,256))
					bcFill = choice(range(1,256))
				rectColor = color_rgb(rFill, gFill, bFill)

				circColor = color_rgb(rcFill,gcFill,bcFill)
				circ.setFill(circColor)

				rect.setFill(rectColor)
				rect.setOutline(rectColor)
				rect.draw(win)
				if not('no' in flair):
					circ.draw(win)

	tileFill()

tileFill()

#i am a bully
