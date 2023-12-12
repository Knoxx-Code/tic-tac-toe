
# Create empty board as a list(will be a list of lists)
board = []


# Function to create board
def createBoard(board):
    for row in range(3):
        board_rows = []  # create lists that will hold the rows
        for column in range(3):
            board_rows.append(" ")
        board.append(board_rows)
    return board


# Function to print in tic-tac-toe format
def printBoard(board):
    for i, row in enumerate(board):
        print(' ' + ' | '.join(row) + ' ')
        if i < len(board) - 1:
            print("-----------")


# Function that checks if a player has won
def isWin(board, player):
    rows = len(board)
    columns = len(board[0])

    # Check diagonals
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        return True

    if board[0][2] == player and board[1][1] == player and board[2][0] == player:
        return True

    # Check rows
    for x in range(rows):
        if board[x][0] == player and board[x][1] == player and board[x][2] == player:
            return True
    # Check columns
    for y in range(columns):
        if board[0][y] == player and board[1][y] == player and board[2][y] == player:
            return True

    return False


# Function that checks if the board is full
def isFull(board):
    for rows in board:
        for x in rows:
            if x == ' ':
                return False
    return True


# Function that checks if the game has ended
def isEnd(board):
    return isWin(board, 'X') or isWin(board, 'O') or isFull(board)


# Function to get and store all possible moves available on the board
def ai_possible_moves(board):
    possible_moves = []
    rows = len(board)
    columns = len(board[0])

    for x in range(rows):
        for y in range(columns):
            if board[x][y] == ' ':
                possible_moves.append((x, y))
    return possible_moves


# Function to return the opposite symbol of whatever the player chooses
def opponent(player):
    return 'O' if player == 'X' else 'X'


# Function to get the various utilities as required
def utility(board, player):
    # Win
    if isWin(board, player):
        return 1
    # Lose/Opponent wins
    elif isWin(board, opponent(player)):
        return -1
    # Draw
    else:
        return 0


# Function to evaluate the minimax algorithm and return best score
def minimax(board, depth, maximizing_player, player):
    # Return utility value of player
    if isEnd(board):
        return utility(board, player)

    # If current player is maximizing
    if maximizing_player:
        best_score = -1000
        # Loop through the possible moves
        for move in ai_possible_moves(board):
            board_copy = place_symbol(board, player, move)
            # Recursive call with a copy of the board, incremented depth and maximizing is set to false to simulate
            # opponents turn
            score = minimax(board_copy, depth + 1, False, player)
            # Get the max score and update best score accordingly
            best_score = max(best_score, score)
        # Return the max which is the best score if AI is maximizing
        return best_score
    # If current player is minimizing
    else:
        best_score = 1000
        for move in ai_possible_moves(board):
            # Creates copy of board with opponent's symbol placed
            board_copy = place_symbol(board, opponent(player), move)
            # Recursive call with a copy of the board, incremented depth and maximizing is set to true to simulate
            # opponents turn
            score = minimax(board_copy, depth + 1, True, player)
            # Get the min score and update best score
            best_score = min(best_score, score)
        # Return the min which is the best score if AI is minimizing
        return best_score


# Function to choose which move the AI makes based on the minimax algorithm
def ai_make_move(board, player):
    best_score = -1000
    best_move = None

    # Loop through the possible moves
    for move in ai_possible_moves(board):
        # Create copy of board with symbol placed
        board_copy = place_symbol(board, player, move)
        # Call the minimax function to evaluate the score
        score = minimax(board_copy, 0, False, player)
        # Check if the score is greater than the best score
        if score > best_score:
            # Update best score
            best_score = score
            # Update best move
            best_move = move
    # Return the best move
    return best_move


# Function that places a symbol in the position chosen by a player
def place_symbol(board, player, move):
    # Create empty list to copy board
    board_copy = []
    for row in board:
        row_cpy = row[:]
        board_copy.append(row_cpy)
    # Extract the coordinates from 'move'
    row, column = move

    board_copy[row][column] = player

    return board_copy


# Function that will handle the game loop
def play(board):
    print("----------TIC-TAC-TOE-----------")

    # Get the input from the user to get the symbol chosen
    human = input("Please select your symbol('X' or 'O'): ").upper()

    # Set the AI to be the other symbol of whatever the user chooses
    ai = opponent(human)

    # Check for invalid user inputs
    while human != 'X' and human != 'O':
        human = input("Invalid marker. Please enter 'X' or 'O': ").upper()

    # Set the current player to be human
    player = human

    # Game loop
    while not isEnd(board):
        printBoard(board)
        # Check if player is 'human'
        if player == human:
            print(f"--HUMAN'S TURN--")
            print("Enter coordinates where you want to place your symbol")
            # Loop to ensure a player does not select a coordinate that's not empty
            while True:
                row = int(input("Select row: "))
                column = int(input("Select column: "))
                if board[row][column] == ' ':
                    break
                else:
                    print("This coordinate is filled. Select another")
        else:
            print(f"--AI'S TURN--")
            row, column = ai_make_move(board, player)
            print(f"AI chooses row: {row} col: {column}")

        # Place marker/ symbol on the board
        board = place_symbol(board, player, (row, column))

        # Check if one of the players has won
        if isWin(board, player):
            printBoard(board)
            if player == ai:
                print(f"Player {player}: AI WINS!")
            elif player == human:
                print(f"Player {player}: YOU WIN!")
            break

        # Switch players
        if player == human:
            player = ai
        else:
            player = human
    # In the event of a tie
    if not isWin(board, human) and not isWin(board, ai) and isFull(board):
        printBoard(board)
        print("It's a tie!")


# Main function
if __name__ == "__main__":
    # Call the create board function
    currentBoard = createBoard(board)
    # Call the play function with the current board
    play(currentBoard)
