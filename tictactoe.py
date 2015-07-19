__author__ = 'yhuang087'


from random import randint

game = []

for x in range(0,3):
    row = []
    for y in range(0,3):
        row.append(0)
    game.append(row)

def print_game(game):
    for rowindex in range(0,3):
        for columnindex in range(0,3):
            if game[rowindex][columnindex] == 1:
                print 'O ',
            if game[rowindex][columnindex] == -1:
                print 'X ',
            if game[rowindex][columnindex] == 0:
                print '- ',
        print ''

turn = randint(0,1)

# computer starts with 0. computer is X


def cturn():
    while True:
        computer_row = randint(0,2)
        computer_column = randint(0,2)
        if game[computer_row][computer_column] == 0:
            game[computer_row][computer_column] = 1
            break


def pturn():
    while True:
        print 'Your Turn'
        player_row = int(raw_input('Input row: ')) - 1
        player_column = int(raw_input('Input column: ')) - 1
        if game[player_row][player_column] == 0:
            game[player_row][player_column] = -1
            break
        else:
            print "Illegal move. Please retry again."

def is_game_over():
    for row in game:
        total = sum(row)
        if total == 3 or total == -3:
            return True

    for columnindex in range(0,3):
        total = 0
        for rowindex in range(0,3):
            total += game[rowindex][columnindex]
        if total == 3 or total == -3:
            return True

    if game[0][0] + game[1][1] + game[2][2] == 3 or game[0][0] + game[1][1] + game[2][2] == -3:
        return True
    if game[0][2] + game[1][1] + game[2][0] == 3 or game[0][2] + game[1][1] + game[2][0] == -3:
        return True

while not is_game_over():
    print print_game(game)
    if turn == 0:
        turn += 1
        cturn()


    elif turn == 1:
        turn -= 1
        pturn()


