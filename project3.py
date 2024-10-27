import random  # Importing the random module to generate a random number

# Greeting message asking the user if they want to play
play_game = input("Do you want to play the number guessing game? (Yes/No): ").strip().lower()

# If the user says no, print a farewell message and exit
if play_game != "yes":
    print("Maybe next time!")
else:
    # Generate a random secret number between 1 and 10
    secret_number = random.randint(1, 10)
    
    # Initialize user's guess to None to enter the loop
    guess = None

    # Loop until the user guesses the correct number
    while guess != secret_number:
        # Ask the user to guess a number between 1 and 10
        guess = int(input("Guess a number between 1 and 10: "))

        # Check if the guess is too low, too high, or correct
        if guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")
        else:
            print("Congratulations! You've guessed the number!")

    # Farewell message after the user guesses correctly
    print("Thanks for playing! Goodbye!")
