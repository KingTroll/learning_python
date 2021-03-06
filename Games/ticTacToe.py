#! python3
#ticTacToe

import sys
import random
import os




def board():
    global the_board
    global turns_played
    
    the_board = {
            7: "7", 8: "8", 9: "9",
            4: "4", 5: "5", 6: "6",
            1: "1", 2: "2", 3: "3"
            }

    turns_played = []


# The board grid
def print_board(board):
    os.system("clear")
    print(board[7] + "|" + board[8] + "|" + board[9])
    print("-+-+-")
    print(board[4] + "|" + board[5] + "|" + board[6])
    print("-+-+-")
    print(board[1] + "|" + board[2] + "|" + board[3])


def rounds(played):
        while True:
            play = input("Play again?(y/n): ")
            
            if play == "n":
                os.system("clear")
                sys.exit()
            elif play == "y" or play == "":
                os.system("clear")
                board()
                played.clear()
                break


# Sets the winner
def win(board):
    if "X" in board[1] and "X" in board[2] and "X" in board[3] or "X" in board[4] and "X" in board[5] and "X" in board[6] or "X" in board[7] and "X" in board[8] and "X" in board[9]:
        print_board(the_board)
        print("X Wins!!!")
        return True
    elif "X" in board[1] and "X" in board[4] and "X" in board[7] or "X" in board[2] and "X" in board[5] and "X" in board[8] or "X" in board[3] and "X" in board[6] and "X" in board[9]:
        print_board(the_board)
        print("X Wins!!!")
        return True
    elif "X" in board[3] and "X" in board[5] and "X" in board[7] or "X" in board[1] and "X" in board[5] and "X" in board[9]:
        print_board(the_board)
        print("X Wins!!!")
        return True

    elif "O" in board[1] and "O" in board[2] and "O" in board[3] or "O" in board[4] and "O" in board[5] and "O" in board[6] or "O" in board[7] and "O" in board[8] and "O" in board[9]:
        print_board(the_board)
        print("O Wins!!!")
        return True
    elif "O" in board[1] and "O" in board[4] and "O" in board[7] or "O" in board[2] and "O" in board[5] and "O" in board[8] or "O" in board[3] and "O" in board[6] and "O" in board[9]:
        print_board(the_board)
        print("O Wins!!!")
        return True
    elif "O" in board[3] and "O" in board[5] and "O" in board[7] or "O" in board[1] and "O" in board[5] and "O" in board[9]:
        print_board(the_board)
        print("O Wins!!!")
        return True


def bot(turn, played):
    while True:
        bot = random.randint(1, 9)

        if bot not in played:
            played.append(bot)
            break
    return bot


# Move validation
def player(turn, played):
    while True:
        try:
            move = input()
            
            if move != "":  #(1) prevents empty string to int error
                move = int(move)

                if move in the_board.keys(): #(2) checks if the move played isn't too high or low
                    if move not in played: #(3) Prevents overide of values
                        played.append(move)
                        return move
                    else: #(3)
                        print_board(the_board)
                        print("Error: Space already taken")
                        print("Turn " + turn)
                else: #(2)
                    print_board(the_board)
                    print("Error: Only between 1-9, as shown in the diagram")
                    print("Turn " + turn)
            else: #(1)
                print_board(the_board)
                print("Turn " + turn)
        except ValueError:
            print("Error: Only whole-numbers betweem 1-9, as shown in the diagram")
            print("Turn " + turn)


def main_menu():
    while True:
        os.system("clear")

        try:
            board()
            print("X and O:")
            game_mode = input("1. Single Player \n2. Muliplayer \n")

            while True:
                os.system("clear")

                if game_mode == "1":
                    single_player(turns_played)
                elif game_mode == "2":
                    multiplayer(turns_played)
                else:
                    print("X and O:")
                    game_mode = input("1. Single Player \n2. Muliplayer \nPress 1 for a singleplayer game and 2 for a multiplayer game \n")
        except KeyboardInterrupt:
            os.system("clear")
            sys.exit()


def single_player(played):
    try:
        turn = "X"
        print_board(the_board)

        for turn_number in range(10):
            if turn_number == 9:
                print_board(the_board)
                print("donkey game")
                rounds(played)
                single_player(played)

            if turn == "X":
                print("Turn " + turn)
                move = player(turn, played)
                the_board[move] = turn
                turn = "O"
            else:
                move = bot(turn, played)
                the_board[move] = turn
                turn = "X"
                print_board(the_board)

            if win(the_board):
                rounds(played)
                single_player(played)
    except KeyboardInterrupt:
        main_menu()


def multiplayer(played):
    try:
        turn ="X"
        print_board(the_board)

        for turn_number in range(10):
            if turn_number == 9:
                print_board(the_board)
                print("Donkey Game")
                rounds(played)
                multiplayer(played)

            print("Turn " + turn)
            move = player(turn, played)
            the_board[move] = turn

            if turn == "X":
                turn = "O"
            else:
                turn = "X"
            
            print_board(the_board)

            if win(the_board):
                rounds(played)
                multiplayer(played)
    except KeyboardInterrupt:
        main_menu()





main_menu()

