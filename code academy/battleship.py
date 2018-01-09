from random import randint
board = []
for i in range(5):
    board.append(["O"]*5)


def print_board(board):
    for j in board:
        print(''.join(j))
print_board(board)


def random_row(board):
    return randint(0, len(board)-1)


def random_column(board):
    return randint(0, len(board)-1)
ship_row = random_row(board)
ship_column = random_column(board)

guess_row = int(input("guess row :"))
guess_column = int(input("guess column :"))

print(ship_column)
print(ship_row)

if guess_row == ship_row and guess_column == ship_column:
    print("congratulations you sank my battleship")
else:
    print("you missed my battleship")
    board[guess_row][guess_column] = 'x'
    print_board(board)



