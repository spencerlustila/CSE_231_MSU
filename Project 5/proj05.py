##############################################################################
# CSE 231 proj05
#
# Algorithm 
#   Calls a function to ask the user for a file name
#       If the user inputs an invalid file name and error prints
#       The user is asked again until they provide a valid file name
#   Runs a for loop to find out the Gender and Political Affiliation\
#       of each person in the file
#   Inputs the Gender and Political affiliation numbers into function and \
#       the function prints the numbers
#   Asks if the user wants to plot the information in a bar graph
#       If the response is Yes, a bar graph gets printed
##############################################################################

#Retain these import statements which serve the plot function. 
import matplotlib.pyplot as plt
plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt

def open_file(): #function for opening a file
    """

    Checks which file the user wishes to open

    Parameters: NONE

    Returns:  The file the user wishes to open

    """
    valid_file = False #boolean variable telling the loop the user entered a valid name
    while valid_file == False: #loop for checking if the user entered a valid filename
        try: #tries to see if the user inputs a valid file name
            file_name = input("Input a file name: ") #takes the users input
            in_file = open(file_name,"r") #tries to open the file
            return in_file
        except FileNotFoundError: #the user inputted an invalid file name
            print("File not found.") #prints the error statement
        else: #the except was not triggered
            valid_file = True #the user inputted a valid option
    return in_file #returns the file name

def get_gender(data_line): #function for finding the gender of a person
    """

    Checks the gender of the user submitted line

    data_line: the user submitted line of the file

    Returns:  The gender of the person on the submitted line

    """
    gender = data_line[39:].strip() #reads the gender of the person
    return gender #returns the gender

def is_mike(data_line): #function for checking if the person is named Mike or Michael
    """

    Checks if the persons name is Mike or Michael

    data_line: the user submitted line of the file

    Returns:  True or False depending on if the persons name is Mike or Michael

    """
    for i,ch in enumerate(data_line): #for loop for reading all characters in line
        if ch == ",": #checks to see when the first comma is
            if (data_line[i+1:30].strip()) == "Mike" or (data_line[i+2:30].strip()) == "Michael": #checks \
            #if the first name is Mike or Michael
                return True #the users name was Mike or Michael
            else: #the name is not Mike
                return False #returns false

def get_party(data_line): #function for checking the politcal party of the person
    """

    Checks the party of the person

    data_line: the user submitted line of the file

    Returns:  The political party of the person

    """
    if data_line[30].lower() == "d": #the persons party is Democrat
        return "Democrat" #returns the users party
    if data_line[30].lower() == "r": #the persons party is Republican
        return "Republican" #returns the users party

def print_result(c_rm, c_rf, c_dm, c_df, c_m): #function for printing the results of the people in the file
    """

    Prints the results of the people in the file

    c_rm: the number of male Republicans
    c_rf: the number of female Republicans
    c_dm: the number of male Democrats
    c_df: the number of female Democrats
    c_m:  the number of Mikes or Michaels

    Returns:  NONE, but prints the results of the people in the file

    """
    print("{:<10s}{:>14s}{:>14s}".format("Party","Republican","Democrat")) #prints the \
    #header for the results
    print("{:<10s}{:>14d}{:>14d}".format("Male",c_rm, c_dm)) #prints the number of male \
    #Republicans and Democrats
    print("{:<10s}{:>14d}{:>14d}".format("Female",c_rf, c_df)) #prints the number of \
    #female Republicans and Democrats
    print() #prints an empty line
    print("Dudes named Mike: {:<14d}".format(c_m)) #prints the number of Mikes or Michaels

def plot_data(c_rm, c_rf, c_dm, c_df, c_m):
    '''
    Plot a figure with provided data. This function is completed and only for fun :)
    Input: 
    c_rm, c_rf, c_dm, c_df, c_m: integers indicate number of Repub_male, 
    Repub_female, Demo_male, Demo_female and dudes named 'Mike'.
    Return: No Return.
    '''
    ylabels = ("Dudes named Mike","Republican_Female", "Republican_Male", "Democratic_Female", \
               "Democratic_Male")
#    ylabels = ("Republican_Male", "Republican_Female", "Democratic_Male", "Democratic_Female", \
    #"Dudes named Mike")
    ypos = np.arange(len(ylabels))
    count = np.array([c_m, c_rf, c_rm, c_df, c_dm,])
#    count = np.array([c_rm, c_rf, c_dm, c_df, c_m])
    plt.barh(ypos, count, align = 'center', alpha = 0.4)
    plt.yticks(ypos, ylabels)
    plt.xlabel('Count')
    plt.title("How many female representatives in congress this year?")
    plt.savefig("plot.png")


def main(): #the main function of the program
    """

    The main function of the program, that calls all the other functions

    Parameters: NONE

    Returns:  NONE, but prints the question to ask the user if they want to graph the results

    """
    c_m = 0 #variable for number of Mikes and Michaels
    c_dm = 0 #variable for number of Democractic Males
    c_df = 0 #Variable for number of Democratic Females
    c_rm = 0 #Variable for number of Republican Males
    c_rf = 0 #Variable for number of Republican Females
    in_file_obj = open_file() #calls the open_file function and stores the returned file name
    for line in in_file_obj: #for loop for reading every line of the file
        if get_party(line) == "Democrat" and get_gender(line) == "male": #checks the person \
        #is a Democratic male
            c_dm += 1 #adds 1 to the number of Democratic Males
        if get_party(line) == "Democrat" and get_gender(line) == "female": #checks if the \
        #person is a Democractic Female
            c_df += 1 #adds 1 to the number of Democractic Females
        if get_party(line) == "Republican" and get_gender(line) == "male": #checks if the \
        #person is a Republican Male
            c_rm += 1 #adds 1 to the number of Republican Males
        if get_party(line) == "Republican" and get_gender(line) == "female": #checks if the \
        #person is a Republican Female
            c_rf += 1 #adds 1 to the number of Republican Females
        if is_mike(line) == True: #calls the is_mike function, and checks if the returned \
        #value is True
            c_m += 1 #adds 1 to the number of Mikes and Michaels
            
    print_result(c_rm, c_rf, c_dm, c_df, c_m) #calls the print_result function to print the results
    
    ask = input("Do you want to plot? ") #asks the user if they want to plot a bar graph
    if ask.lower() == "yes": #checks if the user's response is yes
        plot_data(c_rm, c_rf, c_dm, c_df, c_m) #calls the plot_data function and plots the graph
            
if __name__ == '__main__': #checks if the two strings are the same
    main() #calls the main function