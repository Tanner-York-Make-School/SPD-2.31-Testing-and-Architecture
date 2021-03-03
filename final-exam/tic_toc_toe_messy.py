"""
Tic Tac Toe
Reference: With modification from http://inventwithpython.com/chapter10.html.

# TODOs:
# 1. Find all TODO items and see whether you can improve the code.
#    In most cases (if not all), you can make them more readable/modular.
# 2. Add/fix function's docstrings
"""

import random

# I didn't refactor the draw and is_winner, that uses the magic number 10,
# function because that would be drastically changing how the
# code works. Instead of creating a normal tic tac toe game like intended,
# it would add a new feature for creating larger boards, no longer making this
# refactoring but adding a new feature.

def draw_board(board):
    """This function prints out the board that it was passed."""
    # "board" is a list of 10 strings representing the board (ignore index 0)
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')

def input_player_letter():
    """Lets the player type which letter they want to be. Returns a list with the
    player’s letter as the first item, and the computer's letter as the second."""
    letter = ''
    while letter not in ('X', 'O'):
        print('Do you want to be X or O?')
        letter = input().upper()

    # the first element in the list is the player’s letter, the second is the computer's letter.
    if letter == 'X':
        return ['X', 'O']
    return ['O', 'X']

def who_goes_first():
    """Randomly choose the player who goes first."""
    if random.randint(0, 1) == 0:
        return 'computer'
    return 'player'

def play_again():
    """Returns True if the player wants to play again, otherwise it returns False."""
    print('Do you want to play again? (yes or no)')
    return input().lower().startswith('y')

def make_move(board, letter, move):
    """Makes a move on the given board with the given letter and move"""
    board[move] = letter

def is_winner(board, letter):
    """Given a board and a player’s letter, this function returns True if
    that player has won."""
    return ((board[1] == letter and board[2] == letter and board[3] == letter) or # across the top
      (board[4] == letter and board[5] == letter and board[6] == letter) or # across the middle
      (board[7] == letter and board[8] == letter and board[9] == letter) or # across the bottom
      (board[1] == letter and board[4] == letter and board[7] == letter) or # down the left side
      (board[2] == letter and board[5] == letter and board[8] == letter) or # down the middle
      (board[3] == letter and board[6] == letter and board[9] == letter) or # down the right side
      (board[3] == letter and board[5] == letter and board[7] == letter) or # diagonal
      (board[1] == letter and board[5] == letter and board[9] == letter)) # diagonal

def get_board_copy(board):
    """Make a duplicate of the board list and return it the duplicate."""
    return list(board)

def is_space_free(board, move):
    """Return true if the passed move is free on the passed board."""
    return board[move] == ' '

def get_player_move(board):
    """Let the player type in their move."""
    player_move = ' '
    options = set(str(i) for i in range(1, len(board)))
    while (player_move not in options or
      not is_space_free(board, int(player_move))):
        print('What is your next move? (1-9)')
        player_move = input()
    return int(player_move)

def choose_random_move_from_list(board, moves_list):
    """Returns a valid move from the passed list on the passed board or None
    if there is no valid move."""
    possible_moves = []
    for i in moves_list:
        if is_space_free(board, i):
            possible_moves.append(i)
    if possible_moves:
        return random.choice(possible_moves)

def is_next_move_win(board, letter):
    """Returns true is if the given letter can make a winning move, false if not"""
    for i in range(1, 10):
        copy = get_board_copy(board)
        if is_space_free(copy, i):
            make_move(copy, letter, i)
            if is_winner(copy, letter):
                return i

def get_computer_move(board, temp_computer_letter):
    """Given a board and the computer's letter, determine where to move and return that move."""
    if temp_computer_letter == 'X':
        temp_player_letter = 'O'
    else:
        temp_player_letter = 'X'

    # Here is our algorithm for our Tic Tac Toe AI:
    # First, check if we can win in the next move
    is_ai_winner = is_next_move_win(board, temp_computer_letter)
    if is_ai_winner:
        return is_ai_winner

    # Check if the player could win on their next move, and block them.
    is_player_winner = is_next_move_win(board, temp_player_letter)
    if is_player_winner:
        return is_player_winner

    # Try to take one of the corners, if they are free.
    move = choose_random_move_from_list(board, [1, 3, 7, 9])
    if move is not None:
        return move

    # Try to take the center, if it is free.
    if is_space_free(board, 5):
        return 5

    # Move on one of the sides.
    return choose_random_move_from_list(board, [2, 4, 6, 8])

def is_board_full(board):
    """Return True if every space on the board has been taken.
    Otherwise return False."""
    for i in range(1, len(board)):
        if is_space_free(board, i):
            return False
    return True

def start_new_round(board, temp_player_letter, temp_computer_letter, temp_turn):
    """Starts a round and plays it through untill the player and computer takes their turn"""
    while True:
        if temp_turn == 'player':
            # Player’s turn.
            draw_board(board)
            move = get_player_move(board)
            make_move(board, temp_player_letter, move)

            if is_winner(board, temp_player_letter):
                draw_board(board)
                print('Hooray! You have won the game!')
                break

            temp_turn = 'computer'

        else:
            # Computer’s turn.
            move = get_computer_move(board, temp_computer_letter)
            make_move(board, temp_computer_letter, move)

            if is_winner(board, temp_computer_letter):
                draw_board(board)
                print('The computer has beaten you! You lose.')
                break

            temp_turn = 'player'

        if is_board_full(board):
            draw_board(board)
            print('The game is a tie!')
            break

def start_session(board_size=10):
    """Starts a session for playing mutliple games with the bot"""
    print('Welcome to Tic Tac Toe!')
    while True:

        # Reset the board
        the_board = [' '] * board_size
        player_letter, computer_letter = input_player_letter()
        turn = who_goes_first()
        print('The ' + turn + ' will go first.')

        start_new_round(the_board, player_letter, computer_letter, turn)

        if not play_again():
            break

if __name__ == '__main__':
    start_session()
