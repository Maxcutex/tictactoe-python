# Implementation of Two Player Tic-Tac-Toe game in Python.

theBoard = {'7': ' ', '8': ' ', '9': ' ',
            '4': ' ', '5': ' ', '6': ' ',
            '1': ' ', '2': ' ', '3': ' '}

track_moves = []
board_keys = []

for key in theBoard:
    board_keys.append(key)


def printBoard(board):
    print(board['7'] + '|' + board['8'] + '|' + board['9'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['1'] + '|' + board['2'] + '|' + board['3'])


# Now we'll write the main function which has all the gameplay functionality.
def game():
    turn = 'X'
    count = 0
    i = 1

    # for i in range(10):
    while i < 10:
        printBoard(theBoard)
        print("It's your turn," + turn + ".Move to which place? Press '0' to go back")

        move = input()
        if move == '0':
            if not track_moves:
                print("You can't go back beyond this point")
            else:
                last_item = str(track_moves[-1])
                theBoard[last_item] = ' '
                track_moves.pop()
                i -= 1
                count -= 1
        else:

            if theBoard[move] == ' ':
                theBoard[move] = turn
                count += 1
                i += 1
                track_moves.append(move)
                print(track_moves)
            else:
                print("That place is already filled.\nMove to which place?")
                continue

            # Now we will check if player X or O has won,for every move after 5 moves.
            if count >= 5:
                if theBoard['7'] == theBoard['8'] == theBoard['9'] != ' ':  # across the top
                    printBoard(theBoard)
                    print("\nGame Over.\n")
                    print(" **** " + turn + " won. ****")
                    break
                elif theBoard['4'] == theBoard['5'] == theBoard['6'] != ' ':  # across the middle
                    printBoard(theBoard)
                    print("\nGame Over.\n")
                    print(" **** " + turn + " won. ****")
                    break
                elif theBoard['1'] == theBoard['2'] == theBoard['3'] != ' ':  # across the bottom
                    printBoard(theBoard)
                    print("\nGame Over.\n")
                    print(" **** " + turn + " won. ****")
                    break
                elif theBoard['1'] == theBoard['4'] == theBoard['7'] != ' ':  # down the left side
                    printBoard(theBoard)
                    print("\nGame Over.\n")
                    print(" **** " + turn + " won. ****")
                    break
                elif theBoard['2'] == theBoard['5'] == theBoard['8'] != ' ':  # down the middle
                    printBoard(theBoard)
                    print("\nGame Over.\n")
                    print(" **** " + turn + " won. ****")
                    break
                elif theBoard['3'] == theBoard['6'] == theBoard['9'] != ' ':  # down the right side
                    printBoard(theBoard)
                    print("\nGame Over.\n")
                    print(" **** " + turn + " won. ****")
                    break
                elif theBoard['7'] == theBoard['5'] == theBoard['3'] != ' ':  # diagonal
                    printBoard(theBoard)
                    print("\nGame Over.\n")
                    print(" **** " + turn + " won. ****")
                    break
                elif theBoard['1'] == theBoard['5'] == theBoard['9'] != ' ':  # diagonal
                    printBoard(theBoard)
                    print("\nGame Over.\n")
                    print(" **** " + turn + " won. ****")
                    break

                    # If neither X nor O wins and the board is full, we'll declare the result as 'tie'.
            if count == 9:
                print("\nGame Over.\n")
                print("It's a Tie!!")

            # Now we have to change the player after every move.
            if turn == 'X':
                turn = 'O'
            else:
                turn = 'X'

            # Now we will ask if player wants to restart the game or not.
    restart = input("Do want to play Again?(y/n)")
    if restart == "y" or restart == "Y":
        for key in board_keys:
            theBoard[key] = " "

        game()


if __name__ == "__main__":
    game()
