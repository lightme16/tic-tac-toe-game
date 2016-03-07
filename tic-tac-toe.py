
side = True
game_over = False
is_win = False

def show_help():
    print(' ')
    print("{0} {1} {2}\n".format('>' * 6, 'TIC-TAC-TOE GAME','<' * 6))
    print("Welcome stranger!")
    print("Check youself! Can you beat COMP??\n")
    print("Make moves using keys:")
    print(" [0] [1] [2] \n [3] [4] [5] \n [6] [7] [8] \n")

def gen_board():
    global board
    board = ['*'] * 9

def print_board(board):

   for i in range(len(board)):
       print("  [{0}]".format(board[i]),end='')
       if (i + 1) % 3 == 0:
           print(' ')
   print(' ')
  
def valid_moves(board):
    valid = []
    for i in range(len(board)):
        if board[i] == '*':
            valid.append(i)
    return valid

def make_move(board):
    global side
    global game_over
    valid = valid_moves(board)
    print("Avalible moves {0}\n".format(valid))
    if len(valid) == 1:
        game_over = True

    if side:
        move = -1
        while True:
            try:
                move = int(input("Enter your move: \n"))
            except:
                print("Error! Enter a number") 
                                
            if move in valid:
                board[move] = 'X'
                print_board(board)
                break
            else:
                print("Illegal move! You can choose this moves {0}".format(valid))
                
        is_win = is_won(board)
        if is_win:
            return
        side = False
    else: 
        move = find_best_move(board, side, valid)
        board[move] = 'O'
        print_board(board)
        is_win = is_won(board)
        if is_win:
            return
        side = True
    print(' ')

def find_best_move(board, side, valid):
    global game_over
    value_of_cells = {0:2, 1:1, 2:2, 3:1, 4:3, 5:1, 6:2, 7:1, 8:2}
        
    best_move = None
    best_attack_move = None
    best_defence_move = None
    for item in valid:
        board[item] = 'X'
        is_win = is_won(board)
        if is_win:
            #print("COMP:Lose in the next move {0}".format(item))
            best_defence_move = item
        board[item] = 'O'
        is_win = is_won(board)
        if is_win:
            #print("COMP:Win in the next move {0}".format(item))
            best_attack_move = item
        board[item] = '*'
        
    best_move = best_attack_move
    if not best_move:
        best_move = best_defence_move       
    if not best_move:
        new = {}
        for key, value in value_of_cells.items():
            for i in range(len(valid)):
                if key == valid[i]:
                    new[key] = value
        best_move = max(new, key=new.get)
    return best_move
    
     

def get_side():
    ask_for_side  = input("Do you want play first? [Y]/[n]\n")
    global side
    if ask_for_side.lower() == 'y':
        side = True
    else:
        side = False

def is_won(board):
    is_win = check_horizontal(board) or check_vertical(board) or check_dialinalOne(board) or check_dialinalTwo(board)
    return is_win
    

def check_horizontal(board):
    is_win = False
    for i in range(3):
        if board[i*3] == board[i*3+1] == board[i*3+2] and board[i*3] != '*':
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

show_help()
gen_board()
get_side()
print_board(board) 

while(not game_over and not is_win):
    is_win = is_won(board)
    make_move(board)
    is_win = is_won(board)

if is_win:
    print("\tCongratulation!")
    if side: 
        print("\n   X winner!")
    else:
        print("\n   O winner! COMP win! ")
    print(' ')
else:
    print("   Game over!")
    print("\n   Draw")

