import random
from banner import banner

banner("Rock Paper Scissors", "By Isaac Finkbeiner")
print("We are going to play Rock, Paper, Scissors. The first to win Two out of Three rounds is the winner.")
print("If a triangle = 5 sides, how many sides does a hotdog have?")
player_score = 0
cpu_score = 0

#create a list of play options
t = ["", "Rock", "Paper", "Scissors"]

#assign a random play to the computer

#set player to False
player = False

while player_score < 2:
    computer = random.randint(1,3)
#set player to True
    if cpu_score == 2:
        print("")
        print("Oh no! The computer won! Try again, you puny mortal! You must follow Turtle_Dude_8 on Twitch to repent for your sins and failures.")
        break
    print("")
    print(f"SCORE: {player_score} - {cpu_score}")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")
    player = int(input("What is your choice? "))
    if player == computer:
        print("You have tied with the CPU!")
    elif player == 1:
        if computer == 2:
            print(f"You lose! {t[computer]} covers {t[player]}")
            cpu_score = cpu_score + 1
        else:
            print(f"You win! {t[player]} smashes {t[computer]}")
            player_score = player_score + 1
    elif player == 2:
        if computer == 3:
            print(f"You lose! {t[computer]} cut {t[player]}")
            cpu_score = cpu_score + 1
        else:
            print(f"You win! {t[player]} covers {t[computer]}")
            player_score = player_score + 1
    elif player == 3:
        if computer == 1:
            print(f"You lose... {t[computer]} smashes {t[player]}")
            cpu_score = cpu_score + 1
        else:
            print(f"You win! {t[player]} cut {t[computer]}")
            player_score = player_score + 1
    else:
        print("Invalid, check spelling!")

if player_score == 2:
    print("")
    print("Congratz!!! You won against the computer! Great job! Play again sometime! And Follow Turtle_Dude_8 on Twitch!")