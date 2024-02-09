# Prototype 1 ==> Hexagon: red | Circle: green | Square: blue | border-color: yellow
# Prototype 2 ==> Hexagon: blue | Circle: purple | Square: yellow | border-color: red

'''
Group 5:

1. Mohammad Ali
2. Naqiya
3. Yaseen Gaber

Github Links:

https://github.com/MohammadAlSubaiei/GCIS/upload/master
https://github.com/naqiyahathiari/group.git
https://github.com/Yaseen-Gaber/Group_5.git

^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Ctrl + Shift + V: [for pasting in MS VS Code] <--- Prototype 1 & Prototype 2
|
red
green
blue
yellow
&
blue
purple
yellow
red
'''

import turtle

turtle.speed(1) # 0 ==> fastest (No_Animation) | 1 ==> slowest (Animation) | 6 ==> Normal (default turtle speed)
turtle.bgcolor('LightBlue')
# turta = turtle # Create a turtle object

# Create a turtle screen
screen = turtle.Screen()

# Set the width and height of the turtle canvas to fullscreen
screen.setup(width=1.0, height=1.0)
screen.title("Activity 1")

# Print screen information
print()
print("Screen width:", screen.window_width())
print("Screen height:", screen.window_height())
print("Screen background color:", screen.bgcolor())
print()

"""
The setPos function: 

This function provides 3 arguments in which one argument takes 2 parameters, x and y.
1. For the first line of the function which is called turta.pu( ) is the same as turtle.penup( ) which means it lifts the pen from the canvas and stops drawing.
2. The second line of code in  the function says turta.goto( ) which means it gives the turtle a location to go to.
3. The last line of code in this function which is turta.pd( ) tells the turtle to lower the pen to start drawing. 

So in short the program tells the turtle to raise its pen, go to a certain location in the window, then lowering the pen down to start drawing.
"""

def setPos(turta, x, y):
    turta.pu()          # Lift the pen up, so no drawing occurs while moving
    turta.goto(x, y)    # Move the turtle to the specified (x, y) coordinates
    turta.pd()          # Put the pen back down, so drawing resumes

"""
def hexagon()

In this function we are giving 3 parameters:

1. turta is a name given to the turtle module
2. the hexacolor is the parameter used to give the color
3. bordercolor is the parameter used to give the border color for the hexagon

We made the hexagon by modifying the circle module command but giving it 6 sides with a radius 50:
this will create a circle with 6 sides of each angle 60 degrees(a hexagon).

The fillcolour function uses the input given in the parameter of hexa_color to fill it.
"""

def hexagon(turta, hexa_color, border_color):
    turta.pensize(2)
    turta.pencolor(border_color)
    turta.lt(90)
    turta.fillcolor(hexa_color)
    turta.begin_fill()
    turta.circle(50, 360, 6) # turta.circle(radius=, extent=, steps=)
    turta.end_fill()

"""
Def square()

In this function we are creating the square function with 3 parameters:

1. the turta which is another name for the turtle module
2. square_color-parameter for color of the square
3. border_color-parameter for border color

We have set heading to 0 which means it faces East (default turtle position).
Similar to hexagon we take the input for the parameters for fillcolor, bordercolor and turta.
We make the square by moving the turtle forward 90 steps then turning to left 90 degrees and moving 90 steps forward.
Similarly we repeat this 2 more times to complete the square.
"""

def square(turta, square_color, border_color):
    turta.seth(0)
    turta.pensize(2)
    turta.pencolor(border_color)
    turta.fillcolor(square_color)
    turta.begin_fill()
    turta.fd(90)
    turta.lt(90)
    turta.fd(90)
    turta.lt(90)
    turta.fd(90)
    turta.lt(90)
    turta.fd(90)
    turta.end_fill()
    turta.lt(90)

"""
def circle()

In this function we are creating the circle function with 3 parameters:

1. the turta which is another name for the turtle module
2. circle_color-parameter for color of the circle
3. border_color-parameter for border color

Similar to hexagon and square we take the input for the parameters for fillcolor, bordercolor and turta.
We use the circle module of turtle to create a circle with a negative radius of 50 degrees.
"""

def circle(turta, circle_color, border_color):
    turta.pensize(2)
    turta.pencolor(border_color)
    turta.fillcolor(circle_color)
    turta.begin_fill()
    turta.circle(-50)
    turta.end_fill()

"""
def pattern()

In this function, it draws a pattern using a turtle graphics object.
setPos(x, y) is used to set the position of the turtle by giving the x and y coordinates.
We are using the setpos to give the x and y coordinates.
We set position for each of the hexagon, circle, and square according to our calculations by giving x and y coordinates.

The Parameters we have used:
turtle: Turtle graphics module
hexa_color: Will take input for color of the hexagon
circle_color: Will take input for color of the circle
square_color: Will take input for color of the square
border_color: Will take input for color of the borders for all shapes

With these specifications, it will make all the hexagon, square and circle with their respective colours.
"""

def pattern(turta, hexa_color, circle_color, square_color, border_color):

    setPos(turtle, -180, 100) # Set position for the 1st hexagon ↓
    hexagon(turta=turta, hexa_color=hexa_color, border_color=border_color)
    setPos(turtle, -150, 100) # Set position for 1st circle ↓
    circle(turta=turta, circle_color=circle_color, border_color=border_color)
    setPos(turtle, -10, 55) # Set position for 1st square ↓
    square(turta=turta, square_color=square_color, border_color=border_color)

    setPos(turtle, -80, -15) # Set position for 2nd hexagon ↓
    hexagon(turta=turta, hexa_color=hexa_color, border_color=border_color)
    setPos(turtle, -50, -10) # Set position for 2nd circle ↓
    circle(turta=turta, circle_color=circle_color, border_color=border_color)
    setPos(turtle, 90, -60) # Set position for 2nd square ↓
    square(turta=turta, square_color=square_color, border_color=border_color)

    setPos(turtle, 25, -125) # Set position for 3rd hexagon ↓
    hexagon(turta=turta, hexa_color=hexa_color, border_color=border_color)
    setPos(turtle, 55, -125) # Set position for 3rd circle ↓
    circle(turta=turta, circle_color=circle_color, border_color=border_color)
    setPos(turtle, 195, -175) # Set position for 3rd square ↓
    square(turta=turta, square_color=square_color, border_color=border_color)
    # turtle.pu()
    # turtle.home()

"""
The main() function:

This functions stores the pattern(turta=, hexa_color=, circle_color=, square_color=, border_color=) function within it. 
Then is called at the end of the program.
The function pattern is called in the main() instead of calling all of the other functions in main().
The reason why we made this function is to make it less complicated because it's easier to create a function that calls the other functions (pattern)
"""

def main():
    pattern(turtle, input("Enter the color of hexagon: "),
    input("Enter the color of circle: "),
    input("Enter the color of square: "),
    input("Enter the color of shape borders: "))
    print()
    turtle.done()

main()