#!/usr/bin/python3
"""
    Displays the TIC-TAC-TOE game board.

: Param Board: List [List [Str]], The game board represented by a list of lists.
: Return: none
    """
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board):
    """
    Check if a player won.

    : Param Board: List [List [Str]], The game board represented by a list of lists.
    : Return: Bool, True if a player won, otherwise False.
    """
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != " ":
            return True

    for col in range(len(board[0])):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return True

    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return True

    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return True

    return False

def tic_tac_toe():
    """
    Launches part of TIC-TAC-TOE between two human players.

    : return: None
    """
    board = [[" "]*3 for _ in range(3)]
    player = "X"
    move_count = 0

    while not check_winner(board) and move_count < 9:
        print_board(board)
        try:
            row = int(input("Enter row (0, 1, or 2) for player " + player + ": "))
            col = int(input("Enter column (0, 1, or 2) for player " + player + ": "))

            # Validation des entrées
            if row not in [0, 1, 2] or col not in [0, 1, 2]:
                print("Invalid input. Please enter 0, 1, or 2 for both row and column.")
                continue  # Continue à la prochaine itération de la boucle

            # Vérifier si la case est disponible
            if board[row][col] == " ":
                board[row][col] = player
                move_count += 1
                if check_winner(board):
                    break

                player = "O" if player == "X" else "X"
            else:
                print("This location is already taken! Try again.")
        except ValueError:
            print("Invalid input. Please enter numerical values for row and column.")

    print_board(board)
    if check_winner(board):
        print("Player " + ("O" if player == "X" else "X") + " won!")
    else:
        print("Draw!")

if __name__ == "__main__":
    tic_tac_toe()
