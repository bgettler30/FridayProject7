# Import the random module
import random

# Greeting message
print("Welcome to the PowerBall Lottery Number Generator!")

# Generate five white ball numbers (1-69)
white_ball_1 = random.randint(1, 69)
white_ball_2 = random.randint(1, 69)
white_ball_3 = random.randint(1, 69)
white_ball_4 = random.randint(1, 69)
white_ball_5 = random.randint(1, 69)

# Generate the red PowerBall number (1-26)
red_ball = random.randint(1, 26)

# Print the generated numbers with appropriate spacing
print(f"{white_ball_1} {white_ball_2} {white_ball_3} {white_ball_4} {white_ball_5}   {red_ball}")

# Farewell message
print("Good luck! Play responsibly!")
