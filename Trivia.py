import random

questions = {
    "What is the capital of India?": "New Delhi",
    "Which planet is known as the Red Planet?": "Mars",
    "Who wrote the national anthem of India?": "Rabindranath Tagore",
    "What is the largest ocean in the world?": "Pacific Ocean",
    "Which animal is known as the King of the Jungle?": "Lion",
    "How many continents are there on Earth?": "7",
    "What is the chemical symbol for water?": "H2O",
    "Which year did India gain independence?": "1947",
    "What is the fastest land animal?": "Cheetah",
    "Who is known as the Father of the Indian Constitution?": "Dr. B.R.Ambedkar"
}

def trivia_game():
    questions_list = list(questions.keys())
    total_questions = 5
    score = 0

    selected_question = random.sample(questions_list, total_questions)

    for index, question in enumerate(selected_question):
        print(f"{index + 1}. {question}")
        user_answer = input("Your answer: ").lower().strip()
        correct_answer = questions[question]
        
        if user_answer == correct_answer.lower():
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! The correct answer is: {correct_answer}.\n")    

    print(f"Game Over! Your Score is: {score}/{total_questions}")

trivia_game()