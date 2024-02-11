from random import randint
from time import sleep


def tic_tac_toe():
    def show_board():  # prints out "board" list to look like an actual tic-tac-toe board
        board_square, board_square_counter = 0, 0
        print()
        for _ in range(len(board)):
            print(board[board_square], end="")
            board_square += 1
            board_square_counter += 1
            if board_square_counter == 5:
                print()
                board_square_counter = 0

    def check_piece_pos(pos):  # checks if where player 1/2 has chosen to place they're piece is a valid position
        return True if 1 <= pos <= 9 else False

    def update_occupied_squares(square):  # updates "occupied_squares" list to keep count of occupied spaces
        occupied_squares[square] = True if occupied_squares[square] is False else False

    def occupied_squares_full():  # checks if the "occupied_squares" list is full or not
        total = 0
        for a in range(len(occupied_squares)):
            total += 1 if occupied_squares[a] is not False else 0
        return True if total == 10 else False

    def check_for_wins():  # checks if a player has won based off of all tic-tac-toe win cases
        if (  # all player 1 win cases
            (board[0] == p1_piece and board[2] == p1_piece and board[4] == p1_piece or 
            board[10] == p1_piece and board[12] == p1_piece and board[14] == p1_piece or 
            board[20] == p1_piece and board[22] == p1_piece and board[24] == p1_piece or 
            board[0] == p1_piece and board[10] == p1_piece and board[20] == p1_piece or 
            board[2] == p1_piece and board[12] == p1_piece and board[22] == p1_piece or 
            board[4] == p1_piece and board[14] == p1_piece and board[24] == p1_piece or 
            board[0] == p1_piece and board[12] == p1_piece and board[24] == p1_piece or 
            board[4] == p1_piece and board[12] == p1_piece and board[20] == p1_piece
            )):
            print(f"\n{p1} wins!")
            return True
        elif (  # all player 2 win cases
            (board[0] == p2_piece and board[2] == p2_piece and board[4] == p2_piece or 
            board[10] == p2_piece and board[12] == p2_piece and board[14] == p2_piece or 
            board[20] == p2_piece and board[22] == p2_piece and board[24] == p2_piece or 
            board[0] == p2_piece and board[10] == p2_piece and board[20] == p2_piece or 
            board[2] == p2_piece and board[12] == p2_piece and board[22] == p2_piece or 
            board[4] == p2_piece and board[14] == p2_piece and board[24] == p2_piece or 
            board[0] == p2_piece and board[12] == p2_piece and board[24] == p2_piece or 
            board[4] == p2_piece and board[12] == p2_piece and board[20] == p2_piece
            )):
            print(f"\n{p2} wins!")
            return True
        else:  # nobody has won
            return False

    def check_for_ties():  # checks if there's any ties if there are no wins and the board is full
        return True if check_for_wins() is False and occupied_squares_full() is True else False

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    # "empty" squares: row 1 (0, 2, 4), row 3 (10, 12, 14), row 5 (20, 22, 24)
    board = ["1", "|", "2", "|", "3",
            "-", "-", "-", "-", "-",
            "4", "|", "5", "|", "6",
            "-", "-", "-", "-", "-",
            "7", "|", "8", "|", "9"]
    occupied_squares = ["",
                        False, False, False,
                        False, False, False,  # keeps count of which squares on the board are occupied
                        False, False, False,]  # The "" keeps the index in order to keep the "update_occupied_squares" function working

    # choosing who goes first via coin flip
    print("\n\nBefore the game begins, we will select who goes first at random...\n")
    coin_flip = randint(1, 2)
    p1 = p1_name if coin_flip == 1 else p2_name
    p2 = p2_name if coin_flip == 1 else p1_name
    for _ in range(6):  # player names "animation"
        print(p2, end="")
        sleep(0.3)
        print(end="\r")
        print(p1, end="")
        sleep(0.3)
        print(end="\r")
    print(f"{p1} goes first!!")
    sleep(1)

    # allows player 1 to choose whether they'll be X or O
    while True:
        p1_piece_choice = input(f"\n{p1}, choose whether you want to be 'X' or 'O': ")
        if (p1_piece_choice == "X" or p1_piece_choice == "x" or 
            p1_piece_choice == "O" or p1_piece_choice == "o" or p1_piece_choice == "0"
            ):
            p1_piece, p2_piece = "O", "X"
            if p1_piece_choice == "X" or p1_piece_choice == "x":
                p1_piece, p2_piece = "X", "O"
            break
        print("Invalid input!")
        continue

    # continues to actual tic-tac-toe game
    p1_turn, p2_turn = 0, 0  # count the amount of turns each player has
    while True:
        show_board()
        if p1_turn == p2_turn:  # checks which player has the current turn
            while True:  # checks if the current players turn piece position is valid
                try:
                    p1_piece_pos = int(input(f"\n{p1}, choose where you want to place your piece: "))
                except ValueError:
                    print("Place Taken!")
                    continue
                if check_piece_pos(p1_piece_pos) is False or occupied_squares[p1_piece_pos] is True:
                    print("Place Taken!")
                    continue
                elif check_piece_pos(p1_piece_pos) is True and occupied_squares[p1_piece_pos] is False:
                    for b in range(len(board)):
                        board[b] = p1_piece if board[b] == f"{p1_piece_pos}" else board[b]
                    update_occupied_squares(p1_piece_pos)
                    p1_turn += 1
                    break  # breaks loop that checks current player's turn
        else:
            while True:  # checks if the current players turn piece position is valid
                try:
                    p2_piece_pos = int(input(f"\n{p2_name}, choose where you want to place your piece: "))
                except ValueError:
                    print("Place Taken!")
                    continue
                if check_piece_pos(p2_piece_pos) is False or occupied_squares[p2_piece_pos] is True:
                    print("Place Taken!")
                    continue
                elif check_piece_pos(p2_piece_pos) is True and occupied_squares[p2_piece_pos] is False:
                    for c in range(len(board)):
                        board[c] = p2_piece if board[c] == f"{p2_piece_pos}" else board[c]
                    update_occupied_squares(p2_piece_pos)
                    p2_turn += 1
                    break  # breaks loop that checks current player's turn

        if check_for_wins() is True:  # if a player has won, the game ends
            show_board(); sleep(2)
            break
        if check_for_ties() is True:  # if there is a tie, the game ends
            print("\nTIE!!"); show_board(); sleep(2)
            break
        continue  # if a player hasn't won, the game continues


if __name__ == "__main__":
    while True:
        input("\nWelcome to Tic-Tac-Toe! Press 'enter' to begin...")  # game intro

        p1_name = input("\nPlayer 1, enter your username: ")  # getting player usernames
        print(f"Welcome, {p1_name}!")
        p2_name = input("\nPlayer 2, enter your username: ")
        print(f"Welcome, {p2_name}!")

        tic_tac_toe()  # runs "tic_tac_toe" function containing tic-tac-toe game

        option = ""  # keeps count of what the player chooses
        while True:  # menu to play another game, start over completely, or quit the game
            try:
                reset = int(input(
                    "\nWould you like to:\n"
                    "1) Play another game\n"
                    "2) Start over\n"
                    "3) Quit\n"
                    "Choose: "
                    ))
                if reset == 1:
                    tic_tac_toe()
                    continue
                elif reset == 2:
                    option = "start over"
                    break
                elif reset == 3:
                    break
                else:
                    print("Invalid input!")
                    continue
            except ValueError:
                print("Invalid input!")
                continue

        if option == "start over":
            continue

        print("\nBYE!!\n")
        sleep(2)
        break
