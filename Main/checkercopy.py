import random
import checkerex
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
    global brp
    for row in game_board:
        print(row)
    print('')
    print(turn)
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
    global Valid
    global stupiderror
    global extraturn
    if turn == 'Black':
        if Valid == True or move == 'move':
            if not (1 <= move[0] <= 8):
                print(Nonev)
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
        if Valid == True or to == 'to':
            if to[0] < 1 or to[0] > 8:
                print(Nonev)
                failfunc()
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
                else:
                    print(Nonev)
                    movevalid = False
                    toQValid = False
                    toPValid = False
                    extraturn +=1
                if movevalid == True and toQValid == True or movevalid == True and toPValid == True:
                    rowm[move[1]] = '--'
        else:
            failfunc()

    elif turn == 'White':
        if Valid == True or move == 'move':
            if not (1 <= move[0] <= 8):
                print(Nonev)
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
        if Valid == True or to == 'to':
            if to[0] < 1 or to[0] > 8:
                print(Nonev)
                failfunc()
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

                else:
                    print(Nonev)
                    movevalid = False
                    toQValid = False
                    toPValid = False
                    extraturn +=1
                if movevalid == True and toQValid == True or movevalid == True and toPValid == True:
                    rowm[move[1]] = '--'
        else:
            failfunc()
    

while game_state == True:
    Printboard()

    try:
        move = [int(input('peice-y:')),int(input('peice-z:'))]
        to = [int(input('to-y:')),int(input('to-z:'))]
        if move[0] > 8 or to[0] > 8 or move[1] > 8 or to[1] > 8:
            move = [0,0]
            to = [0,0]
    except:
        print('Input must be a number 1-8')
        move = [0,0]
        to = [0,0]
    
    row = game_board[move[0]]


    if QM == True:
        row = game_board[move[0]]
        piece = row[move[1]]

        if piece == 'BQ':
            Black_QM = True
        elif piece == 'WQ':
            White_QM = True

    if move[0] - to[0] == 2 or move[0] + to[0] == 2:
        #row = game_board[to[0]-(move[0]-to[0])]
        capturable = False
    if not move[0] == to[0]-1 and not move[0] == to[0]+1 or not move[1] == to[1]-1 and not move[1] == to[1]+1:
            if capturable == False:
                move = [0,0]
                to = [0,0]
    if turn == 'Black' and Black_QM == False and not move[0] == to[0]-1:
        if capturable == False:
            move = [0,0]
            to = [0,0]
    if turn == 'White' and White_QM == False and not move[0] == to[0]+1:
        if capturable == False:
            move = [0,0]
            to = [0,0]

    movement()
    if Valid == True and stupiderror == False and extraturn == 0:
        if turn == 'White':
            turn = 'Black'
        elif turn == 'Black':
            turn = 'White'
        #save_board = [br0, br1, br2, br3, br4, br5, br6, br7, br8]
    elif Valid == True and stupiderror == False and extraturn > 0:
        extraturn -= 1
    else:
        if stupiderror == True:
            x= 2
        else:
            failfunc()

    movetake1 = 0
    movetake2 = 0
    movetake3 = 0
    movetake4 = 0
    stupiderror = False
    Valid = True
    Black_QM = False
    White_QM = False
    movevalid = False
    print('')