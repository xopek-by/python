import random

start = input('Hello, type "coin" to get an answer ')
if start == "coin":
    coin = random.randint(0,1)
    if coin == 1:
        print("Head")
    else:
        print("Tails")
else:
    print("You need to type only coin") 