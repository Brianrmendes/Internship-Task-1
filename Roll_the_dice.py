import random

def rolldice(min, max):
    while True:
        print("Rolling the dice....")
        number = random.randint(min, max)
        print(f"Your number : {number}")
        choice = input("Do you want to Roll the dice again? (y/n)")
        if choice.lower() == 'n':
            print("Thanks for playing!")
            break

rolldice(1, 6)