import math

# Define constants for player X, player O, and empty cell
PLAYER_X = 'X'
PLAYER_O = 'O'
EMPTY = ' '

# Define the Tic-Tac-Toe board size
BOARD_SIZE = 3

# Function to print the board
def print_board(board):
    for row in board:
        print("|".join(row))
        print("-" * (BOARD_SIZE * 2 - 1))

# Function to check if a player has won
def check_winner(board, player):
    # Check rows
    for row in board:
        if all(cell == player for cell in row):
            return True
    # Check columns
    for col in range(BOARD_SIZE):
        if all(board[row][col] == player for row in range(BOARD_SIZE)):
            return True
    # Check diagonals
    if all(board[i][i] == player for i in range(BOARD_SIZE)) or \
       all(board[i][BOARD_SIZE - i - 1] == player for i in range(BOARD_SIZE)):
        return True
    return False

# Function to check if the board is full
def is_board_full(board):
    return all(cell != EMPTY for row in board for cell in row)

# Function to evaluate the board for the minimax algorithm
def evaluate(board):
    if check_winner(board, PLAYER_X):
        return 1
    elif check_winner(board, PLAYER_O):
        return -1
    else:
        return 0

# Minimax algorithm implementation
def minimax(board, depth, maximizing_player):
    if check_winner(board, PLAYER_X):
        return 1
    elif check_winner(board, PLAYER_O):
        return -1
    elif is_board_full(board):
        return 0
    
    if maximizing_player:
        max_eval = -math.inf
        for row in range(BOARD_SIZE):
            for col in range(BOARD_SIZE):
                if board[row][col] == EMPTY:
                    board[row][col] = PLAYER_X
                    eval = minimax(board, depth + 1, False)
                    board[row][col] = EMPTY
                    max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = math.inf
        for row in range(BOARD_SIZE):
            for col in range(BOARD_SIZE):
                if board[row][col] == EMPTY:
                    board[row][col] = PLAYER_O
                    eval = minimax(board, depth + 1, True)
                    board[row][col] = EMPTY
                    min_eval = min(min_eval, eval)
        return min_eval

# Function to find the best move for the AI player
def find_best_move(board):
    best_eval = -math.inf
    best_move = None
    for row in range(BOARD_SIZE):
        for col in range(BOARD_SIZE):
            if board[row][col] == EMPTY:
                board[row][col] = PLAYER_X
                eval = minimax(board, 0, False)
                board[row][col] = EMPTY
                if eval > best_eval:
                    best_eval = eval
                    best_move = (row, col)
    return best_move

# Function to play the game
def play_game():
    board = [[EMPTY] * BOARD_SIZE for _ in range(BOARD_SIZE)]
    print("Welcome to Tic-Tac-Toe!")
    print_board(board)
    while True:
        # Player's move
        row, col = map(int, input("Enter row and column for your move (e.g., 1 2): ").split())
        row -= 1
        col -= 1
        if board[row][col] != EMPTY:
            print("Invalid move! Cell is already occupied.")
            continue
        board[row][col] = PLAYER_O
        print_board(board)
        if check_winner(board, PLAYER_O):
            print("Congratulations! You win!")
            break
        if is_board_full(board):
            print("It's a tie!")
            break
        
        # AI's move
        print("AI is thinking...")
        row, col = find_best_move(board)
        board[row][col] = PLAYER_X
        print(f"AI's move: ({row + 1}, {col + 1})")
        print_board(board)
        if check_winner(board, PLAYER_X):
            print("AI wins!")
            break
        if is_board_full(board):
            print("It's a tie!")
            break

# Play the game
play_game()
