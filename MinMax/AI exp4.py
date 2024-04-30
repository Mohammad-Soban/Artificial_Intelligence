def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board, player):
    # Check rows, columns, and diagonals
    for i in range(3):
        if all([cell == player for cell in board[i]]) or all([board[j][i] == player for j in range(3)]):
            return True
    if all([board[i][i] == player for i in range(3)]) or all([board[i][2-i] == player for i in range(3)]):
        return True
    return False

def is_full(board):
    return all([cell != ' ' for row in board for cell in row])

def minimax(board, depth, is_maximizing):
    if check_winner(board, 'O'):
        return 10 - depth
    elif check_winner(board, 'X'):
        return -10 + depth
    elif is_full(board):
        return 0

    if is_maximizing:
        best_score = float('-inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'O'
                    score = minimax(board, depth + 1, False)
                    board[i][j] = ' '
                    best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'X'
                    score = minimax(board, depth + 1, True)
                    board[i][j] = ' '
                    best_score = min(score, best_score)
        return best_score

def make_best_move(board):
    best_move = None
    best_score = float('-inf')
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = 'O'
                score = minimax(board, 0, False)
                board[i][j] = ' '
                if score > best_score:
                    best_score = score
                    best_move = (i, j)
    return best_move

def main():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    print_board(board)
    while True:
        while True:
            try:
                x, y = map(int, input("Enter your move (row, column): ").split())
                if x < 0 or x > 2 or y < 0 or y > 2:
                    print("Invalid input. Row and column must be between 0 and 2.")
                    continue
                if board[x][y] != ' ':
                    print("Cell already occupied. Try again.")
                    continue
                break
            except ValueError: 
                print("Invalid input. Please enter two integers separated by a space.")
        board[x][y] = 'X'
        print_board(board)
        if check_winner(board, 'X'):
            print("You win!")
            break
        if is_full(board):
            print("It's a tie!")
            break
        print("Computer's turn:")
        computer_move = make_best_move(board)
        board[computer_move[0]][computer_move[1]] = 'O'
        print_board(board)
        if check_winner(board, 'O'):
            print("Computer wins!")
            break
        if is_full(board):
            print("It's a tie!")
            break

if __name__ == "__main__":
    main()
  