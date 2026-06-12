# Project 84 - Tic Tac Toe command line game implementation.
# 1- Define global winning combinations and board utilities:

WIN_COMBINATIONS = [
    (0, 1, 2), (3, 4, 5), (6, 7, 8),
    (0, 3, 6), (1, 4, 7), (2, 5, 8),
    (0, 4, 8), (2, 4, 6),
]


# 2- create the board factory

def create_board():
    return [" "] * 9


# 3- display the board

def display_board(board):
    def cell(i):
        return board[i] if board[i] != " " else str(i + 1)

    print()
    print(f" {cell(0)} | {cell(1)} | {cell(2)} ")
    print("---+---+---")
    print(f" {cell(3)} | {cell(4)} | {cell(5)} ")
    print("---+---+---")
    print(f" {cell(6)} | {cell(7)} | {cell(8)} ")
    print()


# 4- check for winner

def has_winner(board, player):
    return any(
        board[a] == board[b] == board[c] == player
        for a, b, c in WIN_COMBINATIONS
    )


# 5- check if board is full

def board_full(board):
    return " " not in board


# 6- validate moves

def valid_move(board, position):
    if position < 1 or position > 9:
        return False
    return board[position - 1] == " "


# 7- apply a move

def apply_move(board, position, player):
    board[position - 1] = player


# 8- ask human for a move

def ask_move(board):
    while True:
        entry = input("Choose a cell (1-9): ").strip()
        try:
            pos = int(entry)
        except ValueError:
            print("Please enter a number from 1 to 9.")
            continue
        if valid_move(board, pos):
            return pos
        print("Cell occupied or out of range. Try again.")


# 9- minimax algorithm for the AI

def minimax(board, is_ai_turn, ai_player, human_player):
    if has_winner(board, ai_player):
        return 10
    if has_winner(board, human_player):
        return -10
    if board_full(board):
        return 0

    if is_ai_turn:
        best = -float("inf")
        for i in range(9):
            if board[i] == " ":
                board[i] = ai_player
                score = minimax(board, False, ai_player, human_player)
                board[i] = " "
                best = max(best, score)
        return best

    worst = float("inf")
    for i in range(9):
        if board[i] == " ":
            board[i] = human_player
            score = minimax(board, True, ai_player, human_player)
            board[i] = " "
            worst = min(worst, score)
    return worst


# 10- find best move for AI

def best_move_ai(board, ai_player, human_player):
    best_score = -float("inf")
    best_pos = None
    for i in range(9):
        if board[i] == " ":
            board[i] = ai_player
            score = minimax(board, False, ai_player, human_player)
            board[i] = " "
            if score > best_score:
                best_score = score
                best_pos = i + 1
    return best_pos


# 11- two-player mode

def play_two_players():
    board = create_board()
    turn = "X"

    while True:
        display_board(board)
        print(f"Player {turn}'s turn")
        pos = ask_move(board)
        apply_move(board, pos, turn)

        if has_winner(board, turn):
            display_board(board)
            print(f"Player {turn} wins!")
            break
        if board_full(board):
            display_board(board)
            print("Draw.")
            break

        turn = "O" if turn == "X" else "X"


# 12- play against AI

def play_vs_ai():
    board = create_board()
    human = "X"
    ai = "O"
    human_turn = True

    print("\nYou are X. The AI is O.")
    print("If you want chances, try to win or draw.\n")

    while True:
        display_board(board)

        if human_turn:
            print("Your turn (X)")
            pos = ask_move(board)
            apply_move(board, pos, human)

            if has_winner(board, human):
                display_board(board)
                print("You won!")
                break
            if board_full(board):
                display_board(board)
                print("Draw.")
                break

            human_turn = False
        else:
            print("AI is thinking...")
            pos = best_move_ai(board, ai, human)
            apply_move(board, pos, ai)
            print(f"AI played in cell {pos}")

            if has_winner(board, ai):
                display_board(board)
                print("AI wins.")
                break
            if board_full(board):
                display_board(board)
                print("Draw.")
                break

            human_turn = True


# 13- main menu

def main():
    print("=== TIC TAC TOE ===")
    print("1. Two players")
    print("2. Play vs AI")
    option = input("Choose mode (1 or 2): ").strip()

    if option == "1":
        play_two_players()
    elif option == "2":
        play_vs_ai()
    else:
        print("Invalid option.")


if __name__ == "__main__":
    main()

# Note: Minimax AI is strong even more than i expected; it's very hard to beat. Consider adding difficulty levels later.