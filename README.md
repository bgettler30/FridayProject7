# FridayProject7  ReadMe Notes

project1. Madlib Notes
 Define the game function to contain all the logic

 Welcome message and instructions for the player

 Gathering user input for each required word
 Input: Large object (singular)
 Input: Large objects (plural)
 Input: Adjective to describe the day
 Input: A body part
 Input: Name of a restaurant
 Input: First food item
 Input: Second food item (different from the first)

 Constructing the Mad Lib story with user inputs

 Displaying the completed Mad Lib story to the user

 Run the game by calling the function

project2. Powerball Numbers
 Importing the random module to generate random numbers.
Displaying a greeting message to the user, explaining what the program does.
Generating five random numbers between 1 and 69 for the white balls:
First white ball number
Second white ball number
Third white ball number
Fourth white ball number
Fifth white ball number
Generating one random number between 1 and 26 for the red PowerBall.
Printing all six numbers with appropriate spacing:
One space between the first five white ball numbers.
Three spaces between the fifth white ball and the red PowerBall number.
Displaying a farewell message to the user, encouraging responsible play.

project3. Guessing Game
Import the random module to generate a random number between 1 and 10.
Greeting message asks the user if they want to play the game.
Check the user’s response:
If they type anything other than "yes", the program prints "Maybe next time!" and ends.
Generate a random number between 1 and 10 if the user chooses to play.
Create a loop that asks the user to guess the number:
If the guess is too low, print "Too low! Try again."
If the guess is too high, print "Too high! Try again."
If the guess is correct, print "Congratulations! You've guessed the number!" and exit the loop.
Farewell message is displayed when the game ends.

project4. Quizbowl
Dictionary Structure:

The dictionary holds questions as keys and their correct answers as values.
For Loop:

The loop iterates over each question-answer pair.
It prints the question, collects the user’s answer, and checks if it's correct.
Score Tracking:

A counter tracks how many correct answers the user provides.
Feedback:

The user receives feedback immediately after each answer.

project5. Colortext
Define five functions:

Each function takes a string parameter (text) and returns the text wrapped in ANSI escape codes for specific colors.
Example functions:
redText(): Returns the text formatted in red.
blueText(): Returns the text formatted in blue.
greenText(): Returns the text formatted in green.
yellowText(): Returns the text formatted in yellow.
brownText(): Returns the text formatted in brown.
Main Program Logic:

Calls each of the five functions to display sample text in the corresponding color.
User Input Section:

Prompts the user to choose a color and enter a string of text.
Displays the text in the chosen color using the appropriate function.
If the user enters an invalid color, the text is displayed without color.
ANSI Escape Codes:

These codes are used to change the color of text in the terminal.
Example: \033[91m is the code for red text, and \033[0m resets the color back to normal.

Project 6: Bank Class

Class Definition**:
   A BankAccount class with attributes for account_number and balance
 Methods
  deposit(amount)`: Adds money to the account.
  withdraw(amount)`: Withdraws money from the account if there are sufficient funds.
  check_balance()`: Displays the current balance.
 Main Program Logic:
   Uses an indefinite loop to ask the user if they want to deposit, withdraw, or check their balance.
   The loop continues until the user exits.

Sample Execution:



