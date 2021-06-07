# Project Title

Project 1 - Cellular Automata

## Description

Utilizing C++ we need to write a number of functions that when combined, are able to run a cellular automata (see Elementary Cellular Automata on this page: https://en.wikipedia.org/wiki/Cellular_automaton).

In this project you will ultimately write a program that reads in a set of rules, a number of lines to iterate the cellular automata (CA) by, and a starting line. The state of each cell is a single digit character (0-9).

### Function Descriptions

* In a function named "get_line_sum", it should take a string representing a line of CA and return an int that is the sum of all the CA digits.
* In a function named "get_next_state" returns a char and takes two strings. The first string represents a neighborhood of a cell (always length 3). The second parameter is a multiline string like the following:
  ```
  001 -> 2
  010 -> 1
  100 -> 3
  002 -> 1
  ```
  * According to the first rule, if the neighborhood is "001" the result of this function should be a '2'.
  * A neighborhood of "100" should return a '3'.
  * A unspecified neighborhood (like "111" returns the default state of '0'.
  * This multiline string is represented in C++ using raw string literals (see https://en.cppreference.com/w/cpp/language/string_literal).
* In a function named "update_line", it should take two string parameters, but returns nothing. The first parameter is a string denoting a line/row of cells, the second parameter is a multiline string of rules (see previous function). Instead of returning a newline, the first parameter should be altered to represent updating each cell for the next generation.
  * Note, the line wraps around from beginning to end, so that the first position in a line is neighbors with the last position.
* In a function named "run_cellular_automata", this function should take a multiline string of rules (see previous), an int denoting the number of iterations/generations to update the CA, and a string representing the starting state of the line.
   * This function should return a multiline string with a line for each update (and the sum of the digits). See the relevant test cases for exact output.
* In a main function, write a program that reads in from standard in a multiline string denoting rules, a period on its own line denotes the end of the rules, then an int denoting the number of lines of output, then a string denoting the starting line. Output the result from run_cellular_automata.

## Author

Ankit Hegde : ankithegde@hotmail.com
