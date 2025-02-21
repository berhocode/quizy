# A simple MATH QUIZ GAME, by Aymane Berhoua - @berhocode
# Program name: Quizy+

import random
import time

def generate_question(difficulty):
    operations = ['+', '-', '*', '/']
    op = random.choice(operations)
    
    if difficulty == 'easy':
        num1, num2 = random.randint(1, 10), random.randint(1, 10)
    elif difficulty == 'medium':
        num1, num2 = random.randint(10, 50), random.randint(10, 50)
    else:  # hard
        num1, num2 = random.randint(50, 100), random.randint(1, 100)
    
    if op == '/' and num2 == 0:
        num2 = 1  # Avoid division by zero
    
    question = f"{num1} {op} {num2}"
    answer = eval(question)
    return question, round(answer, 2)

def math_quiz():
    sentence = "Welcome to the Math Quiz Game!"

    for i in range(len(sentence)):
        print(f"\r{sentence[:i+1]}", end="")
        time.sleep(0.1)  # Adjust speed if needed

    print()


    difficulty = input("Choose difficulty (easy, medium, hard): ").lower()
    
    if difficulty not in ['easy', 'medium', 'hard']:
        print("Invalid difficulty level! Defaulting to easy.")
        difficulty = 'easy'
    
    score = 0
    total_questions = 5
    
    for _ in range(total_questions):
        question, correct_answer = generate_question(difficulty)
        
        try:
            user_answer = float(input(f"Solve: {question} = "))
            if user_answer == correct_answer:
                print("Correct! 🎉")
                score += 1
            else:
                print(f"Wrong! The correct answer was {correct_answer}.")
        except ValueError:
            print("Invalid input! Skipping question.")
    
    print(f"\nGame Over! Your final score: {score}/{total_questions}")
    
if __name__ == "__main__":
    math_quiz()