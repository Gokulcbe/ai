# Constants for players
PLAYER_X = 'X'
PLAYER_O = 'O'
EMPTY = ' '

def print_board(board):
    for row in board:
        print("|".join(row))
        print("-----")
    print()

def evaluate(board):
    # Check rows, columns, and diagonals for a win
    for row in board:
        if row.count(PLAYER_X) == 3:
            return 10
        elif row.count(PLAYER_O) == 3:
            return -10

    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != EMPTY:
            if board[0][col] == PLAYER_X:
                return 10
            else:
                return -10

    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != EMPTY:
        if board[0][0] == PLAYER_X:
            return 10
        else:
            return -10

    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != EMPTY:
        if board[0][2] == PLAYER_X:
            return 10
        else:
            return -10

    # If no winner, it's a tie
    return 0

def is_moves_left(board):
    for row in board:
        if EMPTY in row:
            return True
    return False

def minimax(board, depth, is_maximizing):
    score = evaluate(board)
    if score == 10:
        return score - depth
    if score == -10:
        return score + depth
    if not is_moves_left(board):
        return 0
    if is_maximizing:
        best = -float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == EMPTY:
                    board[i][j] = PLAYER_X
                    best = max(best, minimax(board, depth+1, not is_maximizing))
                    board[i][j] = EMPTY
        return best
    else:
        best = float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == EMPTY:
                    board[i][j] = PLAYER_O
                    best = min(best, minimax(board, depth+1, not is_maximizing))
                    board[i][j] = EMPTY
        return best

def find_best_move(board):
    best_val = -float('inf')
    best_move = (-1, -1)
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                board[i][j] = PLAYER_X
                move_val = minimax(board, 0, False)
                board[i][j] = EMPTY
                if move_val > best_val:
                    best_move = (i, j)
                    best_val = move_val
    return best_move

def play_game():
    board = [[EMPTY]*3 for _ in range(3)]
    print("Welcome to Tic Tac Toe!")
    print_board(board)
    while True:
        # Player's move
        while True:
            row = int(input("Enter row (0, 1, or 2): "))
            col = int(input("Enter column (0, 1, or 2): "))
            if board[row][col] == EMPTY:
                board[row][col] = PLAYER_O
                break
            else:
                print("That spot is already taken. Try again.")

        print_board(board)

        # Check if player wins
        if evaluate(board) == -10:
            print("You win!")
            break

        # Check for tie
        if not is_moves_left(board):
            print("It's a tie!")
            break

        # AI's move
        print("AI's move:")
        ai_move = find_best_move(board)
        board[ai_move[0]][ai_move[1]] = PLAYER_X
        print_board(board)

        # Check if AI wins
        if evaluate(board) == 10:
            print("AI wins!")
            break

        # Check for tie
        if not is_moves_left(board):
            print("It's a tie!")
            break

play_game()
