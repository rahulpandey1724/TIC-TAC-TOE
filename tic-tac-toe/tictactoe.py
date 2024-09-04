board = [" "] * 9

def print_board():

    print(f"| {board[0]} | {board[1]} | {board[2]} |")
    print(f"| {board[3]} | {board[4]} | {board[5]} |")
    print(f"| {board[6]} | {board[7]} | {board[8]} |")

def user_play(user_icon):

    print("Your chance to play",user_icon)
    user_choice = int(input("Enter a number from 1-9 : "))

    # put the user icon in the user choice space
    if board[user_choice - 1] == " ":
        board[user_choice - 1] = user_icon
    else:
        print("This space is already taken;, try another")
        user_play(user_icon)

def is_victory(user_icon):
    if (board[0] == user_icon and board[1] == user_icon and board[2] == user_icon) or \
    (board[3] == user_icon and board[4] == user_icon and board[5] == user_icon) or \
    (board[6] == user_icon and board[7] == user_icon and board[8] == user_icon) or \
    (board[0] == user_icon and board[3] == user_icon and board[6] == user_icon) or \
    (board[1] == user_icon and board[4] == user_icon and board[7] == user_icon) or \
    (board[2] == user_icon and board[5] == user_icon and board[8] == user_icon) or \
    (board[0] == user_icon and board[4] == user_icon and board[8] == user_icon) or \
    (board[2] == user_icon and board[4] == user_icon and board[6] == user_icon):
        return True
    else:
        return False

def is_draw():
    if " " not in board:
        return True
    else:
        return False

# start playing here
while True:

    print_board()
    user_play('X')
    print_board()

    # Either X wins
    if is_victory('X'):
        print("X wins!")
        break
    # Either It's tie
    elif is_draw():
        print("It's a draw")
        break

    # Nothing happens, other user plays
    user_play('O')
    print_board()

    # Either O wins
    if is_victory('O'):
        print("O wins!")
        break

    # Either it's a tie
    elif is_draw():
        print("It's a draw")
        break

    # Nothing happens, other user plays