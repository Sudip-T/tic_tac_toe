import random
import os.path
import json


total_score = 0

def draw_board(board):
    for x in range(3):
        print('\n-------------')
        print('|', end='')
        for y in range(3):
            print('', board[x][y], end=' |')
    print('\n -------------')
    print()


def readyToPlay():
    print('-----------------------------------------------')
    play_game = input('Are you ready to play? Enter Yes or No :--- ')
    print('-----------------------------------------------')
    if play_game.lower()[0] == 'y':
        return True
    

def chooseFirstTurn():
    if random.randint(0,1) == 0:
        print('You make first move.')
        return 'Player'
    else:
        print('Computer makes first move.')
        return 'Computer'
    

def welcome(board):
    print('\n')
    print('Welcome to the Tic-Tac-Toe game.\n--------------------------------\nThe board layout is shown below:')
    draw_board(board)
    print('When prompted, enter the number corresponding the square.')
    # return ' '


def empty_board(board):
    for x in range(3):
        for j in range(3):
            board[x][j]=' ' 
    return board


def available_space(board, position):
    empty_space = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                x = j+1 + i*3
                empty_space.append(x)
    if position in empty_space:
        return True


def computer_choice(board):
    position = random.randint(1,9)
    while not available_space(board, position):
        position = random.randint(1,9)
    return position
    # while position not in range(1,9) or not available_space(board, position):
    #     position = random.randint(1,9)
    # print(position)


def check_for_win(board, mark):
    return ((board[2][0] == mark and board[2][1] == mark and board[2][2] == mark) or 
            (board[1][0] == mark and board[1][1] == mark and board[1][2] == mark) or 
            (board[0][0] == mark and board[0][1] == mark and board[0][2] == mark) or 
            (board[2][0] == mark and board[1][0] == mark and board[0][0] == mark) or 
            (board[2][1] == mark and board[1][1] == mark and board[0][1] == mark) or 
            (board[2][2] == mark and board[1][2] == mark and board[0][2] == mark) or 
            (board[2][0] == mark and board[1][1] == mark and board[0][2] == mark) or 
            (board[2][2] == mark and board[1][1] == mark and board[0][0] == mark)) 


def checkDraw(board):
    if (' ' not in board[0]) and (' ' not in board[1]) and (' ' not in board[2]):
        print('Its a Draw!')


def playerChoice(board):
    position = 0
    while position not in range(1, 10) or not available_space(board, position):
        try:
            position = int(input('Choose your next position (1-9): '))
        except:
            print('Error!')
            return playerChoice(board)
        if not available_space(board, position):
            print('Space not available...')
    return position


def fillPosition(board, marker, position):
    row_pos = (position-1) // 3
    col_pos = (position-1) % 3
    board[row_pos][col_pos]=marker


def  whowins(board):
    if check_for_win(board, 'O'):
        print('----------------')
        print(f'Computer win!!!')
        print('----------------')
        return True
    elif check_for_win(board, 'X'):
        print('-----------')
        print(f'You win!!!')
        print('-----------')
        return True
    

def dashBoard(board, choice):
    if choice == '1':
        play_game(board)
    elif choice == '2':
        save_score(total_score)
    elif choice == '3':
        leader_board = load_scores()
        display_leaderboard(leader_board)
    elif choice == 'q':
        print('---------------------------------------')
        print('Thank you for playing Tic-Tac-Toe game.')
        print('---------------------------------------')
        return True


def menu():
    print()
    print('Enter one of the following:')
    print(" "*4,'1 - Play the game')
    print(" "*4,'2 - Save your score in the leaderboard')
    print(" "*4,'3 - Load and display the leaderboard')
    print(" "*4,'q - End the program')
    choice = input('1, 2, 3, q :--- ')
    if choice not in ['1','2','3','q']:
        return menu()
    return choice


def play_game(board):
    global total_score
    print()
    print('Game Begins!!!')
    empty_board(board)
    draw_board(board)
    turn = chooseFirstTurn()
    for i in range(9):
        if turn == 'Computer':
            fillPosition(board, 'O', computer_choice(board))
            draw_board(board)
            if whowins(board):
                total_score -=1
                break
            checkDraw(board)
            turn = 'Player'
        else:
            fillPosition(board, 'X', playerChoice(board))
            draw_board(board)
            if whowins(board):
                total_score += 1
                break
            checkDraw(board)
            turn = 'Computer'


def load_scores():
    filename = 'leaderboard.txt'

    if os.path.exists(filename):
        with open(filename, 'r') as file:
            leaders = json.load(file)
            return leaders
    else:
        print('No such file exists')
        return False


def save_score(score):
    player_name = input('Enter your name to save score: ')

    filename = 'leaderboard.txt'
    leader_file = {}

    if os.path.exists(filename):
        try:
            with open(filename, 'r') as file:
                leader_file = json.load(file)
        except json.JSONDecodeError:
            print("Invalid JSON data in the file.")

    leader_file[player_name] = score

    with open(filename, 'w') as f:
        json.dump(leader_file, f)

    return


def display_leaderboard(leaders):
    if leaders != False:
        sorted_dict = dict(sorted(leaders.items(), key=lambda x:x[1]))
        for k, v in sorted_dict.items():
            print(f'Player_Name: {k}        {v}')