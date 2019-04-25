import sys
#    Starting point for Extra Credit
#    Tic Tac Toe game program


def clear():
    return [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]

# ///////  display  ////////
# // Display the current status of the board on the
# // screen, using hyphens (-) for horizontal lines
# // and pipes (|) for vertical lines.


def display(board):
    column_count = 0
    row_count = 0
    for row in board:
        for column in row:
            if column_count == len(row) - 1:
                print(column)
            else:
                print(column+'|', end='')
                column_count += 1
        if row_count == len(board) - 1:
            print(end="")
        else:
            print("------")
        row_count += 1
        column_count = 0
    row_count = 0
    return True

# ///////  takeTurn  ////////
# // Allow the nextPlayer to take a turn.
# // Send output to screen saying whose turn
# // it is and specifying the format for input.
# // Read user's input and verify that it is a
# // valid move.  If it's invalid, make them
# // re-enter it.  When a valid move is entered,
# // put it on the board.


def takeTurn(board, nextPlayer):
    print("""It is now """+nextPlayer+"""'s turn.
Please enter your move in row and column.
So row: 0 and column: 0 would be the top left, and row: 0 and column: 2 would be the top right.""")
    print("Type !q to exit the program")
    row_position = None
    column_position = None
    while check_current_position(row_position,column_position,board) is False:
        row_position = check_variable_type("Enter row: ")
        column_position = check_variable_type("Enter column: ")
        print("This place is already occupied.")
    board[row_position][column_position] = nextPlayer
    if nextPlayer == 'X':
        nextPlayer = 'O'
    else:
        nextPlayer = 'X'
    return nextPlayer

def check_current_position(row_position,column_position,board):
    if row_position is None or column_position is None or board[row_position][column_position] != " ":
        return False
    else:
        return True

def check_variable_type(string):
    temp_string = None
    while temp_string is None or isinstance(temp_string,str):
        temp_string = input(string)
        try:
            temp_string = int(temp_string)
        except:
            if is_exit(temp_string):
                sys.exit()
            else:
                print("Please Enter a integer number")
        else:
            if temp_string < 0 or temp_string > 3:
                temp_string = None
                print("Number should between 0 and 3")
    return temp_string

def is_exit(arg):
    if arg == '!q':
        return True

# ///////  winner  /////////
# // Examines the board and returns one of the following:
# // ' ' (a space) meaning the game is not yet over
# // 'X' meaning that player X has won
# // 'O' meaning that player O has won
# // '?' meaning that the game is over because the board
# //     is full, but no one won.


def winner(board):
    horizontal = check_horizontal(board)
    vertical = check_veritical(board)
    slanted = check_slanted(board)
    if horizontal is not None:
        winner = horizontal
    elif vertical is not None:
        winner = vertical
    elif vertical is not None:
        winner = slanted
    elif check_space(board):
        winner = ' '
    else:
        winner = '?'
    return winner

def check_space(board):
    for row in board:
        if " " in row:
            return True

def check_horizontal(board):
    winner = None
    count = 0
    for row in board:
        for column in range(1,len(row)):
            if row[column-1] == row[column]:
                count += 1
        if count == len(row):
            winner = row[0]

    return winner

def check_slanted(board):
    winner = None
    count_top = 0
    count_bottom = 0
    for row in range(1,len(board)):
        for column in range(1,len(board)):
            if board[row-1][column-1] == board[row][column]:
                count_top += 1
            elif board[row-1][len(board)-column] == board[row][len(board)-column-1]:
                count_bottom += 1
        if count_top == len(board):
            winner = board[count_top][0]
        elif count_bottom == len(board):
            winner = board[count_bottom][0]
        count_top = 0
        count_bottom = 0
    return winner

def check_veritical(board):
    winner = None
    count = 0
    for row in range(1,len(board)):
        for column in range(1,len(board)):
            if board[row-1][column-1] == board[row][column-1]:
                count += 1
        if count == len(board):
            winner = board[count][0]
        count = 0
    return winner
# ///////  main  ////////
# // No changes needed in this function.
# // It declares the variables, initializes the game,
# // and plays until someone wins or the game becomes unwinnable.


def main():
    board = clear()
    nextPlayer = 'X'
    winningPlayer = ' '

    display(board)

    while winningPlayer == ' ':
        nextPlayer = takeTurn(board, nextPlayer)
        display(board)
        winningPlayer = winner(board)
        if winningPlayer == '?':
            print("Nobody won. Please play again.")
        elif winningPlayer != ' ':
            print("Congratulations, ", winningPlayer, " YOU WON!")
    return True


main()
