# Project Title

Project 7

## Description

Utilizing Python, create a program that allows users to play a game of connect 4.

Provided test inputs and verification program.

### Function Descriptions

* **`initialize()`**
  * Creates a list of lists that the game will be played in
  * Parameters: NONE
  * Returns:  TThe list of lists called board

* **`choose_color()`**
  * Finds the color the user wants to use as theirs
  * Parameters: NONE
  * Returns:  The user's color, and the opponent's color

* **`board_display(board)`**
  * Prints the list of lists as a formatted game board
  * `board`: The list of lists returned in initialize
  * Returns:  NONE, but prints the formatted board

* **`drop_disc(board, column, color)`**
  * Drops the disc into the board
  * `board`:  the list of list returned in initialiae
  * `column`: the column the user wants to drop the disc into
  * `color`:  the color that the user is
  * Returns:  the row that the disc dropped into, full if the column in full, None if the user entered an invalid number

* **`check_disc(board, row, column)`**
  * Checks if there is a winning sequence at a specific row and column
  * `board`: the list of lists created in initialize
  * `row`: the row the user wants to check
  * `column`: the column the user wants to check
  * Returns:  True if there is winning sequence, False if there is not, None if the row is invalid

* **`is_game_over(board)`**
  * Checks if the game is over
  * `board`: the list of lists created in initialize
  * Returns:  The winning color if the game is over, otherwise False, or Draw if the gmae is a draw

## Author

Ankit Hegde : ankithegde@hotmail.com
