import turtle
import time

def main ():
    luke = turtle.Turtle()
    print("The Upsidedown House")
    
    #Square
    luke.color("red")
    luke.begin_fill()   

    for side in range(4): 
        luke.forward(200)
        luke.left(90)

    luke.end_fill()
        
    #Triangle
    luke.color("Blue")
    luke.begin_fill()
    for side in range(3):
        luke.forward(200)
        luke.right(120)
    luke.end_fill()

    
    leo = turtle.Turtle()
    #Winddow 1
    leo.color("Yellow")
    leo.penup()
    leo.lt(90)
    leo.fd(20)
    leo.rt(90)
    leo.fd(20)
    leo.pendown()
    leo.begin_fill()
    for side in range(4):
        leo.forward(30)
        leo.left(90)
    leo.end_fill()


    josh = turtle.Turtle()
    #Window 2
    josh.color("Yellow")
    josh.penup()
    josh.left(90)
    josh.forward(20)
    josh.right(90)
    josh.forward(150)
    josh.pendown()
    josh.begin_fill()
    for side in range(4):
        josh.forward(30)
        josh.left(90)
    josh.end_fill()


    t = turtle.Turtle()
    #Door
    t.color("brown")
    t.penup()
    t.left(90)
    t.forward(200)
    t.right(90)
    t.forward(100)
    t.pendown()
    t.begin_fill()
    t.forward(30)
    t.right(90)
    t.forward(60)
    t.right(90)
    t.forward(60)
    t.right(90)
    t.forward(60)
    t.end_fill()
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
    time.sleep(15)

main()


















'''
import turtle

t = turtle.Turtle()

def square():
    for i in range(4):
        t.fd(100)
        t.lt(90)
    

def triangle():
    for i in range(3):
        t.fd(100)
        t.rt(120)


def house():
    square()
    triangle()

house()
'''