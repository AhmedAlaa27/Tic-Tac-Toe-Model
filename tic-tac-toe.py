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
