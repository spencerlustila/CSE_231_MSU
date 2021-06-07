################################################################
# CSE 231 proj02
#
# Algorithm 
#   Print the Prompt
#   If the user wants to draw circles
#       Ask the number of circles
#       Ask the radius of the largest circle
#   If the user wants to draw squares
#       Ask the number of squares
#       Ask the side length of the squares
#   Prints error messages if the inputted information is wrong
#   If the user inputted 0, the program will end
#   Draws the shape
#   Restarts the Kernel
################################################################

import turtle, os, random, time

#Symbolic Constants (Including all the output messages from the Strings file)
PROMPT = '''
what do you want to draw:
          
	(0) to quit         
	(1) circles         
	(2) square spiral.
    
choice: '''
CIRCLE_DESCRIPTION = "\nThis program draws concentric circles of many \
different colors.\n"
NEGATIVE_CIRCLE_ERROR = "Number of circles must be positive; try again."
CIRCLE_RADIUS_ERROR = "The radius must be an integer between 50 and 200; \
try again."
SQUARE_DESCRIPTION = "\nThis program draws squares of many colors.\n"
NEGATIVE_SQUARE_ERROR = "Number of squares must be positive; try again."
SQUARE_LENGTH_ERROR = "The side length must be an integer between 50 and \
200; try again."
WRONG_CHOICE_NUMBER = "Invalid choice; try again."
CIRCLE_NUM_PROMPT = "Enter the number of circles to draw: "
INITIAL_CIRCLE_RADIUS_PROMPT = "\nEnter the radius (>=50, <=200) of the \
largest circle: "
CIRCLE_RADIUS_PROMPT = "Enter the radius (>=50, <=200) of the largest circle: "
SQUARE_NUM_PROMPT = "Enter the number of squares to draw: "
INITIAL_SQUARE_LENGTH_PROMPT = "\nEnter the side length (>=50, <=200) of \
the largest square: "
SQUARE_LENGTH_PROMPT = "Enter the side length (>=50, <=200) of the \
largest square: "

#Initialization (Collects the required information from the user)
choice_str = input(PROMPT) #Prints the prompt, and takes the user's choice
choice_int = int(choice_str) #Converts the user's input into an int
circle_num_int = 0 #number of circles the user wants to draw
circle_radius_int = 0 #radius of the largest circle the user wants to draw
square_num_int = 0 #number of sqares the user wants to draw
square_length_int = 0 #side length of the squares

while choice_int != 0: #Figuring out what shape the user wants to draw
    if choice_int == 1: #the user has selected to draw a circle
        print(CIRCLE_DESCRIPTION) #prints the description of the circle
        circle_num_int = int(input(CIRCLE_NUM_PROMPT)) #asks for the number \
        #of circles
        if circle_num_int <= 0: #the user has inputted a negative number
            print(NEGATIVE_CIRCLE_ERROR) #prints the error
            circle_num_int = int(input(CIRCLE_NUM_PROMPT)) #asks user for \
            #number of circles
        circle_radius_int = int(input(INITIAL_CIRCLE_RADIUS_PROMPT)) #asks \
        #user for radius of largest circle
        if (circle_radius_int < 50) or (circle_radius_int > 200): #checks \
        #if the radius is too large or small
            print(CIRCLE_RADIUS_ERROR) #prints the error
            circle_radius_int = int(input(CIRCLE_RADIUS_PROMPT)) #asks user \
            #for the radius of the largest circle
        break #ends the while loop
    if choice_int == 2: #the user has selected to draw squares
        print(SQUARE_DESCRIPTION)
        square_num_int = int(input(SQUARE_NUM_PROMPT)) #asks for the number \
        #of squares
        if square_num_int <= 0: #the user has inputted a negative number
            print(NEGATIVE_SQUARE_ERROR) #prints the error
            square_num_int = int(input(SQUARE_NUM_PROMPT)) #asks user for \
            #number of square
        square_length_int = int(input(INITIAL_SQUARE_LENGTH_PROMPT)) #asks \
        #user for side length of the squares
        if (square_length_int < 50) or (square_length_int > 200): #checks \
        #if the side length is too large or small
            print(SQUARE_LENGTH_ERROR)
            square_length_int = int(input(SQUARE_LENGTH_PROMPT)) #asks user \
            #for the side lengths of the squares
        break #ends the while loop
    if (choice_int < 0) or (choice_int > 0): #checks to see if the user /
    #inputted a wrong choice number
        print(WRONG_CHOICE_NUMBER) #prints the error
        choice_str = input(PROMPT) #Prints the prompt, and takes the user's \
        #choice
        choice_int = int(choice_str) #Converts the user's input into an int
        
if choice_int == 0: #checks to see if the user wants to quit
    os._exit(0) #ends the program
    
#Drawing
turtle.hideturtle() #hides the turtle's arrow from the drawing
turtle.speed(100) #speeds up the turtle to have the drawing finish faster

if choice_int == 1: #checks to see if the user wants to print a circle
    for i in range(circle_num_int): #creates a loop that will create the number \
    #of circles the user inputted
        turtle.begin_fill() #starts the filling of the shape the turtle draws
        turtle.penup() #lifts the pen up
        turtle.color(random.random(), random.random(), random.random()) #randomizes \
        #the color choices for the circles
        if i == 0: #checks if it is drawing the first circle
            turtle.goto(0,-circle_radius_int) #translates the starting point \
            #so that the circle is in the center of the popup
        turtle.pendown() #puts the pen down
        turtle.circle(circle_radius_int - (circle_radius_int * (i/10))) #changes \
        #the radius of the circle so that it will become smaller by 10% each time
        turtle.end_fill() #ends the filling of the shape the turtle draws
        turtle.penup() #lefts the pen up
        turtle.goto(0,-circle_radius_int + (circle_radius_int * ((i+1)/10))) #moves \
        #the starting point of the turtle so that the next circle starts 10% \
        #above the starting of the previous circle
elif choice_int == 2: #checks to see if the user wants to print a square
    turtle.setheading(0)#sets the starting direction to 0 degrees
    for i in range(square_num_int): #creates a loop that will create the number \
    #of squares the user inputted        
        turtle.begin_fill() #starts the filling of the shape the turtle draws
        turtle.color(random.random(), random.random(), random.random())
        n_int = 0 #while loop counter integer
        while n_int < 4: #creates a loop to the draw the 4 sides of the square
            turtle.forward(square_length_int) #draws the side length to the one \
            #the user inputted
            turtle.right(90) #turns the turtle right 90 degrees
            n_int += 1 #adds 1 to the counter variable
        turtle.end_fill() #ends the filling of the shape the turtle draws
        turtle.setheading(0 - (360/square_num_int) * (i + 1)) #changes the direction \
        #of the turtle so that the drawing forms a spiral depending on the \
        #inputted number of squares    

time.sleep(4) #will show the drawing for 4 seconds
os._exit(1) #will close the drawing window, and restart the Kernel