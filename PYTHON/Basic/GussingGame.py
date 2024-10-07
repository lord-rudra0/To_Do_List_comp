import random

# Initialize the guess variable
guess = 0

# Generate a random number between 1 and 20
rand = random.randrange(1, 21)
count=0

# Game loop to keep asking for guesses until the correct number is guessed
while guess != rand:
    guess = int(input("Guess a number between 1 and 20: "))
    count=count+1
    if guess == rand:
        print("Congrats, you got it!")
    elif guess > rand:
        print("Too high!")
    else:
        print("Too low!")
print( "you guessed for", count, "Times")
        
