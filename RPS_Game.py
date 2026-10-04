""" 
    choose rock paper scissor :- rock 
    computer chooser:-scissor 
    you win! rock beats scissor.

"""



import random

while True:
    choices=["ROCK", "PAPER", "SCISSOR"]
    user=input("Enter Your Bid:=").upper()
    computer=random.choice(choices)

    if user==computer:
        print("======= It's a Tie ========= ")

    elif (user=="ROCK" and computer=="SCISSOR" or\
          user=="PAPER" and computer=="ROCK" or\
        user=="SCISSOR" and computer=="PAPER"):
        print("========= congratulation you win =============")
        break

    else:
        print("Computer Won")
