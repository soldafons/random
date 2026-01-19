import random

num = [1 , 2 , 3 , 4 , 5 , 6]
rcnum = random.choice(num)

while True:
    guess = input("Guess the number the dice will fall on:")
    try:
        guess = int(guess)

        if guess == rcnum:
            print("Hooray!")
        elif guess != rcnum:
            print("Sorry , you lost")
        break
    except ValueError:
        print("Enter a number pls")

