import turtle

def moonLight(t):

    t.penup()
    x = 200
    y = 150
    t.setheading(270)
    t.pendown()  
    t.color("Gray")

    t.setpos(x- (x/1.75), y -(y/12))
    for n in range(200):
        t.forward(50)
        t.left(70)

def springStretch(t):

    t.color("Black")
    t.penup()
    t.setpos(-60, 90)
    t.pendown()

    for side in range(10) :
        t.circle(20)
        t.left(10)
    

def printMenu():
    """ This function prints the menu to the screen """

    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("~  Menu of Turtle Patterns to Draw")
    print("~  1: Moon Light")
    print("~  2: Spring Stretch")
    print("~  3: Exit")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")


def main():
    t = turtle.Turtle()
    t.speed(10)

    choice = "-1"
    
    while(choice != "4"):
        printMenu()
        choice = input("Look at the menu. Which item would you like to draw? 1, 2, or 3. Select 4 to exit. ")

        if(choice == "1"):
            moonLight(t)
        elif(choice == "2"):
            springStretch(t)
        
        elif(choice == "3"):
            print("Thank you for drawing today.")
        else:
            print("Oops, an invalid option was picked. Please try again.")

main()