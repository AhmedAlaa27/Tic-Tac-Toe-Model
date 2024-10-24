import math

board = [' ' for _ in range(9)]

def print_board():
    """Prints the current state of the Tic-Tac-Toe board."""
    for row in [board[i * 3:(i + 1) * 3] for i in range(3)]:
        print('| ' + ' | '.join(row) + ' |')

def check_winner(board, player):
    """Checks if the given player has won the game."""
    winning_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columns
        [0, 4, 8], [2, 4, 6]              # diagonals
    ]
    for combo in winning_combinations:
        if all(board[i] == player for i in combo):
            return True
    return False

def is_board_full(board):
    """Checks if the board is full."""
    return ' ' not in board

def switch_player(current_player):
    """Switches between the two players."""
    return 'O' if current_player == 'X' else 'X'


def make_move(board, position, player):
    """Allows a player to place their mark on the board."""
    if board[position] == ' ':
        board[position] = player
        return True
    return False


def check_game_over(board, player):
    """Checks if the game has ended (win or draw)."""
    if check_winner(board, player):
        print(f"Player {player} wins!")
        return True
    elif is_board_full(board):
        print("The game is a draw!")
        return True
    return False


def get_user_input():
    """Gets the player's move input."""
    while True:
        try:
            user_input = int(input("Enter your move (1-9): ")) - 1
            if user_input >= 0 and user_input < 9:
                return user_input
            else:
                print("Invalid input. Please choose a number between 1 and 9.")
        except ValueError:
            print("Invalid input. Please enter a number.")


def minimax(board, depth, is_maximizing):
    """Recursive Minimax function to evaluate game states."""
    
    # BASE CASES
    if check_winner(board, 'O'):
        return 1
    elif check_winner(board, 'X'):
        return -1
    elif is_board_full(board):
        return 0
    
    # MAXIMIZING PLAYER (AI)
    if is_maximizing:
        best_score = -math.inf
        for i in range(len(board)):
            if board[i] == ' ':
                board[i] = 'O'
                score = minimax(board, depth + 1, False)
                board[i] = ' '
                best_score = max(best_score, score)
        return best_score
    # MINIMIZING PLAYER (HUMAN)
    else:
        best_score = math.inf
        for i in range(len(board)):
            if board[i] == ' ':
                board[i] = 'X'
                score = minimax(board, depth + 1, True)
                board[i] = ' '
                best_score = min(best_score, score)
        return best_score
            

def get_ai_move():
    """Determines the AI's best move using the Minimax algorithm."""
    best_score = -math.inf
    best_move = None
    
    for i in range(len(board)):
        if board[i] == ' ':
            board[i] = 'O'
            score = minimax(board, 0, False)
            board[i] = ' '
            
            if score > best_score:
                best_score = score
                best_move = i
    return best_move

def play_game():
    print("Welcome to Tic-Tac-Toe!")
    print_board()

    current_player = 'X'

    while True:
        if current_player == 'X':
            position = get_user_input()
            if make_move(board, position, current_player):
                print_board()
                if check_game_over(board, current_player):
                    break
                current_player = switch_player(current_player)
        else:
            print("AI's turn!")
            position = get_ai_move()
            if make_move(board, position, current_player):
                print_board()
                if check_game_over(board, current_player):
                    break
                current_player = switch_player(current_player)

play_game()
