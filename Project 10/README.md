# Project Title

Project 10

## Description

Utilizing Python, Implement a card game called Basra.

### Function Descriptions

* **`distribute_cards(deck,p1_cards,p2_cards,t_cards,round1)`**
  * Distributes cards to players and the table
  * `deck`:     The deck of cards that the game is being played with
  * `p1_cards`: Player 1's deck of cards
  * `p2_cards`: Player 2's deck of cards
  * `t_cards`:  The table's deck of cards
  * `round1`:   a boolean value that tells if it is the first round or not
  * Returns:  None, but changes the values inside of the lists of decks
    
* **`get_card_index(card,cards_list)`**
  * Gets the index of a matching card
  * `card`: The card trying to be found
  * `card_list`: The list of cards the card is trying to found in
  * Returns:  The index of the card, or None if the card is not found
    
* **`get_matching_cards(card,t_cards)`**
  * Gets a list of the matching cards on the table
  * `card`: The card trying to be found
  * `t_cards`: The list of cards on the table
  * Returns:  The a list of the matching cards
    
* **`numeric_card(card)`**
  * Gets a boolean depending on the rank of the card
  * `card`: The card trying to see the rank of
  * Returns:  True or False depending on if the rank is less than or greater than 10
    
* **`remove_cards(cards_list,cards)`**
  * Removes cards from a list of cards
  * `cards_list`: The list of cards being removed from
  * `cards`:      The list of cards that are trying to be removed from cards_list
  * Returns:  None, but modifies the cards_list
    
* **`get_sum_matching_cards(card,t_cards)`**
  * this function return a list of cards that add up to card rank, if the card is Jack, Queen or king, the function returns empty list
    
* **`sum_rank(cards)`**
  * Gets a sum of the ranks in the list of cards
  * `cards`: The list of cards
  * Returns:  The total of the ranks of the cards
    
* **`jack_play(card,player,pile,basra,t_cards)`**
  * Changes the values of the lists if the card is a Jack
  * `card`:    The Jack
  * `player`:  The players list of cards
  * `pile`:    The players pile of won cards
  * `basra`:   Player's basra list
  * `t_cards`: The cards on the table
  * Returns:  None, but changes the values of the parameter lists
    
* **`seven_diamond_play(card,player,pile,basra,t_cards)`**
  * Changes the values of the lists if the card is a seven of diamonds
  * `card`:    Seven of Diamonds
  * `player`:  The players list of cards
  * `pile`:    The players pile of won cards
  * `basra`:   Player's basra list
  * `t_cards`: The cards on the table
  * Returns:  None, but changes the values of the parameter lists
    
* **`play(card,player,pile,basra,t_cards)`**
  * Changes the values of the lists if the card is a seven of diamonds
  * `card`:    The card to play with
  * `player`:  The players list of cards
  * `pile`:    The players pile of won cards
  * `basra`:   Player's basra list
  * `t_cards`: The cards on the table
  * Returns:  None, but changes the values of the parameter lists
    
* **`compute_score(p1_pile,p2_pile,basra_1,basra_2)`**
  * Changes the values of the lists if the card is a seven of diamonds
  * `p1_pile`: Player 1's deck
  * `p2_pile`: Player 2's deck
  * `basra_1`: Player 1's basra deck
  * `basra_2`: Player 2's basra deck
  * Returns:  The scores of the players
    
* **`display_table(t_cards,p1_cards,p2_cards)`**
  * Display the game table.

## Author

Ankit Hegde : ankithegde@hotmail.com
