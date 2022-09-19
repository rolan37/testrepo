'''
background color = blue
its made up of shapes (rectangles)   ---> 14 rectangles

rectangles(red, gray, blue, black, white)
'''


import turtle as t

t.bgcolor("#03fca5")   # color picker to select the HEX color
t.penup()              # lifts the penup
t.hideturtle()         # hides the turtle 


#
def rectangle(vertical, horizontal,color):      #user defined function
    t.color(color)
    t.pendown()
    t.begin_fill()
    
    for i in range(1,3):                        #runs the loops 2 times
        t.forward(3*horizontal)                   #accepts length of the rectangle
        t.right(90)                              #angle of the rectangle
        t.forward(3*vertical)                     #accepts the breadth od the rectangle
        t.right(90)                              #angle of the rectangle
    t.end_fill()
    t.penup()


# t.goto(x,y)       ----> x value will move the turtle left and right
#                   ----> y value will move the turtle up and down


t.goto(3*-20,3*80)       # ----> takes you to any point on the canvas
rectangle(30,40,"#0b1354")   # HEAD

t.goto(3*-10, 3*50)
rectangle(10,20, "yellow")  # neck

t.goto(3*-40,3*40)               #left arm
rectangle(40, 10, "#f51685")

t.goto(3*30,3*40)               #left arm
rectangle(40, 10, "#f51685")

t.goto(3*-30,3*40)                # body
rectangle(60,60, "#0b1354")

t.goto(3*-10,3*10)                # inside body
rectangle(20,20, "yellow")

t.goto(3*-20,3*-20)           
rectangle(30,40, "red")

t.goto(3*0,3*70)                  #eye outside
rectangle(10,10, "red")

t.goto(3*2.5,3*67.5)                  #eye inside
rectangle(5,5, "yellow")

t.begin_fill()
t.pendown()
t.circle(100)      # this functions draws a circle on the canvas of size 100px
t.end_fill()
t.penup()
