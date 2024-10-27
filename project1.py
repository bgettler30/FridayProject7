# Mad Lib Game Code

def mad_lib_game():
    print("Welcome to the Friday Mad Lib! 🎉")
    print("Provide the words requested, and we'll create a fun story for you.")

    # Gathering user input
    large_object = input("1. A large object (singular): ")
    large_objects_plural = input("2. Large objects (plural): ")
    adjective = input("3. An adjective: ")
    body_part = input("4. A body part: ")
    restaurant = input("5. A restaurant: ")
    first_food = input("6. A food: ")
    second_food = input("7. Another food: ")

    # Creating the story with user inputs
    story = f"""
    I’ve had a very {adjective} day.
    This morning, I dropped a box of {large_objects_plural} on my {body_part}.
    Then, at lunch, I went to {restaurant} for their delicious {first_food},
    But the waiter brought me {second_food}, which I was not hungry for.
    Finally, on my way home, I was cut off by a van with a large {large_object} strapped to the roof.
    """

    # Display the completed Mad Lib story
    print("\nHere is your Mad Lib story:")
    print(story)

# Run the game
mad_lib_game()