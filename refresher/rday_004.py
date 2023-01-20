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
import random as rand
from replit import clear

mov = {
    1: paper,
    2: rock,
    3: scissors,
    }


    
playing = True 
while playing != False:
    clear()
    user_choice = int(input(f"Choose:\n 1 for paper\n 2 for rock\n 3 for scissors\n"))
    robot_choice = rand.randint(1,3)
    if (user_choice == robot_choice):
        print(f"Player:\n{mov[user_choice]}\nBot:\n{mov[robot_choice]}\nYou Tied!")
    elif (user_choice == 1 and robot_choice ==2):
        print(f"Player:\n{mov[user_choice]}\nBot:\n{mov[robot_choice]}\nYou Won!")
    elif (user_choice == 2 and robot_choice ==3):
        print(f"Player:\n{mov[user_choice]}\nBot:\n{mov[robot_choice]}\nYou Won!")
    elif (user_choice == 3 and robot_choice ==1):
        print(f"Player:\n{mov[user_choice]}\nBot:\n{mov[robot_choice]}\nYou Won!")
    else:
        print(f"Player:\n{mov[user_choice]}\nBot:\n{mov[robot_choice]}\nYou Lose!")
    
    still_playing = input("Play again? \nType: 'yes' or 'no' ").lower()
    if still_playing != 'yes':
        playing = False
        
        
        
    