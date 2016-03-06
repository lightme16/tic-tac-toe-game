#TODO: Нельзя одновременно ходить на одно и тоже поле

import random

X = 1
O = 0


side = True
game_over = False
is_win = False

def gen_board():
    global board
    board = ['*'] * 9

def print_board(board):
   print('=' * 35)
   print(' ')
   print("{0} {1} {2}".format('>' * 6, 'TIC-TAC_-TOE GAME','<' * 6))

   print('=' * 35)
   print(' ' * 2)
   for i in range(len(board)):
       print("\t|{0}|".format(board[i]),end='')
       if (i + 1) % 3 == 0:
           print(' ')
           print(' ')
   print(' ')
   print('=' * 35)


   print("{0} {1} {2}".format('=' * 12, 'KEY HELP','=' * 12))
   print(' ' * 2)
   for i in range(len(board)):
       print("\t|{0}|".format(i),end='')
       if (i + 1) % 3 == 0:
           print(' ')
           print(' ')
   print(' ')
   print('=' * 35)
   



def valid_moves(board):
    global valid
    valid = []
    for i in range(len(board)):
        if board[i] == '*':
            valid.append(i)
    return valid

def make_move(board):
    global side
    valid = valid_moves(board)
    global game_over
    if len(valid) == 1:
        game_over = True
    
    if side:
        while True:
            try:
                move = int(input("Enter next move: \n"))
            except:
                print("Error! Enter a nuber")
            else:
                break
            
            
        print('Your move is {0}, valid is {1}'.format(move,valid))
        if move in valid:
            board[move] = 'X'
            print('Done!')
        else:
            print("Illegal move!")
        side = False
    else: 
        move = find_best_move(board, side)
        board[move] = 'O'
        side = True


    print_board(board)
    print(' ')

def find_best_move(board, side):
    value_of_cells = {0:2, 1:1, 2:2, 3:1, 4:3, 5:1, 6:2, 7:1, 8:2}
    valid = valid_moves(board)
    global game_over
    if len(valid) == 1:
        game_over = True
   
    new = {}
    for key, value in value_of_cells.items():
        for i in range(len(valid)):
            if key == valid[i]:
                new[key] = value
    best_move = max(new, key=new.get)
    return best_move
    
     

def get_side():
    ask_for_side  = input("Do you want play as X? Y/n\n")
    global side
    if ask_for_side.lower() == 'y':
        side = True
    else:
        side = False

def is_won(board):
    global is_win
    is_win = check_horizontal(board) or check_vertical(board) or check_dialinalOne(board) or check_dialinalTwo(board)
#    print('is_win = {0}'.format(is_win))
    print(' ')
    return is_win
    

def check_horizontal(board):
    is_win = False
    for i in range(3):
        if board[i] == board[i+1] == board[i+2] != '*':
            is_win = True
    return is_win


def check_vertical(board):
    is_win = False
    for i in range(3):
        if board[i] == board[i+3] == board[i+6] != '*':
            is_win = True
    return is_win
    
def check_dialinalOne(board):
    is_win = False
    if board[0] == board[4] == board[8] != '*':
        is_win = True
    return is_win

def check_dialinalTwo(board):
    is_win = False
    if board[2] == board[4] == board[6] != '*':
        is_win = True
    return is_win

gen_board()
get_side()

while(not game_over and not is_win):
    is_win = is_won(board)
    global side
    print_board(board) 
    make_move(board)

if is_win:
    print("Congratilation!")
    print(' ')
    print('=' * 35)

