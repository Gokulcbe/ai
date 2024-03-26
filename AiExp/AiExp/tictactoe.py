import math

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def is_winner(board, player):
    # Check rows
    for row in board:
        if all(cell == player for cell in row):
            return True
    # Check columns
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    # Check diagonals
    if all(board[i][i] == player for i in range(3)) or \
       all(board[i][2-i] == player for i in range(3)):
        return True
    return False

def is_full(board):
    return all(cell != " " for row in board for cell in row)

def get_empty_cells(board):
    return [(i, j) for i in range(3) for j in range(3) if board[i][j] == " "]

def minimax(board, depth, maximizing):
    if is_winner(board, "X"):
        return 1
    elif is_winner(board, "O"):
        return -1
    elif is_full(board):
        return 0

    if maximizing:
        max_eval = -math.inf
        for i, j in get_empty_cells(board):
            board[i][j] = "X"
            eval = minimax(board, depth+1, False)
            board[i][j] = " "
            max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = math.inf
        for i, j in get_empty_cells(board):
            board[i][j] = "O"
            eval = minimax(board, depth+1, True)
            board[i][j] = " "
            min_eval = min(min_eval, eval)
        return min_eval

def get_best_move(board):
    best_eval = -math.inf
    best_move = None
    for i, j in get_empty_cells(board):
        board[i][j] = "X"
        eval = minimax(board, 0, False)
        board[i][j] = " "
        if eval > best_eval:
            best_eval = eval
            best_move = (i, j)
    return best_move

def main():
    board = [[" "]*3 for _ in range(3)]
    current_player = "X"
    
    while True:
        print_board(board)
        if current_player == "X":
            i, j = map(int, input("Enter row and column (0-2) for your move: ").split())
            if board[i][j] != " ":
                print("Cell already occupied. Try again.")
                continue
            board[i][j] = current_player
        else:
            print("AI is thinking...")
            i, j = get_best_move(board)
            board[i][j] = current_player
        if is_winner(board, current_player):
            print_board(board)
            print(f"{current_player} wins!")
            break
        if is_full(board):
            print_board(board)
            print("It's a draw!")
            break
        current_player = "O" if current_player == "X" else "X"

if __name__ == "__main__":
    main()
