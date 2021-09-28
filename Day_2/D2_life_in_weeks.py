# This programm is calculating how many month, weeks and days is left for you, if you will live until 90 years

# Waiting an age input from user and checking is that number less, then 90
years = 90
age = int(input("What is your current age?\n"))
while age >= years:
    print("Sorry, seems like you already died(")
    age = int(input("Input correct age, less then 90\n"))
else:
# Calculating years left to 90
    y = years - age

# Calculating days, weeks and month
    m = y * 12
    w = y * 52
    d = y * 365

# Writing the answer
    print(f"Your have {y} years until 90. This is {m} month. Or {w} weeks. Or {d} days")