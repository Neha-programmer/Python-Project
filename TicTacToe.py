# Game Board
board=["-", "-", "-",
       "-", "-", "-",
       "-", "-", "-"]
# If game still going
game_still_going = True
# Who won? or tie?
Winner= None
# Who's turn is it
current_player = "X"
# play a game of tic tac toe

def play_game():
    display_board()
    # while the game is still going
    while game_still_going:
        # handle a single turn of an arbitary player
        handle_turn(current_player)
        # check if the game has ended
        check_if_game_over()
        # flip to the other player
        flip_player()
    # The game has ended
    if Winner == "X" or Winner == "O":
        print(Winner + " won.")
    elif Winner == None:
        print("Tie.")

# display game board to screen
def display_board():
   print("\n")
   print(board[0] + " | " + board[1] + " | " + board[2])
   print(board[3] + " | " + board[4] + " | " + board[5])
   print(board[6] + " | " + board[7] + " | " + board[8])
   print("\n")

# handle a single turn of an arbitary player
def handle_turn(player):
    print(player + "'s turn.")
    position = input("Choose a position from 1-9: ")
    valid = False
    while not valid:
        while position not in ["1","2","3","4","5","6","7","8","9"]:
            position = input("Invalid input. Choose a position from 1-9: ")
        position = int(position) -1
        if board[position] == "-":
            valid = True
        else:
            print("You can't go there. Go again.")
    board[position] = player
    display_board()

def check_if_game_over():
    check_for_winner()
    check_if_tie()

def check_for_winner():
    # set up global variables
    global Winner
    # check rows
    row_winner = check_rows()
    # check columns
    column_winner = check_columns()
    # check diagonals
    diagonal_winner = check_diagonals()
    if row_winner:
        Winner = row_winner
    elif column_winner:
        Winner = column_winner
    elif diagonal_winner:
        Winner = diagonal_winner
    else:
        Winner = None

def check_rows():
    # set up global variables
    global game_still_going
    # check if any of the rows have all the same value (and is not empty)
    row_1 = board[0] == board[1] == board[2] != "-"
    row_2 = board[3] == board[4] == board[5] != "-"
    row_3 = board[6] == board[7] == board[8] != "-"
    # if any row does have a match , flag that there is a win
    if row_1 or row_2 or row_3:
        game_still_going = False
    # return the winner (X or O)
    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]
    else:
        return

def check_columns():
    # set up global variables
    global game_still_going
    # check if any of the columns have all the same value (and is not empty)
    column_1 = board[0] == board[3] == board[6] != "-"
    column_2 = board[1] == board[4] == board[7] != "-"
    column_3 = board[2] == board[5] == board[8] != "-"
    # if any column does have a match , flag that there is a win
    if column_1 or column_2 or column_3:
        game_still_going = False
    # return the winner (X or O)
    if column_1:
        return board[0]
    elif column_2:
        return board[1]
    elif column_3:
        return board[2]
    else:
        return

def check_diagonals():
    # set up global variables
    global game_still_going
    # check if any of the diagonals have all the same value (and is not empty)
    diagonal_1 = board[0] == board[4] == board[8] != "-"
    diagonal_2 = board[6] == board[4] == board[2] != "-"
    # if any diagonal does have a match , flag that there is a win
    if diagonal_1 or diagonal_2 :
        game_still_going = False
    # return the winner (X or O)
    if diagonal_1:
        return board[0]
    elif diagonal_2:
        return board[6]
    else:
        return

def check_if_tie():
    global game_still_going
    if "-" not in board:
        game_still_going =False
        return True
    else:
        return False

def flip_player():
    # global variables we need
    global current_player
    # if the current player was X , then change it to 0
    if current_player == "X":
        current_player = "O"
    # if the current player is O , then change it to X
    elif current_player == "O":
        current_player = "X"

play_game()




