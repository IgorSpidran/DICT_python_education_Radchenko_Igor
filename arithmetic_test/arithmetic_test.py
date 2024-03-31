import random

def generate_question(level):
    if level == 1:
        # Генеруємо два випадкових числа в діапазоні від 2 до 9
        num1 = random.randint(2, 9)
        num2 = random.randint(2, 9)
        # Випадково обираємо арифметичну операцію
        operation = random.choice(['+', '-', '*'])
        # Складаємо рядок завдання
        question = f"{num1} {operation} {num2}"
        # Розраховуємо правильну відповідь
        if operation == '+':
            answer = num1 + num2
        elif operation == '-':
            answer = num1 - num2
        elif operation == '*':
            answer = num1 * num2
    elif level == 2:
        # Генеруємо випадкове число від 11 до 29
        num = random.randint(11, 29)
        # Складаємо рядок завдання
        question = f"{num} squared"
        # Розраховуємо правильну відповідь
        answer = num ** 2
    return question, answer

def save_result(name, correct_answers, level):
    result = f"{name}: {correct_answers}/5 in level {level} "
    if level == 1:
        result += "(simple operations with numbers 2-9)"
    elif level == 2:
        result += "(integral squares of 11-29)"
    with open("results.txt", "a") as file:
        file.write(result + "\n")

def main():
    # Запитуємо рівень складності
    while True:
        level = input("Which level do you want? Enter a number:\n1 - simple operations with numbers 2-9\n2 - integral squares of 11-29\n> ")
        if level in ['1', '2']:
            level = int(level)
            break
        else:
            print("Incorrect format.")
    correct_answers = 0
    # Виконуємо 5 завдань
    for _ in range(5):
        # Генеруємо завдання
        question, correct_answer = generate_question(level)
        # Виводимо завдання
        print(question)
        # Зчитуємо введення користувача
        user_answer = input("> ")
        try:
            user_answer = int(user_answer)
        except ValueError:
            print("Incorrect format.")
            continue
        # Перевіряємо відповідь
        if user_answer == correct_answer:
            print("Right!")
            correct_answers += 1
        else:
            print("Wrong!")
    # Виводимо результат
    print(f"Your mark is {correct_answers}/5. Would you like to save the result? Enter yes or no.")
    save = input("> ").lower()
    if save in ['yes', 'y']:
        name = input("What is your name?\n> ")
        save_result(name, correct_answers, level)
        print("The results are saved in \"results.txt\".")

if __name__ == "__main__":
    main()
