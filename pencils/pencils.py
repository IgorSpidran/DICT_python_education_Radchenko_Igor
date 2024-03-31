import random


# Функція для перевірки чи гра закінчилася
def is_game_over(pencils_count):
    return pencils_count == 0


# Функція для визначення переможця
def get_winner(player):
    return "Jack" if player == "John" else "John"


# Функція для вибору кількості олівців, які візьме бот
def choose_pencils_to_take(pencils_count):
    if pencils_count % 4 == 0:
        return random.randint(1, 3)
    else:
        return pencils_count % 4


def main():
    # Попросіть користувача ввести кількість олівців
    while True:
        pencils_count_input = input("How many pencils would you like to use:\n> ")
        try:
            pencils_count = int(pencils_count_input)
            if pencils_count <= 0:
                print("The number of pencils should be positive.")
                continue
            break
        except ValueError:
            print("The number of pencils should be numeric.")

    # Попросіть користувача вказати, хто буде першим гравцем
    first_player = input("Who will be the first (John, Jack):\n> ")
    if first_player not in ["John", "Jack"]:
        print("Choose between 'John' and 'Jack'")
        return

    # Друкуємо кількість олівців у вигляді вертикальної смуги
    print("|" * pencils_count)

    # Основний цикл гри
    while not is_game_over(pencils_count):
        if first_player == "Jack":
            pencils_taken = choose_pencils_to_take(pencils_count)
            print(f"Jack's turn:\n{pencils_taken}")
            pencils_count -= pencils_taken
        else:
            while True:
                try:
                    pencils_taken = int(input(f"{first_player}'s turn:\n> "))
                    if pencils_taken < 1 or pencils_taken > 3 or pencils_taken > pencils_count:
                        print("Invalid input. Possible values: '1', '2' or '3'")
                        continue
                    break
                except ValueError:
                    print("Invalid input. Possible values: '1', '2' or '3'")
            pencils_count -= pencils_taken

        # Виведення стану гри після ходу
        print("|" * pencils_count)

        # Перехід до іншого гравця
        first_player = "Jack" if first_player == "John" else "John"

    # Визначення переможця
    winner = get_winner(first_player)
    print(f"{winner} won!")


if __name__ == "__main__":
    main()
