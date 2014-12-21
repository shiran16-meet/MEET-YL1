#paintproject - shiran fournier

import turtle

turtle.shape("turtle")

def make_a_square(x,y):
    
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    turtle.goto(x,y+100)
    turtle.goto(x+100,y+100)
    turtle.goto(x+100,y)
    turtle.goto(x,y)
    turtle.penup()
turtle.onscreenclick(make_a_square,btn=3,add=True)


def make_a_circle(x,y):
    turle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    turtle.circle()
    turtle.penup()
    

turtle.getscreen().onkeypress(make_a_circle,"c")
turtle.getscreen().listen()


def make_a_triangle(x,y):
    
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    turtle.goto(x+60,y-70)
    turtle.goto(x-60,y-70)
    turtle.goto(x,y)
    turtle.penup()



turtle.onscreenclick(make_a_triangle,btn=1,add=True)

#color 1
def switch_color():
    turtle.color("red")

  #switch color
turtle.getscreen().onkeypress(switch_color,"r")
turtle.getscreen().listen()

    #color 2
def switch_color2():
    turtle.color("blue")

    #switch color
turtle.getscreen().onkeypress(switch_color2,"b")
turtle.getscreen().listen()

#color 3
def switch_color3():
    turtle.color("green")

    #switch color
turtle.getscreen().onkeypress(switch_color3,"g")
turtle.getscreen().listen()
    
#color 4
def switch_color4():
    turtle.color("yellow")

    #switch color
turtle.getscreen().onkeypress(switch_color4,"y")
turtle.getscreen().listen()

turtle.mainloop
    
    
    
