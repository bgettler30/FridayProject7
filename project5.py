# Functions to change text color using ANSI escape codes

def redText(text):
    return f"\033[91m{text}\033[0m"  # Red text

def blueText(text):
    return f"\033[94m{text}\033[0m"  # Blue text

def greenText(text):
    return f"\033[92m{text}\033[0m"  # Green text

def yellowText(text):
    return f"\033[93m{text}\033[0m"  # Yellow text

def brownText(text):
    return f"\033[33m{text}\033[0m"  # Brown text

# Main Program Logic
print(redText("This is red text"))
print(blueText("This is blue text"))
print(greenText("This is green text"))
print(yellowText("This is yellow text"))
print(brownText("This is brown text"))

# User input to choose a color and display text
color_choice = input("Choose a color (red, blue, green, yellow, brown): ").strip().lower()
user_text = input("Enter the text you want to display: ")

# Display text in the chosen color
if color_choice == "red":
    print(redText(user_text))
elif color_choice == "blue":
    print(blueText(user_text))
elif color_choice == "green":
    print(greenText(user_text))
elif color_choice == "yellow":
    print(yellowText(user_text))
elif color_choice == "brown":
    print(brownText(user_text))
else:
    print("Invalid color choice. Displaying text without color.")
    print(user_text)
