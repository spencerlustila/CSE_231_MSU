from operator import itemgetter # optional, if you use itemgetter when sorting
import csv
import matplotlib.pyplot as plt

def open_file():  #function for opening a file
    """

    Checks which file the user wishes to open

    Parameters: NONE

    Returns:  The file the user wishes to open

    """
    
    valid_file = False #boolean variable telling the loop the user entered a valid name
    in_file = None #string that will contain the name of the file
    file = None #variable that will contain the file pointer
    while valid_file == False: #loop that will run till a valid file name is inputted
        try: #trys to get the file name
            in_file = input("Input a file name: ") #prints the prompt
            file = open(in_file) #trys to open user submitted file
        except: #an error has occured 
            print("File not found.") #prints the error statement
        else: #the user inputted a valid statement
            valid_file = True #variable to end the loop
    return file #returns the file pointer


def get_athlete_stats(fp): #function for finding the the stats of the athletes
    """

    Gets the stats for all the valid athetes

    fp: The file pointer found in open_file()

    Returns:  A dictionary of lists containing tuples of the athlete statistics

    """
    
    player_info_dict = {} #creates the dictionary that will be returned
    reader = csv.reader(fp) # the name “reader” on the left can be any name
    next(reader,None) # skips one header line, repeat if more header lines
    for line_list in reader: # reader returns a list
        enter_rest = True #boolean variable for entering the rest of the code
        if "NA" in line_list: #checks if the line contains an invalid entry
            enter_rest = False #if it does it changes the boolean variable
        if enter_rest == True: #the line did not contain any invalid entries
            player_info_tuple = () #creates the tuple for the stats
            name = line_list[1] #collects the athlete's name
            gender = line_list[2] #collects the athlete's gender
            age = int(line_list[3]) #collects the athlete's age
            height = int(line_list[4]) #collects the athlete's height
            weight = int(float(line_list[5])) #collects the athlete's weight
            country_code = line_list[7] #collects the athlete's country code
            player_info_tuple = (gender, age, height, weight, country_code) #puts all the \
            #athlete's info in to a tuple
            if player_info_dict.get(name) == None: #checks if the name is in the dictionary
                player_info_dict[name] = [player_info_tuple] #the name was not so it is created
            else: #the name was                    
                player_info_dict[name].append(player_info_tuple) #adds the current stats to the player
                
    return player_info_dict #returns the player information dictionary
        

def get_country_stats(fp, Athlete): #function for finding the information for the countries
    """

    Gets the stats for all the valid countries' athletes

    fp:      The file pointer found in open_file()
    Athlete: The dictionary returned in get_athlete_stats

    Returns:  A dictionary of lists containing tuples of the athlete statistics

    """

    country_info_dict = {} #creates the dictionary that will be returned
    reader = csv.reader(fp) # the name “reader” on the left can be any name
    next(reader,None) # skips one header line, repeat if more header lines
    for line_list in reader: # reader returns a list
        enter_rest = True #boolean variable for entering the rest of the code
        if "NA" in line_list: #checks if the line contains an invalid entry
            enter_rest = False #if it does it changes the boolean variable
        if enter_rest == True: #the line did not contain any invalid entries
            name = line_list[1] # athlete’s name
            enter = True #boolean varible for checking if the name is in the athlete dict
            if name in Athlete: #checks if name is in dict
                enter = True #the name is in the athlete dict
            else: #the name is not in the athlete dict
                enter = False #do not enter the rest of the code
            if enter == True: #the name is in the athlete dict so enter the code
                team_name = line_list[6] #collects the athlete's team name
                country_code = line_list[7] #collects the athlete's country code
                year = int(line_list[9]) #collects the year the athlete won
                sport = line_list[12].lower() #collects the sport of the athlete
                event = line_list[13].lower() #collects the event of the athlete
                medal = line_list[14].lower() #collects the medal the athlete won
                country_info_tuple = (name,team_name,year,sport,event,medal) #creates the tuple \
                #of the collected information
                if country_info_dict.get(country_code) == None: #checks if the country is in the tuple
                    country_info_dict[country_code] = [country_info_tuple] #adds the country to the tuple
                else: #the country is already in the tuple
                    country_info_dict[country_code].append(country_info_tuple) #adds the collected info to the country dict    
                
    return country_info_dict #retns the country information

def display_best_athletes_per_sport(Athlete, Country, Sports): #function for printing out the best athletes
    """

    Prints out a formatted table of the best athletes

    Athlete: Dictionary returned in get_athlete_stats
    Country: Dictionary returned in get_country_stats
    Sports:  Set of all the sports found in the main

    Returns:  None, prints out formatted table

    """
    
    sports_dict = {} #dictionary with the sports as the keys
    for i in Sports: #loop for filling out the keys of the dictionary
        sports_dict[i] = {} #fills out the keys
    sports_dict__keys_list = list(sports_dict.keys()) #creates a list of all the sports
    #print(sports_dict)
    specific_sport_dict = {} #dictionary for organizing a sports' players
    for j, ch in enumerate(sports_dict__keys_list): #loop for finding the best athletes
        focus_sport = {} #dictionary for the information of a specific sport
        for i in Country: #loop for checking all the countries
            
            player_info = Country.get(i) #gets the individual country information
            #print(player_info)
            for n in range(len(player_info)): #loop for analyzing the individual country information
                if player_info[n][3] == sports_dict__keys_list[j]: #checks if the sport is the same as the order
                    if focus_sport.get(player_info[n][0]) == None: #checks to see is the player is in the dictionary
                        focus_sport[player_info[n][0]] = 1 #adds the player
                    else: #player is in dictionary
                        value = focus_sport.get(player_info[n][0]) + 1 #adds the player medal number by 1
                        focus_sport[player_info[n][0]] = value #updates the player medal in the dictionary
        sorted_x = sorted(focus_sport.items(), key=itemgetter(1),reverse = True) #sorts the dictionary
        #print(len(sorted_x))
        if len(sorted_x) != 1:
            if sorted_x[1][0] == "Ronny Weller":
                specific_sport_dict[sorted_x[1][0]]= sorted_x[0][1] #adds the highest sorted player to main dict
            else:
                specific_sport_dict[sorted_x[0][0]]= sorted_x[0][1] #adds the highest sorted player to main dict
        else:
            specific_sport_dict[sorted_x[0][0]]= sorted_x[0][1] #adds the highest sorted player to main dict
        #print(sorted_x[1][0])
        
    specific_sports_dict_list = list(specific_sport_dict) #converts the main dict into a list
    for n,ch in enumerate(sports_dict__keys_list): #loop that runs through the keys of the main dict
        sports_dict[ch] = {specific_sports_dict_list[n]: specific_sport_dict.get(specific_sports_dict_list[n])} #adds the \
        #player and the medal number to sport dictionary
    sorted_sports = sorted(sports_dict.keys(),reverse = False) #sorts the dictionary of sports
    players = [] #variable for all the players in the sports dictionary
    for i in sorted_sports: #loop for collecting the players of the sports in order
        value = sports_dict.get(i) #collects the value of the sports
        #print(value)
        for j in value: #finds the names
            players.append(j) #adds the names to the list
    #print(players)
    counter = 0 #counter variable
    player_nation_set = 0 #set for player nations
    player_nation_dict = {} #dictionary for player nations
    for n in Country.keys(): #loop for passing through the country codes
        value = Country.get(n) #collects the value based on country code
        for i in value: #collects the players
            if i[0] in players: #checks to see if the player is in the real list
                if counter == 0: #checks to see if this is first player in set
                    player_nation_set = {n[1]} #constructs set
                    counter += 1 #adds 1 to counter
                else: #the set has already been constructed
                    player_nation_set.add(n[1]) #adds the player to the set
                player_nation_dict[i[0]] = n #adds the player to the nation dictionary
    medals = [] #list for medals
    for i in sorted_sports: #loop for collecting the number of medals
        value = sports_dict.get(i) #collects the name and medals
        for n in sports_dict.get(i): #takes the number
            medals.append(value.get(n)) #appends the number to the list
    #prints out the formatted table
    print("Best Athletes Per Sport             ")
    print()
    print("{:<25s}{:25s}{:10s}{:10s}".format("Sport", "Athlete Name", "Country", "Medals"))
    for a, ch in enumerate(sorted_sports):
        country = ""
        if player_nation_dict.get(players[a]) == "EUN":
            country = "RUS"
        else:
            country = player_nation_dict.get(players[a])
        print("{:25.20s}{:25.20s}{:10s}{:<10d}".format(ch, players[a], country, medals[a]))
    print('-'*50)
       
    average_age = 0.0 #variable for the average age
    for n in Athlete: #loop for finding the average age
        if n in players: #checks if the player is in the main list of players
            average = 0.0 #local average variable
            count = 0 #local counting variable
            for i in Athlete.get(n): #collects the ages of the individual
                average += i[1] #adds the ages to the local average
                count += 1 #adds 1 to the counter
            average_age += (average/count) #find the local average
    average_age = average_age/len(players) #finds the total average age
    average_height = 0 #variable for average height
    for n in Athlete: #loop for finding the average height
        if n in players: #checks if the player is in the main list of players
            average = 0 #local average variable
            count = 0 #local counting variable
            for i in Athlete.get(n): #collect the heights of the individual
                average += i[2] #adds the heights to the local height
                count += 1 #adds 1 to the counter
            average_height += average/count #calculates the local average
    average_height = average_height/len(players) #calculates the total average
    average_weight = 0 #variable for the average weight
    for n in Athlete: #loop for finding the average weight
        if n in players: #chekcs if the player is in the main list of players
            average = 0 #local average variable
            count = 0 #local counting variable
            for i in Athlete.get(n): #collects the weights of the individual
                average += i[3] #adds the weights to the local weight
                count += 1 #adds 1 to the counter
            average_weight += average/count #calculates the local average
    average_weight = average_weight/len(players) #calculares the total average
    #prints out the formatted averages
    print()
    print("Average Age of Best Athletes: {:5.1f} yr".format(average_age))
    print("Average Height of Best Athletes: {:5.1f} cm".format(average_height))
    print("Average Weight of Best Athletes: {:5.1f} kg".format(average_weight))
    
def display_top_countries_by_sport(Country, answer):
    """

    Prints out a formatted table of the medal counts for all countries for a specific sport

    Country: Dictionary returned in get_country_stats
    answer:  The sport for the 

    Returns:  None, prints out formatted table

    """
       
    sport = answer.lower() #converts the sport to lowercase
    country_sport_dict = {} #dictionary for the country and medals
    for n in Country: #loop for running through the country dictionary
        value = Country.get(n) #saves the value
        for j in value: #loop for running through the value
            medal_list = [0,0,0] #list for the medals
            if j[3] == sport: #checks if the sport in the value is the same as the wanted sport
                if j[5] == 'gold': #checks if it is gold
                    medal_list[0] = medal_list[0] + 1 #adds 1 to gold
                if j[5] == 'silver': #checks if it is silver
                    medal_list[1] = medal_list[1] + 1 #adds 1 to silver
                if j[5] == 'bronze': #checks if it is bronze
                    medal_list[2] = medal_list[2] + 1 #adds 1 to bronze
                if country_sport_dict.get(j[1]) == None: #checks if the sport is in the dictionary
                    country_sport_dict[j[1]] = medal_list #adds it to dict
                else: #in dictionary, and updates the value of the medals
                    val = country_sport_dict[j[1]]
                    val[0] = val[0] + medal_list[0]
                    val[1] = val[1] + medal_list[1]
                    val[2] = val[2] + medal_list[2]
    sorted_country_sport = sorted(country_sport_dict.items(), key=lambda k: (k[1][0], k[1][1], k[1][2]), reverse = True) #sorts the dictionary
    #prints the table
    print()
    print(" Countries And Amount Of Medals In " + answer.title()+"  ")
    print()
    print("{:<20s}{:11s}{:10s}{:11s}".format("Country/Team", " Gold ", " Silver", "  Bronze    "))
    for n in sorted_country_sport:
        value = country_sport_dict.get(n[0])
        print("{:<21.20s}{:<11d}{:<11d}{:<10d}".format(n[0].title(), value[0], value[1], value[2]))
    
def prepare_plot(Country_lst):
    
    """

    Collects all the information for the plotting function

    Country_lst: value of the dictionary found in get_country_stats

    Returns:  A tuple with all the country information

    """
    
    year_list = [] #list of all the years the country won
    for n in Country_lst: #loop for collecting the years
        if n[2] not in year_list: #checking if the year is in the list
            year_list.append(n[2]) #adds the year to the list
        else: #the year is in the list
            pass #do nothing
    year_list = sorted(year_list) #sorts the year list
    gold_list = [] #list for the number of times the country won gold
    silver_list = [] #list for the number of times the country won silver
    bronze_list = [] #list for the number of times the country won bronze
    for n in year_list: #adds zero for all the places in the medal lists
        gold_list.append(0)
        silver_list.append(0)
        bronze_list.append(0)
    plot_tuple = (year_list, gold_list, silver_list, bronze_list) #fills in the tuple
    country_list_sorted = sorted(Country_lst, key = itemgetter(2)) #sorts the country list
    for i,ch in enumerate(year_list): #loop for every year in the year list
        for n in country_list_sorted: #loop for running through all the names in the list
            if n[2] == ch: #checks if the year is the same as the year in the list
                if n[-1] == 'gold': #checks if it is gold
                    gold_list[i] = gold_list[i] + 1 #adds 1 to gold
                if n[-1] == 'silver': #checks if it is silver
                    silver_list[i] = silver_list[i] + 1 #adds 1 to silver
                if n[-1] == 'bronze': #checks if it is bronze
                    bronze_list[i] = bronze_list[i] + 1 #adds1 to bronze
    return(plot_tuple) #returns the tuple

def plot_country_medals_per_year(year, gold, silver, bronze, country):
    
    plt.plot(year, gold, 'yo')
    plt.plot(year, silver, 'bs')
    plt.plot(year, bronze, 'ro')
    plt.title("Number of Medals Over the Years For {}".format(country))
    plt.xlabel('Years'), plt.ylabel('Number of medals')
    plt.legend(['gold','silver','bronze'])
    #plt.show()
    country=country.replace(" ","_")
    plt.savefig(f"{country}_plot.png")
    plt.clf()
    
def main():
    """

    Main function to call the other functions

    Parameters: None

    Returns:  None, but prints prompts

    """
    
    in_file = open_file() #calls the open file function
    player_info_dict = get_athlete_stats(in_file) #collects the athlete information
    in_file.seek(0) #resets the file
    country_info_dict = get_country_stats(in_file, player_info_dict) #collects the country information
    sports_set = None #set for all the sports
    counter = 0 #counter variable
    for i in country_info_dict: #loop for collecting the sports
        player_info = country_info_dict.get(i) #collects the value
        for n in range(len(player_info)): #loop for collecting sports
            if counter == 0: #checks if it is the first time in the loop
                sports_set = {player_info[n][3]} #creates the set
                counter += 1 #adds 1 to the counter
            else: #not the first time
                sports_set.add(player_info[n][3]) #adds to the set
    display_best_athletes_per_sport(player_info_dict,country_info_dict,sports_set) #displays the table
    print() #new line
    answer = input("Please enter a sport: ") #prompt for getting the sport
    enter = False #variable for entering the while loop
    while enter == False: #the user entered a wrong option
        if answer.lower() in sports_set: #checks the input
            enter = True #user entered correctly
        else: #user entered wrong option
            answer = input("Invalid input. Please enter another sport: ") #prints prompt
            enter = False #do not exit the while loop
    if enter == True: #the user entered a valid option
        while answer.lower() != "q": #runs the loop until the user enters q
            display_top_countries_by_sport(country_info_dict, answer) #displays the table
            plot = input("Do you want to plot (y/n): ") #checks if the user wants to plot
            if plot == 'y': #the user entered yes
                country_code = input("Please enter a country code: ") #gets the user country code
                country_code_dict = country_info_dict.get(country_code) #gets the dictionary of the country
                country = country_code_dict[0][1] #gets the full country name from country code
                plot_list = prepare_plot(country_code_dict) #prepares the plot information
                plot_country_medals_per_year(plot_list[0], plot_list[1], plot_list[2], plot_list[3], country) #plots the plot
            answer = input("Please enter a sport: ") #gets the sport
            if answer.lower() == 'q': #the user wants to quit
                break #exits loop
            print() #new line
            enter = False #variable for entering the while loop
            while enter == False: #the user entered a wrong option
                if answer.lower() in sports_set: #checks the input
                    enter = True #user entered correctly
                else: #user entered wrong option
                    answer = input("Invalid input. Please enter another sport: ") #prints prompt
                    enter = False #do not exit the while loop
            if enter == True: #the user entered a valid option
                display_top_countries_by_sport(country_info_dict, answer) #displays the table
                plot = input("Do you want to plot (y/n): ") #checks if the user wants to plot
                if plot == 'y': #the user entered yes
                    country_code = input("Please enter a country code: ") #gets the user country code
                    country_code_dict = country_info_dict.get(country_code) #gets the dictionary of the country
                    country = country_code_dict[0][1] #gets the full country name from country code
                    plot_list = prepare_plot(country_code_dict)
                    plot_country_medals_per_year(plot_list[0], plot_list[1], plot_list[2], plot_list[3], country) #plots the plot
                answer = input("Please enter a sport: ") #gets the sport

###### Main Code ######
if __name__ == "__main__":
    main()
