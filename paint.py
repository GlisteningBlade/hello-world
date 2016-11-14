# Paint Program?

from graphics import *


win = GraphWin('Paint!',500,500)

p1 = Point(0,0)

p2 = Point(100,100)
p3 = Point(0,100)
p4 = Point(100,200)
p5 = Point(0,200)
p6 = Point(100,300)

p7 = Point(0,300)
p8 = Point(100,400)

p9 = Point(0,400)
p10 = Point(100,500)

p20 = Point(200,400)
p21 = Point(300,500)


p22 = Point(150,450)

circ1 = Circle(p22,50)

circ1.draw(win)

recti = Rectangle(p20,p21)


recti.draw(win)






rect1 = Rectangle(p1,p2)
rect1.setFill('red')

rect2 = Rectangle(p3,p4)
rect2.setFill('blue')

rect3 = Rectangle(p5,p6)
rect3.setFill("purple")

rect4 = Rectangle(p7,p8)
rect4.setFill('pink')

rect5 = Rectangle(p9,p10)
rect5.setFill('black')

rect1.draw(win)
rect2.draw(win)
rect3.draw(win)
rect4.draw(win)
rect5.draw(win)

mColor = 'blue'
mShape = 'rect'

while True:
	p5 = win.getMouse()
	if p5.getX() < 100:
		if p5.getY() < 100:
			mColor = 'red'
		elif p5.getY() < 200:
			mColor = 'blue'
		elif p5.getY() < 300:
			mColor = 'purple'
		elif p5.getY() < 400:
			mColor = 'pink'
		elif p6.getY() < 500:
			mColor = 'black'
	elif p5.getX() > 400:
		if p5.getY() < 100:
			mShape = 'rect'
		elif p5.getY() < 200:
			mShape = 'circ'
	else:
		if mShape == 'rect':
			x1 = p5.getX() + 5
			x2 = p5.getX() - 5
			y1 = p5.getY() + 5
			y2 = p5.getY() - 5
			px = Point(x1,y1)
			py = Point(x2,y2)
			rectidk = Rectangle(px,py)
			rectidk.setFill(mColor)
			rectidk.setOutline(mColor)
			rectidk.draw(win)
		else:
			circ = Circle(p5,5)
			circ.setFill(mColor)
			circ.setOutline(mColor)
			circ.draw(win)
			