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

def print_choice(c):
  match c:
    case 0:
      print(rock)
    case 1:
      print(paper)
    case 2:
      print(scissors)
    case _:
      return "Incorrect Value"

while True:
  user_choice = (input("What do you choose? Type \n 0 -> Rock \n 1 --> Paper \n 2 --> Scissors \n ==> 9 to exit\n0/1/2:"))
  user_choice = int(user_choice)
  computers_choice = random.randint(0,2)

  # exit condition
  if user_choice == 9:
    break

  print("User Choice:")
  val = print_choice(user_choice)

  if val == "Incorrect Value":
    print(val)
    continue

  print(f"Computers Choice: {computers_choice}")
  print_choice(computers_choice)

  if user_choice == computers_choice:
    print("Draw")
  elif user_choice == 0:
    if computers_choice == 2:    # Rock beat scissor
      print("User Wins")
    else:
      print("Computer Wins")    # paper beats rock
  elif user_choice == 1:
    if computers_choice == 0:    # Paper beats scissor
      print("User Wins")
    else:
      print("Computer Wins")
  elif user_choice == 2:
    if computers_choice == 1:    # scissor beats paper
      print("User Wins")
    else:
      print("Computer Wins")

exit()