
side = True # отвечает за порядок первого хода
game_over = False # индикатор окончания игры
is_win = False # индикаторы попеды в игре

# выводит приветственное сообщение и подсказку
def show_help():
    print(' ') # печатает отступ
    print("{0} {1} {2}\n".format('>' * 6, 'TIC-TAC-TOE GAME','<' * 6))  
    print("Welcome stranger!")
    print("Check youself! Can you beat COMP??\n")
    print("Make moves using keys:")
    print(" [0] [1] [2] \n [3] [4] [5] \n [6] [7] [8] \n") # печатает квадрат игрового полля с подприсанными цифрами 

# генерирует поле
def gen_board(): 
    global board # обьявяет переменную board(поле) видимой вне тела метода

 # обьявляется переменная типа лист и заполняется 9 елемнтами.
 # "*" - пустая ячейка, собственно создается пуское поле
    board = ['*'] * 9

def print_board(board): # печатает поле
   for i in range(len(board)): # проход по каждому елементу поля столько раз, сколько содержится елементов в board
       print("  [{0}]".format(board[i]),end='') # печать елемента и обертка елмента в квадратные скобки
#  то бы напечатать квадрат, а не прямую линию, 
#  после каждого елемента кратного 3ке добавляем отступ. 
#  К переменной i добавляем 1, что бы отсчет начинался с единицы, а не с нуля 
       if (i + 1) % 3 == 0: 
           print(' ')       
   print(' ')
  
def valid_moves(board): # возвращат доступные ходы из board
    valid = [] # инициализация пустого элемента типа лист
    for i in range(len(board)): # проход по board
        if board[i] == '*': # если елемент пуст, те не содержит Х или О
            valid.append(i) # добавляем его в valid
    return valid # возвращаем свободные ячейки в листе

def make_move(board):
    global side # указываем, что мы будем использовать статическую переменную sid
    global game_over # аналогично
    valid = valid_moves(board) # получаем доступные ходы
    print("Avalible moves {0}\n".format(valid)) # печатаем доступные ходы
    if len(valid) == 1: # если остался только один доступный ход
        game_over = True #  обьявляем игра завершенной

    if side: # если истинна, то значит первым человек
        move = -1 # заранее инициализируем перемнную
        while True: # вечный цикл, использован для того, что бы неограниченное количество раз уточнять елемент при некорректном вводе
            try:
                move = int(input("Enter your move: \n")) # просим вести ход с клавиатуры и приводим к числовому формату
            except:
                print("Error! Enter a number") # если неудается привести ввод к числовому формату, выдаем ошибку
                                
            if move in valid: # если введенный ход содержется в списке доступных ходов
                board[move] = 'X' # делаем ход на указанный индекс
                print_board(board) # печатаем поле
                break # выходим из бесконечного цыкла
            else: # если ход не доступн
                print("Illegal move! You can choose this moves {0}".format(valid)) # напечатать ошибку и вывести доступные ходы
                
    else: # если ложь, то значит ходит компьютер 
        move = find_best_move(board, side, valid) # вызванная функция получает аргументы доска, 
                                                  # сторона и доступные ходы и возвращает лучшый ход
        board[move] = 'O'
        print_board(board)

    is_win = is_won(board) # после хода проверить, не стал ли он выграшным
    if is_win: # если правда
        return # завершыть функцию
    side = not side # поменять сторору на противоположную
    print(' ') 

def find_best_move(board, side, valid):
    global game_over
    value_of_cells = {0:2, 1:1, 2:2, 3:1, 4:3, 5:1, 6:2, 7:1, 8:2} # переменная типа словарь, где ход:ценность_хода
                                                                   # указания для копмьютера, по поводу ценности каждого хода
                                                                   # например, ход в центр(4) имеет наивысшую ценность - 3 очка
        
    best_move = None # инициализация лучшего хода
    best_attack_move = None # инициализация лучшего атакующего хода
    best_defence_move = None # инициализауия лучшего защитного хода
    for item in valid: # проход по доступным елементам. ищем следующий ход человека, который приведет к выигрышу
        board[item] = 'X' # делаем пробный ход за человека
        is_win = is_won(board) # проверяем, не стал ли он победным
        if is_win: # если истина
            #print("COMP:Lose in the next move {0}".format(item)) при желании можно включить подстазки
            best_defence_move = item # этот ход принесет человеку победу в следующем раунде, 
                                     # поэтому, лучшея защита - предотвратить его.
        board[item] = 'O' #  дальше делаем пробный ход за компьютер
        is_win = is_won(board) # проверяем виыгрыш
        if is_win: 
            #print("COMP:Win in the next move {0}".format(item))
            best_attack_move = item # ход который принесет победу компьютеру
        board[item] = '*' # после анализа, возращаем прежнее значение ячейки, что бы не нарушить логику игры
        
    best_move = best_attack_move # назначаем лучшим ходом атакующим, так как он обеспечет в следующем ходу победу
                                 # если он не задан, то присваивается прежнее значение - None 
    if not best_move: # Если лучший ход имеет значение None, так как лучший атакующий ход не найден
        best_move = best_defence_move # то лчшим ходом обозначаем защитный ход
    if not best_move: # если лучшего хода все равное нет
        new = {} # инициализируем новый словарь
        for key, value in value_of_cells.items(): # проходим по словарю ценности ходов, выделяем ключ и значение словаря
            for i in range(len(valid)):           # проходим циклом столько раз, сколько елементов в доступных значениях
                if key == valid[i]:               # если ход есть в доступных
                    new[key] = value # добавляем его в новый словарь доступных елементов с их ценностью
        best_move = max(new, key=new.get) # с новго словаря находим ход с найбольшей ценностью
    return best_move # возращаем лучший ход
    
     

def get_side(): # узнает сторону игрока
    ask_for_side  = input("Do you want play first? [Y]/[n]\n")
    global side # переменная сторона доступна за пределами метода
    if ask_for_side.lower() == 'y': # если сторона = у
        side = True
    else:
        side = False

def is_won(board):
    # если по горизонтали, вертекали или по диагоналях обнаружено пересечение полей(те победа), назначить значение истина
    is_win = check_horizontal(board) or check_vertical(board) or check_dialinalOne(board) or check_dialinalTwo(board)
    return is_win
    

def check_horizontal(board):
    is_win = False # заранее обьявляем отсутствие победы
    for i in range(3): # 3 раза проходим по поля, так как поле содержит 3 горизонтальных поля
        if board[i*3] == board[i*3+1] == board[i*3+2] and board[i*3] != '*': # если все элменты равны и не пустые(*)
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
#==================================================================
# Начало игры. Когда скрипт запускается, действия начинаются отсюда
#===================================================================
show_help() # вывести приведприе и подсказку
gen_board() # сгенерировать поле
get_side() # узнать сторону игрока
print_board(board) # напечатать сторону

while(not game_over and not is_win): # пока игра не кончена или нет победителя
    is_win = is_won(board) # проверить есть ли победитель
    make_move(board) # сделать ход в зависимости от side
    is_win = is_won(board) # снова проверить нет ли победител

if is_win: # если есть победитель
    print("   Congratulation!")
    if side: 
        print("\n   X winner!")
    else:
        print("\n   O winner! COMP win! ")
    print(' ')
else: # если победителя нет
    print("   Game over!")
    print("\n   Draw")

