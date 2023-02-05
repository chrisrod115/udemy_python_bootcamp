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

# Write your code below this line 👇
import random as rand
from replit import clear

"""mov = {
    1: paper,
    2: rock,
    3: scissors,
}

playing = True
while playing != False:
    clear()
    user_choice = int(input(f"Choose:\n 1 for paper\n 2 for rock\n 3 for scissors\n"))
    robot_choice = rand.randint(1, 3)
    if (user_choice == robot_choice):
        print(f"Player:\n{mov[user_choice]}\nBot:\n{mov[robot_choice]}\nYou Tied!")
    elif (user_choice == 1 and robot_choice == 2):
        print(f"Player:\n{mov[user_choice]}\nBot:\n{mov[robot_choice]}\nYou Won!")
    elif (user_choice == 2 and robot_choice == 3):
        print(f"Player:\n{mov[user_choice]}\nBot:\n{mov[robot_choice]}\nYou Won!")
    elif (user_choice == 3 and robot_choice == 1):
        print(f"Player:\n{mov[user_choice]}\nBot:\n{mov[robot_choice]}\nYou Won!")
    else:
        print(f"Player:\n{mov[user_choice]}\nBot:\n{mov[robot_choice]}\nYou Lose!")

    still_playing = input("Play again? \nType: 'yes' or 'no' ").lower()
    if still_playing != 'yes':
        playing = False

"""
rock_paper_sci_dict = {
    1: "rock",
    2: "paper",
    3: "scissors",
}
visual_list = {
    1: rock,
    2: paper,
    3: scissors,
}
playing = True
while playing != False:
    print("Welcome to my game :) ! \n")
    player_move: int = int(input("Type either: (1 = rock) (2 = paper) (3 = scissors)\n"))
    pc_move: int = rand.randint(1, 3)
    print(f"You chose {rock_paper_sci_dict[player_move]}\n{visual_list[player_move]}")
    print(f"PC chose {rock_paper_sci_dict[pc_move]}\n{visual_list[pc_move]}")
    if player_move == pc_move:
        print("TIE")
    elif player_move == 1 and pc_move == 3:
        print("You are the Winner!")
    elif player_move == 2 and pc_move == 1:
        print("You are the Winner!")
    elif player_move == 3 and pc_move == 2:
        print("You are the Winner!")
    else:
        print("Soz you lost!")
    again_player: int = int(input("Want to play again? (1 = yes) (2 = no)"))
    if again_player == 2:
        playing = False
