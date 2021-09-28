# Welcome to the party calculator. He will calculate how much each of the participants in the party should pay, including a tip to the waiter.

# Printing greetings
print("Welcome to the tip calculator")

# Reading total bill, number of peoples and tips persentage
bill = input("What was total bill?\n$")
peoples = input("How many people to split the bill\n")
percent = input("What percentage tip would you like to give?\n")

# Rounding and changing types of numbers
peoples_calc = int(peoples)
bill_with_tip = float(bill) * (float(percent) / 100 + 1)

# Calculating the final sum
bill_per_person = round(bill_with_tip / peoples_calc, 2)
print(f"So, you spend {bill} dollars with {int(peoples_calc-1)} friends, and decide to pay {percent}% tips. Each people should pay {bill_per_person} dollars")