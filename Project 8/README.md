# Project Title

Project 8

## Description

Utilizing Python, plot and find data based on provided CSV files.

### Function Descriptions

* **`open_file()`**
  * Checks which file the user wishes to open
  * Parameters: NONE
  * Returns:  The file the user wishes to open
    
* **`get_athlete_stats(fp)`**
  * Gets the stats for all the valid athetes
  * `fp`: The file pointer found in open_file()
  * Returns:  A dictionary of lists containing tuples of the athlete statistics
    
* **`get_country_stats(fp, Athlete)`**
  * Gets the stats for all the valid countries' athletes
  * `fp`:      The file pointer found in open_file()
  * `Athlete`: The dictionary returned in get_athlete_stats
  * Returns:  A dictionary of lists containing tuples of the athlete statistics
    
* **`display_best_athletes_per_sport(Athlete, Country, Sports)`**
  * Prints out a formatted table of the best athletes
  * `Athlete`: Dictionary returned in get_athlete_stats
  * `Country`: Dictionary returned in get_country_stats
  * `Sports`:  Set of all the sports found in the main
  * Returns:  None, prints out formatted table
    
* **`display_top_countries_by_sport(Country, answer)`**
  * Prints out a formatted table of the medal counts for all countries for a specific sport
  * `Country`: Dictionary returned in get_country_stats
  * `answer`:  The sport for the 
  * Returns:  None, prints out formatted table
    
* **`prepare_plot(Country_lst)`**
  * Collects all the information for the plotting function
  * `Country_lst`: value of the dictionary found in get_country_stats
  * Returns:  A tuple with all the country information

## Author

Ankit Hegde : ankithegde@hotmail.com
