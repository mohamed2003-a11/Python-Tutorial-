


def printBoard(board):

    print(board['1'] + '|' + board['2'] + '|' + board['3'])
    print ('-----')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-----')
    print(board['7'] + '|' + board['8'] + '|' + board['9'])

def game():
    TheBoard = {
        '1': ' ', '2': ' ', '3': ' ',
        '4': ' ', '5': ' ', '6': ' ',
        '7': ' ', '8': ' ', '9': ' '
    }
    turn = 'X'
    count = 0
    for i in range(10):
        printBoard(TheBoard)
        print("it's your turn " + turn + " Choose the place " )
        move = input()
        if move not in TheBoard.keys():
            print("Please inter only numbers from 1 to 9")
            continue
        if TheBoard[move] == ' ':
            TheBoard[move] = turn
            count += 1
        else:
            print("The place is already taken.\n Please choose another place")
            continue
        if count >= 5 :
            if  TheBoard['1'] == TheBoard['2'] == TheBoard['3']  != ' ' :# across the top
                printBoard(TheBoard)
                print('Game Over\n')
                print('*****'+ turn +'won*****')
                break
            elif  TheBoard['4'] == TheBoard['5'] == TheBoard['6']  != ' ' :# across the middle
                printBoard(TheBoard)
                print('Game Over\n')
                print('*****' + turn + 'won*****')
                break
            elif TheBoard['7'] == TheBoard['8'] == TheBoard['9'] != ' ':  # across the button
                printBoard(TheBoard)
                print('Game Over\n')
                print('*****' + turn + 'won*****')
                break
            elif TheBoard['1'] == TheBoard['4'] == TheBoard['7'] != ' ':  # across the left side
                printBoard(TheBoard)
                print('Game Over\n')
                print('*****' + turn + 'won*****')
                break
            elif TheBoard['2'] == TheBoard['5'] == TheBoard['8'] != ' ':  # across the middle side
                printBoard(TheBoard)
                print('Game Over\n')
                print('*****' + turn + 'won*****')
                break
            elif TheBoard['3'] == TheBoard['6'] == TheBoard['9'] != ' ':  # across the right side
                printBoard(TheBoard)
                print('Game Over\n')
                print('*****' + turn + 'won*****')
                break
            elif TheBoard['1'] == TheBoard['5'] == TheBoard['9'] != ' ':  # across the dilog
                printBoard(TheBoard)
                print('Game Over\n')
                print('*****' + turn + 'won*****')
                break
            elif TheBoard['3'] == TheBoard['5'] == TheBoard['7'] != ' ':  # across the dilog
                printBoard(TheBoard)
                print('Game Over\n')
                print('*****' + turn + 'won*****')
                break
        if count == 9 :
                print("****Game Over*****")
                print("It's a Tie!!")
        if turn == 'X':
                turn = 'O'
        else:
                turn = 'X'
        # to switch between players
if __name__ == "__main__":
    while True:
        game()
        response = input("Play again? (y/n): ").lower()

        if response == "y":
            continue
        elif response == "n":
            print("Have a good day!")
            break
        else:
            print("Invalid choice, please enter y or n.")

