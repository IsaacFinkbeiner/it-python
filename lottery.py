import random
from banner import banner
banner("LOTTERY", "Isaac Finkbeiner")
print("")
print("Welcome to the Lottery Game. Choose a number between 1 and 999. If you guess the same as the computer you will win 10 times your bet amount. ")

balance = 20


while balance != 0:
    print(f"BALANCE: ${balance}")
    bet = int(input("How much do you want to bet? "))
    balance = balance - bet
    if balance < 0:
        balance = balance + bet
        print(f"You bet {bet} but you only had {balance}. Please try again.")
        continue
    pick = int(input("What number do you pick? "))
    number = random.randint(1, 1)
    if pick == number:
        print(f"Awesome, you chose {pick}, and so did the computer! You won ${bet * 10} this round! ")
        bet_reward = bet * 11
        balance = balance + bet_reward
    else:
        print(f"I'm sorry, but you chose {pick} and the computer chose {number}. You lose ${bet} this round. ")
    if balance > 999999:
        print(f"BALANCE: ${balance}")
        print("You win! Congratz!")
        break
if balance == 0:
    print("YOU LOSE AND ARE TRASH. Try again!")