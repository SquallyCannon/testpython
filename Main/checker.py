import random
import checkerex
game_state = True
turn = 'Black'
game_board = 'An error has occored'
Nonev = 'None valid move.'
Valid = True
Black_QM = False
White_QM = False
br0 = ['0 ','1 ', '2 ', '3 ', '4 ', '5 ', '6 ', '7 ', '8 ']
br1 = ['1 ','BP', '--', 'BP', '--', 'BP', '--', 'BP', '--']
br2 = ['2 ','--', 'BP', '--', 'BP', '--', 'BP', '--', 'BP']
br3 = ['3 ','BP', '--', 'BP', '--', 'BP', '--', 'BP', '--']
br4 = ['4 ','--', '--', '--', '--', '--', '--', '--', '--']
br5 = ['5 ','--', '--', '--', '--', '--', '--', '--', '--']
br6 = ['6 ','--', 'WP', '--', 'WP', '--', 'WP', '--', 'WP']
br7 = ['7 ','WP', '--', 'WP', '--', 'WP', '--', 'WP', '--']
br8 = ['8 ','--', 'WP', '--', 'WP', '--', 'WP', '--', 'WP']
game_board = [br0, br1, br2, br3, br4, br5, br6, br7, br8]
save_board = game_board
def Printboard():
    print(game_board[1-1])
    print(game_board[2-1])
    print(game_board[3-1])
    print(game_board[4-1])
    print(game_board[5-1])
    print(game_board[6-1])
    print(game_board[7-1])
    print(game_board[8-1])
    print(game_board[9-1])

while game_state == True:
    print(Printboard())
    print('')
    print(turn)

    
    move = [int(input('peice-y:')),int(input('peice-z:'))]
    to = [int(input('to-y:')),int(input('to-z:'))]


    if turn == 'Black':
        if move[0] == 0 or move[0] > 8:
            print(Nonev)
            Valid = False
        elif move[0] == 1:
            if br1[move[1]] == 'BP' or br1[move[1]] == 'BQ':
                if br1[move[1]] == 'BQ':
                    Black_QM = True
                brp = br1[move[1]]
                br1[move[1]] = '--'
            else:
                print(Nonev)
                Valid = False
        elif move[0] == 2:
            if br2[move[1]] == 'BP' or br2[move[1]] == 'BQ':
                if br2[move[1]] == 'BQ':
                    Black_QM = True
                brp = br2[move[1]]
                br2[move[1]] = '--'
            else:
                print(Nonev)
                Valid = False
        elif move[0] == 3:
            if br3[move[1]] == 'BP' or br3[move[1]] == 'BQ':
                if br3[move[1]] == 'BQ':
                    Black_QM = True
                brp = br3[move[1]]
                br3[move[1]] = '--'
            else:
                print(Nonev)
                Valid = False
        elif move[0] == 4:
            if br4[move[1]] == 'BP' or br4[move[1]] == 'BQ':
                if br4[move[1]] == 'BQ':
                    Black_QM = True
                brp = br4[move[1]]
                br4[move[1]] = '--'
            else:
                print(Nonev)
                Valid = False
        elif move[0] == 5:
            if br5[move[1]] == 'BP' or br5[move[1]] == 'BQ':
                if br5[move[1]] == 'BQ':
                    Black_QM = True
                brp = br5[move[1]]
                br5[move[1]] = '--'
            else:
                print(Nonev)
                Valid = False
        elif move[0] == 6:
            if br6[move[1]] == 'BP' or br6[move[1]] == 'BQ':
                if br6[move[1]] == 'BQ':
                    Black_QM = True
                brp = br6[move[1]]
                br6[move[1]] = '--'
            else:
                print(Nonev)
                Valid = False
        elif move[0] == 7:
            if br7[move[1]] == 'BP' or br7[move[1]] == 'BQ':
                if br7[move[1]] == 'BQ':
                    Black_QM = True
                brp = br7[move[1]]
                br7[move[1]] = '--'
            else:
                print(Nonev)
                Valid = False
        elif move[0] == 8:
            if br8[move[1]] == 'BP' or br8[move[1]] == 'BQ':
                if br8[move[1]] == 'BQ':
                    Black_QM = True
                brp = br8[move[1]]
                br8[move[1]] = '--'
            else:
                print(Nonev)
                Valid = False

        if Valid == True:
            if to[0] == 0 or to[0] > 8:
                print(Nonev)
                game_board = save_board
            elif to[0] == 1:
                if br1[to[1]] == '--':
                    br1[to[1]] = 'BP'
                    if Black_QM == True:
                        br1[to[1]] = 'BQ'
                else:
                    print(Nonev)
                    game_board = save_board
            elif to[0] == 2:
                if br2[to[1]] == '--':
                    br2[to[1]] = 'BP'
                    if Black_QM == True:
                        br2[to[1]] = 'BQ'
                else:
                    print(Nonev)
                    game_board = save_board
            elif to[0] == 3:
                if br3[to[1]] == '--':
                    br3[to[1]] = 'BP'
                    if Black_QM == True:
                        br3[to[1]] = 'BQ'
                else:
                    print(Nonev)
                    game_board = save_board
            elif to[0] == 4:
                if br4[to[1]] == '--':
                    br4[to[1]] = 'BP'
                    if Black_QM == True:
                        br4[to[1]] = 'BQ'
                else:
                    print(Nonev)
                    game_board = save_board
            elif to[0] == 5:
                if br5[to[1]] == '--':
                    br5[to[1]] = 'BP'
                    if Black_QM == True:
                        br5[to[1]] = 'BQ'
                else:
                    print(Nonev)
                    game_board = save_board
            elif to[0] == 6:
                if br6[to[1]] == '--':
                    br6[to[1]] = 'BP'
                    if Black_QM == True:
                        br6[to[1]] = 'BQ'
                else:
                    print(Nonev)
                    game_board = save_board
            elif to[0] == 7:
                if br7[to[1]] == '--':
                    br7[to[1]] = 'BP'
                    if Black_QM == True:
                        br7[to[1]] = 'BQ'
                else:
                    print(Nonev)
                    game_board = save_board
            elif to[0] == 8:
                if br8[to[1]] == '--':
                    br8[to[1]] = 'BQ'
                    if Black_QM == True:
                        br8[to[1]] = 'BQ'
                else:
                    print(Nonev)
                    game_board = save_board

        else:
            game_board = save_board

    elif turn == 'White':
        if move[0] == 0 or move[0] > 8:
            print(Nonev)
            Valid = False
        elif move[0] == 1:
            if br1[move[1]] == 'WP' or br1[move[1]] == 'WQ':
                if br1[move[1]] == 'WQ':
                    White_QM = True
                brp = br1[move[1]]
                br1[move[1]] = '--'
            else:
                print(Nonev)
                Valid = False
        elif move[0] == 2:
            if br2[move[1]] == 'WP' or br2[move[1]] == 'WQ':
                if br2[move[1]] == 'WQ':
                    White_QM = True
                brp = br2[move[1]]
                br2[move[1]] = '--'
            else:
                print(Nonev)
                Valid = False
        elif move[0] == 3:
            if br3[move[1]] == 'WP' or br3[move[1]] == 'WQ':
                if br3[move[1]] == 'WQ':
                    White_QM = True
                brp = br3[move[1]]
                br3[move[1]] = '--'
            else:
                print(Nonev)
                Valid = False
        elif move[0] == 4:
            if br4[move[1]] == 'WP' or br4[move[1]] == 'WQ':
                if br4[move[1]] == 'WQ':
                    White_QM = True
                brp = br4[move[1]]
                br4[move[1]] = '--'
            else:
                print(Nonev)
                Valid = False
        elif move[0] == 5:
            if br5[move[1]] == 'WP' or br5[move[1]] == 'WQ':
                if br5[move[1]] == 'WQ':
                    White_QM = True
                brp = br5[move[1]]
                br5[move[1]] = '--'
            else:
                print(Nonev)
                Valid = False
        elif move[0] == 6:
            if br6[move[1]] == 'WP' or br6[move[1]] == 'WQ':
                if br6[move[1]] == 'WQ':
                    White_QM = True
                brp = br6[move[1]]
                br6[move[1]] = '--'
            else:
                print(Nonev)
                Valid = False
        elif move[0] == 7:
            if br7[move[1]] == 'WP' or br7[move[1]] == 'WQ':
                if br7[move[1]] == 'WQ':
                    White_QM = True
                brp = br7[move[1]]
                br7[move[1]] = '--'
            else:
                print(Nonev)
                Valid = False
        elif move[0] == 8:
            if br8[move[1]] == 'WP' or br8[move[1]] == 'WQ':
                if br8[move[1]] == 'WQ':
                    White_QM = True
                brp = br8[move[1]]
                br8[move[1]] = '--'
            else:
                print(Nonev)
                Valid = False

        if Valid == True:
            if to[0] == 0 or to[0] > 8:
                print(Nonev)
                game_board = save_board
            elif to[0] == 1:
                if br1[to[1]] == '--':
                    br1[to[1]] = 'WQ'
                    if White_QM == True:
                        br1[to[1]] = 'WQ'
                else:
                    print(Nonev)
                    game_board = save_board
            elif to[0] == 2:
                if br2[to[1]] == '--':
                    br2[to[1]] = 'WP'
                    if White_QM == True:
                        br2[to[1]] = 'WQ'
                else:
                    print(Nonev)
                    game_board = save_board
            elif to[0] == 3:
                if br3[to[1]] == '--':
                    br3[to[1]] = 'WP'
                    if White_QM == True:
                        br3[to[1]] = 'WQ'
                else:
                    print(Nonev)
                    game_board = save_board
            elif to[0] == 4:
                if br4[to[1]] == '--':
                    br4[to[1]] = 'WP'
                    if White_QM == True:
                        br4[to[1]] = 'WQ'
                else:
                    print(Nonev)
                    game_board = save_board
            elif to[0] == 5:
                if br5[to[1]] == '--':
                    br5[to[1]] = 'WP'
                    if White_QM == True:
                        br5[to[1]] = 'WQ'
                else:
                    print(Nonev)
                    game_board = save_board
            elif to[0] == 6:
                if br6[to[1]] == '--':
                    br6[to[1]] = 'WP'
                    if White_QM == True:
                        br6[to[1]] = 'WQ'
                else:
                    print(Nonev)
                    game_board = save_board
            elif to[0] == 7:
                if br7[to[1]] == '--':
                    br7[to[1]] = 'WP'
                    if White_QM == True:
                        br7[to[1]] = 'WQ'
                else:
                    print(Nonev)
                    game_board = save_board
            elif to[0] == 8:
                if br8[to[1]] == '--':
                    br8[to[1]] = 'WP'
                    if White_QM == True:
                        br8[to[1]] = 'WQ'
                else:
                    print(Nonev)
                    game_board = save_board

        else:
            game_board = save_board
            
    if Valid == True:
        if turn == 'White':
            turn = 'Black'
        elif turn == 'Black':
            turn = 'White'
    save_board = game_board
    Valid = True
    Black_QM = False
    White_QM = False
    print('')
