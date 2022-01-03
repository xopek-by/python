import random
# Get the names
names_string = input("Give me everybody's names, separated by a comma. ")
# Split names into the list
names = names_string.split(", ")
# Get the nubmers of the names
number = len(names)
# Select random person from the list
choice_number = random.randint(0,number-1)
# Print the result
print (f"{names[choice_number]} is paying for the meal today")