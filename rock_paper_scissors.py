import random

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
images = [rock,paper,scissors]

comp_choice = random.randint(0,2)
player_choice = int(input("What do you chose? Type 0 for Rock, 1 for Paper or 2 for Scissors"))
print("You chose\n"+images[player_choice])

print("Computer chose:\n"+images[comp_choice])

if comp_choice == 0 :
    if player_choice == 0:
        print("It's a draw.")
    elif player_choice == 1:
        print("You lose!")
    else:
        print("You win!")

if comp_choice == 1 :
    if player_choice == 1:
        print("It's a draw.")
    elif player_choice == 2:
        print("You lose!")
    else:
        print("You win!")

if comp_choice == 2 :
    if player_choice == 1:
        print("It's a draw.")
    elif player_choice == 0:
        print("You lose!")
    else:
        print("You win!")
