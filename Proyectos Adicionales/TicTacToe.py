from IPython.display import clear_output

def boardDisplay(board):
    clear_output()
    print(board[0]+"|"+board[1]+"|"+board[2])
    print("-----")
    print(board[3]+"|"+board[4]+"|"+board[5])
    print("-----")
    print(board[6]+"|"+board[7]+"|"+board[8])

def instructions(test_board):
    print("The goal of this program is to play Tic Tac Toe! Just select the cell in which you want to put your mark (X or O)."+
    "\nThe first player will chose the mark he wants to use. Be advice the number in each cell "+
    "represents the number you must hit yo put your mark")
    boardDisplay(test_board)
    print("\nHave Fun!")

def win_check(board,mark):
    
    return ((board[0] == mark and board[1] == mark and board[2] == mark) or # across the top
    (board[3] == mark and board[4] == mark and board[5] == mark) or # across the middle
    (board[6] == mark and board[7] == mark and board[8] == mark) or # across the bottom
    (board[0] == mark and board[3] == mark and board[6] == mark) or # down the middle
    (board[1] == mark and board[4] == mark and board[7] == mark) or # down the middle
    (board[2] == mark and board[5] == mark and board[8] == mark) or # down the right side
    (board[0] == mark and board[4] == mark and board[8] == mark) or # diagonal
    (board[2] == mark and board[4] == mark and board[6] == mark)) # diagonal

def game(player1,player2, board):
    roundGame=0
    while " " in board:
        roundGame+=1
        print(f"\nWelcome to round {roundGame}")
        position=0
        position=int(input("\nChoose your position to play Player 1: "))
        board[position-1]=player1
        boardDisplay(board)
        if win_check(board,player1):
            print("You just won Player 1, Congrats! ")
            break
        if roundGame==5 and not win_check(board,player1):
            print("OH OH  there was a Tie!")
            break
        position=int(input("\nChoose your position to play Player 2: "))
        board[position-1]=player2
        boardDisplay(board)
        if win_check(board,player2):
            print("You just won Player 2, Congrats! ")
            break
        clear_output(wait=False)

def replay():
    game=input("Do you want to play a game of Tic Tac Toe? (y/n): ")
    if game.lower()=="y":
        return True
    else:
        return False

test_board=["1","2","3","4","5","6","7","8","9"]
instructions(test_board)
game_on=replay()
while game_on: 
    board=[" "," "," "," "," "," "," "," "," "]
    boardDisplay(board)


    #Assign the Letter
    player1=input("Please tell me what is it that you desire (x/o): ")
    if player1.lower()=="x":
        player2="O"
    else:
        player2="X"

    print(f"Great! Player 1 will use {player1.upper()}"
          + f" and Player 2 will use {player2}")

    game(player1,player2,board)
    game_on=replay()

print("\nThis small game was created by Roger Urrutia. Hope you liked it.")