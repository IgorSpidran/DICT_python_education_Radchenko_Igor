import random


def print_snake(domino_snake):
    if len(domino_snake) <= 6:
        print("Domino snake:", domino_snake)
    else:
        print("Domino snake:", domino_snake[:3], " ... ", domino_snake[-3:])


def print_player_pieces(player_pieces):
    print("Your pieces:")
    for i, piece in enumerate(player_pieces, start=1):
        print(f"{i}:{piece}")


def initialize_pieces():
    pieces = []
    for i in range(7):
        for j in range(i, 7):
            pieces.append([i, j])
    return pieces


def draw_pieces(stock_pieces, num_pieces):
    drawn_pieces = random.sample(stock_pieces, num_pieces)
    for piece in drawn_pieces:
        stock_pieces.remove(piece)
    return drawn_pieces, stock_pieces


def is_valid_move(piece, domino_snake):
    left_end, right_end = domino_snake[0][0], domino_snake[-1][1]
    return piece[0] in (left_end, right_end) or piece[1] in (left_end, right_end)


def make_move(player_pieces, domino_snake, stock_pieces, piece, position):
    if position == "left":
        if piece[1] == domino_snake[0][0]:
            domino_snake.insert(0, piece)
        else:
            domino_snake.insert(0, piece[::-1])
    elif position == "right":
        if piece[0] == domino_snake[-1][1]:
            domino_snake.append(piece)
        else:
            domino_snake.append(piece[::-1])
    player_pieces.remove(piece)


def evaluate_pieces(computer_pieces, domino_snake):
    count = {i: 0 for i in range(7)}
    for piece in computer_pieces:
        count[piece[0]] += 1
        count[piece[1]] += 1
    for piece in domino_snake:
        count[piece[0]] += 1
        count[piece[1]] += 1
    evaluations = {}
    for piece in computer_pieces:
        evaluation = count[piece[0]] + count[piece[1]]
        evaluations[piece] = evaluation
    return evaluations


def computer_turn(computer_pieces, domino_snake, stock_pieces):
    evaluations = evaluate_pieces(computer_pieces, domino_snake)
    sorted_pieces = sorted(evaluations.keys(), key=lambda x: evaluations[x], reverse=True)
    for piece in sorted_pieces:
        if is_valid_move(piece, domino_snake):
            position = "right" if random.choice([True, False]) else "left"
            make_move(computer_pieces, domino_snake, stock_pieces, piece, position)
            return piece
    return None


def main():
    stock_pieces = initialize_pieces()
    player_pieces, stock_pieces = draw_pieces(stock_pieces, 7)
    computer_pieces, stock_pieces = draw_pieces(stock_pieces, 7)
    domino_snake = [random.choice(stock_pieces)]
    stock_pieces.remove(domino_snake[0])

    while True:
        print("=" * 60)
        print("Stock size:", len(stock_pieces))
        print(f"Computer pieces: {len(computer_pieces)}")
        print_snake(domino_snake)
        print_player_pieces(player_pieces)

        if not player_pieces:
            print("Status: The game is over. You won!")
            break
        elif not computer_pieces:
            print("Status: The game is over. The computer won!")
            break
        elif len(set(sum(domino_snake, []))) == 14 and sum(
                piece.count(domino_snake[-1][1]) for piece in player_pieces) == 8:
            print("Status: The game is over. It's a draw!")
            break

        print("Status: It's your turn to make a move. Enter your command.")
        player_move = input("> ").strip()

        if player_move.isdigit():
            piece_index = int(player_move) - 1
            if 0 <= piece_index < len(player_pieces):
                piece = player_pieces[piece_index]
                if is_valid_move(piece, domino_snake):
                    position = "left" if piece[1] == domino_snake[0][0] else "right"
                    make_move(player_pieces, domino_snake, stock_pieces, piece, position)
                else:
                    print("Illegal move. Please try again.")
                    continue
            else:
                print("Invalid input. Please try again.")
                continue
        else:
            print("Invalid input. Please try again.")
            continue

        if not player_pieces:
            print("Status: The game is over. You won!")
            break
        elif not computer_pieces:
            print("Status: The game is over. The computer won!")
            break
        elif len(set(sum(domino_snake, []))) == 14 and sum(
                piece.count(domino_snake[-1][1]) for piece in player_pieces) == 8:
            print("Status: The game is over. It's a draw!")
            break

        input("Status: Computer is about to make a move. Press Enter to continue...")

        computer_move = computer_turn(computer_pieces, domino_snake, stock_pieces)
        if not computer_move:
            print("Computer decided to pass.")
        else:
            print("Computer's move:", computer_move)

    print_snake(domino_snake)


if __name__ == "__main__":
    main()
