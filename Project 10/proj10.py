##############################################################################
# CSE 231 proj10
#
# Algorithm 
#   Keeps on getting card index until the deck is empty or the player quits
#   Displays table after every card movement
#   Displays scores of players
#   Displays winner
##############################################################################

from cards import Card
from cards import Deck
from itertools import zip_longest,chain,combinations #for displaying the table and sum

def distribute_cards(deck,p1_cards,p2_cards,t_cards,round1):
    """

    Distributes cards to players and the table

    deck:     The deck of cards that the game is being played with
    p1_cards: Player 1's deck of cards
    p2_cards: Player 2's deck of cards
    t_cards:  The table's deck of cards
    round1:   a boolean value that tells if it is the first round or not

    Returns:  None, but changes the values inside of the lists of decks

    """

    if round1 == True: #checks if it is the first round
        for i in range(4): #loop to distribute 4 cards
            p1_cards.append(deck.deal()) #appends the last card in the deck to the hand
        for i in range(4): #loop to distribute 4 cards
            p2_cards.append(deck.deal()) #appends the last card in the deck to the hand
        for i in range(4): #loop to distribute 4 cards
            t_cards.append(deck.deal()) #appends the last card in the deck to the hand
    else: #it is not the first round
        for i in range(4): #loop to distribute 4 cards
            p1_cards.append(deck.deal()) #appends the last card in the deck to the hand
        for i in range(4): #loop to distribute 4 cards
            p2_cards.append(deck.deal()) #appends the last card in the deck to the hand

def get_card_index(card,cards_list):
    """

    Gets the index of a matching card

    card: The card trying to be found
    card_list: The list of cards the card is trying to found in

    Returns:  The index of the card, or None if the card is not found

    """
    
    for i, ch in enumerate(cards_list): #loop for running through all the cards in the list
        if card.__eq__(ch): #checks if the card is the same number and suit as the card list card
            return i #retuns the card index
    return None #returns None

def get_matching_cards(card,t_cards):
    """

    Gets a list of the matching cards on the table

    card: The card trying to be found
    t_cards: The list of cards on the table

    Returns:  The a list of the matching cards

    """

    matching_list = [] #the list of matching cards
    for i in t_cards: #loop for running through each element of the table cards
        if card.equal_value(i): #checks if the rank is the same
            matching_list.append(i) #appends the matching cards
    return matching_list #retuns the list

def numeric_card(card):
    """

    Gets a boolean depending on the rank of the card

    card: The card trying to see the rank of

    Returns:  True or False depending on if the rank is less than or greater than 10

    """

    if card.rank() <= 10: #the card is less than or equal to 10
        return True #returns True
    elif card.rank() > 10: #the cars is greater than 10
        return False #returns False

def remove_cards(cards_list,cards):
    """

    Removes cards from a list of cards

    cards_list: The list of cards being removed from
    cards:      The list of cards that are trying to be removed from cards_list

    Returns:  None, but modifies the cards_list

    """

    for i in cards: #loop that runs through the list of cards that are being removed from the cards_list
        if get_card_index(i, cards_list) != None: #checks if the card is in the cards_list
            cards_list.remove(i) #removes the card from the cards_list

def get_sum_matching_cards(card,t_cards):
    '''this function return a list of cards that add up to card rank,
    if the card is Jack, Queen or king, the function returns empty list'''

    matching_sum_list=[]
    numeric_list=[]

    # make a list of the numeric cards on the table
    if len(t_cards)>1:
        for i in t_cards:
            if numeric_card(i):
                numeric_list.append(i)

    # collect pairs of numeric cards that sum to card
    if len(numeric_list) > 1:
        # collect combinations of length 2, i.e. pairs, of cards
        # only if the ranks of the pair sum to card's rank
        matching_sum_pair = [seq for seq in combinations(numeric_list, 2) \
                         if seq[0].rank() + seq[1].rank() == card.rank()]
        # combine the list of lists into one list
        matching_sum_list = list(chain(*matching_sum_pair))
    
    return matching_sum_list


def sum_rank(cards): #optional
    """

    Gets a sum of the ranks in the list of cards

    cards: The list of cards

    Returns:  The total of the ranks of the cards

    """

    total = 0 #total of the ranks
    for i in cards: #loop that runs through the list of cards
        total += i.rank() #adds the ranks to the total variable
        
    return total #returns the total

def jack_play(card,player,pile,basra,t_cards):
    """

    Changes the values of the lists if the card is a Jack

    card:    The Jack
    player:  The players list of cards
    pile:    The players pile of won cards
    basra:   Player's basra list
    t_cards: The cards on the table

    Returns:  None, but changes the values of the parameter lists

    """

    if t_cards == []: #checks if the table is empty
        t_cards.append(card) #adds the jack to the table
        player.remove(card) #removes the jack from the player's deck
    else: #the table is not empty
        jack_found = False #varible check if the jack is on the table
        for i in t_cards: #runs trhough all the cards on the table
            if card.equal_value(i): #checks if a table card is a jack
                jack_found = True #a Jack has been found
        for i in t_cards: #runs through the cards on the table
            pile.append(i) #adds the table cards to the pile
        basra_bool = False #variable to say if the jack has bee added to the basra
        if jack_found == True: #checks if the table has a jack
            basra.append(card) #adds the jack to the basra
            player.remove(card) #removes the card from the players deck
            basra_bool = True #the card has been added to the basra
        if basra_bool == False: #the jack was not added to the basra
            pile.append(card) #added the jack to the pile
            player.remove(card) #removes the card from the player's deck
        t_cards.clear() #removes the cards from the table
            
def seven_diamond_play(card,player,pile,basra,t_cards):
    """

    Changes the values of the lists if the card is a seven of diamonds

    card:    Seven of Diamonds
    player:  The players list of cards
    pile:    The players pile of won cards
    basra:   Player's basra list
    t_cards: The cards on the table

    Returns:  None, but changes the values of the parameter lists

    """

    if t_cards == []: #checks if the table is empty
        t_cards.append(card) #adds the card to the table
        player.remove(card) #removes the card from the player's deck
    else: #the table is not empty
        total = sum_rank(t_cards) #gets the total of the table cards
        for i in t_cards: #loop that runs through the table cards
            pile.append(i) #adds the cards to the pile
        if total <= 10: #checks if total of the table cards is less than or equal to 10
            basra.append(card) #adds the card to the basra
        else: #the total is greater than 10
            pile.append(card) #adds the card to the pile
        player.remove(card) #removes the card from the players deck
        t_cards.clear() #clears the table cards

def play(card,player,pile,basra,t_cards):
    """

    Changes the values of the lists if the card is a seven of diamonds

    card:    The card to play with
    player:  The players list of cards
    pile:    The players pile of won cards
    basra:   Player's basra list
    t_cards: The cards on the table

    Returns:  None, but changes the values of the parameter lists

    """

    if t_cards == []: #checks if the table is empty
        t_cards.append(card) #adds the card to the table
        player.remove(card) #removes the card from the player's deck
    else: #the table is not empty
        if card.rank() == 11: #checks if the card is a jack
            jack_play(card,player,pile,basra,t_cards) #runs the jack function
        elif card.rank() == 7 and card.suit() == 2: #checks if the card is a 7 of diamonds
            seven_diamond_play(card,player,pile,basra,t_cards) #runs the 7 of diamonds function
        elif card.rank() > 11: #checks if the card is a king or queen
            matching_list = get_matching_cards(card,t_cards) #gets the list of matching cards
            if matching_list == []: #checks if the matching list is empty
                t_cards.append(card) #adds the card to the table
            else: #the matching list is not empty
                remove_cards(t_cards,matching_list) #removes the matching cards from the table
                for i in matching_list: #loop that runs through the matching list
                    pile.append(i) #adds the matching cards to the pile
                if t_cards == []: #checks if the table is empty
                    basra.append(card) #adds the card to the basra
                else: #the table is not empty
                    pile.append(card) #adds the card to the pile
            player.remove(card) #removes the card for the player's deck
        elif card.rank() <= 10: #checks if the card is a number card
            entered_sum = False
            entered_match = False
            matching_list = get_matching_cards(card,t_cards) #gets the a list of matching cards
            matching_sum_list = get_sum_matching_cards(card,t_cards) #gets the list of matching sum cards
            if matching_sum_list != []:
                remove_cards(t_cards, matching_sum_list) #removes the sums from the table
                if matching_list==[]:
                    for i in matching_sum_list: #runs through the matching sum list
                        pile.append(i) #adds the matching sum list to the pile
                    if t_cards == []: #checks if the table is empty
                        basra.append(card) #adds the card to the basra
                    else: #the table is not empty
                        pile.append(card) #adds the card to the pile
                entered_sum = True
            if matching_list != []: #checks if the matching list is empty
                remove_cards(t_cards, matching_list) #removes the matching cards from the table
                for i in matching_list: #runs though the matching list
                    pile.append(i) #adds the matching list to the pile
                for i in matching_sum_list: #runs through the matching sum list
                    pile.append(i) #adds the matching sum list to the pile
                if t_cards == []: #checks if the table is empty
                    basra.append(card) #adds the card to the basra
                else: #the table is not empty
                    pile.append(card) #adds the card to the pile
                entered_match = True
            else: #the matching list empty
                t_cards.append(card) #adds the card to the table
            if entered_sum == True and entered_match != True:
                t_cards.remove(card)
            player.remove(card) #removes the card from the player deck
                
def compute_score(p1_pile,p2_pile,basra_1,basra_2):
    """

    Changes the values of the lists if the card is a seven of diamonds

    p1_pile: Player 1's deck
    p2_pile: Player 2's deck
    basra_1: Player 1's basra deck
    basra_2: Player 2's basra deck

    Returns:  The scores of the players

    """

    player1_score = 0 #player 1's score
    player2_score = 0 #player 2's score
    if len(p1_pile) + len(basra_1) >= 27: #the length of player 1's pile is more than 27
        player1_score += 30 #adds the points
    if len(p2_pile) + len(basra_2) >= 27: #the length of player 2's pile is more than 27
        player2_score += 30 #adds the points
    if len(p1_pile) == len(p2_pile): #the piles are the same length
        player1_score += 0 #adds the points
        player2_score += 0 #adds the points
    if basra_1 != []: #checks if the player 1 basra is empty
        for i in basra_1: #runs through the basra
            if i.rank() == 11: #checks if the card is a jack
                player1_score += 30 #adds the points
            if i.rank() > 11: #checks if the card is a king or a queen
                player1_score += 20 #adds the points
            if i.rank() <= 10: #checks if the card is a number card
                player1_score += 10 #adds the points
    if basra_2 != []: #checks if the player 2 basra is empty
        for i in basra_2: #runs through the basra
            if i.rank() == 11: #checks if the card is jack
                player2_score += 30 #adds the points
            if i.rank() > 11: #checks if the card is a king or a queen
                player2_score += 20 #adds the points
            if i.rank() <= 10: #checks if the card is number card
                player2_score += 10 #adds the points
    return player1_score, player2_score #returns the player points
        
def display_table(t_cards,p1_cards,p2_cards): 
    '''Display the game table.'''
    print("\n"+36*"=")
    print("{:^36s}".format('Player1'))
    print(9*" ", end = ' ')
    for card in p1_cards:
        print("{:>3s}".format(str(card)),end = ' ')
    print()
    print(9*" " + " {0[0]:>3d} {0[1]:>3d} {0[2]:>3d} {0[3]:>3d}".format(range(4)))
    table = zip_longest(*[iter(t_cards)]*4,fillvalue=0)
    hline = "\n" + 36*"-" 
    str_ = hline + '\n '
    for row in table:
        str_ += 9*" "
        for c in range(0, 4):
            str_ += ("{:>3s}".format(str(row[c])) \
                     if row[c] is not 0 else ' ') +' '
        str_ += '\n'
    str_ += hline + '\n '
    print (str_)

    print(9*" " + " {0[0]:>3d} {0[1]:>3d} {0[2]:>3d} {0[3]:>3d}".format(range(4)))
    print(9*" ", end = ' ')
    for card in p2_cards:
        print("{:>3s}".format(str(card)),end = ' ')
    print()
    print("{:^36s}".format('Player2'))
    print(36*"=")
            
    
def main():
    '''main function'''
    RULES = '''
    Basra Card Game:
        This game belongs to a category of card games called “fishing cards games”. 
        Each player in turn matches a card from their hand with one (or more) of those 
        lying face-up on the table and then takes them. 
        If the card which the player played out does not match one of the existing cards, 
        it stays on the table.
    To win, you have to collect more points.'''
    
    print(RULES) 

    p1_cards = [] # card in hands player1
    p2_cards = [] #card in hands player2
    t_cards = []   # card on the floor
    p1_pile = [] # for player1
    p2_pile = [] # for player2
    basra_1 = []
    basra_2 = []
    
    deck = Deck() #creates Deck object
    
    
    answer = input("Would you like to play? y/Y or n/N?")  #prints prompt
    while answer!='n': #runs until np
        deck.shuffle() #shuffles deck
        print(" ---------Start The game--------") #prints message
        print("Dealing the cards, 4 cards for each player, 4 cards on the table") #prints message
        distribute_cards(deck,p1_cards,p2_cards,t_cards,True) #deals the cards
        print("Cards left:  {}".format(len(deck))) #prints the number of cards left
        display_table(t_cards,p1_cards,p2_cards) #displays the table
        player1_length = len(p1_cards) #length of p1 deck
        player2_length = len(p2_cards) #length of p2 deck
        play_num = 1 #player 1 turn
        quit_bool = False #the user quit variable
        valid_index = False #valid index var
        index = None #index var
        while valid_index == False: #loop will run till a valid index is inputted
            index = input("Player {:d} turn: -> ".format(play_num)) #prints prompt
            if index.lower() == "q": #checks if user quit
                quit_bool = True #the user quit
                break #exit loop
                break #exit loop
            index = int(index) #makes the string into int
            if 0 <= index <= len(p1_cards)-1: #checks if the int is in boundaries
                valid_index = True #int is in boundaries
            else: #int is not in boundaries
                print('Please enter a valid card index, 0 <= index <= {:d}'.format(player1_length-1)) #print error
        player = 1 #player 1 turn
        while valid_index == True: #replace by the correct condition
            if player%2 != 0: #checks whose turn it is
                play(p1_cards[index],p1_cards,p1_pile,basra_1,t_cards) #plays player 1
                player += 1 #adds player num
            else:
                play(p2_cards[index],p2_cards,p2_pile,basra_2,t_cards) #plays player 2
                player+=1 #adds player num
            display_table(t_cards,p1_cards,p2_cards) #displays table
            if (len(p1_cards)==0 and len(p2_cards)==0): #checks if players are empty
                if len(deck) != 0: #checks if deck is not empty
                    if t_cards != []: #checks if the table is empty
                        if (player-1)%2 != 0: #checks the player num
                            for j in t_cards: #loop for adding table cards to player pile
                                p1_pile.append(j)
                        else:
                            for j in t_cards:
                                p2_pile.append(j)
                    t_cards.clear() #clears the table
                    display_table(t_cards,p1_cards,p2_cards) #displays the table
                    print("\n------Start new round-----")  #prints message
                    print("Dealing the cards, 4 cards for each player") #prints message
                    distribute_cards(deck,p1_cards,p2_cards,t_cards,False) #deals cars
                    print("Cards left:  {}".format(len(deck)))  #prints message
                    display_table(t_cards,p1_cards,p2_cards)#displays table
                    player = 1 #sets player num
                else: #the deck is empty
                    display_table(t_cards,p1_cards,p2_cards) #displays table
                    p1_score, p2_score = compute_score(p1_pile,p2_pile,basra_1,basra_2) #gets the scores
                    print("player 1:  {}".format(p1_score)) #display p1 score
                    print("player 2:  {}".format(p2_score)) #display p2 score
                    print() #new line
                    if p1_score > p2_score: #checks whose score is higher
                        print("Player 1 is the winner")
                    elif p2_score > p1_score:
                        print("Player 2 is the winner")
                    elif p2_score == p1_score:
                        print("No winner: equal score")
                    break #exit loop
                    break #exit loop
            valid_index = False #valid index var
            while valid_index == False: #loop will run till a valid index is inputted
                if player%2 != 0: #checks whose turn it is
                    index = input("Player {:d} turn: -> ".format(1))
                else:
                    index = input("Player {:d} turn: -> ".format(2))
                if index.lower() == "q": #checks if the user wants to quit
                    quit_bool = True #wants to quit
                    break #exit loop
                    break #exit loop
                index = int(index) #converts str to int
                cards=None #gets the length of the player deck
                if player%2 != 0: #checks whose turn it is
                    cards = p1_cards
                else:
                    cards = p2_cards
                if 0 <= index <= len(cards)-1: #checks if index is within limits
                    valid_index = True
                else: #prints errors
                    if player%2 != 0:
                        print('Please enter a valid card index, 0 <= index <= {:d}'.format(len(p1_cards)-1))
                    else:
                        print('Please enter a valid card index, 0 <= index <= {:d}'.format(len(p2_cards)-1))
                

        if quit_bool != True:
            answer = input("Would you like to play? y/Y or n/N?")
            p1_cards.clear() # card in hands player1
            p2_cards.clear() #card in hands player2
            t_cards.clear()   # card on the floor
            p1_pile.clear() # pile for player1
            p2_pile.clear() # pile for player2
            basra_1.clear() # basra for player1
            basra_2.clear() #basra for player2
        else: #the user quit
            print('Thanks for playing. See you again soon.')
            break
            break
    else:
        print(' Thanks for playing. See you again soon.')
    
    
      
# main function, the program's entry point
if __name__ == "__main__":
    main()
