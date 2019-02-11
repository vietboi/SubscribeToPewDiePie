import turtle

def turtleLetter(letter,tur):
    if letter=="box":
        tur.forward(40)
        tur.right(90)
        tur.forward(60)
        tur.right(90)
        tur.forward(40)
        tur.right(90)
        tur.forward(60)

    elif letter == "A":
        tur.pu()
        tur.fd(5)
        tur.right(90)
        tur.fd(5)
        tur.pd()
        tur.fd(30)
        tur.right(180)
        tur.fd(30)
        tur.right(90)
        tur.fd(20)
        tur.right(90)
        tur.fd(30)
        tur.right(180)
        tur.fd(15)
        tur.left(90)
        tur.fd(20)
        tur.pu()
        tur.right(180)
    elif letter == "B":
        tur.pu()
        tur.fd(5)
        tur.right(90)
        tur.fd(5)
        tur.pd()
        tur.fd(60)
        tur.left(90)
        tur.fd(30)
        tur.left(90)
        tur.fd(30)
        tur.left(90)
        tur.fd(30)
        tur.pu()
        tur.left(180)
        tur.forward(30)
        tur.left(90)
        tur.pd()
        tur.fd(30)
        tur.left(90)
        tur.fd(30)
        tur.pu()
        tur.right(180)
        tur.fd(60)
        
        
        
	
    elif letter == "C":
        
        tur.pu()
        tur.fd(5)
        tur.fd(5)
        tur.pd()
        tur.right(180)
        tur.fd(30)
        tur.left(90)
        tur.fd(60)
        tur.left(90)
        tur.fd(30)
        tur.pu()
        tur.right(180)
        tur.right(90)
        tur.fd(60)
        tur.right(90)
        tur.fd(20)
    elif letter == "D":
        tur.pu()
        tur.left(90)
        tur.left(180)
        tur.pd()
        tur.fd(60)
        tur.right(90)
        tur.right(90)
        tur.right(90)
        tur.circle(30,180)
        tur.pu()
        tur.right(180)
        tur.fd(50)
        
    elif letter == "E":
        tur.pu()
        tur.left(90)
        tur.fd(5)
        tur.fd(5)
        tur.pd()
        tur.fd(60)
        tur.right(90)
        tur.fd(30)
        tur.left(180)
        tur.fd(30)
        tur.left(90)
        tur.fd(30)
        tur.left(90)
        tur.fd(30)
        tur.left(180)
        tur.fd(30)
        tur.left(90)
        tur.fd(30)
        tur.left(90)
        tur.fd(30)
        tur.pu()
        tur.left(90)
        tur.fd(60)
        tur.right(90)
        tur.fd(30)
    elif letter == "F":
        tur.pu()
        tur.right(90)
        tur.fd(60)
        tur.pd()
        tur.right(180)
        tur.fd(60)
        tur.right(90)
        tur.fd(30)
        tur.left(180)
        tur.fd(30)
        tur.left(90)
        tur.fd(30)
        tur.left(90)
        tur.fd(30)
        tur.left(90)
        tur.pu()
        tur.right(180)
        tur.right(90)
        tur.fd(30)
        tur.right(90)
        tur.fd(30)
        tur.right(90)
        tur.fd(60)
    elif letter == "G":
        tur.pu()
        tur.fd(20)
        tur.right(90)
        tur.fd(30)
        tur.pd()
        tur.left(90)
        tur.fd(25)
        tur.right(90)
        tur.circle(-30,300)
        tur.pu()
        tur.left(30)
        tur.fd(60)

    elif letter == "H":
	    pass
    elif letter == "I":
	    pass
    elif letter == "J":
	    pass
    elif letter == "K":
	    pass
    elif letter == "L":
	    pass
    elif letter == "M":
	    pass
    elif letter == "N":
	    pass
    elif letter == "O":
	    pass
    elif letter == "P":
	    pass		
    elif letter == "Q":
	    pass
    elif letter == "R":
	    pass
    elif letter == "S":
	    pass
    elif letter == "T":
	    pass
    elif letter == "U":
	    pass
    elif letter == "V":
            pass
    elif letter == "W":
	    pass
    elif letter == "X":
	    pass
    elif letter == "Y":
	    pass
    elif letter == "Z":
	    pass		

        
    elif letter == "Ax":
        # code here
        tur.forward(40)
		
    else:
        turtleLetter("box",tur)
	
2






window = turtle.Screen()
tur = turtle.Turtle()
tur.speed(2)
#turtleLetter("box",tur)
turtleLetter("E",tur)
turtleLetter("F",tur)
turtleLetter("G",tur)

window.exitonclick()
