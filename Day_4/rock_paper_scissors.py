import random

# ASCII pictures in variables
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''
scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
#Write your code below this line 👇

# create the list from out ASCII symbols, for further actions with it
game = [rock,paper,scissors]

# read the user answer and write it as a list position (answer-1)
user_input = int(input("Make the choose \n1. Rock \n2. Paper \n3. Scissors \n"))-1

# checking the correctness of the input
if user_input >= 3 or user_input < 0:
    print ("You choose invalid number, you loose")
else:
    user_choose = game[user_input]
    print(f"Your choose: {user_choose}")
    
    # randomly generate computer answer, select needed image and print it
    computer_input = random.randint(0,int(len(game)-1))
    computer_choose = game[computer_input]
    print(f"Computer choose: {computer_choose}")

    if user_input == computer_input:
        print ("Draw!")
    elif user_input == 0 and computer_input == 2:
        print("You win!")
    elif user_input == 2 and computer_input == 0:
        print("You loose :(")
    elif user_input > computer_input == 2:
        print("You win!")
    elif user_input < computer_input == 2:
        print("You loose :(")

