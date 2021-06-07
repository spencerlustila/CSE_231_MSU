##############################################################################
# CSE 231 proj06
#
# Algorithm 
#   Asks the user for 2 CSV file names
#       If the input is invalid, the program will ask until a valid one is\
#           given
#   Asks the user for how they would like to sort the table to display
#       Sorts the data based on the user chosen number
#       Displays the table
#   Asks the user if they would like to plot the journal data
#       If the answer is invalid, the program will ask until a valid one is\
#           given
#       If the answer is yes, the data is sorted, then displayed in bar graph
#       If the answer is no, the program ends
##############################################################################

from operator import itemgetter
import csv
import pylab as py

def open_file(): #function for opening a file
    """

    Checks which file the user wishes to open

    Parameters: NONE

    Returns:  The file the user wishes to open

    """
    
    valid_file = False #boolean variable telling the loop the user entered a valid name
    while valid_file == False: #loop for checking if the user entered a valid filename
        try: #tries to see if the user inputs a valid file name
            file_name = input("Please enter a valid filename: ") #takes the users input
            file_pointer = open(file_name, "r") #tries to open the file
            return file_pointer
        except FileNotFoundError: #the user inputted an invalid file name
            print("Error opening the file. ", end = "") #prints the error statement
        else: #the except was not triggered
            valid_file = True #the user inputted a valid option
    return file_pointer #returns the file name

def read_journal_file(fp): #function for finding information in a journal file
    """

    Creates a list of tuples that contains information regarding a journal file

    fp:  The file pointer that was returned in open_file

    Returns:  A list of tuples that contains information regarding a journal file

    """
    
    list_of_tuples = [] #varibale for list of tuples
    reader = csv.reader(fp) # create csv reader
    head = 0 #header counter variable
    while head < 2: #while loop to skip the headers
        next(reader,None) # read one line (useful for skip)
        head += 1 #adds 1 to the header counter
    for line_list in reader: #line_list is a list of the line
        name = line_list[0][:30] #assigns name to the first 30 characters of the first index
        total_cites = int(line_list[1].replace(",","")) #assigns total cites to the first \
        #index and takes out the commas, and makes it an int
        try:
            journal_impact = float(line_list[2]) #assigns the journal impact to second index and \
            #makes it a float
        except ValueError: #the CSV has a invalid type
            continue #forgets about it and continues to run the function
        journal_info_tuple = (name, total_cites, journal_impact) #creates a tuple of the found \
        #information
        list_of_tuples.append(journal_info_tuple) #appends the tuple to the list
    list_of_tuples = sorted(list_of_tuples, key = itemgetter(2), reverse = True) #sorts the list \
    #by the 2nd index, and reverses the order
    return(list_of_tuples) #returns the sorted list of tuples

def read_category_file(fp): #function for finding information in a category file
    """

    Creates a list of tuples that contains information regarding a category file

    fp:  The file pointer that was returned in open_file

    Returns:  A list of tuples that contains information regarding a category file

    """
    
    list_of_tuples = [] #varibale for list of tuples
    reader = csv.reader(fp) # create csv reader
    head = 0 #header counter variable
    while head < 2: #while loop to skip the headers
        next(reader,None) # read one line (useful for skip)
        head += 1 #adds 1 to the header counter
    for line_list in reader: #line_list is a list of the line
        name = line_list[0][:30] #assigns name to the first 30 characters of the first index
        total_cites = int(line_list[3].replace(",","")) #assigns total cites to the third \
        #index and takes out the commas, and makes it an int
        num_journals = int(line_list[2]) #assigns the journal impact to third index and \
        #makes it a int
        avg = total_cites/num_journals #average citations per journal
        category_info_tuple = (name, num_journals, total_cites, avg) #creates a tuple of the found \
        #information
        list_of_tuples.append(category_info_tuple) #appends the tuple to the list
    list_of_tuples = sorted(list_of_tuples, key = itemgetter(0), reverse = False) #sorts the list \
    #by the first index
    return(list_of_tuples) #returns the sorted list of tuples

def display_table(data): #function for printing the table of the data
    """

    Prints the first 20 elements of the sorted data

    data:  The user inputted sorted data

    Returns:  NONE, but prints a formatted table

    """
    
    total_journals = 0 #total number of journals
    total_cite = 0 #total number of citations
    total_avg = 0 #total citations per journal
    print("{:23s}{}{:23s}".format(" ", "Citation Data of the Top 20 Categories ", " ")) #prints the table title
    print("{:30s}{:>12s}{:>18s}{:>25s}".format('Category','Journals','Total Citations','Citation per Journal')) #prints \
    #the table header
    i = 0 #counter variable
    while i < 20: #while loop for printing the first 20 tuples
        print("{:30s}{:>12,d}{:>18,d}{:>25,.3f}".format(data[i][0],data[i][1],data[i][2],data[i][3])) #prints the formatted \
        #tuple information
        total_journals += data[i][1] #adds the journal number to the total journal number
        total_cite += data[i][2] #adds the citation number to the total citation number
        total_avg += data[i][3] #adds the citation per journal number to the total citation per journal number
        i += 1 #adds one to the counter
    print(85*"-") #prints the 85 dashes
    print("{:30s}{:>12,d}{:>18,d}{:>25,.3f}".format("TOTAL",total_journals,total_cite,total_avg)) #prints the formatted \
    #total information
    
def sort_data(data, column): #function for sorting the list of tuples
    """

    Sorts the list of tuples according to the user requested column

    data:    The list of tuples the user wants to sort
    Column:  The column that the user wants to sort the list by

    Returns:  The sorted list

    """
    
    boolean_val = False #boolean variable to reverse the list
    if column == 0: #the user has chosen to sort by the first column
        boolean_val = False #the list will be sorted alphabetically
    else: #the user did not choose the first column
        boolean_val = True #the list will be sorted in the reverse order
    sorted_data = sorted(data,key = itemgetter(column), reverse = boolean_val) #sorts the list by the user \
    #defined column    
    return sorted_data #returns the sorted list

def prepare_plot_data(data): #function for preparing the journal data for graphing
    """

    Sorts the data, and finds the 10 highest impacts and its respective name

    data:  The user inputted journal name

    Returns:  The 10 highest impacts and its respective name

    """
    
    names_list = [] #list of higest impact names
    impact_factor_list = [] #list of the highest impacts
    sorted_data = sort_data(data, 2) #calls the sort function and sorts the journal data \
    #by the second index
    i = 0 #counter variable for loop
    while i < 10: #loop for collecting the highest impact data
        names_list.append(sorted_data[i][0]) #appends the highest impact data to the outer list
        impact_factor_list.append(sorted_data[i][2]) #appends the highest impact to the outer list
        i += 1 #adds one to the counter
    return names_list, impact_factor_list #returns the highest impact names, and the highest impacts

def plot_data(name,impact_factor): #fucntion for plotting the data
    '''
        Plots the bar chart of the Journal Impact Factor
        
        Input:
            data (list) -> List of journals and their impact factor
            
        Returns:
            None
    '''
    
    
    py.barh(name,impact_factor)

    py.title("Journal Impact Factor")
    py.xlabel('Impact Factor')
    py.ylabel('Journal Name')
    
    # To pass the Mimir plot test you must uncomment the 'savefig' line and comment out the 'show' line
    py.savefig("plot.png")
    #py.show()
    

def main(): #function that calls all the other functions
    """

    The main function of the program, that calls all the other functions

    Parameters: NONE

    Returns:  NONE, but prints the questions necessary for calling all the functions

    """
    
    file_pointer_category = open_file() #calls the open file function to open the first file
    file_pointer_journal = open_file() #calls the open file function to open the second file
    
    column = "" #creates the column variable
    valid_column = False #variable for telling the loop if the user entered a valid column number
    while valid_column == False: #loop that runs while the user has not inputted a valid number
        column = input("Column number to sort data (1-category, 2-journals, 3-citations, 4-average citations): ") #prompt \
        #for getting the column number from the user
        if (column == "1"): #the user has inputted the number 1
            column = 0 #converts the number to the one required for the functions
            valid_column = True #the user has entered a valid number
        elif (column == "2"): #the user has inputted the number 2
            column = 1 #converts the number to the one required for the functions
            valid_column = True #the user has entered a valid number
        elif (column == "3"): #the user has inputted the number 3
            column = 2 #converts the number to the one required for the functions
            valid_column = True #the user has entered a valid number
        elif (column == "4"): #the user has inputted the number 4
            column = 3 #converts the number ot the one required for the functions
            valid_column = True #the user has entered a valid number
        else: #the user has not entered one of the options
            print("Incorrect column number. Try Again!") #prints error message
            valid_column = False #the user has entered an invalid number
    print() #adds a line between the prompt and the table
    category = read_category_file(file_pointer_category) #calls the read category file to sort the file
    data_sorted = sort_data(category, int(column)) #sorts the data for the table
    display_table(data_sorted) #calls the display data function to print the table
    
    plot_input = False #boolean variable for checking if the user inputted a valid option
    plot_bool = False #boolean variable for checking if the user wants to graph
    choice = "" #variable for the users choice
    while plot_input == False: #loop that runs as long as the user has not entered a valid option
        choice = input("Do you want to plot the journal data (yes/no)? ") #prints the prompt
        if choice.lower() == "yes": #the user wants to graph
            plot_bool = True #sets the graphing variable to true
            plot_input = True #sets the correct input variable to true
        elif choice.lower() == "no": #the user does not want to graph
            plot_bool = False #sets the graphing variable to false
            plot_input = True #sets the correct input variable to true
        else: #the user has not entered on of the options
            print("Incorrect answer! Enter yes/no") #prints error
            plot_input = False #sets the correct input variable to false
    if plot_bool == True: #checks if the user wants to graph
        data = read_journal_file(file_pointer_journal) #calls the read journal file function to sort the file
        names_list, impact_factor_list = prepare_plot_data(data) #calls the prepare plot data fucntion to \
        #find the information for the graph
        plot_data(names_list,impact_factor_list) #calls the plot function to graph the bar graph

if __name__ == "__main__": #checks to see to enter the main function
    main() #calls the main function