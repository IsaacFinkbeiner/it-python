import random
from banner import banner

yes = 0
while yes == 0:
    banner("Fuze Jäger Montange", "Isaac Finkbeiner, Ryan Anderson, and Blaise Brockway")
    print("We are going to play a GAME! It's called Fuze, Jäger, Montange. The first to win Two out of Three rounds is the winner.")


    player_score = 0
    cpu_score = 0

    #create a list of play options
    t = ["", "Fuze", "Jäger", "Montange"]

    #assign a random play to the computer

    #set player to False
    player = False

    while player_score < 3:
        computer = random.randint(1,3)
    #set player to True
        if cpu_score == 3:
            print("")
            print("Oh no! The computer won! Try again, you puny mortal! You must follow Turtle_Dude_8 on Twitch to repent for your sins and failures.")
            break
        print("")
        print(f"SCORE: {player_score} - {cpu_score}")
        print("1. Fuze")
        print("2. Jäger")
        print("3. Montange")
        player = int(input("What is your choice? "))
        if player == computer:
            print("You have traded with the CPU!")
        elif player == 1:
            if computer == 2:
                print(f"You lose! {t[computer]} Countered {t[player]}'s Cluster Grenade")
                cpu_score = cpu_score + 1
            else:
                print(f"You win! {t[player]} Teamkills {t[computer]}")
                player_score = player_score + 1
        elif player == 2:
            if computer == 3:
                print(f"You lose! {t[computer]} Absolutely Destroyed {t[player]}'s Forehead")
                cpu_score = cpu_score + 1
            else:
                print(f"You win! {t[player]} Countered {t[computer]}'s Cluster Grenade")
                player_score = player_score + 1
        elif player == 3:
            if computer == 1:
                print(f"You lose... {t[computer]} Teamkills {t[player]}")
                cpu_score = cpu_score + 1
            else:
                print(f"You win! {t[player]} Absolutely Destroyed {t[computer]}'s Forehead")
                player_score = player_score + 1
        else:
            print("Invalid, check spelling!")

    if player_score == 3:
        print("")
        print("Congratz!!! You won against the computer! Great job! And Follow Turtle_Dude_8 on Twitch!")
    play_again = "no"
    while play_again == "no":
        print("")
        play_again = input("Play again?   -->   Type yes or no? ")
        if play_again == "yes":
            print("cool")
            computer_score = 0
            player_score = 0
        else:
            print("SAY yes YOU UTTER FRIDGE")
            play_again = "no"