# Project Title

Project 9

## Description

Utilize Python to simulate a password cracking program

### Function Descriptions

* **`open_file(in_file = "pass.txt")`**
  * Opens a user selected file
  * `in_file`: The file of the user wants to open
  * Returns:  The opened file pointer
    
* **`check_characters(password, characters)`**
  * Checks if the password has a certain character
  * `password`:   The user's password
  * `characters`: The collection of elements to check if the password has
  * Returns:  The True or False
    
* **`password_entropy_calculator(password)`**
  * Calculates the entropy of the password
  * `password`: The password the user wants the entropy of
  * Returns:  The opened file pointer
    
* **`build_password_dictionary(fp)`**
  * Builds a dictionary for the file
  * `fp`: The file opened in open_file
  * Returns:  The dictionary for the file
    
* **`cracking(fp,hash_D)`**
  * Checks if the dictionary is cracked
  * `fp`:     The file of hash and hex codes
  * `hash_D`: The dictionary returned in build_password_dictionary
  * Returns:  A list of tuples, the cracked count, and the uncracked count
    
* **`create_set(fp)`**
  * Creates a set from a file pointer
  * `fp`: The file full of the words for the set
  * Returns:  A set made up of words from the file
    
* **`common_patterns(D,common,names,phrases)`**
  * Creates a dictionary of patterns
  * `D`:       dictionary in build_password_dictionary
  * `common`:  set of phrases
  * `names`:   set of phrases
  * `phrases`: set of phrases
  * Returns:  The dictionary of patterns

## Author

Ankit Hegde : ankithegde@hotmail.com
