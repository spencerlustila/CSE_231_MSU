##############################################################################
# CSE 231 proj07
#
# Algorithm 
#   Asks the user to pick a color
#       If the input is invalid, the program will ask until a valid one is\
#           given
#   Then the program will run continuously and ask the user for a number to\
#       drop their disc into
#           The program will check after every input, if the game is complete
#   After the game ends the program prints the winner
##############################################################################

pieces = {'black':'b', 'white':'w'}
COLUMN = 7
ROW = 6

def initialize(): #function for creating the game board
    """

    Creates a list of lists that the game will be played in

    Parameters: NONE

    Returns:  TThe list of lists called board

    """
    
    board = [[],[],[],[],[],[]] #creates a list of lists with 6 indexes
    for i in range(6): #loop for filling the list of lists
        board[i] = [0,0,0,0,0,0,0] #fills each indes of the list with 0s
    return board #returns the filled board

def choose_color(): #function for getting the user's color
    """

    Finds the color the user wants to use as theirs

    Parameters: NONE

    Returns:  The user's color, and the opponent's color

    """
    
    wrong_color = "Wrong color; enter only 'black' or 'white', try again." #string if the inputted color is not valid
    valid_color = False #boolean variable for checking if the user's color is correct
    color = "" #variable that the user's color will be put into
    alternate_color = "" #variable that the opponent's color will be put into
    while valid_color == False: #loop that will run as long as the user does not input a valid color
        color = input("Pick a color: ") #prints the prompt
        if color.lower() == "white": #checks if the user chose white
            color = "white" #sets the user's color to white
            alternate_color = "black" #sets the opponent's color to black
            valid_color = True #the user has entered a valid color
        elif color.lower() == "black": #checks if the user chose black
            color = "black" #sets the user's color to black
            alternate_color = "white" #sets the opponents color to white
            valid_color = True #the user has inputted a valid color
        else: #the user has not entered a valid color
            print(wrong_color) #prints the error message
            valid_color = False #the user did not enter a valid color
    return color, alternate_color #returns the colors of the players

def board_display(board): #function for displaying the board
    """

    Prints the list of lists as a formatted game board

    board: The list of lists returned in initialize

    Returns:  NONE, but prints the formatted board

    """
    
    print("Current board:") #header of the fomatted board
    C = COLUMN
    R = ROW
    hline = '\n' + (' ' * 2) + ('+---' * C) + '+' + '\n'
    numline = ' '.join([(' ' + str(i) + ' ') \
                        for i in range(1, C + 1)])
    str_ = (' ' * 3) + numline + hline
    for r in range(0, R):
        str_ += str(r+1) + ' |'
        for c in range(0, C):
            str_ += ' ' + \
                (str(board[r][c]) \
                     if board[r][c] is not 0 else ' ') + ' |'
        str_ += hline
    print (str_)

def drop_disc(board, column, color): #function for dropping the disk in the board
    """

    Drops the disc into the board

    board:  the list of list returned in initialiae
    column: the column the user wants to drop the disc into
    color:  the color that the user is

    Returns:  the row that the disc dropped into, full if the column in full, None if \
              the user entered an invalid number

    """
    
    row = 0 #variable for the row
    valid_column = False #boolean variable for checking if the user inputted a valid column
    column_error = "Invalid column: 1 <= column <= 7. Please try again." #the error message
    if column <= 7 and column >= 1: #checks if the user entered a valid number
        valid_column = True #the user entered a valid number
    else: #the user did not enter a valid number
        print(column_error) #prints the error
        valid_column = False #the user did not enter a valid number
    if valid_column == True: #the user entered a valid number
        initial_passed = False #boolean variable for checking if column is full
        for n in range(6): #loop that checks every index in a column
            if (board[5-n][column-1] == "w") or (board[5-n][column-1] == "b"): #checks if a row has something in it
                pass #passes
            else: #the row does now have anything in it
                board[5-n][column-1] = color[:1] #drops the user's disc into the column
                initial_passed = True #the disc was dropped
                row = 6-n #the row that the disc was dropped into
                break #exits the loop
        if initial_passed == False: #the column was full
            print("This column is full. Please try again.") #prints the error message
            return "full" #returns full
        return row #returns the row the disc was dropped into
        

def check_disc(board, row, column): #function for checking if there is a winning sequence
    """

    Checks if there is a winning sequence at a specific row and column

    board: the list of lists created in initialize
    row: the row the user wants to check
    column: the column the user wants to check

    Returns:  True if there is winning sequence, False if there is not, None if the row is invalid

    """
    
    row = row-1 #sets the row to the acutal index value
    if row < 0: #checks if the row is negative
        return None #returns None
    column = column-1 #sets the column to the actual index value
    if column < 0: #checks if the column is negative
        return None #returns None
    
    if board[row][column] == 0: #checks if the number being checked is 0, and thus does not win
        return False #returns Flase
    
    column_list = [] #variabele for the list of the column the user wants to check
    for n in range(6): #loop to create the list of column values
        column_list.append(board[n][column]) #adds the value to the column list
    row_list = board[row] #creates the row list
    
    #list variables that every possibility will be in
    diagnol_list1 = []
    diagnol_list2 = []
    diagnol_list3 = []
    diagnol_list4 = []
    diagnol_list5 = []
    diagnol_list6 = []
    #if statements that fill the lists with the chosen range in the parameters
    if row == 0 and column == 0: #chosen row 1 and column 1
        diagnol_list1.append(board[row][column])
        diagnol_list1.append(board[row+1][column+1])
        diagnol_list1.append(board[row+2][column+2])
        diagnol_list1.append(board[row+3][column+3])
    elif row == 0 and column == 6: #chosen row 1 and column 7
        diagnol_list2.append(board[row][column])
        diagnol_list2.append(board[row+1][column-1])
        diagnol_list2.append(board[row+2][column-2])
        diagnol_list2.append(board[row+3][column-3])
    elif row == 5 and column == 0: #chosen row 6 and column 1
        diagnol_list2.append(board[row][column])
        diagnol_list2.append(board[row-1][column+1])
        diagnol_list2.append(board[row-2][column+2])
        diagnol_list2.append(board[row-3][column+3])
    elif row == 5 and column == 6:#chosen row 6 and column 7
        diagnol_list1.append(board[row][column])
        diagnol_list1.append(board[row-1][column-1])
        diagnol_list1.append(board[row-2][column-2])
        diagnol_list1.append(board[row-3][column-3])
    elif 0 <= row <= 1 and column == 1:#chosen row between 1 and 2 and column 2
        if row == 1: ##chosen row 2
            diagnol_list1.append(board[row-1][column-1])
            diagnol_list1.append(board[row][column])
            diagnol_list1.append(board[row+1][column+1])
            diagnol_list1.append(board[row+2][column+2])
            diagnol_list4.append(board[row][column])
            diagnol_list4.append(board[row+1][column+1])
            diagnol_list4.append(board[row+2][column+2])
            diagnol_list4.append(board[row+3][column+3])
        else: #chosen row 1
            diagnol_list1.append(board[row][column])
            diagnol_list1.append(board[row+1][column+1])
            diagnol_list1.append(board[row+2][column+2])
            diagnol_list1.append(board[row+3][column+3])
    elif 0 <= row <= 1 and column == 2: #chosen row between 1 and 2 and column 2
        if row == 1:#chosen row 2
            diagnol_list2.append(board[row-1][column+1])
            diagnol_list2.append(board[row][column])
            diagnol_list2.append(board[row-1][column+1])
            diagnol_list2.append(board[row-2][column+2])
            diagnol_list1.append(board[row-1][column-1])
            diagnol_list1.append(board[row][column])
            diagnol_list1.append(board[row+1][column+1])
            diagnol_list1.append(board[row+2][column+2])
            diagnol_list4.append(board[row][column])
            diagnol_list4.append(board[row+1][column+1])
            diagnol_list4.append(board[row+2][column+2])
            diagnol_list4.append(board[row+3][column+3])
        else:#chosen row 1
            diagnol_list1.append(board[row][column])
            diagnol_list1.append(board[row+1][column+1])
            diagnol_list1.append(board[row+2][column+2])
            diagnol_list1.append(board[row+3][column+3])
    elif row == 2 and column == 1: #chosen row 3 and column 2
        diagnol_list2.append(board[row+1][column-1])
        diagnol_list2.append(board[row][column])
        diagnol_list2.append(board[row-1][column+1])
        diagnol_list2.append(board[row-2][column+2])
        diagnol_list1.append(board[row-1][column-1])
        diagnol_list1.append(board[row][column])
        diagnol_list1.append(board[row+1][column+1])
        diagnol_list1.append(board[row+2][column+2])
        diagnol_list3.append(board[row][column])
        diagnol_list3.append(board[row+1][column+1])
        diagnol_list3.append(board[row+2][column+2])
        diagnol_list3.append(board[row+3][column+3])
    elif row == 3 and column == 1:#chosen row 4 and column 2
        diagnol_list1.append(board[row-1][column-1])
        diagnol_list1.append(board[row][column])
        diagnol_list1.append(board[row+1][column+1])
        diagnol_list1.append(board[row+2][column+2])
        diagnol_list2.append(board[row+1][column-1])
        diagnol_list2.append(board[row][column])
        diagnol_list2.append(board[row-1][column+1])
        diagnol_list2.append(board[row-2][column+2])
        diagnol_list3.append(board[row][column])
        diagnol_list3.append(board[row-1][column+1])
        diagnol_list3.append(board[row-2][column+2])
        diagnol_list3.append(board[row-3][column+3])
    elif row == 4 and column == 1:#chosen row 5 and column 2
        diagnol_list2.append(board[row+1][column-1])
        diagnol_list2.append(board[row][column])
        diagnol_list2.append(board[row-1][column+1])
        diagnol_list2.append(board[row-2][column+2])
        diagnol_list3.append(board[row][column])
        diagnol_list3.append(board[row-1][column+1])
        diagnol_list3.append(board[row-2][column+2])
        diagnol_list3.append(board[row-3][column+3])
    elif row == 5 and column == 1:#chosen row 6 and column 2
        diagnol_list2.append(board[row][column])
        diagnol_list2.append(board[row-1][column+1])
        diagnol_list2.append(board[row-2][column+2])
        diagnol_list2.append(board[row-3][column+3])
    elif row == 2 and column == 2:#chosen row 3 and column 3
        diagnol_list1.append(board[row][column])
        diagnol_list1.append(board[row+1][column+1])
        diagnol_list1.append(board[row-1][column-1])
        diagnol_list1.append(board[row-2][column-2])
        diagnol_list4.append(board[row][column])
        diagnol_list4.append(board[row-1][column-1])
        diagnol_list4.append(board[row+1][column+1])
        diagnol_list4.append(board[row+2][column+2])
        diagnol_list5.append(board[row][column])
        diagnol_list5.append(board[row+1][column+1])
        diagnol_list5.append(board[row+2][column+2])
        diagnol_list5.append(board[row+3][column+3])
    elif row == 3 and column == 2:#chosen row 4 and column 3
        diagnol_list1.append(board[row][column])
        diagnol_list1.append(board[row-1][column-1])
        diagnol_list1.append(board[row-2][column-2])
        diagnol_list1.append(board[row+1][column+2])
        diagnol_list4.append(board[row][column])
        diagnol_list4.append(board[row-1][column-1])
        diagnol_list4.append(board[row+1][column+1])
        diagnol_list4.append(board[row+2][column+2])
        diagnol_list2.append(board[row][column])
        diagnol_list2.append(board[row+1][column-1])
        diagnol_list2.append(board[row+2][column-2])
        diagnol_list2.append(board[row-1][column+1])
        diagnol_list3.append(board[row][column])
        diagnol_list3.append(board[row+1][column-1])
        diagnol_list3.append(board[row-1][column+1])
        diagnol_list3.append(board[row-2][column+2])
        diagnol_list5.append(board[row][column])
        diagnol_list5.append(board[row-1][column+1])
        diagnol_list5.append(board[row-2][column+2])
        diagnol_list5.append(board[row-3][column+3])
    elif row == 4 and column == 2:#chosen row 4 and column 3
        diagnol_list1.append(board[row][column])
        diagnol_list1.append(board[row+1][column+1])
        diagnol_list1.append(board[row-1][column-1])
        diagnol_list1.append(board[row-2][column-2])
        diagnol_list2.append(board[row][column])
        diagnol_list2.append(board[row+1][column-1])
        diagnol_list2.append(board[row-1][column+1])
        diagnol_list2.append(board[row-2][column+2])
        diagnol_list3.append(board[row][column])
        diagnol_list3.append(board[row-1][column+1])
        diagnol_list3.append(board[row-2][column+2])
        diagnol_list3.append(board[row-3][column+3])
    elif row == 5 and column == 2:#chosen row 6 and column 3
        diagnol_list2.append(board[row][column])
        diagnol_list2.append(board[row-1][column+1])
        diagnol_list2.append(board[row-2][column+2])
        diagnol_list2.append(board[row-3][column+3])
    elif row == 0 and column == 3:#chosen row 1 and column 4
        diagnol_list2.append(board[row][column])
        diagnol_list2.append(board[row+1][column-1])
        diagnol_list2.append(board[row+2][column-2])
        diagnol_list2.append(board[row+3][column-3])
        diagnol_list1.append(board[row][column])
        diagnol_list1.append(board[row+1][column+1])
        diagnol_list1.append(board[row+2][column+2])
        diagnol_list1.append(board[row+3][column+3])
    elif row == 1 and column == 3:#chosen row 2 and column 4
        diagnol_list1.append(board[row][column])
        diagnol_list1.append(board[row-1][column-1])
        diagnol_list1.append(board[row+1][column+1])
        diagnol_list1.append(board[row+2][column+2])
        diagnol_list4.append(board[row][column])
        diagnol_list4.append(board[row+1][column+1])
        diagnol_list4.append(board[row+2][column+2])
        diagnol_list4.append(board[row+3][column+3])
        diagnol_list2.append(board[row][column])
        diagnol_list2.append(board[row-1][column+1])
        diagnol_list2.append(board[row+1][column-1])
        diagnol_list2.append(board[row+2][column-2])
        diagnol_list3.append(board[row][column])
        diagnol_list3.append(board[row+1][column-1])
        diagnol_list3.append(board[row+2][column-2])
        diagnol_list3.append(board[row+3][column-3])
    elif row == 2 and column == 3:#chosen row 3 and column 4
        diagnol_list1.append(board[row][column])
        diagnol_list1.append(board[row-1][column-1])
        diagnol_list1.append(board[row-2][column-2])
        diagnol_list1.append(board[row+1][column+1])
        diagnol_list4.append(board[row][column])
        diagnol_list4.append(board[row-1][column-1])
        diagnol_list4.append(board[row+1][column+1])
        diagnol_list4.append(board[row+2][column+2])
        diagnol_list6.append(board[row][column])
        diagnol_list6.append(board[row+1][column+1])
        diagnol_list6.append(board[row+2][column+2])
        diagnol_list6.append(board[row+3][column+3])
    elif row == 3 and column == 3:#chosen row 4 and column 4
        diagnol_list1.append(board[row][column])
        diagnol_list1.append(board[row-1][column-1])
        diagnol_list1.append(board[row-2][column-2])
        diagnol_list1.append(board[row-3][column-3])
        diagnol_list4.append(board[row][column])
        diagnol_list4.append(board[row-1][column-1])
        diagnol_list4.append(board[row-2][column-2])
        diagnol_list4.append(board[row+1][column+1])
        diagnol_list2.append(board[row][column])
        diagnol_list2.append(board[row-1][column-1])
        diagnol_list2.append(board[row+1][column+1])
        diagnol_list2.append(board[row+2][column+2])
        diagnol_list3.append(board[row][column])
        diagnol_list3.append(board[row-1][column+1])
        diagnol_list3.append(board[row-2][column+2])
        diagnol_list3.append(board[row-3][column+3])
        diagnol_list5.append(board[row][column])
        diagnol_list5.append(board[row-1][column+1])
        diagnol_list5.append(board[row-2][column+2])
        diagnol_list5.append(board[row+1][column-1])
        diagnol_list6.append(board[row][column])
        diagnol_list6.append(board[row-1][column+1])
        diagnol_list6.append(board[row+1][column-1])
        diagnol_list6.append(board[row+2][column-2])
    elif row == 4 and column == 3:#chosen row 5 and column 4
        diagnol_list1.append(board[row][column])
        diagnol_list1.append(board[row+1][column-1])
        diagnol_list1.append(board[row-1][column+1])
        diagnol_list1.append(board[row-2][column+2])
        diagnol_list2.append(board[row][column])
        diagnol_list2.append(board[row-1][column+1])
        diagnol_list2.append(board[row-2][column+2])
        diagnol_list2.append(board[row-3][column+3])
        diagnol_list3.append(board[row][column])
        diagnol_list3.append(board[row+1][column+1])
        diagnol_list3.append(board[row-1][column-1])
        diagnol_list3.append(board[row-2][column-2])
        diagnol_list4.append(board[row][column])
        diagnol_list4.append(board[row-1][column-1])
        diagnol_list4.append(board[row-2][column-2])
        diagnol_list4.append(board[row-3][column-3])
    elif row == 5 and column == 3:#chosen row 6 and column 4
        diagnol_list1.append(board[row][column])
        diagnol_list1.append(board[row-1][column-1])
        diagnol_list1.append(board[row-2][column-2])
        diagnol_list1.append(board[row-3][column-3])
        diagnol_list2.append(board[row][column])
        diagnol_list2.append(board[row-1][column+1])
        diagnol_list2.append(board[row-2][column+2])
        diagnol_list2.append(board[row-3][column+3])
    elif row == 0 and column == 4:#chosen row 1 and column 5
        diagnol_list1.append(board[row][column])
        diagnol_list1.append(board[row+1][column-1])
        diagnol_list1.append(board[row+2][column-2])
        diagnol_list1.append(board[row+3][column-3])
    elif row == 1 and column == 4:#chosen row 2 and column 5
        diagnol_list1.append(board[row][column])
        diagnol_list1.append(board[row-1][column-1])
        diagnol_list1.append(board[row+1][column+1])
        diagnol_list1.append(board[row+2][column+2])
        diagnol_list2.append(board[row][column])
        diagnol_list2.append(board[row-1][column+1])
        diagnol_list2.append(board[row+1][column-1])
        diagnol_list2.append(board[row+2][column-2])
        diagnol_list3.append(board[row][column])
        diagnol_list3.append(board[row+1][column-1])
        diagnol_list3.append(board[row+2][column-2])
        diagnol_list3.append(board[row+3][column-3])
    elif row == 2 and column == 4:#chosen row 3 and column 5
        diagnol_list1.append(board[row][column])
        diagnol_list1.append(board[row+1][column-1])
        diagnol_list1.append(board[row-1][column+1])
        diagnol_list1.append(board[row-2][column+2])
        diagnol_list2.append(board[row][column])
        diagnol_list2.append(board[row-1][column+1])
        diagnol_list2.append(board[row+1][column-1])
        diagnol_list2.append(board[row+2][column-2])
        diagnol_list3.append(board[row][column])
        diagnol_list3.append(board[row+1][column-1])
        diagnol_list3.append(board[row+2][column-2])
        diagnol_list3.append(board[row+3][column-3])
    elif row == 3 and column == 4:#chosen row 4 and column 5
        diagnol_list1.append(board[row][column])
        diagnol_list1.append(board[row+1][column-1])
        diagnol_list1.append(board[row-1][column+1])
        diagnol_list1.append(board[row-2][column+2])
        diagnol_list2.append(board[row][column])
        diagnol_list2.append(board[row-1][column+1])
        diagnol_list2.append(board[row+1][column-1])
        diagnol_list2.append(board[row+2][column+2])
        diagnol_list3.append(board[row][column])
        diagnol_list3.append(board[row-1][column-1])
        diagnol_list3.append(board[row+1][column+1])
        diagnol_list3.append(board[row+2][column+2])
        diagnol_list4.append(board[row][column])
        diagnol_list4.append(board[row+1][column+1])
        diagnol_list4.append(board[row-1][column-1])
        diagnol_list4.append(board[row-2][column-2])
        diagnol_list5.append(board[row][column])
        diagnol_list5.append(board[row-1][column-1])
        diagnol_list5.append(board[row-2][column-2])
        diagnol_list5.append(board[row-3][column-3])
    elif row == 4 and column == 4:#chosen row 5 and column 5
        diagnol_list1.append(board[row][column])
        diagnol_list1.append(board[row+1][column+1])
        diagnol_list1.append(board[row-1][column-1])
        diagnol_list1.append(board[row-2][column-2])
        diagnol_list2.append(board[row][column])
        diagnol_list2.append(board[row-1][column-1])
        diagnol_list2.append(board[row-2][column-2])
        diagnol_list2.append(board[row-3][column-3])
        diagnol_list3.append(board[row][column])
        diagnol_list3.append(board[row+1][column-1])
        diagnol_list3.append(board[row-1][column+1])
        diagnol_list3.append(board[row-2][column+2])
    elif row == 5 and column == 4:#chosen row 6 and column 5
        diagnol_list1.append(board[row][column])
        diagnol_list1.append(board[row-1][column-1])
        diagnol_list1.append(board[row-2][column-2])
        diagnol_list1.append(board[row-3][column-3])
    elif row == 0 and column == 5:#chosen row 1 and column 6
        diagnol_list1.append(board[row][column])
        diagnol_list1.append(board[row+1][column-1])
        diagnol_list1.append(board[row+2][column-2])
        diagnol_list1.append(board[row+3][column-3])
    elif row == 1 and column == 5:#chosen row 2 and column 6
        diagnol_list1.append(board[row][column])
        diagnol_list1.append(board[row-1][column+1])
        diagnol_list1.append(board[row+1][column-1])
        diagnol_list1.append(board[row+2][column-2])
        diagnol_list2.append(board[row][column])
        diagnol_list2.append(board[row+1][column-1])
        diagnol_list2.append(board[row+2][column-2])
        diagnol_list2.append(board[row+3][column-3])
    elif row == 2 and column == 5:#chosen row 3 and column 6
        diagnol_list1.append(board[row][column])
        diagnol_list1.append(board[row-1][column+1])
        diagnol_list1.append(board[row+1][column-1])
        diagnol_list1.append(board[row+2][column-2])
        diagnol_list2.append(board[row][column])
        diagnol_list2.append(board[row+1][column-1])
        diagnol_list2.append(board[row+2][column-2])
        diagnol_list2.append(board[row+3][column-3])
        diagnol_list3.append(board[row][column])
        diagnol_list3.append(board[row+1][column+1])
        diagnol_list3.append(board[row-1][column-1])
        diagnol_list3.append(board[row-2][column-2])
    elif row == 3 and column == 5:#chosen row 4 and column 6
        diagnol_list1.append(board[row][column])
        diagnol_list1.append(board[row-1][column+1])
        diagnol_list1.append(board[row+1][column-1])
        diagnol_list1.append(board[row+2][column-2])
        diagnol_list2.append(board[row][column])
        diagnol_list2.append(board[row+1][column+1])
        diagnol_list2.append(board[row-1][column-1])
        diagnol_list2.append(board[row-2][column-2])
        diagnol_list3.append(board[row][column])
        diagnol_list3.append(board[row-1][column-1])
        diagnol_list3.append(board[row-2][column-2])
        diagnol_list3.append(board[row-3][column-3])
    elif row == 4 and column == 5:#chosen row 5 and column 6
        diagnol_list1.append(board[row][column])
        diagnol_list1.append(board[row+1][column+1])
        diagnol_list1.append(board[row-1][column-1])
        diagnol_list1.append(board[row-2][column-2])
        diagnol_list2.append(board[row][column])
        diagnol_list2.append(board[row-1][column-1])
        diagnol_list2.append(board[row-2][column-2])
        diagnol_list2.append(board[row-3][column-3])
    elif row == 5 and column == 5:#chosen row 6 and column 6
        diagnol_list1.append(board[row][column])
        diagnol_list1.append(board[row-1][column-1])
        diagnol_list1.append(board[row-2][column-2])
        diagnol_list1.append(board[row-3][column-3])
    elif row == 1 and column == 0: #chosen row 2 and column 1
        diagnol_list1.append(board[row][column])
        diagnol_list1.append(board[row+1][column+1])
        diagnol_list1.append(board[row+2][column+2])
        diagnol_list1.append(board[row+3][column+3])
    elif row == 2 and column == 0:#chosen row 3 and column 1
        diagnol_list1.append(board[row][column])
        diagnol_list1.append(board[row+1][column+1])
        diagnol_list1.append(board[row+2][column+2])
        diagnol_list1.append(board[row+3][column+3])
    elif row == 3 and column == 0:#chosen row 4 and column 1
        diagnol_list1.append(board[row][column])
        diagnol_list1.append(board[row-1][column+1])
        diagnol_list1.append(board[row-2][column+2])
        diagnol_list1.append(board[row-3][column+3])
    elif row == 4 and column == 0:#chosen row 5 and column 1
        diagnol_list1.append(board[row][column])
        diagnol_list1.append(board[row-1][column+1])
        diagnol_list1.append(board[row-2][column+2])
        diagnol_list1.append(board[row-3][column+3])
    elif row == 1 and column == 6:#chosen row 2 and column 7
        diagnol_list1.append(board[row][column])
        diagnol_list1.append(board[row+1][column-1])
        diagnol_list1.append(board[row+2][column-2])
        diagnol_list1.append(board[row+3][column-3])
    elif row == 2 and column == 6:#chosen row 3 and column 7
        diagnol_list1.append(board[row][column])
        diagnol_list1.append(board[row+1][column-1])
        diagnol_list1.append(board[row+2][column-2])
        diagnol_list1.append(board[row+3][column-3])
    elif row == 3 and column == 6:#chosen row 4 and column 7
        diagnol_list1.append(board[row][column])
        diagnol_list1.append(board[row-1][column-1])
        diagnol_list1.append(board[row-2][column-2])
        diagnol_list1.append(board[row-3][column-3])
    elif row == 4 and column == 6:#chosen row 5 and column 7
        diagnol_list1.append(board[row][column])
        diagnol_list1.append(board[row-1][column-1])
        diagnol_list1.append(board[row-2][column-2])
        diagnol_list1.append(board[row-3][column-3])
        
    matching_list1 = ['w','w','w','w'] #winning list of all white
    matching_list2 = ['b','b','b','b'] #winning list of blacks
    
    #checks every single diagonal and row and column to see if they match the winning lists
    if row_list[0:4] == matching_list1:
        return True
    elif row_list[0:4] == matching_list2:
        return True
    elif row_list[0+1: 4+1] == matching_list1:
        return True
    elif row_list[0+1: 4+1] == matching_list2:
        return True
    elif row_list[0+2: 4+2] == matching_list1:
        return True
    elif row_list[0+2: 4+2] == matching_list2:
        return True
    elif row_list[0+3: 4+3] == matching_list1:
        return True
    elif row_list[0+3: 4+3] == matching_list2:
        return True
    elif column_list[0:4] == matching_list1:
        return True
    elif column_list[0:4] == matching_list2:
        return True
    elif column_list[0+1: 4+1] == matching_list1:
        return True
    elif column_list[0+1: 4+1] == matching_list2:
        return True
    elif column_list[0+2: 4+2] == matching_list1:
        return True
    elif column_list[0+2: 4+2] == matching_list2:
        return True
    elif diagnol_list1 == matching_list1:
        return True
    elif diagnol_list1 == matching_list2:
        return True
    elif diagnol_list2 == matching_list1:
        return True
    elif diagnol_list2 == matching_list2:
        return True
    elif diagnol_list3 == matching_list1:
        return True
    elif diagnol_list3 == matching_list2:
        return True
    elif diagnol_list4 == matching_list1:
        return True
    elif diagnol_list4 == matching_list2:
        return True
    elif diagnol_list5 == matching_list1:
        return True
    elif diagnol_list5 == matching_list2:
        return True
    elif diagnol_list6 == matching_list1:
        return True
    elif diagnol_list6 == matching_list2:
        return True
    else: #none matched the winning lists
        return False
    
def is_game_over(board): #function for checking if the game is over
    """

    Checks if the game is over

    board: the list of lists created in initialize

    Returns:  The winning color if the game is over, otherwise False, or Draw if the gmae is a draw

    """
    
    i_count = 0 #checks the amount of 0s in the board
    for n in board: #loop for checking the amount of zeros in the board
        for i in n: #loop for checking the amount of zeros in the board
            if i == 0: #checks if the index is 0
                i_count += 1 #adds 1 to the number of zeros
            
    if i_count == 0: #checks if the variable is more than 0
        return "draw" #returns draw
    
    for n,ch in enumerate(board): #loop for checking every index in the board if it wins
        for i,hc in enumerate(ch): #loop for checking every index in the board if it wins
            result = check_disc(board, n, i) #calls the check disc function
            if result == True: #checks if the result is Ture
                if hc == "w": #checks if the winning piece was white
                    return "white" #retunrns white
                elif hc == "b": #checks if the winning piece was black
                    return "black" #returns black
    return False #returns False


def main(): #the main function of the game
    """

    The main function of the game that basically runs the game

    Parameters: None

    Returns:  None, but prints the game

    """
    
    banner = """
       ____ ___  _   _ _   _ _____ ____ _____ _  _   
      / ___/ _ \| \ | | \ | | ____/ ___|_   _| || |  
     | |  | | | |  \| |  \| |  _|| |     | | | || |_ 
     | |__| |_| | |\  | |\  | |__| |___  | | |__   _|
      \____\___/|_| \_|_| \_|_____\____| |_|    |_|  
    """
    intro = """
    Connect Four is a two-player connection game in which the players first choose a color and \
    then take turns dropping one colored disc from the top into a seven-column, six-row vertically suspended grid. \
    The pieces fall straight down, occupying the lowest available space within the column. \
    The objective of the game is to be the first to form a horizontal, vertical, or diagonal line of four of one's own discs. 
    """
    usage = """
        Usage:
            pass:   give up, admit defeat
            exit:   exit the game
            i:      drop a disk into column i
    """
    print(banner)
    print(intro)
    print(usage)
     
    continue_game = 'yes'  # can't use "continue" because it has a special meaning
    while continue_game == 'yes': #loop for running the game while the user wants to
        board = initialize() #creates the board
        
        player_color, alternate_color = choose_color() #calls the color function to get the player's color
        who_is_who = "You are '{:s}' and your opponent is '{:s}'." #color string
        print(who_is_who.format(player_color, alternate_color)) #prints the color string
        
        board_display(board) #displays the board
        
        game_finished = False #boolean variable for checking if the game is finished
        prompt = "{:s}'s turn :> " #the prompt of whose turn it is
        loser = "{:s} gave up! {:s} is the winner!! yay!!!" #string for the loser
        winner = "{:s} wins!" #string for the winner
        draw = "This game ends in a draw."
        while game_finished != True: #loop that runs while the game is not complete
            column_full = True #boolean variable that runs until the column isn't full
            player_column = "" #variable for the player's selected column
            passed = False #boolean variable for checking if the user passed
            exited = False #boolean variable for checking if the user wants to exit
            player1_complete = False #boolean variable for checking if player1 has finished their turn
            change_complete = False #boolean varible for not going to the next player if the game is over
            while column_full == True: #loop that runs until the user selects a free column
                valid_input = False #boolean variable to check if the user entered a valid input
                while valid_input == False: #loop that runs until the user inputs a valid input
                    try: #trys the program
                        player_column = input(prompt.format(player_color)) #prints the prompt and takes the input of the player
                        if player_column.lower() == "exit": #checks if the user wants to exit
                            passed = True #the user chose to exit
                            exited = True #the user chose to exit
                            game_finished = True #the game is finished
                            column_full = False #the column is not full
                            break #exits the loop
                        if player_column.lower() == "pass": #checks if the user wants to pass
                            passed = True #the user wants to pass
                            game_finished = True #the game is finished
                            print(loser.format(player_color, alternate_color)) #prints the loser message
                            column_full = False #the column is not full
                            break #leaves the loop
                        else: #the user does not want to leave or pass
                            player_column = int(player_column) #converts the input into an int
                    except ValueError: #if the user entered an invalid option
                        print("Invalid option") #prints erro
                        print(usage) #prints the instructions
                        column_full = False #the column is not full
                        passed = True #the user did pass
                    else: #the user entered a valid input
                        valid_input = True #the user entered a valid input
                        response = drop_disc(board, player_column, player_color)  #drops the disc                      
                        if response == "full" or response == None: #checks if the column is full or wrong
                            column_full = True #the column is full or wrong
                        else: #the column is not full or wrong
                            column_full = False #the column is not full
                            board_display(board) #displays the baord
                            result = is_game_over(board) #checks if the game is over
                            if result == player_color: #checks if the answer is the same as the player color
                                print(winner.format(player_color)) #prints the winning message
                                change_complete = True #the program will not go to the next player
                            elif result == "draw": #checks if the result is a draw
                                print(draw) #prints the draw message
                            if change_complete == True: #checks if to skip the next person
                                player1_complete = False #skip the next person
                            else: #do not skip the next person
                                player1_complete = True #the player has finished their turn
                    if player1_complete == True: #checks if the player has completed their turn
                        opponent_column_full = True #boolean variable that runs while the columnn is not full
                        while opponent_column_full == True: #loop that runs while the column is full
                            opponent_column = input(prompt.format(alternate_color)) #gets the opponents input
                            opponent_column = int(opponent_column) #converts the opponents input to an int
                            response = drop_disc(board, opponent_column, alternate_color) #drops the disc
                            if response == "full" or response == None: #checks if the response is full or wrong
                                opponent_column_full = True #the column is full or wrong
                            else: #the column is not full or wrong
                                opponent_column_full = False #the column is not full
                                board_display(board) #prints the board
                                result = is_game_over(board) #checks if the game is complete
                                if result == alternate_color: #if the game is won by the opponent
                                    print(winner.format(alternate_color)) #print the winning message
                                elif result == "draw": #checks if the game is a draw
                                    print(draw) #prints the drawing message
                                valid_input = False #the user did not enter a valid input
            if passed == True: #the user passed
                break #exit the loop
            game_finished = True #ends the game
        if exited != True: #the user did not exit the game
            continue_game = input("Would you like to play again? ").lower() #checks if they want to play again
        else: #the user did exit
            continue_game = "" #do not play again
    else: #the user does not want to play
        print("\nThanks for playing! See you again soon!") #prints the exit message
    
if __name__ == "__main__": #checks to see to enter the main function
    main() #calls the main function
