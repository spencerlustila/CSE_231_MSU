##############################################################################
# CSE 231 proj09
#
# Algorithm 
#   Prints a banner and gets the users input
#   Runs the specific user input
#       if 1 then prints a table of cracking info
#       if 2 then prints a table of pattern info
#       if 3 then prints entropy of password
#       if 4 then quits
#   program continuously asks for option until user exits
##############################################################################

from math import log2
from operator import itemgetter
from hashlib import md5
from string import ascii_lowercase, ascii_uppercase, digits, punctuation


def open_file(in_file = "pass.txt"):
    """

    Opens a user selected file

    in_file: The file of the user wants to open

    Returns:  The opened file pointer

    """

    valid_answer = False #boolean variable that controls the loop
    while valid_answer == False: #while loop that runs until a valid answer is given
        try: #tries to find 
            in_file = input('Common passwords file [enter for default]: ')
            if in_file == "":
                in_file = "pass.txt"
            in_file = open(in_file)
        except FileNotFoundError: 
            print('File not found. Try again.')
        else:
            valid_answer = True
    return in_file
            
def check_characters(password, characters):
    """

    Checks if the password has a certain character

    password:   The user's password
    characters: The collection of elements to check if the password has

    Returns:  The True or False

    """

    for i in password: #loop to run through all elements of the password
        if i in characters: #checks if the element is in the characters
            return True #the element is in the characters
    return False #the element is not in the characters


def password_entropy_calculator(password):
    """

    Calculates the entropy of the password

    password: The password the user wants the entropy of

    Returns:  The opened file pointer

    """

    n_var = None #n variable for entropy equation
    #the following returns 0 if the length of the password is 0
    if len(password) == 0: #if statement to check the length
        return 0 #returns 0
    else:
        n_var = 94 #sets the n variable
    #the following sets the n variable if the password contains only numbers
    only_numbers = False #boolean variable for checking if the password has only numbers
    false = False
    for i in password: #loop for checking every element in password
        if i in digits: #checks if the i is a number
            only_numbers = True #sets the boolean variable
        else:
            only_numbers = False #sets the boolean variable
            false = True
        if false == True:
            only_numbers = False
    if only_numbers == True: #checks if the password only contains numbers
        n_var = 10 #sets the n variable
        l_var = len(password) #finds the length
        entropy = l_var * log2(n_var) #calculates the entropy
        entropy = round(entropy, 2) #rounds the entropy
        return entropy #returns the entropy
    #the following sets the n variable if the password contains only special characters
    only_special_characters = None #boolean variable for checking if the password has only special characters
    false = False
    for i in password: #loop for checking every element in the password
        if i in punctuation: #checks if the i is a special character
            only_special_characters = True #sets the boolean variable
        else: #the i is not a punctuation
            only_special_characters = False #sets the boolean variable
            false = True
        if false == True:
            only_special_characters = False
    if only_special_characters == True: #checks if the password only contains special characters
        n_var = 32 #sets the n varbale
        l_var = len(password) #finds the length
        entropy = l_var * log2(n_var) #calculates the entropy
        entropy = round(entropy, 2) #rounds the entropy
        return entropy #returns the entropy
    #the following sets the n variable if the password does not contain any letters
    only_num_special_char = None #boolean variable for checking if the password only contains numbers and special characters
    if check_characters(password, ascii_lowercase) == True or check_characters(password, ascii_uppercase): #calls the previous \
    #function to check if the password contains any letters
        only_num_special_char = False #sets the boolean variable
    else: #the password did not contain any letters
        only_num_special_char = True #sets the boolean variable
    if only_num_special_char == True: #checks if the password contained any letters
        n_var = 42 #sets the n variable
        l_var = len(password) #finds the length
        entropy = l_var * log2(n_var) #calculates the entropy
        entropy = round(entropy, 2) #rounds the entropy
        return entropy #returns the entropy
    #the following sets the n variable if the password contains only lowers
    only_lower = None #boolean variable for checking if the password contains only lowers
    if check_characters(password, ascii_uppercase) == True: #checks if the password contains uppers
        only_lower = False #sets the boolean variable
    elif check_characters(password, digits) == True: #checks if the password contains numbers
        only_lower = False #sets the boolean variable
    elif check_characters(password, punctuation) == True: #checks if the password contains punctuation
        only_lower = False #sets the boolean variable
    else: #the password contains only lowers
        only_lower = True #sets the boolean variable
    if only_lower == True: #checks if the password only contained lowers
        n_var = 26 #sets the n variable
        l_var = len(password) #finds the length
        entropy = l_var * log2(n_var) #calculates the entropy
        entropy = round(entropy, 2) #rounds the entropy
        return entropy #returns the entropy
    #the following sets the n variable if the password contains only uppers
    only_upper = None #boolean variable for checking if the password contains only uppers
    if check_characters(password, ascii_lowercase) == True: #checks if the password contains lowers
        only_upper = False #sets the boolean variable
    elif check_characters(password, digits) == True: #checks if the password contains numbers
        only_upper = False #sets the boolean variable
    elif check_characters(password, punctuation) == True: #checks if the password contains punctuation
        only_upper = False #sets the boolean variable
    else: #the password contains only uppers
        only_upper = True #sets the boolean variable
    if only_upper == True: #checks if the password only contained uppers
        n_var = 26 #sets the n variable
        l_var = len(password) #finds the length
        entropy = l_var * log2(n_var) #calculates the entropy
        entropy = round(entropy, 2) #rounds the entropy
        return entropy #returns the entropy
    #the following sets the n variable if the password contains only letters
    only_letters = None #boolean variable for checking if the password contains only numbers
    if check_characters(password, digits) == True: #checks if the password contains numbers
        only_letters = False #sets the boolean variable
    elif check_characters(password, punctuation) == True: #checks if the password contains punctuation
        only_letters = False #sets the boolean variable
    else: #the password contains only letters
        only_letters = True #sets the boolean variable
    if only_letters == True: #checks if the password only contained letters
        n_var = 52 #sets the n variable
        l_var = len(password) #finds the length
        entropy = l_var * log2(n_var) #calculates the entropy
        entropy = round(entropy, 2) #rounds the entropy
        return entropy #returns the entropy
    #the following sets the n variable if the password contains only numbers and lowers
    only_num_lower = None #boolean variable for checking if the password contains only numbers and lowers
    if check_characters(password, ascii_uppercase) == True: #checks if the password contains uppers
        only_num_lower = False #sets the boolean variable
    elif check_characters(password, punctuation) == True: #checks if the password contains punctuation
        only_num_lower = False #sets the boolean variable
    else: #the password contains only letters
        only_num_lower = True #sets the boolean variable
    if only_num_lower == True: #checks if the password only contained numbers and lowers
        n_var = 36 #sets the n variable
        l_var = len(password) #finds the length
        entropy = l_var * log2(n_var) #calculates the entropy
        entropy = round(entropy, 2) #rounds the entropy
        return entropy #returns the entropy
    #the following sets the n variable if the password contains only numbers and uppers
    only_num_upper = None #boolean variable for checking if the password contains only numbers and uppers
    if check_characters(password, ascii_lowercase) == True: #checks if the password contains lowers
        only_num_upper = False #sets the boolean variable
    elif check_characters(password, punctuation) == True: #checks if the password contains punctuation
        only_num_upper = False #sets the boolean variable
    else: #the password contains only letters
        only_num_upper = True #sets the boolean variable
    if only_num_upper == True: #checks if the password only contained numbers and uppers
        n_var = 36 #sets the n variable
        l_var = len(password) #finds the length
        entropy = l_var * log2(n_var) #calculates the entropy
        entropy = round(entropy, 2) #rounds the entropy
        return entropy #returns the entropy
    #the following sets the n variable if the password contains only special characters and uppers
    only_special_upper = None #boolean variable for checking if the password contains only special characters and uppers
    if check_characters(password, ascii_lowercase) == True: #checks if the password contains lowers
        only_special_upper = False #sets the boolean variable
    elif check_characters(password, digits) == True: #checks if the password contains numbers
        only_special_upper = False #sets the boolean variable
    else: #the password contains only special characters and uppers
        only_special_upper = True #sets the boolean variable
    if only_special_upper == True: #checks if the password only contained special characters and uppers
        n_var = 58 #sets the n variable
        l_var = len(password) #finds the length
        entropy = l_var * log2(n_var) #calculates the entropy
        entropy = round(entropy, 2) #rounds the entropy
        return entropy #returns the entropy
    #the following sets the n variable if the password contains only special characters and lowers
    only_special_lowers = None #boolean variable for checking if the password contains only special characters and lowers
    if check_characters(password, ascii_uppercase) == True: #checks if the password contains uppers
        only_special_lowers = False #sets the boolean variable
    elif check_characters(password, digits) == True: #checks if the password contains numbers
        only_special_lowers = False #sets the boolean variable
    else: #the password contains only special characters and uppers
        only_special_lowers = True #sets the boolean variable
    if only_special_lowers == True: #checks if the password only contained special characters and lowers
        n_var = 58 #sets the n variable
        l_var = len(password) #finds the length
        entropy = l_var * log2(n_var) #calculates the entropy
        entropy = round(entropy, 2) #rounds the entropy
        return entropy #returns the entropy
    #the following sets the n variable if the password contains no uppers
    not_uppers = None #boolean variable for checking if the password contains no uppers
    if check_characters(password, ascii_uppercase) == True: #checks if the password contains uppers
        not_uppers = False #sets the boolean variable
    else: #the password contains no uppers
        not_uppers = True #sets the boolean variable
    if not_uppers == True: #checks if the password only contained no uppers
        n_var = 68 #sets the n variable
        l_var = len(password) #finds the length
        entropy = l_var * log2(n_var) #calculates the entropy
        entropy = round(entropy, 2) #rounds the entropy
        return entropy #returns the entropy
    #the following sets the n variable if the password contains no lowers
    not_lowers = None #boolean variable for checking if the password contains no lowers
    if check_characters(password, ascii_lowercase) == True: #checks if the password contains lowers
        not_lowers = False #sets the boolean variable
    else: #the password contains no lowers
        not_lowers = True #sets the boolean variable
    if not_lowers == True: #checks if the password only contained no lowers
        n_var = 68 #sets the n variable
        l_var = len(password) #finds the length
        entropy = l_var * log2(n_var) #calculates the entropy
        entropy = round(entropy, 2) #rounds the entropy
        return entropy #returns the entropy
    #the following sets the n variable if the password contains no special characters
    not_special = None #boolean variable for checking if the password contains no special characters
    if check_characters(password, punctuation): #checks if the password contains special characters
        not_special = False #sets the boolean variable
    else: #the password contains no special characters
        not_special = True #sets the boolean variable
    if not_special == True: #checks if the password only contained no special characters
        n_var = 62 #sets the n variable
        l_var = len(password) #finds the length
        entropy = l_var * log2(n_var) #calculates the entropy
        entropy = round(entropy, 2) #rounds the entropy
        return entropy #returns the entropy
    #the following sets the n variable if the password contains no digits
    not_digits = None #boolean variable for checking if the password contains no digits
    if check_characters(password, digits): #checks if the password contains digits
        not_digits = False #sets the boolean variable
    else: #the password contains no digits
        not_digits = True #sets the boolean variable
    if not_digits == True: #checks if the password only contained no digits
        n_var = 84 #sets the n variable
        l_var = len(password) #finds the length
        entropy = l_var * log2(n_var) #calculates the entropy
        entropy = round(entropy, 2) #rounds the entropy
        return entropy #returns the entropy

    l_var = len(password) #finds the length
    entropy = l_var * log2(n_var) #calculates the entropy
    entropy = round(entropy, 2) #rounds the entropy
    return entropy #returns the entropy

def build_password_dictionary(fp):
    """

    Builds a dictionary for the file

    fp: The file opened in open_file

    Returns:  The dictionary for the file

    """

    pass_dict = dict() #variable for the dictionary
    for i,line in enumerate(fp): #loop for running through every line of the file
        hash_code = md5((line.strip()).encode()).hexdigest() #finds the hash code
        pass_tup = (line.strip(), i+1, password_entropy_calculator(line.strip())) #builds the tuple
        pass_dict[hash_code] = pass_tup #adds the new item to the dictionary
        
    return pass_dict #returns the dictionary

def cracking(fp,hash_D):
    """

    Checks if the dictionary is cracked

    fp:     The file of hash and hex codes
    hash_D: The dictionary returned in build_password_dictionary

    Returns:  A list of tuples, the cracked count, and the uncracked count

    """

    list_of_tuples = [] #list of tuuples
    cracked_count = 0 #number of cracked codes
    uncracked_count = 0 #number of uncracked codes
    for line in fp: #loop that runs through every line of the file
        hash_code = "" #variable that stores the hash code
        colon = False #variable for checking if the colon is there
        for i in line: #loop that runs through every element in the line
            if i == ":": #checks if the element is a colon
                colon = True #variable for checking if the colon is there
            elif i != ":" and colon == False: #makes sure that the element is before the colon
                hash_code += i #adds the element to the hash code
        if hash_D.get(hash_code) == None: #checks if the hash code is in the dict
            uncracked_count += 1 #it wasn't so it adds to the uncracked 
        else: #it was 
            cracked_count += 1 #adds to cracked
            value = hash_D.get(hash_code) #finds the value
            tup = (hash_code, value[0], value[2]) #adds to the tuple
            list_of_tuples.append(tup) #appends to the list
    list_of_tuples = sorted(list_of_tuples, key=lambda elem: elem[1]) #sorts the list
    return(list_of_tuples, cracked_count, uncracked_count) #returns the list, and counts

def create_set(fp):  
    """

    Creates a set from a file pointer

    fp: The file full of the words for the set

    Returns:  A set made up of words from the file

    """

    word_set = set() #variable for the set
    for line in fp: #loop for reading every line in the file
        word_set.add(line.strip()) #adds the word to the set
        
    return word_set #returns the set

def common_patterns(D,common,names,phrases):
    """

    Creates a dictionary of patterns

    D:       dictionary in build_password_dictionary
    common:  set of phrases
    names:   set of phrases
    phrases: set of phrases

    Returns:  The dictionary of patterns

    """

    pattern_dict = dict() #dictionary of patterns
    list_of_values = [] #list that contains the values of D
    for key, values in D.items(): #loop that runs through all the items in D
        list_of_values.append(values[0]) #appends the value to the list
    for n in list_of_values: #runs through all the values in the list
        listt = [] #list for the passwords
        for i in common: #loop that runs through the phrases in the set
            if i.lower() in n: #checks if the word is the value
                if i.lower() in listt: #checks if the word is in the list
                    pass #passes
                else: #the word is not in the list
                    listt.append(i.lower()) #adds the word to the list
        for i in names: #loop that runs through the phrases in the set
            if i.lower() in n: #checks if the word is the value
                if i.lower() in listt: #checks if the word is in the list
                    pass #passes
                else: #the word is not in the list
                    listt.append(i.lower()) #adds the word to the list
        for i in phrases: #loop that runs through the phrases in the set
            if i.lower() in n: #checks if the word is the value
                if i.lower() in listt: #checks if the word is in the list
                    pass #passes
                else: #the word is not in the list
                    listt.append(i.lower()) #adds the word to the list
        listt = sorted(listt) #sorts the list
        pattern_dict[n] = listt #adds the key and value to the new dictionary
        
    return pattern_dict #returns the dictionary
                
def main():
    """

    Main function that calls the other functions

    Parameters: NONE

    Returns:  None, but prints prompts

    """
    
    BANNER = """
       -Password Analysis-

          ____
         , =, ( _________
         | ='  (VvvVvV--'
         |____(


    https://security.cse.msu.edu/
    """

    MENU = '''
    [ 1 ] Crack MD5 password hashes
    [ 2 ] Locate common patterns
    [ 3 ] Calculate entropy of a password
    [ 4 ] Exit

    [ ? ] Enter choice: '''


    print(BANNER) #prints the above banner
    valid_choice = False #boolean variable for while loop
    choice = None #creates the choice variable outside the while loop
    while valid_choice == False: #loop for getting a valid menu option
        choice = input(MENU) #gets menu option
        if int(choice) >= 1 and int(choice) <= 4: #checks menu option
            valid_choice = True #menu option was valid
        else: #menu option was invalid
            print('Error. Try again.') #prints error
            valid_choice = False #boolean variable for while loop
    while choice != "4": #loop for running program until user exits
        if choice == "1": #user chose 1
            in_file = open_file() #opens file
            hash_file = input('Hashes file: ') #gets the hashes file
            hash_file = open(hash_file) #opens the hashes file
            print("\nCracked Passwords:") #prints table title
            hash_D = build_password_dictionary(in_file) #builds the dictionary
            list_of_tuples, cracked_count, uncracked_count = cracking(hash_file, hash_D) #gets the cracking info
            for i in list_of_tuples: #loop for printing table
                print('[ + ] {:<12s} {:<34s} {:<14s} {:.2f}'.format("crack3d!", i[0], i[1], i[2])) #prints rows until end
            print('[ i ] stats: cracked {:,d}; uncracked {:,d}'.format(cracked_count, uncracked_count)) #prints totals
        elif choice == "2": #user chose 2
            in_file = open_file() #opens file
            hash_D = build_password_dictionary(in_file) #buils dictionary
            commons = input('Common English Words file: ') #gets commons file
            common = open(commons) #opens commons file
            common_s = set() #commons set variable
            for line in common: #loop for filling commons set
                common_s.add(line.strip()) #adds element to commons set
            name = input('First names file: ') #gets name file
            names = open(name) #opens name file
            names_s = set() #name set variable
            for line in names: #loop for filling name set
                names_s.add(line.strip()) #adds element to name set
            phrase = input('Phrases file: ') #gets phrase file
            phrases = open(phrase) #opens phrase file
            phrases_s = set() #phrase set variable
            for line in phrases: #loop for filling phrase set
                phrases_s.add(line.strip()) #adds element to phrase set
            D_patterns = common_patterns(hash_D,common_s,names_s,phrases_s) #gets the patterns dict
            print("Password             Patterns") #prints table title
            for k,v in D_patterns.items(): #loop for printing table info
                 print("{:20s} [".format(k),end='')# print password 
                 print(', '.join(v),end=']\n') # print comma separated list
        elif choice == "3": #user chose 3
            password = input('Enter the password: ') #gets the password from user
            entropy = password_entropy_calculator(password) #calls function to get entropy
            print('The entropy of {} is {}'.format(password, entropy)) #prints results
        valid_choice = False #boolean variable for while loop
        choice = None #creates the choice variable outside the while loop
        while valid_choice == False: #loop for getting a valid menu option
            choice = input(MENU) #gets menu option
            if int(choice) >= 1 and int(choice) <= 4: #checks menu option
                valid_choice = True #menu option was valid
            else: #menu option was invalid
                print('Error. Try again.') #prints error
                valid_choice = False #boolean variable for while loop
    
    
    
    
    
if __name__ == '__main__':
    main()