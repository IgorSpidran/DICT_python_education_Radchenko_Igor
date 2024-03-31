import random


def get_computer_choice(options):
    return random.choice(options)


def find_winner(user_choice, computer_choice, options):
    if user_choice == computer_choice:
        return "There is a draw (" + computer_choice + ")"
    elif (user_choice in options[:len(options) // 2]) and (computer_choice in options[len(options) // 2:]):
        return "Well done. The computer chose " + computer_choice + " and failed"
    elif (user_choice in options[len(options) // 2:]) and (computer_choice in options[:len(options) // 2]):
        return "Sorry, but the computer chose " + computer_choice
    else:
        return "Invalid input"


def update_rating(user_choice, computer_choice, user_rating):
    if user_choice == computer_choice:
        user_rating += 50
    elif user_choice in ['rock', 'paper', 'scissors']:
        user_rating += 100
    return user_rating


def write_rating_to_file(ratings):
    with open("rating.txt", "w") as file:
        for name, rating in ratings.items():
            file.write(name + " " + str(rating) + "\n")


def main():
    user_name = input("Enter your name: ").strip()
    print("Hello, " + user_name)

    try:
        with open("rating.txt", "r") as file:
            ratings = dict([line.strip().split() for line in file])
            user_rating = int(ratings.get(user_name, 0))
    except FileNotFoundError:
        ratings = {}
        user_rating = 0

    options_input = input(
        "Enter options separated by comma (or press Enter for default options - rock, paper, scissors): ").strip()
    options = options_input.split(",") if options_input else ['rock', 'paper', 'scissors']

    print("Okay, let's start")

    while True:
        user_input = input("> ").lower()

        if user_input == "!exit":
            print("Bye!")
            write_rating_to_file(ratings)
            break
        elif user_input == "!rating":
            print("Your rating:", user_rating)
        elif user_input in options:
            computer_choice = get_computer_choice(options)
            print(find_winner(user_input, computer_choice, options))
            user_rating = update_rating(user_input, computer_choice, user_rating)
            ratings[user_name] = user_rating
        else:
            print("Invalid input")


if __name__ == "__main__":
    main()
