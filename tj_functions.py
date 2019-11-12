import turtle
bob=turtle.Turtle()
bob.speed(0)
turtle.colormode(255)

def mazeghost():
    bob.begin_fill()
    for times in range(2):
        bob.forward(21)
        bob.right(90)
        bob.forward(10)
        bob.right(90)
    bob.end_fill()
    bob.begin_fill()
    bob.right(90)
    bob.forward(15)
    bob.left(135)
    bob.forward(5)
    bob.right(90)
    bob.forward(5)
    bob.left(90)
    bob.forward(5)
    bob.right(90)
    bob.forward(5)
    bob.left(90)
    bob.forward(5)
    bob.right(90)
    bob.forward(5)
    bob.left(135)
    bob.forward(5)
    bob.left(90)
    bob.forward(11)
    bob.left(180)
    bob.circle(10)
    bob.end_fill()


def mazepacman():
    circle(5,"yellow")

    bob.color("black")

    jump(30,-158)

    bob.width(1)

    bob.left(180)
    bob.right(25)
    polygon(3,20,"black")

def maze():
    walls()

    jump(0,320)

    bob.width(20)
    bob.left(90)
    bob.forward(60)
    bob.right(90)

    bob.width(20)

    jump(-230,295)

    smallmazebox()

    jump(-195,215)

    bob.width(20)
    bob.forward(40)

    jump(-145,215)

    bob.left(90)
    bob.forward(124)
    bob.left(180)
    bob.forward(62)
    bob.right(90)
    bob.forward(70)

    jump(0,215)

    bob.right(90)
    bob.forward(75)
    bob.left(180)
    bob.forward(75)
    bob.left(90)
    bob.forward(75)
    bob.left(180)
    bob.forward(150)

    jump(-135,295)

    bob.width(10)
    longmazebox()

    jump(65,295)

    longmazebox()

    jump(235,255)

    smallmazebox()

    jump(200,216)

    bob.width(20)
    bob.forward(40)

    jump(145,216)

    bob.right(90)
    bob.forward(124)
    bob.left(180)
    bob.forward(62)
    bob.left(90)
    bob.forward(70)

    bob.width(10)
    bob.color("blue")

    jump(-20,95)

    bob.forward(60)
    bob.left(90)
    bob.forward(85)
    bob.left(90)
    bob.forward(160)
    bob.left(90)
    bob.forward(85)
    bob.left(90)
    bob.forward(60)

    jump(25,95)

    bob.color("white")
    bob.forward(50)

    jump(-145,16)

    bob.color("blue")
    bob.width(20)

    bob.left(90)
    bob.forward(70)

    jump(145,16)

    bob.forward(70)

    jump(0,-54)

    mazetshape()
    
    jump(0,-185)

    mazetshape()

    jump(-285,-185)

    bob.left(90)
    bob.forward(28)

    jump(293,-185)

    bob.left(180)
    bob.forward(28)

    jump(-145,-130)

    bob.left(180)
    bob.forward(80)

    jump(145,-130)

    bob.left(180)
    bob.forward(80)

    jump(-195,-130)

    bob.forward(40)
    bob.left(180)
    bob.forward(40)
    bob.right(90)
    bob.forward(55)

    jump(203,-130)

    bob.forward(55)
    bob.left(180)
    bob.forward(55)
    bob.right(90)
    bob.forward(40)

    jump(145,-184)

    bob.right(90)
    bob.forward(75)
    bob.right(90)
    bob.forward(79)
    bob.right(180)
    bob.forward(180)

    jump(-145,-184)

    bob.right(90)
    bob.forward(75)
    bob.left(90)
    bob.forward(79)
    bob.left(180)
    bob.forward(180)

def mazetshape():
    bob.left(90)
    bob.forward(76)
    bob.left(180)
    bob.forward(152)
    bob.left(180)
    bob.forward(76)
    bob.right(90)
    bob.forward(75)

def longmazebox():
    for times in range(2):
        bob.forward(70)
        roundcurve90right("blue")
        bob.forward(20)
        roundcurve90right("blue")

def smallmazebox():
    for times in range(2):
        roundcurve90left("blue")
        bob.forward(20)
        roundcurve90left("blue")
        bob.forward(30)
        
def walls():
    jump(285,325)
    bob.left(180)
    bob.forward(560)
    jump(-280,325)
    roundcurve90left("blue")
    bob.forward(145)
    roundcurve90left("blue")
    bob.forward(80)
    roundcurve90right("blue")
    bob.forward(60)
    roundcurve90right("blue")
    bob.forward(80)

    jump(-280,20)
    
    bob.left(180)
    bob.forward(80)
    roundcurve90right("blue")
    bob.forward(60)
    roundcurve90right("blue")
    bob.forward(80)
    roundcurve90left("blue")
    bob.forward(240)
    roundcurve90left("blue")
    bob.forward(570)
    roundcurve90left("blue")
    bob.forward(240)
    roundcurve90left("blue")
    bob.forward(80)
    roundcurve90right("blue")
    bob.forward(60)
    roundcurve90right("blue")
    bob.forward(80)
    
    jump(290,82)

    bob.left(180)
    bob.forward(80)
    roundcurve90right("blue")
    bob.forward(60)
    roundcurve90right("blue")
    bob.forward(80)
    roundcurve90left("blue")
    bob.forward(145)
    roundcurve90left("blue")

def roundcurve90right(c):
    bob.width(10)
    bob.color(c)
    for times in range(15):
        bob.right(6)
        bob.forward(1)

def roundcurve90left(c):
    bob.width(10)
    bob.color(c)
    for times in range(15):
        bob.left(6)
        bob.forward(1)

def roundcurve180(c):
    bob.width(3)
    bob.color(c)
    for times in range(28):
        bob.left(6)
        bob.forward(1)
        
def paxman():
    jump(0,-20)
    circle(20,"yellow")
    back()
    bob.color("black")
    bob.begin_fill()
    bob.left(40)
    bob.forward(30)
    bob.right(130)
    bob.forward(40)
    bob.right(130)
    bob.forward(30)
    bob.end_fill()

def back():
    bob.penup()
    bob.home()
    bob.pendown()
    
def spikeflower(distance):
    for times in range(11):
        spike(distance)
        bob.penup()
        bob.home()
        bob.pendown()
        

def spike(distance):
    for times in range(21):
        c=times*12
        bob.color(c,c,c)
        bob.width(times)
        bob.forward(distance)
        bob.left(2)

def tapestry(c1,c2):
    for times in range(6):
        rowtile(c1,c2)
        jump(0,times+1*-200)


def rowtile(c1,c2):
    for times in range(4):
        tile(c1,c2)
        bob.forward(200)
    
def tile(c1,c2):
    polygon(4,200,c1)
    for times in range(4):
        polygon(3,50,c2)
        bob.forward(50)
        polygon(3,50,c2)
        bob.forward(50)
        polygon(3,50,c2)
        bob.forward(50)
        polygon(3,50,c2)
        bob.forward(50)
        bob.left(90)
        
def star(distance, c):
    bob.color(c)
    bob.begin_fill()
    for times in range(5):
        bob.forward(distance)
        bob.left(216)
    bob.end_fill()

def polygon(sides, distance, c):
    bob.color(c)
    angle=360/sides
    bob.begin_fill()
    for times in range(sides):
        bob.forward(distance)
        bob.left(angle)
    bob.end_fill()
    
def jump(x,y):
    bob.penup()
    bob.goto(x,y)
    bob.pendown()
    
def outline(sides, distance, c):
    bob.color(c)
    angle=360/sides
    for times in range(sides):
        bob.forward(distance)
        bob.left(angle)

def explosion(distance,c):
    bob.color(c)
    bob.begin_fill()
    bob.left(22.5)
    for times in range(8):
        bob.left(135)
        bob.forward(distance)
    bob.end_fill()
    bob.right(22.5)

def figure1 (distance,size,c):
    bob.color(c)
    bob.begin_fill()
    bob.circle(size)
    bob.forward(distance)
    bob.circle(size)
    bob.end_fill()
    bob.left(45)
    bob.forward(distance)
    bob.right(90)
    bob.forward(distance)
    bob.left(45)
    bob.begin_fill()
    bob.circle(size)
    bob.forward(distance)
    bob.circle(size)
    bob.end_fill()

def ghost(c):
    bob.color(c)
    bob.begin_fill()
    bob.left(90)
    bob.forward(100)
    bob.circle(50)
    bob.left(90)
    bob.forward(100)
    bob.left(90)
    bob.forward(100)
    bob.left(135)
    bob.forward(35)
    bob.right(90)
    bob.forward(35)
    bob.left(90)
    bob.forward(35)
    bob.right(90)
    bob.forward(35)
    bob.left(45)
    bob.end_fill()

def FadingTriangle():
    for times in range(50):
        c=(250-times*5,250-times*5,0)
        polygon(3,450-times*8,c)

def circle(distance,c):
    bob.begin_fill()
    bob.color(c)
    bob.circle(distance)
    bob.end_fill()
