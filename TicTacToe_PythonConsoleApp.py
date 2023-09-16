import os
import random
import time

def insertBoard(letter, pos):
    board[pos] = letter


def spaceIsFree(pos):
    return board[pos] == ' '

def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def isWinner(bo, le):
    return ((bo[7] == le and bo[8] == le and bo[9] == le) or 
    (bo[4] == le and bo[5] == le and bo[6] == le) or 
    (bo[1] == le and bo[2] == le and bo[3] == le) or 
    (bo[7] == le and bo[4] == le and bo[1] == le) or 
    (bo[8] == le and bo[5] == le and bo[2] == le) or 
    (bo[9] == le and bo[6] == le and bo[3] == le) or
    (bo[7] == le and bo[5] == le and bo[3] == le) or 
    (bo[9] == le and bo[5] == le and bo[1] == le))


def playerMove(char,mode):
    run = True
    while run:
        move = input("Please select a position to place an '" + char + "' (1-9): ")
        clear()
        try:
            move  = int(move)
            if move > 0 and move < 10:
                if spaceIsFree(move):
                    run = False
                    insertBoard(char, move)
                else:
                    printBoard(mode)
                    print("This postion is already occupied!")
            else:
                printBoard(mode)
                print("Please type a number within the range!")
        except:
            printBoard(mode)
            print("Please type a number!")
    print("Placed '" + char + "' on position " + str(move))
        

def selectRandom(li):
    ln = len(li)
    r = random.randrange(0, ln)
    return li[r]

def randomCompMove():
    
    if isBoardFull(board):
        move = 0
        return move
    
    move = random.randint(1,9)
    
    while not board[move] == ' ':
        move = random.randint(1,9)    

    return move
    
def compMove():
    possibleMoves = [x for x, letter in enumerate(board) if letter == ' ' and x != 0]
    move = 0

    for let in ['O','X']:
        for i in possibleMoves:
            boardCopy = board[:]
            boardCopy[i] = let
            if isWinner(boardCopy, let):
                move = i
                return move


    cornersOpen = []
    for i in possibleMoves:
        if i in [1,3,7,9]:
            cornersOpen.append(i)
    if len(cornersOpen) > 0:
        move = selectRandom(cornersOpen)
        return move

    
    if 5 in possibleMoves:
        move = 5
        return move


    edgesOpen = []
    for i in possibleMoves:
        if i in [2,4,6,8]:
            edgesOpen.append(i)

    if len(edgesOpen) > 0:
        move = selectRandom(edgesOpen)

    return move


def isBoardFull(board):
    if board.count(' ') > 1:
        return False
    else:
        return True


def printBoard(mode):
    print("   ["+ mode +"]   ")
    print("   |   |")
    print(" " + board[1] + " | " + board[2] + " | " + board[3])
    print("  1|  2|  3")
    print("-----------")
    print("   |   |")
    print(" " + board[4] + " | " + board[5] + " | " + board[6])
    print("  4|  5|  6")
    print("-----------")
    print("   |   |")
    print(" " + board[7] + " | " + board[8] + " | " + board[9])
    print("  7|  8|  9")
    

def singleEasy():
    print("You are playing level EASY.")
    printBoard("EASY")

    while not isBoardFull(board):
        if not isWinner(board, 'O'):
            playerMove('X',"EASY")
            printBoard("EASY")
        else:
            print("O's win this time...")
            break

        if not isWinner(board, 'X'):
            move = randomCompMove()
            if move == 0:
                print("Game is a Tie! No more spaces left to move.")
            else:
                insertBoard('O', move)
                time.sleep(2)
                clear()
                print("Computer placed an 'O' in position " + str(move) + ".")
                printBoard("EASY")
        else:
            print("You win, good job!")
            break
    return


def singleHard():
    print("You are playing level HARD.")
    printBoard("HARD")

    while not isBoardFull(board):
        if not isWinner(board, 'O'):
            playerMove('X',"HARD")
            printBoard("HARD")
        else:
            print("O's win this time...")
            break

        if not isWinner(board, 'X'):
            move = compMove()
            if move == 0:
                print("Game is a Tie! No more spaces left to move.")
            else:
                insertBoard('O', move)
                time.sleep(2)
                clear()
                print("Computer placed an 'O' in position " + str(move) + ".")
                printBoard("HARD")
        else:
            print("You win, good job!")
            break

def loadingGame():
    clear()
    print("Loading...")
    time.sleep(1)
    clear()

def multi():
    print("Your are playing two-player mode.")
    printBoard("PVP")
    
    while True:
        if not isWinner(board, 'O'):
            playerMove('X',"PVP")
            printBoard("PVP")
        else:
            print("O's win. God job!")
            break
        
        if not isWinner(board,'X'):
            if isBoardFull(board):
                print("Game is a Tie! No more spaces left to move.")
                break
            else:
                playerMove('O',"PVP")
                printBoard("PVP")
        else:
            print("X's win. Good job!")
            break

def main():
    print("Welcome to Tic Tac Toe!")
    print("Available game modes:")
    print("1.Player vs Computer [EASY]")
    print("2.Player vs Computer [HARD]")
    print("3.Player vs Player")
    ans = input("Choose 1-3: ")
    
    while True:
        if ans == "1":
            loadingGame()
            singleEasy()
            break
        elif ans == "2":
            loadingGame()
            singleHard()
            break
        elif ans == "3":
            loadingGame()
            multi()
            break
        else:
            ans = input("Choose 1-3:")

board = [' ' for x in range(10)]
main() 

while True:
    answer = input("Do you want to play again? (Y/N)")
    if (answer.lower() == 'y' or answer.lower == "yes"):
        board = [' ' for x in range(10)]
        clear()
        main()
    else:
        print("Thanks for playing. See you soon...")
        time.sleep(1)
        break
