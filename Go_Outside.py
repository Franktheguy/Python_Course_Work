# This is a fun calculator that converts hours and minutes to seconds to illustrate how long in seconds someone has played a game
# I made this for my kids, if they played more than their alotted time they are instructed to Go Outside!
# Function to convert hours to minutes to seconds
def time_to_seconds(hours, minutes):
    total_seconds = (hours * 3600) + (minutes * 60)
    return total_seconds

# Main program
hours_worked = int(input("How many hours did you play a game? "))
minutes_worked = int(input("How many minutes did you play a game? "))

seconds = time_to_seconds(hours_worked, minutes_worked)

if hours_worked <= 2:
    print("Great job!")
elif hours_worked >= 2:
    print("GO OUTSIDE!")

print("You played", seconds, "seconds")
