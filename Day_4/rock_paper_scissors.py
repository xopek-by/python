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
game_images = [rock,paper,scissors]

# read the user answer and write it as a list position (answer-1)
user_input = int(input("Make the choose \n1. Rock \n2. Paper \n3. Scissors \n"))-1

# checking the correctness of the input
if user_input >= 3 or user_input < 0:
    print ("You choose an invalid number, you loose")
else:
    print(f"You choose: {game_images[user_input]}")
    
    # randomly generate computer answer, select needed image and print it
    computer_input = random.randint(0,2)
    print(f"Computer choose: {game_images[computer_input]}")

    # cheking - who are the winner
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

