def utility(board):
    # Count the number of black coins on the board
    return board.count('B')

def is_terminal_state(board):
    # Check if there is no empty block on the board
    return '0' not in board

def convert_coins(board):
    # Convert consecutive black coins to white coins and vice versa
    new_board = list(board)

    for i in range(len(new_board)):
        if new_board[i] == 'B':
            new_board[i] = 'W'
        elif new_board[i] == 'W':
            new_board[i] = 'B'

    return ''.join(new_board)

def print_board(board):
    print("Current Board:", board.replace('0', '_'))

def min_value(board):
    if is_terminal_state(board):
        print_board(board)
        return utility(board)

    v = float('inf')
    empty_blocks = [i for i, block in enumerate(board) if block == '0']

    for block in empty_blocks:
        new_board = board[:block] + 'B' + board[block+1:]
        new_board = convert_coins(new_board)
        print_board(new_board)
        v = min(v, max_value(new_board))

    return v

def max_value(board):
    if is_terminal_state(board):
        print_board(board)
        return utility(board)

    v = float('-inf')
    empty_blocks = [i for i, block in enumerate(board) if block == '0']

    for block in empty_blocks:
        new_board = board[:block] + 'W' + board[block+1:]
        new_board = convert_coins(new_board)
        print_board(new_board)
        v = max(v, min_value(new_board))

    return v

def mini_max(board):
    return max_value(board)

# Example usage
input_board = "0000W00BBW0"
result = mini_max(input_board)
print("Utility of Player 1 (Player MAX):", result)
