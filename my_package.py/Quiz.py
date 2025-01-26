def run_quiz(questions):  
    score = 0  # Initialize score  

    # Loop through each question  
    for question, options, answer in questions:  
        print(question)  # Display the question  
        for i, option in enumerate(options, start=1):  
            print(f"{i}. {option}")  # Show options  
        
        try:  
            user_answer = int(input("Choose the correct option number: "))  # Get user input  
            if options[user_answer - 1] == answer:  # Check if the answer is correct  
                print("Correct!\n")  
                score += 1  # Increase score  
            else:  
                print(f"Wrong! The correct answer was: {answer}\n")  
        except (ValueError, IndexError):  
            print("Invalid option. Please choose a number from the options.\n")  

    # Display final score  
    print(f"Your final score is: {score} out of {len(questions)}")  

# List of questions, options, and correct answers  
quiz_questions = [  
    ("What is the capital of France?", ["London", "Berlin", "Paris", "Madrid"], "Paris"),  
    ("What is 2 + 2?", ["3", "4", "5", "6"], "4"),  
    ("What is the color of the sky?", ["Blue", "Green", "Red", "Yellow"], "Blue"),  
]  

# Run the quiz  
if __name__ == "__main__":  
    run_quiz(quiz_questions)