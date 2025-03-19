def display_board(board):
    #display the board
    print("\n")
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print("\n")

def player_input(board, player_symbol):
    #prompts player to input position
    #check if position is valid and if it is not taken
    while True:
        try:
            choice = int(input(f"Player {player_symbol}, choose a position (1-9): "))
            if choice < 1 or choice > 9:
                print("Invalid input. Position must be between 1 and 9.")
            elif board[choice - 1] != ' ':
                print("That position is already taken. Choose another.")
            else:
                board[choice - 1] = player_symbol
                break
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 9.")

def check_win(board, player_symbol):
    #check if player has won
    # Possible winning combinations (indices)
    win_combinations = [
        [0, 1, 2],  # row 1
        [3, 4, 5],  # row 2
        [6, 7, 8],  # row 3
        [0, 3, 6],  # column 1
        [1, 4, 7],  # column 2
        [2, 5, 8],  # column 3
        [0, 4, 8],  # diagonal top-left to bottom-right
        [2, 4, 6]   # diagonal top-right to bottom-left
    ]
    
    for combo in win_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] == player_symbol:
            return True
    return False

def check_draw(board):
    #check if game is a draw
    return ' ' not in board

def play():
    # Create a board filled with spaces
    board = [' '] * 9
    current_player = 'X'  # 'X' always goes first in this example
    
    display_board(board)  # Show initial empty board
    
    while True:
        # Prompt current player for input
        player_input(board, current_player)
        
        # Display board after the move
        display_board(board)
        
        # Check for a win
        if check_win(board, current_player):
            print(f"Player {current_player} wins!")
            break
        
        # Check for a draw
        if check_draw(board):
            print("It's a draw!")
            break
        
        # Switch player
        current_player = 'O' if current_player == 'X' else 'X'

if __name__ == "__main__":
    play()
