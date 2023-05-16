from Tic_Tac_Toe import *


def main():
    board = [[i + j*3 for i in range(1,4)] for j in range(3)]
    welcome(board)
    if readyToPlay():
        play_game(board)
        while True:
            if (dashBoard(board, menu())):        
                break

if __name__ == '__main__':
    main()