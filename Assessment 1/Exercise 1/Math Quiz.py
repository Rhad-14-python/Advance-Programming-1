import random

def displayMenu():
    print("DIFFICULTY LEVEL")
    print(" 1. Easy Mode")
    print(" 2. Moderate Mode")
    print(" 3. Advanced Mode")
    choice = int(input("Choose which difficulty level you prefer(1-3): "))
    return choice

def randomInt(min_val, max_val):
    return random.randint(min_val, max_val)

def decideOperation():
    return random.choice(['+', '-'])

def displayProblem(num1, num2, operation):
    print(f"{num1} {operation} {num2} = ?")
    answer = int(input("Here is your answer: "))
    return answer

def isCorrect(user_answer, correct_answer, second_attempt=False):
    if user_answer == correct_answer:
        print("Correct!")
        return True, 10 if not second_attempt else 5
    else:
        if second_attempt:
            print(f"Nice try but the correct answer is {correct_answer}.")
        else:
            print("Incorrect, please try again!")
        return False, 0

def displayResults(score):
    print(f"\nHere is your final score: {score}/100")
    if score > 90:
        grade = "A+"
    elif score > 80:
        grade = "A"
    elif score > 70:
        grade = "B"
    elif score > 60:
        grade = "C"
    else:
        grade = "F"
    print(f"Your grade: {grade}")

def main():
    while True:
        score = 0
        difficulty = displayMenu()
        
        if difficulty == 1:
            min_val, max_val = 1, 9
        elif difficulty == 2:
            min_val, max_val = 10, 99
        elif difficulty == 3:
            min_val, max_val = 1000, 9999
        else:
            print("Invalid choice. Try again.")
            continue

        for _ in range(10):
            num1 = randomInt(min_val, max_val)
            num2 = randomInt(min_val, max_val)
            operation = decideOperation()
            
            if operation == '-' and num1 < num2:
                num1, num2 = num2, num1

            correct_answer = eval(f"{num1} {operation} {num2}")
            user_answer = displayProblem(num1, num2, operation)

            correct, points = isCorrect(user_answer, correct_answer)
            score += points
            
            if not correct:
                user_answer = int(input("Your second attempt: "))
                _, points = isCorrect(user_answer, correct_answer, second_attempt=True)
                score += points

        displayResults(score)
        play_again = input("\nWould you like to play again? (yes/no): ").strip().lower()
        if play_again != 'yes':
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    main()
