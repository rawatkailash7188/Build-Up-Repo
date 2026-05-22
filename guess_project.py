import random


def start_game():
    print("🎯 Welcome to the Number Guessing Game!!!!!!!!!!")
    print("I'm thinking of a number between 1 and 100.")

    # The computer picks a random number
    secret_number = random.randint(1, 100)
    attempts = 0

    # This loop keeps going until the user guesses correctly
    while True:
        try:
            # Take input from the user and convert it to an integer
            guess = int(input("\nEnter your guess: "))
            attempts += 1

            # Check the user's guess against the secret number
            if guess < secret_number:
                print("Too low! 📉 Try a higher number.")
            elif guess > secret_number:
                print("Too high! 📈 Try a lower number.")
            else:
                print(f"🎉 Fantastic! You guessed it in {attempts} attempts!")
                break  # This breaks out of the loop and ends the game

        except ValueError:
            # If the user types a letter instead of a number, this catches the error
            print("❌ Invalid input. Please enter a valid number.")


# This actually triggers the function to start running the game
if __name__ == "__main__":
    start_game()
