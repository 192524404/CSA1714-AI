board = [' ' for _ in range(9)]

def print_board():
    for i in range(0, 9, 3):
        print(f" {board[i]} | {board[i+1]} | {board[i+2]} ")
        if i < 6:
            print("---|---|---")

def check_winner(player):
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8], # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8], # Columns
        [0, 4, 8], [2, 4, 6]              # Diagonals
    ]
    return any(all(board[pos] == player for pos in combo) for combo in win_conditions)

def play_game():
    current_player = 'X'
    for turn in range(9):
        print_board()
        move = int(input(f"Player {current_player}, enter position (0-8): "))
        if board[move] == ' ':
            board[move] = current_player
            if check_winner(current_player):
                print_board()
                print(f"Player {current_player} wins!")
                return
            current_player = 'O' if current_player == 'X' else 'X'
        else:
            print("Invalid move! Try again.")
    print_board()
    print("It's a draw!")

# Run game (Interactive)
if __name__ == "__main__":
    play_game()
