from random import randint

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

game_graphic = [rock, paper, scissors]
selected_throw = ["Rock", "Paper", "Scissors"]

player_selection = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors: "))

if player_selection >= 3:
  print("You typed an invalid number, you lose.")
  exit()

player_throw = selected_throw[player_selection]
player_graphic = game_graphic[player_selection]


comp_selection = randint(0, 2)

comp_throw = selected_throw[comp_selection]
comp_graphic = game_graphic[comp_selection]

print("\n" + "You throw " + player_throw + "\n" + player_graphic + "\n")
print("Your opponent throws " + comp_throw + "\n" + comp_graphic + "\n")

# Determine Winner


if player_selection == 0 and comp_selection == 2:
  print("You Win!")
elif comp_selection == 0 and player_selection == 2:
  print("You Lose.")
elif player_selection > comp_selection:
  print("You Win!")
elif comp_selection > player_selection:
  print("You Lose.")
elif comp_selection == player_selection:
  print("It's a Draw.")
