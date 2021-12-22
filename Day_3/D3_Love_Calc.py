from typing import TYPE_CHECKING


print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is her name? \n")

lower_case_name = (name1 + name2).lower()

t = lower_case_name.count("t")
r = lower_case_name.count("r")
u = lower_case_name.count("u")
e = lower_case_name.count("e")
first = t + r + u + e

l = lower_case_name.count("l")
o = lower_case_name.count("o")
v = lower_case_name.count("v")
e = lower_case_name.count("e")
second = t + o + v + e

lovescore = int(str(first) + str(second))

if (lovescore < 10) or (lovescore > 90):
    print(f"Your score is {lovescore} you go together like coke and mentos.")
elif (lovescore >= 40) and (lovescore <= 50):
    print(f"Your score is {lovescore}, you are alright together.")
else:
    print(f"Your score is {lovescore}.")