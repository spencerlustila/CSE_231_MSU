################################################################
# CSE 231 proj04
#
# Algorithm 
#   Asks the user for which flag they want to draw
#   Takes input
#       If the input is wrong, an error is printed
#   Calls a function
#   Prints all elements of the flag
################################################################

#import statements
import turtle, time

#Symbolic Constants
PROMPT = '''
Select one of the following options:
    TUN: Tunisia
    LBY: Libya
    TUR: Turkey
    SGP: Singapore
    ALL: All Flags
    Q: Quit
'''
FLAG_ERROR = "Flag not recognized."
A_HEIGHT = 240

#Functions
def rectangle(x,y,length,height,color): #function to draw a rectangle
    
    """

    Draw a rectangle of a certain length, height, and color

    x:       x coordinate of starting point
    y:       y coordinate of starting point
    length:  length of the rectangle
    height:  height of the rectangle
    color:   color of the filling of the rectangle

    Returns:  The finished rectangle

    """
    
    turtle.penup() #lifts the pen up
    turtle.setheading(0)
    turtle.goto(x,y) #turtle goes to starting point
    turtle.fillcolor(color) #sets turtle fill color
    turtle.pencolor("black")
    turtle.begin_fill() #begins filling the turtle
    turtle.pendown() #puts the pen down
    i = 0 #counter variable for while loop
    while i < 2: #while loop to draw rectangle
        turtle.right(90) #faces the turtle towards the right by 90 degrees
        turtle.forward(height) #moves the turtle down by the height parameter
        turtle.right(90) #turns the turtle right by 90 degress
        turtle.forward(length) #moves the turtle forward by the length parameter
        i += 1 #adds 1 to the counter variable
    turtle.end_fill() #ends the filling of the turtle
        
def circle(x,y,radius,color): #function to draw a circle

    """

    Count the number of digits in an integer value.

    value:  The value to be processed (int)

    Returns:  The number of digits in value (int)

    """
    
    turtle.penup() #lifts the pen up
    turtle.goto(x,y) #turtle goes to the starting point
    turtle.color(color) #sets the turtle color
    turtle.begin_fill() #begins filling the turtle
    turtle.pendown() #puts the pen down
    turtle.circle(radius) #draws a circle of a certain radius
    turtle.end_fill() #ends fillings the turtle
             
def crescent(x1,y1,x2,y2,R1,R2,color1,color2): #function to draw a crescent

    """

    Draw a crescent

    x1:      x coordinate of starting point of the outside circle
    y1:      y coordinate of starting point of the outside circle
    x2:      x coordinate of starting point of the inside circle
    y2:      y coordinate of starting point of the inside circle
    R1:      radius of the outside circle
    R2:      radius of the inside circle
    color1:  color of the outside circle
    color2:  color of the inside circle

    Returns:  The finished crescent

    """
    
    circle(x1,y1,R1,color1) #calls the circle function to draw the outside circle
    circle(x2,y2,R2,color2) #calls the circle function to draw the inside circle

def star(x,y,size,color,theta): #function to draw a star

    """

    Draw a star at a specific x and y of a certain size, color and outside angles

    x:      x coordinate of starting point
    y:      y coordinate of starting point
    size:   sidelength of one side of the star
    theta:  outside angles of the star

    Returns:  The finshed star

    """
    
    turtle.color(color) #sets the color of the star
    turtle.penup() #lifts the pen up
    turtle.goto(x,y) #moves the turtle to the starting point
    turtle.begin_fill() #begins filling the turtles drawn area
    turtle.left(90) #sets the turtle to face straight up
    for i in range(5): #loop to draw the completed circle
        turtle.forward(size) #moves the turtle forward the user selected amount
        turtle.left(theta/2) #turns the turtle to the inside angles size
        turtle.forward(size) #moves the turtle forward to the user selected amount
        turtle.right(theta) #turns the turtle to the user selected angle
    turtle.end_fill() #ends filling the turtle drawn area
               
def tunisia_flag(x,y,height): #function to draw the flag of Tunisia

    """

    Draw the Tunisian Flag at a certain x, y, and by a certain height

    x:       x coordinate of starting point
    y:       y coordinate of starting point
    height:  height of the flag

    Returns:  The completed flag

    """
    
    length = 1.5 * height #sets the length of the flag to 1.5 times the height
    color = "red" #sets the flag color to red
    rectangle(x,y,length,height,color) #calls the rectangle funtion to draw the \
    #flag outline and main color
    x1 = x-180 #sets the x value of the starting of the circle
    y1 = y-180 #sets the y value of the starting of the circle
    radius = height/4 #sets the radius to be 4 divided by the height
    color = "white" #sets the color to white
    circle(x1,y1,radius,color) #draws the circle
    #draws the innter red circle (cresent)
    x1 = x-180 #sets the x value of the outside red circle
    y1 = y-165 #sets the y value of the outside red circle
    x2 = x-168 #sets the x value of the inside white circle
    y2 = y-156 #sets the y value of the inside white circle
    R1 = ((3 * height)/8)/2 #sets the radius of the outside red circle
    R2 = ((3 * height)/10)/2 #sets the radius of the inside white circle
    color1 = "red" #sets the color of the outside circle
    color2 = "white" #sets the color of the inside circle
    crescent(x1,y1,x2,y2,R1,R2,color1,color2) #calls the crescent function to \
    #draw the crescent
    #draws the star
    x1 = x-176 #sets the x value of the star
    y1 = y-147 #sets the y value of the star
    size = 20 #sets the side length of the star
    color = "red" #sets the color of the star
    theta = 144 #sets the angle of the outside lines of the star
    star(x1,y1,size,color,theta) #calls the star function to draw the star
    
def libya_flag(x,y,height): #function to draw the flag of Libya

    """

    Draw the libyan Flag at a certain x, y, and by a certain height

    x:       x coordinate of starting point
    y:       y coordinate of starting point
    height:  height of the flag

    Returns:  The completed flag

    """
    
    #draws the shape of the flag
    length = 1.5 * height #sets the length of the flag to 1.5 times the height
    color = "black" #sets the flag color to black
    rectangle(x,y,length,height,color) #calls the rectangle funtion to draw the \
    #flag outline and main color
    #draws the top red rectangle
    height1 = height/4 #sets the height of the red rectangle
    color = "red" #sets the color of the rectangle
    rectangle(x,y,length,height1,color) #calls the rectangle function to draw the rectangle
    #draws the bottom green rectangle
    y = (y - height) + (height1) #sets the y value of the bottom green rectangle
    color = "green" #set sthe color of of the rectangle
    rectangle(x,y,length,height1,color) #calls the rectangle function to draw the rectangle
    #draws the crescent
    x1 = x - ((3*height)/4) #sets the x value of the outside circle
    y1 = y + 30 #sets the y value of the value of the outside circle
    x2 = x1 + 10 #sets the x value of the inside circle
    y2 = y1 + 6 #sets the y value of the inside circle
    R1 = (height/4)/2 #sets the radius of the outside circle
    R2 = (height/5)/2 #sets the radius of the inside circle
    color1 = "white" #sets the color of the outside circle
    color2 = "black" #sets the color of the inside circle
    crescent(x1,y1,x2,y2,R1,R2,color1,color2) #calls the crescent function to \
    #draw the crescent
    #draws the star
    x = x1+36 #sets the x value of the star
    y = y1+15 #sets the y value of the star
    size = 12 #sets the sidelength of 1 side of the star
    color = "white" #sets the color of the star
    theta = 144 #sets the outside angle of the star
    star(x,y,size,color,theta) #calls the star function to draw the star
        
def turkey_flag(x,y,height): #function to draw the flag of Turkey

    """

    Draw the Turkish Flag at a certain x, y, and by a certain height

    x:       x coordinate of starting point
    y:       y coordinate of starting point
    height:  height of the flag

    Returns:  The completed flag

    """
    
    length = 1.5 * height #sets the length of the flag to 1.5 times the height
    color = "red" #sets the flag color to red
    rectangle(x,y,length,height,color) #calls the rectangle funtion to draw the \
    #flag outline and main color
    #draws the white bar on the left side of the flag
    x1 = (x-length)+height/30 #sets x coordinate of the starting value
    length = height/30 #sets the length of the rectangle
    height = height #sets the height of the rectangle
    color = "white" #sets the color of the rectangle
    rectangle(x1,y,length,height,color) #calls the rectangle function to draw the rectangle.
    #draws the crescent
    x1 = x-240 #sets the x coordinate of the outside circle
    y1 = y-180 #sets the y coordinate of the outside circle
    x2 = x-225 #sets the x coordinate of the inside circle
    y2 = y-168 #sets the y coordinate of the inside circle
    R1 = height/4 #sets the radius of the outside cirlce
    R2 = ((2*height)/5)/2 #sets the radius of the inside circle
    color1 = "white" #set sthe color of the outside circle
    color2 = "red" #sets the color of the inside circle
    crescent(x1,y1,x2,y2,R1,R2,color1,color2) #calls the crescent function to \
    #draw the crescent
    #draws the star
    x1 = x-173 #sets the x coordinate of the star
    y1 = y-150 #sets the y coordinate of the star
    size = 22 #sets the sidelength of a side of the star
    color = "white" #sets the color of the star
    theta = 144 #sets the angle of the outside of the star
    star(x1,y1,size,color,theta) #calls the star function to draw the star

def singapore_flag(x,y,height): #function to draw the flag of Singapore

    """

    Draw the Singaporean Flag at a certain x, y, and by a certain height

    x:       x coordinate of starting point
    y:       y coordinate of starting point
    height:  height of the flag

    Returns:  The completed flag

    """
    
    length = 1.5 * height #sets the length of the flag to 1.5 times the height
    color = "red" #sets the flag color to red
    rectangle(x,y,length,height,color) #calls the rectangle funtion to draw the \
    #flag outline and main color
    #draws the bottom white rectangle
    y1 = y-120 #sets the y value of the bottom rectangle
    height1 = height/2 #calculates the hiehgt of the bottom rectangle
    color = "white" #changes the color of the bottom rectangle
    rectangle(x,y1,length,height1,color) #calls the rectangle function to draw the rectangle
    #draws the crescent
    x1 = (x-length)+height/3 #sets the x value of the smaller circle
    y1 = y1+(height1-((10*height)/27))/2 #sets the y value of the smaller circle
    x2 = (x-length)+height/3+(height/10) #sets the x value of the bigger circle
    y2 = (y-120)+(height1-((2*height)/5))/2 #sets the y value of the bigger circle
    R1 = ((10*height)/27)/2 #sets the radius of the smaller cirlce
    R2 = ((2*height)/5)/2 #sets the radius of the bigger circle
    color1 = "white" #changes the color of the smaller circle
    color2 = "red" #changes the color of the bigger circle
    crescent(x1,y1,x2,y2,R1,R2,color1,color2) #calls the crescent function to draw the crescent
    #draws the top star
    turtle.setheading(270) #sets the turtle to point directly downward
    x = (x1 + (height/9))-(((4*height)/45)/2) #sets the x value of the star
    y1 = y-((height/4)) + (height/9) 
    size = 8 #sets the sidelength of one side of the star
    color = "white" #changes the color of the star
    theta = 144 #sets the outside angle of the star
    star(x,y1+4,size,color,theta) #calls the star function to draw the star
    #draws the top right star
    turtle.setheading(270) #sets the turtle to point directly downward
    x = (x1+24 + (height/9))-(((4*height)/45)/2) #sets the x value of the star
    y1 = y-((height/4))+(((4*height)/45)/2) #sets the y value of the star
    size = 8 #sets the sidelength of one side of the star
    color = "white" #changes the color of the star
    theta = 144 #sets the outside angle of the star
    star(x-2,y1+2,size,color,theta) #calls the star function to draw the star
    #draws the top left star
    turtle.setheading(270) #sets the turtle to point directly downward
    x = (x1+24 - (height/9))-(((4*height)/45)/2) #sets the x value of the star
    y1 = y-((height/4))+(((4*height)/45)/2) #sets the y value of the star
    size = 8 #sets the sidelength of one side of the star
    color = "white" #changes the color of the star
    theta = 144 #sets the outside angle of the star
    star(x+6,y1+2,size,color,theta) #calls the star function to draw the star
    #draws the bottom left star
    turtle.setheading(270) #sets the turtle to point directly downward
    x = (x1+24 + (height/9))-(((4*height)/45))-7-(((4*height)/45)) #sets the x value of the star
    y1 = y-((height/4))-(((4*height)/45)) #sets the y value of the star
    size = 8 #sets the sidelength of one side of the star
    color = "white" #changes the color of the star
    theta = 144 #sets the outside angle of the star
    star(x,y1+4,size,color,theta) #calls the star function to draw the star
    #draws the bottom right star
    turtle.setheading(270) #sets the turtle to point directly downward
    x = (x1+24 + (height/9))-(((4*height)/45)) #sets the x value of the star
    y1 = y-((height/4))-(((4*height)/45)) #sets the y value of the star
    size = 8 #sets the sidelength of one side of the star
    color = "white" #changes the color of the star
    theta = 144 #sets the outside angle of the star
    star(x+3,y1+4,size,color,theta) #calls the star function to draw the star
  
enter = True #Boolean variable for telling the code to begin printing flags        
while enter == True: #Main Function Loop
    valid_option = False #Boolean variable for validating input is valid
    flag = "" #user choice of flag
    
    while valid_option == False: #checks if the input is valid
        flag = input(PROMPT) #prints the PROMPT
        if flag.lower() == "tun": #checks if user wants to draw Tunisia
            valid_option = True #the user inputted a valid option
            break #exits the loop
        if flag.lower() == "lby": #checks if the user wants to draw Libya
            valid_option = True #the user inputted a valid option
            break #exits the loop
        if flag.lower() == "tur": #checks if the user wants to draw Turkey
            valid_option = True #the user inputted a valid option
            break #exits the loop
        if flag.lower() == "sgp": #checks if the user wants to draw Singapore
            valid_option = True #the user inputted a valid option
            break #exits the loop
        if flag.lower() == "all": #checks if the user wants to draw all flags
            valid_option = True #the user inputted a valid option
            break #exits the loop
        if flag.lower() == "q": #checks if the user wants to quit
            valid_option = True #the user inputted a valid option
            break #exits the loop
        print(FLAG_ERROR) #the user inputted a wrong option
    
    if flag.lower() == "q": #checks if the user wants to quit
        print("Bye") #prints the exit message
        enter = False #does not allow the code to begin flag printing
    
    if enter == True: #the user wants to draw a flag
        #turtle setup information
        turtle.setup (width=1920, height=1080, startx=0, starty=0) #makes the turtle fit a 1080p screen
        turtle.hideturtle() #hids the turtle arrow
        turtle.speed(100) #makes the turtle go at max speed
        if flag.lower() == "tun": #the user wants a flag of Tunisia
            x = 0 #sets the x coordinate of the starting point of the flag
            y = 0 #sets the y coordinate of the starting point of the flag
            tunisia_flag(x,y,A_HEIGHT) #runs the function to draw the Tunisian flag
            time.sleep(4) #keeps the turtle window open for 4 seconds
            turtle.clear() #clears the turtle window
        if flag.lower() == "lby": #the user wants a flag of Libya
            x = 0 #sets the x coordinate of the starting point of the flag
            y = 0 #sets the y coordinate of the starting point of the flag
            libya_flag(x,y,A_HEIGHT) #runs the function to draw the Libyan flag
            time.sleep(4) #keeps the turtle window open for 4 seconds
            turtle.clear() #clears the turtle window
        if flag.lower() == "tur": #the user wants a flag of Turkey
            x = 0 #sets the x coordinate of the starting point of the flag
            y = 0 #sets the y coordinate of the starting point of the flag
            turkey_flag(x,y,A_HEIGHT) #runs the function to draw the Turkey flag
            time.sleep(4) #keeps the turtle window open for 4 seconds
            turtle.clear() #clears the turtle window
        if flag.lower() == "sgp": #the user wants a flag of Singapore
            x = 0 #sets the x coordinate of the starting point of the flag
            y = 0 #sets the y coordinate of the starting point of the flag
            singapore_flag(x,y,A_HEIGHT)
            time.sleep(4) #keeps the turtle window open for 4 seconds
            turtle.clear() #clears the turtle window
        if flag.lower() == "all": #the user wants all the flags
            #draws Tunisia Flag
            x = -100 #sets the x coordinate of the starting point of the flag
            y = 300 #sets the y coordinate of the starting point of the flag
            tunisia_flag(x,y,A_HEIGHT) #runs the function to draw the Tunisian flag
            #draws Libya flag
            x = -100 #sets the x coordinate of the starting point of the flag
            y = -100 #sets the y coordinate of the starting point of the flag
            libya_flag(x,y,A_HEIGHT) #runs the function to draw the Libyan flag
            #draws Turkey Flag
            x = 360 #sets the x coordinate of the starting point of the flag
            y = 300 #sets the y coordinate of the starting point of the flag
            turkey_flag(x,y,A_HEIGHT) #runs the function to draw the Turkey flag
            #draws Singapore Flag
            x = 360 #sets the x coordinate of the starting point of the flag
            y = -100 #sets the y coordinate of the starting point of the flag
            singapore_flag(x,y,A_HEIGHT) #runs the function to draw the Singaporean flag
            time.sleep(4) #keeps the turtle window open for 4 seconds
            turtle.clear() #clears the turtle window