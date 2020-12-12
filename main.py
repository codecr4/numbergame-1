#guess guess game
import random

guess_range = int(input("Enter your guessing range : "))
secret_number = random.randint(1, guess_range)
count = 0
max_guess = 5

while count != max_guess:
    try:
        guess = int(input("Guess : "))

        if guess != secret_number:
            count += 1
            print("try again")

        else:
            print(f"You guess the number , after {count} trials .")
            break
    except ValueError:
        print("please use only numbers ")
else:
    print(f"Game over !! ; the number was {secret_number}")
