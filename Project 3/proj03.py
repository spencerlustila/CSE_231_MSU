################################################################
# CSE 231 proj03
#
# Algorithm 
#   Print the Prompt
#   Ask difficulty of the game
#   Generate Random string
#   Print out the Random string
#   Check if the user inputted string matches the original
#   If it matches tell user
#   If it does not match tell user
#   Print Time taken, and number correct
#   Print Total Number correct
#   Print Reward
################################################################

import string, time
from cse231_random import randint

#Symbolic Constants
ALPHABET_EASY = string.ascii_letters 
ALPHABET = string.ascii_letters + string.punctuation
LEVEL_PROMPT = '''
Please choose the difficulty level:
    E(e) for Easy;
    M(m) for Medium;
    H(h) for Hard;
    Hit "Enter" for Default;
    Q(q) to quit;

Level: '''
DIFFICULTY_ERROR = "Difficulty level not recognized."
EASY_TIME_INTERVAL_INT = 10
MEDIUM_TIME_INTERVAL_INT = 9
HARD_TIME_INTERVAL_INT = 8
TIME_ERROR = "Oops! Too much time."

# prompt for a level (before your while loop)
level_str = input(LEVEL_PROMPT) #asks user for level difficulty
total_denominator = 0 #denominator of the final total
total_level_num = 0 #total amount of levels run in the program
reward = 0 #reward for completing the game
checker_bool = True #variable for telling if all the answers were correct
entered_bool = False #variable for telling if the user inputted a valid option
while (level_str != "q"): #will run the game until the user quits
    if (level_str == ""): #user set difficulty to default
        level_str = "e" #default difficulty is Easy
    if (level_str == "e") or (level_str == "E"): #if the user set difficulty to easy
        entered_bool = True #the user entered a valid option
        level_num_int = 1 #sets the first level to 1
        inputted_word_str = "" #variable for user inputted answer
        inputted_word_lower_str = "" #variable for user inputted answer after making it lowercase
        total_time = 0 #time taken to complete entire level
        while level_num_int <= 10: #loop that runs the level for 10 levels
            random_str = "" #variable for the randomly generated string
            length = randint(3, 5) #boundaries for the length of the generated string
            for i in range(length): #loop that generates the random string
                index = randint(0, len(ALPHABET_EASY)-1) #picks a random letter index in the ALPHABET_EASY constant
                random_str += ALPHABET_EASY[index]  #adds the letters to form a string
            print("Level [{}], game [{}]/[10]".format(level_str.capitalize(),level_num_int)) #print level header
            print("\nEnter this string:", random_str) #print generated string
            start = time.time() #starts the stopwatch
            inputted_word_str = input() #takes the users inputted word
            end = time.time() #stops the stopwatch
            inputted_word_lower_str = inputted_word_str.replace(" ", "") #removes the spaces in the user inputted word
            inputted_word_lower_str  = inputted_word_lower_str.lower() #makes the user inputted word lowercase
            time_flt = (end - start) #calculates the time taken to input the answer
            total_time += time_flt #adds the time taken to the total time taken
            if inputted_word_lower_str == random_str.lower() and time_flt < EASY_TIME_INTERVAL_INT: #the \
            #inputted word is correct and the word was inputted in the time limit
                print("Good job!", "You spent {:4.1f} of {} seconds entering string [{}][{}]"\
                      .format(time_flt, EASY_TIME_INTERVAL_INT, inputted_word_str, random_str)) #answer correct message
                print() #prints new line 
                level_num_int += 1 #increases the level by 1
                reward += (1*len(random_str)) #calculates the reward and adds it
            if time_flt > EASY_TIME_INTERVAL_INT: #if the user exceeds the time limit
                print(TIME_ERROR, "Result of this game is {}/{}".format(level_num_int-1, 10)) #prints error and \
                #ends the game
                total_denominator += 10 #adds 10 to the total denominator
                checker_bool = False #the answer was wrong
                total_level_num += level_num_int-1 #adds the level number to the total
                break #exits the loop
                break #exits the loop
            if inputted_word_lower_str != random_str.lower(): #if the inputted word is wrong
                print("Incorrect.", "Result of this game is {}/10".format(level_num_int) + ".") #prints message \
                #and ends the game
                total_denominator += 10 #adds 10 to the total denominator
                print("Total time for this game: {:4.1f}".format(total_time)) #prints the total time taken
                checker_bool = False #the answer was wrong
                total_level_num += level_num_int-1 #adds the level number to the total
                break #exits the loop
                break #exits the loop 
        if (checker_bool == True) or (level_num_int-1 == 10): #if the user answered all questions corectly
            print("Result of this game is {}/{}".format(level_num_int-1, 10) + ".") #prints the game score
            total_denominator += 10 #adds 10 to the total denominator
            total_level_num += level_num_int-1 #adds the number correct to the total level number
            print("Total time for this game: {:<10.1f}".format(total_time)) #prints the total time  
    if (level_str == "m") or (level_str == "M"): #if the user set difficulty to medium
         entered_bool = True #the user entered a valid option
         level_num_int = 1 #sets the first level to 1
         inputted_word_str = "" #variable for user inputted answer
         total_time = 0 #time taken to complete entire level
         while level_num_int <= 10: #loop that runs the level for 10 levels
             random_str = "" #variable for the randomly generated string
             length = randint(6, 10) #boundaries for the length of the generated string
             for i in range(length): #loop that generates the random string
                 index = randint(0, len(ALPHABET_EASY)-1) #picks a random letter index in the ALPHABET_EASY constant
                 random_str += ALPHABET[index]  #adds the letters to form a string
             print("Level [{}], game [{}]/[10]".format(level_str.capitalize(),level_num_int)) #print level header
             print("\nEnter this string:", random_str) #print generated string
             start = time.time() #starts the stopwatch
             inputted_word_str = input() #takes the users inputted word
             end = time.time() #stops the stopwatch
             time_flt = (end - start) #calculates the time taken to input the answer
             total_time += time_flt #adds the time taken to the total time taken
             if inputted_word_str == random_str and time_flt < MEDIUM_TIME_INTERVAL_INT: #the inputted word is \
             #correct and the word was inputted in the time limit
                 print("Good job!", "You spent {:4.1f} of {} seconds entering string [{}][{}]"\
                       .format(time_flt, MEDIUM_TIME_INTERVAL_INT, inputted_word_str, random_str)) #answer correct message
                 print() #prints new line 
                 level_num_int += 1 #increases the level by 1
                 reward += (2*len(random_str)) #calculates the reward and adds it
             if time_flt > MEDIUM_TIME_INTERVAL_INT: #if the user exceeds the time limit
                 print(TIME_ERROR, "Result of this game is {}/{}".format(level_num_int-1, 10)) #prints error \
                 #and ends the game
                 checker_bool = False #the answer was wrong
                 total_denominator += 10 #adds 10 to the total denominator
                 total_level_num += level_num_int-1 #adds the level number to the total
                 break #exits the loop
                 break #exits the loop
             if inputted_word_str != random_str: #if the inputted word is wrong
                 print("Incorrect.", "Result of this game is {}/10".format(level_num_int-1) + ".") #prints message and ends the game
                 checker_bool = False #the answer was wrong
                 total_denominator += 10 #adds 10 to the total denominator
                 total_level_num += level_num_int-1 #adds the level number to the total
                 print("Total time for this game: {:<10.1f}".format(total_time)) #prints the total time taken
                 break #exits the loop
                 break #exits the loop
         if (checker_bool == True) or (level_num_int-1 == 10): #if the user answered all questions corectly
            print("Result of this game is {}/{}".format(level_num_int-1, 10) + ".") #prints the game score
            total_denominator += 10 #adds 10 to the total denominator
            total_level_num += level_num_int-1 #adds the number correct to the total level number
            print("Total time for this game: {:<10.1f}".format(total_time)) #prints the total time
    if (level_str == "h") or (level_str == "H"): #if the user set difficulty to hard
         entered_bool = True #The user entered a valid option
         level_num_int = 1 #sets the first level to 1
         inputted_word_str = "" #variable for user inputted answer
         total_time = 0 #time taken to complete entire level
         while level_num_int <= 10: #loop that runs the level for 10 levels
             random_str = "" #variable for the randomly generated string
             length = randint(11, 15) #boundaries for the length of the generated string
             for i in range(length): #loop that generates the random string
                 index = randint(0, len(ALPHABET_EASY)-1) #picks a random letter index in the ALPHABET_EASY constant
                 random_str += ALPHABET[index]  #adds the letters to form a string
             print("Level [{}], game [{}]/[10]".format(level_str.capitalize(),level_num_int)) #print level header
             print("\nEnter this string:", random_str) #print generated string
             start = time.time() #starts the stopwatch
             inputted_word_str = input() #takes the users inputted word
             end = time.time() #stops the stopwatch
             time_flt = (end - start) #calculates the time taken to input the answer
             total_time += time_flt #adds the time taken to the total time taken
             if inputted_word_str == random_str and time_flt < HARD_TIME_INTERVAL_INT: #the inputted word is \
             #correct and the word was inputted in the time limit
                 print("Good job!", "You spent {:4.1f} of {} seconds entering string [{}][{}]"\
                       .format(time_flt, HARD_TIME_INTERVAL_INT, inputted_word_str, random_str)) #answer correct message
                 print() #prints new line 
                 level_num_int += 1 #increases the level by 1
                 reward += (3*len(random_str)) #calculates the reward and adds it
             if time_flt > HARD_TIME_INTERVAL_INT: #if the user exceeds the time limit
                 print(TIME_ERROR, "Result of this game is {}/{}".format(level_num_int-1, 10)) #prints error and ends the game
                 checker_bool = False #the answer was wrong
                 total_denominator += 10 #adds 10 to the total denominator
                 total_level_num += level_num_int-1 #adds the level number to the total
                 break #exits the loop
                 break #exits the loop
             if inputted_word_str != random_str: #if the inputted word is wrong
                 print("Incorrect.", "Result of this game is {}/10".format(level_num_int-1) + ".") #prints message and ends the game
                 checker_bool = False #the answer was wrong
                 total_denominator += 10 #adds 10 to the total denominator
                 total_level_num += level_num_int-1 #adds the number correct to the total level number
                 print("Total time for this game: {:<10.1f}".format(total_time)) #prints the total time taken
                 break #exits the loop
                 break #exits the loop
         if (checker_bool == True) or (level_num_int-1 == 10): #if the user answered all questions corectly
            print("Result of this game is {}/{}".format(level_num_int-1, 10) + ".") #prints the game score
            total_denominator += 10 #adds 10 to the total denominator
            total_level_num += level_num_int-1 #adds the number correct to the total level number
            print("Total time for this game: {:<10.1f}".format(total_time)) #prints the total time
    elif(entered_bool == False): #if the user did not enter a valid option
        print(DIFFICULTY_ERROR) #prints an error
    level_str = input(LEVEL_PROMPT) #asks user for level difficulty

print("Your final total: {}/{}".format(total_level_num, total_denominator)) #prints the total score for the whole game
print("Your total reward: {}".format(reward)) #prints the reward