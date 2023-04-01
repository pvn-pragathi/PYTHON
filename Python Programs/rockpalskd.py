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

#Write your code below this line 👇
#Player Side
player_input = int(input("What do you wanna choose?\n1 for rock.\n2 for paper.\n3 for scissors.\n"))

available = [rock,paper,scissors]
player_choice = available[player_input-1]
print(player_choice)

#Computer Side	
computer_input = [rock,paper,scissors]
computer_choice = random.choice(computer_input)
print(computer_choice)

#Logic of winning
if player_choice  == computer_choice:
    print("It is a draw!!!")
elif player_choice == rock and  computer_choice == scissors:
    win = "You won the game."
elif player_choice == scissors and computer_choice == paper:
    win = "You won the game."
elif player_choice == paper and computer_choice == rock:
    win = "You won the game."
else:
    win = "Ohooo!You lost the game"
   
    print(win)
