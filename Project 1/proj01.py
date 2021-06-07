###########################################################
# CSE 231 proj01
#
# Algorithm 
#   Prompt for number of rods
#   Converts it into other units
#   Prints the results
###########################################################

rods_str = input("Input rods: ") # Takes the number of rods from the user
rods_float = float(rods_str) # Converts input from string into floating point

# Conversion & Calculation Constants
METERS_IN_ROD = 5.0292 # Number of meters in 1 rod
RODS_IN_FURLONG = 40 # Number of rods in 1 furlong
METERS_IN_MILE = 1609.34 # Number of meters in 1 mile
METERS_IN_FOOT = 0.3048 # Number of meters in 1 foot
AVG_WALK_SPEED = 3.1 # Walking speed in miles per hour

#Conversions & Calculations
meters_float = METERS_IN_ROD * rods_float # Converts the rods into meters
feet_float = meters_float / METERS_IN_FOOT # Converts the meters into feet
miles_float = meters_float / METERS_IN_MILE # Converts meters into miles
furlongs_float = rods_float / RODS_IN_FURLONG # Converts rods to furlongs
walking_min_float = (miles_float / AVG_WALK_SPEED) * 60 # Calculates walk time

# NOTE: I went to the help room to get assistance with the
#       fact that Mimir is saying that I am missing a
#       newline after "rods." in the following section, and 
#       the teacher that was there said that it was a bug 
#       from Mimir, and that that it was ok. That is why I
#       did not change the code to add the new line. I
#       also submitted the file before with a newline and
#       it said it was wrong so that is why he said that 
#       it is Mimir's fault.

#Print Statements (all numbers are rounded to the third decimal place)
print("You input", round(rods_float, 3), "rods.")
print("Conversions")
print("Meters:", round(meters_float,3))
print("Feet:", round(feet_float, 3))
print("Miles:", round(miles_float, 3))
print("Furlongs:", round(furlongs_float, 3))
print("Minutes to walk", round(rods_float,3), "rods:" \
      , round(walking_min_float,3))