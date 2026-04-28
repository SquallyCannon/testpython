import random
import math
game_state = True
turn = 'Black'

turnson = True
nojumpcapture = False
game_board = 'An error has occored'
Nonev = 'None valid move.'
Valid = True
capturable = False
Black_QM = False
White_QM = False
QM = True
movetake1 = 0
movetake2 = 0
movetake3 = 0
movetake4 = 0
movevalid = False
toQValid = False
toPValid = False
stupiderror = False
extraturn = 0
skip = False
Done = False
fail = 0
failr = 0
tfailW = 0
tfailB = 0
peices = 0
wpeices = 0
bpeices = 0
print('3 failed movements skips your turn. 3 skips in a row = loss')
br0 = ['0','1 ', '2 ', '3 ', '4 ', '5 ', '6 ', '7 ', '8 ']
br1 = ['1','BP', '--', 'BP', '--', 'BP', '--', 'BP', '--']
br2 = ['2','--', 'BP', '--', 'BP', '--', 'BP', '--', 'BP']
br3 = ['3','BP', '--', 'BP', '--', 'BP', '--', 'BP', '--']
br4 = ['4','--', '--', '--', '--', '--', '--', '--', '--']
br5 = ['5','--', '--', '--', '--', '--', '--', '--', '--']
br6 = ['6','--', 'WP', '--', 'WP', '--', 'WP', '--', 'WP']
br7 = ['7','WP', '--', 'WP', '--', 'WP', '--', 'WP', '--']
br8 = ['8','--', 'WP', '--', 'WP', '--', 'WP', '--', 'WP']
br9 = ['Skip', f"(^v^){turn}(^v^)", 'Done']
game_board = [br0, br1, br2, br3, br4, br5, br6, br7, br8, br9]
save_board = game_board
def Printboard():
    global brp
    global br9
    global turn
    br0 = ['0','1 ', '2 ', '3 ', '4 ', '5 ', '6 ', '7 ', '8 ']
    br9 = ['Skip', f"(^v^){turn}(^v^)", 'Done']
    game_board = [br0, br1, br2, br3, br4, br5, br6, br7, br8, br9]
    for row in game_board:
        if row == ['Skip', f"(^v^){turn}(^v^)", 'Done']:
            print(row[0], row[1], row[2])
        else:
            print(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8])
    print('')
    brp = '--'
def failfunc():
    global Valid
    Valid = False
    game_board[move[0]][move[1]] = brp
def setbrp():
    global brp
    global rowm
    rowm = game_board[move[0]]
    if move[0] == 1:
        brp = rowm[move[1]]
    elif move[0] == 2:
        brp = rowm[move[1]]
    elif move[0] == 3:
        brp = rowm[move[1]]
    elif move[0] == 4:
        brp = rowm[move[1]]
    elif move[0] == 5:
        brp = rowm[move[1]]
    elif move[0] == 6:
        brp = rowm[move[1]]
    elif move[0] == 7:
        brp = rowm[move[1]]
    elif move[0] == 8:
        brp = rowm[move[1]]
def movement():
    movetake1 = 0
    movetake2 = 0
    movetake3 = 0
    movetake4 = 0
    toQValid = False
    toPValid = False
    moven = True
    global Valid
    global stupiderror
    global extraturn
    global fail
    global game_state
    global peices

    if turn == 'Black' and moven == True:
        if Valid == True or move == 'move':
            if not (1 <= move[0] <= 8):
                print(Nonev)
                fail += 1
            else:
                rowm = game_board[move[0]]
                if rowm[move[1]] in ('BP', 'BQ'):
                    #setbrp()
                    brp = rowm[move[1]]
                    movevalid = True
                    #rowm[move[1]] = '--'
                else:
                    print(Nonev)
                    failfunc()
                    fail += 1
        if Valid == True or to == 'to':
            if to[0] < 1 or to[0] > 8:
                print(Nonev)
                failfunc()
                fail += 1
            else:
                rowt = game_board[to[0]]
                if rowt[to[1]] == '--' or nojumpcapture == True:
                    if rowm[move[1]] == 'BP' and to[0] == 8 or Black_QM:
                        toQValid = True
                        rowt[to[1]] = 'BQ'
                    else:
                        toPValid = True
                        rowt[to[1]] = 'BP'
                elif rowt[to[1]] in ('WP', 'WQ') and not to[0] > 7 or rowt[to[1]] in ('WP', 'WQ') and not to[0] < 2 or rowt[to[1]] in ('WP', 'WQ') and not to[1] > 7 or rowt[to[1]] in ('WP', 'WQ') and not to[1] < 2:
                    extraturn += 1
                    if move[0] - to[0] > 0:
                        movetake1 = 1
                        to[0] -= 1
                    elif move[0] - to[0] < 0:
                        movetake2 = 1
                        to[0] += 1
                    if move[1] - to[1] > 0:
                        movetake3 = 1
                        to[1] -= 1
                    elif move[1] - to[1] < 0:
                        movetake4 = 1
                        to[1] += 1
                    rowt = game_board[to[0]]
                    if rowt[to[1]] == '--':
                        if rowm[move[1]] == 'BP' and to[0] == 8 or Black_QM:
                            rowt[to[1]] = 'BQ'
                            if movetake1 == 1:
                                to[0] += 1
                            if movetake2 == 1:
                                to[0] -= 1
                            if movetake3 == 1:
                                to[1] += 1
                            if movetake4 == 1:
                                to[1] -= 1
                            rowt = game_board[to[0]]
                            rowt[to[1]] = '--'
                            toQValid = True
                        else:
                            rowt[to[1]] = 'BP'
                            if movetake1 == 1:
                                to[0] += 1
                            if movetake2 == 1:
                                to[0] -= 1
                            if movetake3 == 1:
                                to[1] += 1
                            if movetake4 == 1:
                                to[1] -= 1
                            rowt = game_board[to[0]]
                            rowt[to[1]] = '--'
                            toPValid = True
                    else:
                        print(Nonev)
                        stupiderror = True
                        extraturn -= 1
                        fail += 1
                else:
                    print(Nonev)
                    movevalid = False
                    toQValid = False
                    toPValid = False
                    extraturn +=1
                    fail += 1
                if movevalid == True and toQValid == True or movevalid == True and toPValid == True:
                    rowm[move[1]] = '--'
        else:
            failfunc()
            fail += 1

    elif turn == 'White' and moven == True:
        if Valid == True or move == 'move':
            if not (1 <= move[0] <= 8):
                print(Nonev)
                fail += 1
            else:
                rowm = game_board[move[0]]
                if rowm[move[1]] in ('WP', 'WQ'):
                    #setbrp()
                    brp = rowm[move[1]]
                    movevalid = True
                    #rowm[move[1]] = '--'
                else:
                    print(Nonev)
                    failfunc()
                    fail += 1
        if Valid == True or to == 'to':
            if to[0] < 1 or to[0] > 8:
                print(Nonev)
                failfunc()
                fail += 1
            else:
                rowt = game_board[to[0]]
                if rowt[to[1]] == '--' or nojumpcapture == True:
                    if rowm[move[1]] == 'WP' and to[0] == 1 or White_QM:
                        toQValid = True
                        rowt[to[1]] = 'WQ'
                    else:
                        toPValid = True
                        rowt[to[1]] = 'WP'
                elif rowt[to[1]] in ('BP', 'BQ') and not to[0] > 7 or rowt[to[1]] in ('BP', 'BQ') and not to[0] < 2 or rowt[to[1]] in ('BP', 'BQ') and not to[1] > 7 or rowt[to[1]] in ('BP', 'BQ') and not to[1] < 2:
                    extraturn += 1
                    if move[0] - to[0] > 0:
                        movetake1 = 1
                        to[0] -= 1
                    elif move[0] - to[0] < 0:
                        movetake2 = 1
                        to[0] += 1
                    if move[1] - to[1] > 0:
                        movetake3 = 1
                        to[1] -= 1
                    elif move[1] - to[1] < 0:
                        movetake4 = 1
                        to[1] += 1
                    rowt = game_board[to[0]]
                    if rowt[to[1]] == '--':
                        if rowm[move[1]] == 'WP' and to[0] == 1 or White_QM:
                            rowt[to[1]] = 'WQ'
                            if movetake1 == 1:
                                to[0] += 1
                            if movetake2 == 1:
                                to[0] -= 1
                            if movetake3 == 1:
                                to[1] += 1
                            if movetake4 == 1:
                                to[1] -= 1
                            rowt = game_board[to[0]]
                            rowt[to[1]] = '--'
                            toQValid = True
                        else:
                            rowt[to[1]] = 'WP'
                            if movetake1 == 1:
                                to[0] += 1
                            if movetake2 == 1:
                                to[0] -= 1
                            if movetake3 == 1:
                                to[1] += 1
                            if movetake4 == 1:
                                to[1] -= 1
                            rowt = game_board[to[0]]
                            rowt[to[1]] = '--'
                            toPValid = True
                    else:
                        print(Nonev)
                        stupiderror = True
                        extraturn -= 1
                        fail += 1

                else:
                    print(Nonev)
                    movevalid = False
                    toQValid = False
                    toPValid = False
                    extraturn +=1
                    fail += 1
                if movevalid == True and toQValid == True or movevalid == True and toPValid == True:
                    rowm[move[1]] = '--'
        else:
            failfunc()
            fail += 1
    

while game_state == True:
    Printboard()

    if failr >= 1:
        print('fails:', failr)
    if turn == 'Black' and tfailB >= 1:
        print('Turn fails:', tfailB)
    elif turn == 'White' and tfailW >= 1:
        print('Turn fails:', tfailW)

    for row in game_board:
        for peice in row:
            if peice in ('BP', 'BQ'):
                bpeices += 1
            if peice in ('WP', 'WQ'):
                wpeices += 1
    if bpeices == 0 or wpeices == 0:
        if bpeices == 0:
            print('Black Loses')
        elif wpeices == 0:
            print('White Loses')
        game_state = False
    elif turn == 'Black':
        print(f'You have {bpeices} peices remaining.')
    else:
        print(f'You have {wpeices} peices remaining.')

    if game_state == True:
        try:
            move = [input('peice-y:'),input('peice-x:')]
            to = [input('to-y:'),input('to-x:')]
            if move[0] == 'skip' or move[1] == 'skip' or to[0] == 'skip' or to[1] == 'skip':
                skip = True
                if turn == 'White':
                    tfailW += 1
                elif turn == 'Black':
                    tfailB += 1
            elif move[0] == 'done' or move[1] == 'done' or to[0] == 'done' or to[1] == 'done':
                Done = True
            else:
                move = [int(move[0]),int(move[1])]
                to = [int(to[0]),int(to[1])]
                if move[0] in (11,13,15,17,22,24,26,28,31,33,35,37,42,44,46,48,51,53,55,57,62,64,66,68,71,73,75,77,82,84,86,88):
                    move[1] = move[0]%10
                    move[0] = math.floor(move[0]/10)
                if to[0] in (11,13,15,17,22,24,26,28,31,33,35,37,42,44,46,48,51,53,55,57,62,64,66,68,71,73,75,77,82,84,96,88):
                    to[1] = to[0]%10
                    to[0] = math.floor(to[0]/10)
                if move[0] > 8 or to[0] > 8 or move[1] > 8 or to[1] > 8:
                    brp = '0'
                    move = [0,0]
                    to = [0,0]
                    fail += 1
        except:
            print('Input must be a number 1-8')
            fail += 1
            brp = '0'
            move = [0,0]
            to = [0,0]

        if skip == False and Done == False:
            row = game_board[move[0]]


            if QM == True:
                row = game_board[move[0]]
                piece = row[move[1]]

                if piece == 'BQ':
                    Black_QM = True
                elif piece == 'WQ':
                    White_QM = True

            if not move[0] == to[0]-1 and not move[0] == to[0]+1 or not move[1] == to[1]-1 and not move[1] == to[1]+1:
                move = [0,0]
                to = [0,0]
                fail += 1
            if turn == 'Black' and Black_QM == False and not move[0] == to[0]-1:
                move = [0,0]
                to = [0,0]
                fail += 1
            if turn == 'White' and White_QM == False and not move[0] == to[0]+1:
                move = [0,0]
                to = [0,0]
                fail += 1

            movement()

        if Done == True:
            Printboard()
            game_state = False

        if fail >= 1:
            failr += 1

        if Valid == True and stupiderror == False and extraturn == 0 or failr > 3:
            if turn == 'White':
                turn = 'Black'
                if fail > 3:
                    tfailW += 1
                elif skip == False:
                    tfailW = 0
            elif turn == 'Black':
                turn = 'White'
                if fail > 3:
                    tfailB += 1
                elif skip == False:
                    tfailB = 0
            failr = 0
        elif Valid == True and stupiderror == False and extraturn > 0:
            extraturn -= 1
        else:
            failfunc()


        if tfailW > 3 or tfailB > 3:
            if tfailB > 3:
                print('Black loses')
            elif tfailW > 3:
                print('White loses')
            game_state = False

        movetake1 = 0
        movetake2 = 0
        movetake3 = 0
        movetake4 = 0
        stupiderror = False
        Valid = True
        Black_QM = False
        White_QM = False
        movevalid = False
        skip = False
        fail = 0
        peices = 0
        wpeices = 0
        bpeices = 0
    print('')