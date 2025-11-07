import math

# Print the board
def print_board(board):
    for i, row in enumerate(board):
        print(" | ".join(row))
        if i < 2:
            print("-" * 5)

# Check winner
def check_winner(board):
    # Rows and columns
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != " ":
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != " ":
            return board[0][i]

    # Diagonals
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return board[0][2]

    return None

# Check if moves left
def moves_left(board):
    for row in board:
        if " " in row:
            return True
    return False

# Minimax Algorithm
def minimax(board, depth, is_maximizing):
    winner = check_winner(board)
    if winner == "O":
        return 1
    elif winner == "X":
        return -1
    elif not moves_left(board):
        return 0

    if is_maximizing:
        best_score = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "O"
                    score = minimax(board, depth + 1, False)
                    board[i][j] = " "
                    best_score = max(best_score, score)
        return best_score
    else:
        best_score = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "X"
                    score = minimax(board, depth + 1, True)
                    board[i][j] = " "
                    best_score = min(best_score, score)
        return best_score

# Best Move for AI
def best_move(board):
    best_score = -math.inf
    move = None
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = "O"
                score = minimax(board, 0, False)
                board[i][j] = " "
                if score > best_score:
                    best_score = score
                    move = (i, j)
    return move

# Main Game
def play():
    board = [[" " for _ in range(3)] for _ in range(3)]
    print("Welcome to Tic Tac Toe! You are X and AI is O.")
    print("Choose a cell (0-8) as shown below:")
    print("0 | 1 | 2")
    print("---------")
    print("3 | 4 | 5")
    print("---------")
    print("6 | 7 | 8\n")
    print_board(board)

    while True:
        # Player move
        try:
            cell = int(input("Enter your move (0-8): "))
            if not (0 <= cell <= 8):
                print("Invalid input. Please enter a number between 0 and 8.")
                continue

            row, col = divmod(cell, 3)  # convert cell number to row, col

            if board[row][col] != " ":
                print("Invalid move, spot already taken. Try again.")
                continue
        except ValueError:
            print("Invalid input. Enter a single number (0-8).")
            continue

        board[row][col] = "X"
        print_board(board)

        if check_winner(board) == "X":
            print("🎉 You win!")
            break
        elif not moves_left(board):
            print("🤝 It's a tie!")
            break

        # AI move
        move = best_move(board)
        if move:
            board[move[0]][move[1]] = "O"
            print("\nAI has made its move:")
            print_board(board)

        if check_winner(board) == "O":
            print("😈 AI wins!")
            break
        elif not moves_left(board):
            print("🤝 It's a tie!")
            break


if __name__ == "__main__":
    play()
