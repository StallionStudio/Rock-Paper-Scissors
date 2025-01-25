import random
is_running = True

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

options = [rock, paper, scissors]

while is_running:
    print("Rock - Paper - Scissors")
    print("-------------------------------------------\n")
    print("1. Rock\n2. Paper\n3. Scissors\n")
    player_input = int(input("What do you choose? \n"))
    player_choose = options[player_input]

    computer_input = random.randint(0, 2)
    computer_choose = options[computer_input]

    print("You Choose:")
    print(player_choose)
    print("")

    print("Computer Choose:")
    print(computer_choose)
    print("")

    if player_choose == computer_choose:
        print("Both Wins!\n")
    elif (player_choose == options[0] and computer_choose == options[1]
          or player_choose == options[1] and computer_choose == options[2]
          or player_choose == options[2] and computer_choose == options[0]):
        print(" You Lose!\n")
    elif (player_choose == options[0] and computer_choose == options[2]
          or player_choose == options[1] and computer_choose == options[0]
          or player_choose == options[2] and computer_choose == options[1]):
        print("You Win!\n")
