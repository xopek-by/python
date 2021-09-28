# This programm is calculating how many month, weeks and days is left for you, if you will live until 90 years

# Waiting an age input from user
age = int(input("What is your current age?\n"))

# Calculating years left to 90
y_left = 90 - age

# Calculating days, weeks and month
months = y_left * 12
weeks = y_left * 52
days  = y_left * 365

# Writing the answer
print(f"Your have {y_left} years until 90. This is {months} month. Or {weeks} weeks. Or {days} days")