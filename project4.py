# Define a dictionary with trivia questions and their answers
trivia_questions = {
    "What is the capital of France?": "Paris",
    "What is the largest planet in our solar system?": "Jupiter",
    "Who wrote 'Romeo and Juliet'?": "Shakespeare",
    "What element does 'O' represent on the periodic table?": "Oxygen",
    "How many continents are there on Earth?": "7"
}

# Greet the user
print("Welcome to the Quiz Bowl! Let's see how many questions you can answer correctly.")

# Use a for loop to iterate through the questions
for question, correct_answer in trivia_questions.items():
    # Display the question and prompt the user for an answer
    user_answer = input(f"{question} ").strip().lower()

    # Check if the user's answer matches the correct answer (case-insensitive)
    if user_answer == correct_answer.lower():
        print("Correct!\n")
    else:
        print(f"Incorrect. The correct answer is {correct_answer}.\n")

# Farewell message after the quiz
print("Thanks for playing! Study hard and good luck on your next quiz.")
