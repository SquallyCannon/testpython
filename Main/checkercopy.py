import random
import math
import inspect
from tkinter import *
game_state = True
gamer_state = True
turn = 'Black'
startturn = 'Black'
boardx = '8x8'
if boardx == '8x8':
    boardx = 8
elif boardx == '16x16':
    boardx = 16
widths =3

root = Tk()
root.geometry('400x300')
root.title('ArchCheckers')
lbl = Label(root, text = "Clicked (0, 0)")
lbl.grid()
lbl3 = Label(root, text = "Clicked (--)")
lbl3.grid(row=1)
lbl4 = Label(root, text = f"Turn ({turn})")
lbl4.grid(row=2)
lbl5 = Label(root, text = f"No winner", width=10)
lbl5.grid(row=3)


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
done = False
tosetter = False
donesetter = BooleanVar(value=False)
restart = BooleanVar(value=False)
choice = False
game_end = False
fail = 0
failr = 0
tfailW = 0
tfailB = 0
peices = 0
wpeices = 0
bpeices = 0
checkerp = 0
print('3 failed movements skips your turn. 3 skips in a row = loss')
def board():
    global br0, br1
    global br2
    global br3
    global br4
    global br5
    global br6
    global br7
    global br8
    global br9
    global br10
    global br11
    global br12
    global br13
    global br14
    global br15
    global br16
    global br17
    global game_board
    if boardx == 8:
        br0 = ['0','1 ', '2 ', '3 ', '4 ', '5 ', '6 ', '7 ', '8 ']
        br1 = ['1','BP', '--', 'BP', '--', 'BP', '--', 'BP', '--']
        br2 = ['2','--', 'BP', '--', 'BP', '--', 'BP', '--', 'BP']
        br3 = ['3','BP', '--', 'BP', '--', 'BP', '--', 'BP', '--']
        br4 = ['4','--', '--', '--', '--', '--', '--', '--', '--']
        br5 = ['5','--', '--', '--', '--', '--', '--', '--', '--']
        br6 = ['6','--', 'WP', '--', 'WP', '--', 'WP', '--', 'WP']
        br7 = ['7','WP', '--', 'WP', '--', 'WP', '--', 'WP', '--']
        br8 = ['8','--', 'WP', '--', 'WP', '--', 'WP', '--', 'WP']
        br9 = ['Skip', f"(^v^){turn}(^v^)", 'done']
        game_board = [br0, br1, br2, br3, br4, br5, br6, br7, br8, br9]
    elif boardx == 16:
        br0 =  ['0 ','1 ', '2 ', '3 ', '4 ', '5 ', '6 ', '7 ', '8 ','9 ', '10', '11', '12', '13', '14', '15', '16']
        br1 =  ['1 ','BP', '--', 'BP', '--', 'BP', '--', 'BP', '--','BP', '--', 'BP', '--', 'BP', '--', 'BP', '--']
        br2 =  ['2 ','--', 'BP', '--', 'BP', '--', 'BP', '--', 'BP','--', 'BP', '--', 'BP', '--', 'BP', '--', 'BP']
        br3 =  ['3 ','BP', '--', 'BP', '--', 'BP', '--', 'BP', '--','BP', '--', 'BP', '--', 'BP', '--', 'BP', '--']
        br4 =  ['4 ','--', 'BP', '--', 'BP', '--', 'BP', '--', 'BP','--', 'BP', '--', 'BP', '--', 'BP', '--', 'BP']
        br5 =  ['5 ','BP', '--', 'BP', '--', 'BP', '--', 'BP', '--','BP', '--', 'BP', '--', 'BP', '--', 'BP', '--']
        br6 =  ['6 ','--', 'BP', '--', 'BP', '--', 'BP', '--', 'BP','--', 'BP', '--', 'BP', '--', 'BP', '--', 'BP']
        br7 =  ['7 ','--', '--', '--', '--', '--', '--', '--', '--','--', '--', '--', '--', '--', '--', '--', '--']
        br8 =  ['8 ','--', '--', '--', '--', '--', '--', '--', '--','--', '--', '--', '--', '--', '--', '--', '--']
        br9 =  ['9 ','--', '--', '--', '--', '--', '--', '--', '--','--', '--', '--', '--', '--', '--', '--', '--']
        br10 = ['10','--', '--', '--', '--', '--', '--', '--', '--','--', '--', '--', '--', '--', '--', '--', '--']
        br11 = ['11','WP', '--', 'WP', '--', 'WP', '--', 'WP', '--','WP', '--', 'WP', '--', 'WP', '--', 'WP', '--']
        br12 = ['12','--', 'WP', '--', 'WP', '--', 'WP', '--', 'WP','--', 'WP', '--', 'WP', '--', 'WP', '--', 'WP']
        br13 = ['13','WP', '--', 'WP', '--', 'WP', '--', 'WP', '--','WP', '--', 'WP', '--', 'WP', '--', 'WP', '--']
        br14 = ['14','--', 'WP', '--', 'WP', '--', 'WP', '--', 'WP','--', 'WP', '--', 'WP', '--', 'WP', '--', 'WP']
        br15 = ['15','WP', '--', 'WP', '--', 'WP', '--', 'WP', '--','WP', '--', 'WP', '--', 'WP', '--', 'WP', '--']
        br16 = ['16','--', 'WP', '--', 'WP', '--', 'WP', '--', 'WP','--', 'WP', '--', 'WP', '--', 'WP', '--', 'WP']
        br17 = ['Skip', f"(^v^){turn}(^v^)", 'done']
        game_board = [br0, br1, br2, br3, br4, br5, br6, br7, br8, br9, br10, br11, br12, br13, br14, br15, br16, br17]
def Printboard():
    global brp
    global br17
    global br9
    global br0
    global turn
    global boardx
    if boardx == 8:
        br9 = ['Skip', f"(^v^){turn}(^v^)", 'done']
        game_board = [br0, br1, br2, br3, br4, br5, br6, br7, br8, br9]
    elif boardx == 16:
        br17 = ['Skip', f"(^v^){turn}(^v^)", 'done']
        game_board = [br0, br1, br2, br3, br4, br5, br6, br7, br8, br9, br10, br11, br12, br13, br14, br15, br16, br17]
    for row in game_board:
        if row == ['Skip', f"(^v^){turn}(^v^)", 'done'] or row == ['Skip', f"(^v^){turn}(^v^)", 'done']:
            print(row[0], row[1], row[2])
        elif boardx == 16:
            print(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11], row[12], row[13], row[14], row[15], row[16])
        else:
            print(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8])
    print('')
    brp = '--'
def failfunc():
    global Valid
    Valid = False
    frame = inspect.currentframe().f_back  # caller's frame
    print(f"[Line {frame.f_lineno}] bro")
    game_board[move[0]][move[1]] = brp
def setbrp():
    global brp
    global rowm
    global boardx
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
    if boardx == 16:
        if move[0] == 9:
            brp = rowm[move[1]]
        elif move[0] == 10:
            brp = rowm[move[1]]
        elif move[0] == 11:
            brp = rowm[move[1]]
        elif move[0] == 12:
            brp = rowm[move[1]]
        elif move[0] == 13:
            brp = rowm[move[1]]
        elif move[0] == 14:
            brp = rowm[move[1]]
        elif move[0] == 15:
            brp = rowm[move[1]]
        elif move[0] == 16:
            brp = rowm[move[1]]
def movement():
    movetake1 = 0
    movetake2 = 0
    movetake3 = 0
    movetake4 = 0
    toQValid = False
    toPValid = False
    moven = True
    global Valid, brp
    global stupiderror
    global extraturn
    global fail
    global game_state
    global peices
    global boardx
    global rowm

    if turn == 'Black' and moven == True:
        if Valid == True or move == 'move':
            if not (1 <= move[0] <= boardx):
                print(Nonev)
                fail += 1
            else:
                rowm = game_board[move[0]]
                if rowm[move[1]] in ('BP', 'BQ'):
                    brp = rowm[move[1]]
                    movevalid = True
                else:
                    print(Nonev,'1')
                    Valid = False
                    movevalid = False
                    fail += 1
        if Valid == True or to == 'to':
            if to[0] < 1 or to[0] > boardx:
                print(Nonev)
                failfunc()
                fail += 1
            else:
                rowt = game_board[to[0]]
                if rowt[to[1]] == '--' or nojumpcapture == True:
                    if rowm[move[1]] == 'BP' and to[0] == boardx or Black_QM:
                        toQValid = True
                        rowt[to[1]] = 'BQ'
                    else:
                        toPValid = True
                        rowt[to[1]] = 'BP'
                elif rowt[to[1]] in ('WP', 'WQ') and to[0] in (2,3,4,5,6,7) and to[1] in (2,3,4,5,6,7):
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
                        if rowm[move[1]] == 'BP' and to[0] == boardx or Black_QM:
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
                        print(Nonev,'2')
                        stupiderror = True
                        extraturn -= 1
                        fail += 1
                        movevalid = False
                        toQValid = False
                        toPValid = False
                else:
                    print(Nonev, '3')
                    movevalid = False
                    toQValid = False
                    toPValid = False
                    Valid = False
                    fail += 1
                if movevalid == True and toQValid == True or movevalid == True and toPValid == True:
                    rowm[move[1]] = '--'
        else:
            #failfunc()
            fail += 1

    elif turn == 'White' and moven == True:
        if Valid == True or move == 'move':
            if not (1 <= move[0] <= boardx):
                print(Nonev)
                fail += 1
            else:
                rowm = game_board[move[0]]
                if rowm[move[1]] in ('WP', 'WQ'):
                    brp = rowm[move[1]]
                    movevalid = True
                else:
                    print(Nonev, '4')
                    Valid = False
                    movevalid = False
                    fail += 1
        if Valid == True or to == 'to':
            if to[0] < 1 or to[0] > boardx:
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
                elif rowt[to[1]] in ('BP', 'BQ') and to[0] in (2,3,4,5,6,7) and to[1] in (2,3,4,5,6,7):
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
                        movevalid = False

                else:
                    print(Nonev, '5')
                    movevalid = False
                    toQValid = False
                    toPValid = False
                    Valid = False
                    fail += 1
                if movevalid == True and toQValid == True or movevalid == True and toPValid == True:
                    rowm[move[1]] = '--'
        else:
            #failfunc()
            fail += 1

def clear_board():
    for widget in root.winfo_children():
        if isinstance(widget, Button):
            widget.destroy()
def clicked(posy,posx):
    global move, tosetter
    if tosetter == True:
        return
    gameboard = game_board[posy]
    lbl.configure(text = f"Clicked {posy, posx}")
    lbl3.configure(text = f"Clicked ({gameboard[posx]})")
    move = [posy, posx]
    tosetter = True
    draw_board2()
def clicked2(posy,posx):
    global to, donesetter
    if donesetter == True:
        return
    to = [posy, posx]
    donesetter.set(True)
def draw_board():
    clear_board()
    lbl4.configure(text = f"Turn: {turn}")
    for r in range(boardx):
        for c in range(boardx):
            rowm2 = [r+1,c+1]
            rowm = game_board[rowm2[0]]
            if rowm[rowm2[1]] in ('--'):
                Button(
                    root, width=widths,
                    #command=lambda posy=r, posx=c: clicked(posy+1, posx+1),
                    background='#999999',
                    activebackground="#3a92FF"
                ).grid(row=r+1, column=c+1)
                '''
                if checkerp == 0:
                    Button(
                        root, width=widths,
                        command=lambda posy=r, posx=c: clicked(posy+1, posx+1),
                        background='#999999',
                        activebackground="#3a92FF"
                    ).grid(row=r+1, column=c+1)
                    checkerp = 1
                elif checkerp == 1:
                    Button(
                        root, width=widths,
                        command=lambda posy=r, posx=c: clicked(posy+1, posx+1),
                        background='#777777',
                        activebackground="#3a92FF"
                    ).grid(row=r+1, column=c+1)
                    checkerp = 0'''
            elif rowm[rowm2[1]] in ('BQ', 'BP'):
                if rowm[rowm2[1]] == 'BQ':
                    Button(
                        root,
                        text="BQ", width=widths,
                        command=lambda posy=r, posx=c: clicked(posy+1, posx+1),
                        background='#444444',
                        foreground= '#cccccc',
                        textvariable='#000000',
                        activebackground="#3a92FF"
                    ).grid(row=r+1, column=c+1)
                else:
                    Button(
                        root,
                        text="BP", width=widths,
                        command=lambda posy=r, posx=c: clicked(posy+1, posx+1),
                        background='#222222',
                        foreground= '#cccccc',
                        activebackground="#3a92FF"
                    ).grid(row=r+1, column=c+1)
            elif rowm[rowm2[1]] in ('WQ', 'WP'):
                if rowm[rowm2[1]] == 'WQ':
                    Button(
                        root,
                        text="WQ", width=widths,
                        command=lambda posy=r, posx=c: clicked(posy+1, posx+1),
                        background='#dddddd',
                        activebackground="#3a92FF"
                    ).grid(row=r+1, column=c+1)
                else:
                    Button(
                        root,
                        text="WP", width=widths,
                        command=lambda posy=r, posx=c: clicked(posy+1, posx+1),
                        background='#bbbbbb',
                        activebackground="#3a92FF"
                    ).grid(row=r+1, column=c+1)
    Button(
        root, text='Skip Turn', width=9,
        background='#888888',
        activebackground="#3a92FF",
        command=lambda: skiper()
    ).grid(row=boardx+3, column=2, columnspan= 3)
    Button(
        root, text="End game", width=9,
        background='#888888',
        activebackground="#3a92FF",
        command=lambda: ender() 
    ).grid(row=boardx+3, column=5, columnspan= 3)
def draw_board2():
    clear_board()
    for r in range(boardx):
        for c in range(boardx):
            rowm2 = [r+1,c+1]
            rowm = game_board[rowm2[0]]
            if rowm[rowm2[1]] in ('--'):
                Button(
                    root, width=widths,
                    command=lambda posy=r, posx=c: clicked2(posy+1, posx+1),
                    background='#999999',
                    activebackground="#3a92FF"
                ).grid(row=r+1, column=c+1)
            elif rowm[rowm2[1]] in ('BQ', 'BP'):
                if rowm[rowm2[1]] == 'BQ':
                    Button(
                        root,
                        text="BQ", width=widths,
                        command=lambda posy=r, posx=c: clicked2(posy+1, posx+1),
                        background='#444444',
                        foreground= '#cccccc',
                        activebackground="#3a92FF"
                    ).grid(row=r+1, column=c+1)
                else:
                    Button(
                        root,
                        text="BP", width=widths,
                        command=lambda posy=r, posx=c: clicked2(posy+1, posx+1),
                        background='#222222',
                        foreground= '#cccccc',
                        activebackground="#3a92FF"
                    ).grid(row=r+1, column=c+1)
            elif rowm[rowm2[1]] in ('WQ', 'WP'):
                if rowm[rowm2[1]] == 'WQ':
                    Button(
                        root,
                        text="WQ", width=widths,
                        command=lambda posy=r, posx=c: clicked2(posy+1, posx+1),
                        background='#dddddd',
                        activebackground="#3a92FF"
                    ).grid(row=r+1, column=c+1)
                else:
                    Button(
                        root,
                        text="WP", width=widths,
                        command=lambda posy=r, posx=c: clicked2(posy+1, posx+1),
                        background='#bbbbbb',
                        activebackground="#3a92FF"
                    ).grid(row=r+1, column=c+1)
    Button(
        root, text='Skip Turn', width=9,
        background='#888888',
        activebackground="#3a92FF",
        command=lambda: skiper()
    ).grid(row=boardx+3, column=2, columnspan= 3)
    Button(
        root, text="End game", width=9,
        background='#888888',
        activebackground="#3a92FF",
        command=lambda: ender() 
    ).grid(row=boardx+3, column=5, columnspan= 3)
def end_draw_board():
    clear_board()
    if turn == 'Black':
        lbl5.configure(text = f"White Loses")
    elif turn == 'White':
        print('bwha')
        lbl5.configure(text = f"Black Loses")
    for r in range(boardx):
        for c in range(boardx):
            rowm2 = [r+1,c+1]
            rowm = game_board[rowm2[0]]
            if rowm[rowm2[1]] in ('--'):
                Button(
                    root, width=widths,
                    background='#999999',
                    activebackground="#3a92FF"
                ).grid(row=r+1, column=c+1)
            elif rowm[rowm2[1]] in ('BQ', 'BP'):
                if rowm[rowm2[1]] == 'BQ':
                    Button(
                        root,
                        text="BQ", width=widths,
                        background='#444444',
                        foreground= '#cccccc',
                        activebackground="#3a92FF"
                    ).grid(row=r+1, column=c+1)
                else:
                    Button(
                        root,
                        text="BP", width=widths,
                        background='#222222',
                        foreground= '#cccccc',
                        activebackground="#3a92FF"
                    ).grid(row=r+1, column=c+1)
            elif rowm[rowm2[1]] in ('WQ', 'WP'):
                if rowm[rowm2[1]] == 'WQ':
                    Button(
                        root,
                        text="WQ", width=widths,
                        background='#dddddd',
                        activebackground="#3a92FF"
                    ).grid(row=r+1, column=c+1)
                else:
                    Button(
                        root,
                        text="WP", width=widths,
                        background='#bbbbbb',
                        activebackground="#3a92FF"
                    ).grid(row=r+1, column=c+1)
    Button(
        root, text='Restart', width=9,
        background='#888888',
        activebackground="#3a92FF",
        command=lambda: restarter()
    ).grid(row=boardx+3, column=2, columnspan= 3)
    Button(
        root, text="Don't", width=9,
        background='#888888',
        activebackground="#3a92FF",
        command=lambda: norestarter() 
    ).grid(row=boardx+3, column=5, columnspan= 3)
def skiper():
    global skip, donesetter
    skip = True
    donesetter.set(True)
def ender():
    global done, donesetter, move, to
    done = True
    donesetter.set(True)
def restarter():
    global restart, choice
    choice = True
    restart.set(True)
def norestarter():
    global restart, choice
    choice = False
    restart.set(True)

while gamer_state == True:
    board()
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
            if bpeices == 0 and wpeices == 0:
                print('How-... How did you both manage to loss?')
            elif bpeices == 0:
                print('Black Loses')
            elif wpeices == 0:
                print('White Loses')
            game_end = True
            extraturn = 0
        elif turn == 'Black':
            print(f'You have {bpeices} peices remaining.')
        else:
            print(f'You have {wpeices} peices remaining.')
        if game_end == True:
            Printboard()
            end_draw_board()
            game_state = False
            extraturn = 0
        if game_state == True:
            try:
                draw_board()
                root.wait_variable(donesetter)

                #move = [input('y:'), input('x:')]
                #to = [input('y:'), input('x:')]
                move = [int(move[0]),int(move[1])]
                to = [int(to[0]),int(to[1])]
                if move[0] > boardx or to[0] > boardx or move[1] > boardx or to[1] > boardx:
                    brp = '0'
                    move = [0,0]
                    to = [0,0]
                    fail += 1
            except:
                print(f'Input must be a number 1-{boardx}')
                fail += 1
                brp = '0'
                move = [0,0]
                to = [0,0]


            if skip == False and done == False:
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

            if done == True or game_end == True:
                Printboard()
                end_draw_board()
                game_state = False
                extraturn = 0

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
                failr = 0
            #else:
                #failfunc()

            if tfailW > 3 or tfailB > 3:
                if tfailB > 3:
                    print('Black loses')
                elif tfailW > 3:
                    print('White loses')
                game_end = True
                extraturn = 0

            lbl.configure(text = f"Clicked {0, 0}")
            lbl3.configure(text = f"Clicked (--)")
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
            tosetter = False
            donesetter = BooleanVar(value=False)

        print('')

    root.wait_variable(restart)
    if choice:
        game_state = True
        if startturn == 'Black':
            startturn = 'White'
            turn = 'White'
        elif startturn == 'White':
            startturn = 'Black'
            turn = 'Black'
        extraturn = 0
        game_end = False
        done = False
        restart = BooleanVar(value=False)
        choice = False
        fail = 0
        failr = 0
        tfailW = 0
        tfailB = 0
        lbl5.configure(text = f"No winner")
        print('3 failed movements skips your turn. 3 skips in a row = loss')
    else:
        gamer_state = False
        print('game end')