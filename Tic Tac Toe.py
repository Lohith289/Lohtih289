board = ["-" , "-" , "-" ,
        "-" , "-" , "-" ,
        "-" , "-" , "-"]
current_player = "X"
winner = None
gamerunning = True

def printBoard(board):
    print(board[0]+"|"+board[1]+"|"+board[2])
    print(board[3]+"|"+board[4]+"|"+board[5])
    print(board[6]+"|"+board[7]+"|"+board[8])
printBoard(board)

def playerInput(board):
    inp = int(input("Select a number from 1-9 : "))
    if inp>=1 and inp<=9 and board[inp-1] == "-":
        board[inp-1] = current_player
    elif inp<1 or inp>9:
        print("Out of bounds.Try Again!!")
    else:
        print("Oops!! player in that spot.")

def checkHorizontal(board):
    global winner
    if board[0] == board[1] == board[2] and board[1]!="-":
        winner = board[0]
        return True
    elif board[3] == board[4] == board[5] and board[3] != "-":
        winner = board[3]
        return True
    elif board[6] == board[7] == board[8] and board[6] != "-":
        winner = board[6]
        return True
    
def checkRow(board):
    global winner
    if board[0] == board[3] == board[6] and board[0] !="-":
        winner = board[0]
        return True
    elif board[1] == board[4] == board[7] and board[1]!="-":
        winner = board[1]
        return True
    elif board[2] == board[5] == board[8] and board[2]!="-":
        winner = board[2]
        return True
    
def checkDiagonal(board):
    global winner
    if board[0] == board[4] == board[8] and board[0]!="-":
        winner = board[0]
        return True
    elif board[2] == board[4] == board[6] and board[2]!="-":
        winner = board[2]
        return True
    
def checkTie(board):
    if "-" not in board:
        printBoard(board)
        print("It's a Tie!!")
        gamerunning = False

def checkWin():
    global gamerunning 
    if checkDiagonal(board) or checkHorizontal(board) or checkRow(board):
        print(f"Winner is {winner}")
        gamerunning = False

def switchPlayer():
    global current_player
    if current_player == "X":
        current_player = "O"
    else:
        current_player = "X" 


import random
def computer(board):
    while current_player =="O":
        position = random.randint(0,8)
        if board[position] == "-":
            board[position] = "O"
            switchPlayer()

while gamerunning:
    printBoard(board)
    playerInput(board)
    checkWin()
    checkTie(board)
    switchPlayer()
    computer(board)
    checkWin()
    checkTie(board)