# Project Title

Project 6

## Description

Utilize Python to create a program that reads files with the citation data of each category and the impact factor of various journals, print the average citation rate of the top 20 categories and plot the top 10 journal impact factor.

### Function Descriptions

* **`open_file()`**
  * Checks which file the user wishes to open
  * Parameters: NONE
  * Returns:  The file the user wishes to open
    
* **`read_journal_file(fp)`**
  * Creates a list of tuples that contains information regarding a journal file
  * `fp`:  The file pointer that was returned in open_file
  * Returns:  A list of tuples that contains information regarding a journal file

* **`read_category_file(fp)`**
  * Creates a list of tuples that contains information regarding a category file
  * `fp`:  The file pointer that was returned in open_file
  * Returns:  A list of tuples that contains information regarding a category file

* **`display_table(data)`**
  * Prints the first 20 elements of the sorted data
  * `data`:  The user inputted sorted data
  * Returns:  NONE, but prints a formatted table

* **`sort_data(data, column)`**
  * Sorts the list of tuples according to the user requested column
  * `data`:    The list of tuples the user wants to sort
  * `Column`:  The column that the user wants to sort the list by
  * Returns:  The sorted list

* **`prepare_plot_data(data)`**
  * Sorts the data, and finds the 10 highest impacts and its respective name
  * `data`:  The user inputted journal name
  * Returns:  The 10 highest impacts and its respective name

## Author

Ankit Hegde : ankithegde@hotmail.com
