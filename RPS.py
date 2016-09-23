"""
This program is the RPS.py
"""
from random import randint
from time import sleep

options = ["R","P","S"]
Lost_message = "You Lost!"
Win_message= "You won!"

def decide_winner(user_choice, computer_choice):
  print "Your selection is %s" %user_choice
  print "Computer selecting..."
  sleep(1)
  print "The choice of computer is %s" %computer_choice
  user_choice_index = options.index(user_choice)
  if user_choice == computer_choice:
    print "It's a tie!"
  elif user_choice_index == 0 and computer_choice == 2:
    print Win_message
  elif user_choice_index  == 1 and computer_choice == 0:
    print Win_message
  elif user_choice_index  == 2 and computer_choice == 1:
    print Win_message
  elif user_choice_index  > 2:
    print "Your input is a gabbage!"
  else:
    print Lost_message
   
  
def play_RPS():
    print "This is a RPS game!"
    user_choice = raw_input("Select R for Rock, P for Paper, S for Scissor: ")
    user_choice = user_choice.upper()
    computer_choice = options[randint(0,len(options)-1)]
    
    decide_winner(user_choice, computer_choice)

play_RPS()

    
    
  
  
    
    
    
    
  
  
