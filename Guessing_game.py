import random

def play_guessing_game():
    number = random.randint(1, 100)
    attempts = 0
    max_attempts = 5

    print("Welcome to the Guessing Game!")
    print("I have chosen a number between 1 and 100. You have to guess it.")

    while attempts < max_attempts:
        guess = int(input("Enter your guess: "))

        if guess < number:
            print("Too low. Try again.")
        elif guess > number:
            print("Too high. Try again.")
        else:
            print(f"Congratulations! You guessed the number {number} correctly in {attempts+1} attempts!")
            break

        attempts += 1

    if attempts == max_attempts:
        print(f"Sorry, you've reached the maximum number of attempts. The number was {number}.")

play_guessing_game()
