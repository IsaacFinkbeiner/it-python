import random
print("=====================")
print("|  GUESS MY NUMBER  |")
print("|By Isaac Finkbeiner|")
print("=====================")
print("")
name = input("Hi, I'm the computer. What is your name? ")
print("")
the_number = random.randint(0,100)
print(f"Hi {name}")
print("")
print("I'm thingking of an integer between 0 and 100. Can you guess it? ")
print("")

guess = -1

while guess != the_number:
    guess_text = input("What is your guess? ")
    guess = int(guess_text)
    if guess < the_number:
        print(f"Sorry, {name}, but your guess is too LOW. Try again!" )
    elif guess > the_number:
        print(f"Sorry, {name}, but your guess is too HIGH. Try again!" )
    else:
        print(f"You Guessed It! Congrats, {name}")
print("Thanks for playing!" )