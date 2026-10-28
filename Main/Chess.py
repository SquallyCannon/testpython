import random
import math
import Importfunc
import inspect
from tkinter import *
game_state = True
gamer_state = True
turn = 'White'
startturn = 'White'
boardx = 8
test = True
widths = 3

root = Tk()
root.geometry(f'{boardx*40+40}x{boardx*33+33}')
root.title('ArchChess')
x=True
if x:
    randomizerB = False
    randomizerW = False
    nojumpcapture = False
    game_board = 'An error has occored'
    Nonev = 'None valid move.'
    Valid = True
    capturable = False
    movetake1 = 0
    movetake2 = 0
    movetake3 = 0
    movetake4 = 0
    movevalid = False
    toQValid = False
    toPValid = False
    toHValid = False
    toBValid = False
    toKValid = False
    toRValid = False
    stupiderror = False
    extraturn = 0
    skip = False
    done = False
    tosetter = False
    donesetter = BooleanVar(value=False)
    evolveer1 = BooleanVar(value=False)
    evolveer2 = BooleanVar(value=False)
    restart = BooleanVar(value=False)
    choice = False
    game_end = False
    debugon = False
    fail = 0
    failr = 0
    tfailW = 0
    tfailB = 0
    peices = 0
    wpeices = 0
    bpeices = 0
    checkerp = True
    debugad = 0
    turn1 = True
    success = False
    Whiteset = ("WP", "WR", "WH", "WB", "WQ", "WK", "WE")
    Blackset = ("BP", "BR", "BH", "BB", "BQ", "BK", "BE")
    BKcheck = [True, True, True, True, True, True, True, True, True]
    WKcheck = [True, True, True, True, True, True, True, True, True]
    Bok = [False, False, False, False, False, False, False, False, False]
    Wok = [False, False, False, False, False, False, False, False, False]
    enpasantb = []
    enpasantw = []
    Stalemate = False
    WCheck = False
    BCheck = False
    Checkmate = False
color = True
if color:
    emptycolor1 = '#777777' #'#777777'
    emptycolor2 = '#999999' #'#999999'

    WPcolor = '#aaaaaa' #'#bbbbbb'
    WRcolor = '#bbbbbb' #'#bbbbbb'
    WHcolor = '#cccccc' #'#bbbbbb'
    WBcolor = '#dddddd' #'#bbbbbb'
    WQcolor = '#eeeeee' #'#dddddd'
    WKcolor = '#ffffff' #'#bbbbbb'

    BPcolor = '#555555' #'#555555'
    BRcolor = '#444444' #'#444444'
    BHcolor = '#333333' #'#333333'
    BBcolor = '#222222' #'#222222'
    BQcolor = '#111111' #'#111111'
    BKcolor = '#000000' #'#000000'

    buttonscolor = "#888888" #'#888888'
    def rollcolor():
        global emptycolor1, emptycolor2, WPcolor, WRcolor, WHcolor, WBcolor, WQcolor, WKcolor, BQcolor,BRcolor,BHcolor,BBcolor,BKcolor, BPcolor, buttonscolor
        emptycolor1 = "#{:06x}".format(random.randint(0, 0xFFFFFF))
        emptycolor2 ="#{:06x}".format(random.randint(0, 0xFFFFFF))
        WPcolor = "#{:06x}".format(random.randint(0, 0xFFFFFF))
        WRcolor = "#{:06x}".format(random.randint(0, 0xFFFFFF))
        WHcolor = "#{:06x}".format(random.randint(0, 0xFFFFFF))
        WBcolor = "#{:06x}".format(random.randint(0, 0xFFFFFF))
        WQcolor = "#{:06x}".format(random.randint(0, 0xFFFFFF))
        WKcolor = "#{:06x}".format(random.randint(0, 0xFFFFFF))

        BPcolor = "#{:06x}".format(random.randint(0, 0xFFFFFF))
        BRcolor = "#{:06x}".format(random.randint(0, 0xFFFFFF))
        BHcolor = "#{:06x}".format(random.randint(0, 0xFFFFFF))
        BBcolor = "#{:06x}".format(random.randint(0, 0xFFFFFF))
        BQcolor = "#{:06x}".format(random.randint(0, 0xFFFFFF))
        BKcolor = "#{:06x}".format(random.randint(0, 0xFFFFFF))
        buttonscolor = "#{:06x}".format(random.randint(0, 0xFFFFFF))
    #testcolor = "#{:06x}".format(random.randint(0, 0xFFFFFF))
    randomcolor = False
    customcolors = False
    if randomcolor:
        rollcolor()
    elif customcolors:
        emptycolor1 = "#FBFF00" #"#808080"
        emptycolor2 = "#09FF00"
        WPcolor = "#ff9100"
        WQcolor = "#ff0000"
        BPcolor = "#1100FF"
        BQcolor = "#7700ff"
        buttonscolor = "#cc00ff"
    else:
        emptycolor1 = '#777777' #'#777777'
        emptycolor2 = '#999999' #'#999999'

        WPcolor = '#aaaaaa' #'#bbbbbb'
        WRcolor = '#bbbbbb' #'#bbbbbb'
        WHcolor = '#cccccc' #'#bbbbbb'
        WBcolor = '#dddddd' #'#bbbbbb'
        WQcolor = '#eeeeee' #'#dddddd'
        WKcolor = '#ffffff' #'#bbbbbb'

        BPcolor = '#555555' #'#555555'
        BRcolor = '#444444' #'#444444'
        BHcolor = '#333333' #'#333333'
        BBcolor = '#222222' #'#222222'
        BQcolor = '#111111' #'#111111'
        BKcolor = '#000000' #'#000000'

        buttonscolor = "#888888" #'#888888'

    emptytextcolor1 = Importfunc.invert_color(emptycolor1)
    emptytextcolor2 = Importfunc.invert_color(emptycolor2)

    WPtextcolor = Importfunc.invert_color(WPcolor)
    WRtextcolor = Importfunc.invert_color(WRcolor)
    WHtextcolor = Importfunc.invert_color(WHcolor)
    WBtextcolor = Importfunc.invert_color(WBcolor)
    WQtextcolor = Importfunc.invert_color(WQcolor)
    WKtextcolor = Importfunc.invert_color(WKcolor)

    BPtextcolor = Importfunc.invert_color(BPcolor)
    BRtextcolor = Importfunc.invert_color(BRcolor)
    BHtextcolor = Importfunc.invert_color(BHcolor)
    BBtextcolor = Importfunc.invert_color(BBcolor)
    BQtextcolor = Importfunc.invert_color(BQcolor)
    BKtextcolor = Importfunc.invert_color(BKcolor)

    Buttontextcolor = Importfunc.invert_color(buttonscolor)
label=True
if label:
    lbl = Label(root, text = "Clicked (0, 0)")
    lbl.grid(row=0)
    lbl3 = Label(root, text = "Clicked (--)")
    lbl3.grid(row=1)
    lbl4 = Label(root, text = f"Turn ({turn})")
    lbl4.grid(row=2)
    lbl5 = Label(root, text = f"No winner", width=10)
    lbl5.grid(row=3)
    lbl6 = Label(root, text = f"Fails:{failr}", width=10)
    lbl6.grid(row=0, column=1, columnspan=3)
    lbl7 = Label(root, text = f"Mateless", width=10)
    lbl7.grid(row=4)

boardfuctions = True
if boardfuctions:
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
        if boardx == 8 and test == False:
            br0 = ['0','1 ', '2 ', '3 ', '4 ', '5 ', '6 ', '7 ', '8 ', 'errorspace']
            br1 = ['1','BR', 'BH', 'BB', 'BQ', 'BK', 'BB', 'BH', 'BR', 'errorspace']
            br2 = ['2','BP', 'BP', 'BP', 'BP', 'BP', 'BP', 'BP', 'BP', 'errorspace']
            br3 = ['3','--', '--', '--', '--', '--', '--', '--', '--', 'errorspace']
            br4 = ['4','--', '--', '--', '--', '--', '--', '--', '--', 'errorspace']
            br5 = ['5','--', '--', '--', '--', '--', '--', '--', '--', 'errorspace']
            br6 = ['6','--', '--', '--', '--', '--', '--', '--', '--', 'errorspace']
            br7 = ['7','WP', 'WP', 'WP', 'WP', 'WP', 'WP', 'WP', 'WP', 'errorspace']
            br8 = ['8','WR', 'WH', 'WB', 'WQ', 'WK', 'WB', 'WH', 'WR', 'errorspace']
            br9 = ['Skip', f"(^v^){turn}(^v^)", 'done']
            game_board = [br0, br1, br2, br3, br4, br5, br6, br7, br8, br9]
        elif boardx == 16 and test == False:
            br0 =  ['0 ','1 ', '2 ', '3 ', '4 ', '5 ', '6 ', '7 ', '8 ','9 ', '10', '11', '12', '13', '14', '15', '16', 'errorspace']
            br1 =  ['1 ','BP', '--', 'BP', '--', 'BP', '--', 'BP', '--','BP', '--', 'BP', '--', 'BP', '--', 'BP', '--', 'errorspace']
            br2 =  ['2 ','--', 'BP', '--', 'BP', '--', 'BP', '--', 'BP','--', 'BP', '--', 'BP', '--', 'BP', '--', 'BP', 'errorspace']
            br3 =  ['3 ','BP', '--', 'BP', '--', 'BP', '--', 'BP', '--','BP', '--', 'BP', '--', 'BP', '--', 'BP', '--', 'errorspace']
            br4 =  ['4 ','--', 'BP', '--', 'BP', '--', 'BP', '--', 'BP','--', 'BP', '--', 'BP', '--', 'BP', '--', 'BP', 'errorspace']
            br5 =  ['5 ','BP', '--', 'BP', '--', 'BP', '--', 'BP', '--','BP', '--', 'BP', '--', 'BP', '--', 'BP', '--', 'errorspace']
            br6 =  ['6 ','--', 'BP', '--', 'BP', '--', 'BP', '--', 'BP','--', 'BP', '--', 'BP', '--', 'BP', '--', 'BP', 'errorspace']
            br7 =  ['7 ','--', '--', '--', '--', '--', '--', '--', '--','--', '--', '--', '--', '--', '--', '--', '--', 'errorspace']
            br8 =  ['8 ','--', '--', '--', '--', '--', '--', '--', '--','--', '--', '--', '--', '--', '--', '--', '--', 'errorspace']
            br9 =  ['9 ','--', '--', '--', '--', '--', '--', '--', '--','--', '--', '--', '--', '--', '--', '--', '--', 'errorspace']
            br10 = ['10','--', '--', '--', '--', '--', '--', '--', '--','--', '--', '--', '--', '--', '--', '--', '--', 'errorspace']
            br11 = ['11','WP', '--', 'WP', '--', 'WP', '--', 'WP', '--','WP', '--', 'WP', '--', 'WP', '--', 'WP', '--', 'errorspace']
            br12 = ['12','--', 'WP', '--', 'WP', '--', 'WP', '--', 'WP','--', 'WP', '--', 'WP', '--', 'WP', '--', 'WP', 'errorspace']
            br13 = ['13','WP', '--', 'WP', '--', 'WP', '--', 'WP', '--','WP', '--', 'WP', '--', 'WP', '--', 'WP', '--', 'errorspace']
            br14 = ['14','--', 'WP', '--', 'WP', '--', 'WP', '--', 'WP','--', 'WP', '--', 'WP', '--', 'WP', '--', 'WP', 'errorspace']
            br15 = ['15','WP', '--', 'WP', '--', 'WP', '--', 'WP', '--','WP', '--', 'WP', '--', 'WP', '--', 'WP', '--', 'errorspace']
            br16 = ['16','--', 'WP', '--', 'WP', '--', 'WP', '--', 'WP','--', 'WP', '--', 'WP', '--', 'WP', '--', 'WP', 'errorspace']
            br17 = ['Skip', f"(^v^){turn}(^v^)", 'done']
            game_board = [br0, br1, br2, br3, br4, br5, br6, br7, br8, br9, br10, br11, br12, br13, br14, br15, br16, br17]
        elif boardx == 32 and test == False:
            br0 =  ['0 ','1 ', '2 ', '3 ', '4 ', '5 ', '6 ', '7 ', '8 ','9 ', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24','25', '26', '27', '28', '29', '30', '31', '32', 'errorspace']
            br1 =  ['1 ','BP', '--', 'BP', '--', 'BP', '--', 'BP', '--','BP', '--', 'BP', '--', 'BP', '--', 'BP', '--', 'BP', '--', 'BP', '--', 'BP', '--', 'BP', '--','BP', '--', 'BP', '--', 'BP', '--', 'BP', '--', 'errorspace']
            br2 =  ['2 ','--', 'BP', '--', 'BP', '--', 'BP', '--', 'BP','--', 'BP', '--', 'BP', '--', 'BP', '--', 'BP', '--', 'BP', '--', 'BP', '--', 'BP', '--', 'BP','--', 'BP', '--', 'BP', '--', 'BP', '--', 'BP', 'errorspace']
            br3 =  ['3 ','BP', '--', 'BP', '--', 'BP', '--', 'BP', '--','BP', '--', 'BP', '--', 'BP', '--', 'BP', '--', 'BP', '--', 'BP', '--', 'BP', '--', 'BP', '--','BP', '--', 'BP', '--', 'BP', '--', 'BP', '--', 'errorspace']
            br4 =  ['4 ','--', 'BP', '--', 'BP', '--', 'BP', '--', 'BP','--', 'BP', '--', 'BP', '--', 'BP', '--', 'BP', '--', 'BP', '--', 'BP', '--', 'BP', '--', 'BP','--', 'BP', '--', 'BP', '--', 'BP', '--', 'BP', 'errorspace']
            br5 =  ['5 ','BP', '--', 'BP', '--', 'BP', '--', 'BP', '--','BP', '--', 'BP', '--', 'BP', '--', 'BP', '--', 'BP', '--', 'BP', '--', 'BP', '--', 'BP', '--','BP', '--', 'BP', '--', 'BP', '--', 'BP', '--', 'errorspace']
            br6 =  ['6 ','--', 'BP', '--', 'BP', '--', 'BP', '--', 'BP','--', 'BP', '--', 'BP', '--', 'BP', '--', 'BP', '--', 'BP', '--', 'BP', '--', 'BP', '--', 'BP','--', 'BP', '--', 'BP', '--', 'BP', '--', 'BP', 'errorspace']
            br7 =  ['7 ','BP', '--', 'BP', '--', 'BP', '--', 'BP', '--','BP', '--', 'BP', '--', 'BP', '--', 'BP', '--', 'BP', '--', 'BP', '--', 'BP', '--', 'BP', '--','BP', '--', 'BP', '--', 'BP', '--', 'BP', '--', 'errorspace']
            br8 =  ['8 ','--', 'BP', '--', 'BP', '--', 'BP', '--', 'BP','--', 'BP', '--', 'BP', '--', 'BP', '--', 'BP', '--', 'BP', '--', 'BP', '--', 'BP', '--', 'BP','--', 'BP', '--', 'BP', '--', 'BP', '--', 'BP', 'errorspace']
            br9 =  ['9 ','BP', '--', 'BP', '--', 'BP', '--', 'BP', '--','BP', '--', 'BP', '--', 'BP', '--', 'BP', '--', 'BP', '--', 'BP', '--', 'BP', '--', 'BP', '--','BP', '--', 'BP', '--', 'BP', '--', 'BP', '--', 'errorspace']
            br10 = ['10','--', 'BP', '--', 'BP', '--', 'BP', '--', 'BP','--', 'BP', '--', 'BP', '--', 'BP', '--', 'BP', '--', 'BP', '--', 'BP', '--', 'BP', '--', 'BP','--', 'BP', '--', 'BP', '--', 'BP', '--', 'BP', 'errorspace']
            br11 = ['11','BP', '--', 'BP', '--', 'BP', '--', 'BP', '--','BP', '--', 'BP', '--', 'BP', '--', 'BP', '--', 'BP', '--', 'BP', '--', 'BP', '--', 'BP', '--','BP', '--', 'BP', '--', 'BP', '--', 'BP', '--', 'errorspace']
            br12 = ['12','--', 'BP', '--', 'BP', '--', 'BP', '--', 'BP','--', 'BP', '--', 'BP', '--', 'BP', '--', 'BP', '--', 'BP', '--', 'BP', '--', 'BP', '--', 'BP','--', 'BP', '--', 'BP', '--', 'BP', '--', 'BP', 'errorspace']
            br13 = ['13','--', '--', '--', '--', '--', '--', '--', '--','--', '--', '--', '--', '--', '--', '--', '--', '--', '--', '--', '--', '--', '--', '--', '--','--', '--', '--', '--', '--', '--', '--', '--', 'errorspace']
            br14 = ['14','--', '--', '--', '--', '--', '--', '--', '--','--', '--', '--', '--', '--', '--', '--', '--', '--', '--', '--', '--', '--', '--', '--', '--','--', '--', '--', '--', '--', '--', '--', '--', 'errorspace']
            br15 = ['15','--', '--', '--', '--', '--', '--', '--', '--','--', '--', '--', '--', '--', '--', '--', '--', '--', '--', '--', '--', '--', '--', '--', '--','--', '--', '--', '--', '--', '--', '--', '--', 'errorspace']
            br16 = ['16','--', '--', '--', '--', '--', '--', '--', '--','--', '--', '--', '--', '--', '--', '--', '--', '--', '--', '--', '--', '--', '--', '--', '--','--', '--', '--', '--', '--', '--', '--', '--', 'errorspace']
            br17 = ['17','--', '--', '--', '--', '--', '--', '--', '--','--', '--', '--', '--', '--', '--', '--', '--', '--', '--', '--', '--', '--', '--', '--', '--','--', '--', '--', '--', '--', '--', '--', '--', 'errorspace']
            br18 = ['18','--', '--', '--', '--', '--', '--', '--', '--','--', '--', '--', '--', '--', '--', '--', '--', '--', '--', '--', '--', '--', '--', '--', '--','--', '--', '--', '--', '--', '--', '--', '--', 'errorspace']
            br19 = ['19','--', '--', '--', '--', '--', '--', '--', '--','--', '--', '--', '--', '--', '--', '--', '--', '--', '--', '--', '--', '--', '--', '--', '--','--', '--', '--', '--', '--', '--', '--', '--', 'errorspace']
            br20 = ['20','--', '--', '--', '--', '--', '--', '--', '--','--', '--', '--', '--', '--', '--', '--', '--', '--', '--', '--', '--', '--', '--', '--', '--','--', '--', '--', '--', '--', '--', '--', '--', 'errorspace']
            br21 = ['21','WP', '--', 'WP', '--', 'WP', '--', 'WP', '--','WP', '--', 'WP', '--', 'WP', '--', 'WP', '--', 'WP', '--', 'WP', '--', 'WP', '--', 'WP', '--','WP', '--', 'WP', '--', 'WP', '--', 'WP', '--', 'errorspace']
            br22 = ['22','--', 'WP', '--', 'WP', '--', 'WP', '--', 'WP','--', 'WP', '--', 'WP', '--', 'WP', '--', 'WP', '--', 'WP', '--', 'WP', '--', 'WP', '--', 'WP','--', 'WP', '--', 'WP', '--', 'WP', '--', 'WP', 'errorspace']
            br23 = ['23','WP', '--', 'WP', '--', 'WP', '--', 'WP', '--','WP', '--', 'WP', '--', 'WP', '--', 'WP', '--', 'WP', '--', 'WP', '--', 'WP', '--', 'WP', '--','WP', '--', 'WP', '--', 'WP', '--', 'WP', '--', 'errorspace']
            br24 = ['24','--', 'WP', '--', 'WP', '--', 'WP', '--', 'WP','--', 'WP', '--', 'WP', '--', 'WP', '--', 'WP', '--', 'WP', '--', 'WP', '--', 'WP', '--', 'WP','--', 'WP', '--', 'WP', '--', 'WP', '--', 'WP', 'errorspace']
            br25 = ['25','WP', '--', 'WP', '--', 'WP', '--', 'WP', '--','WP', '--', 'WP', '--', 'WP', '--', 'WP', '--', 'WP', '--', 'WP', '--', 'WP', '--', 'WP', '--','WP', '--', 'WP', '--', 'WP', '--', 'WP', '--', 'errorspace']
            br26 = ['26','--', 'WP', '--', 'WP', '--', 'WP', '--', 'WP','--', 'WP', '--', 'WP', '--', 'WP', '--', 'WP', '--', 'WP', '--', 'WP', '--', 'WP', '--', 'WP','--', 'WP', '--', 'WP', '--', 'WP', '--', 'WP', 'errorspace']
            br27 = ['27','WP', '--', 'WP', '--', 'WP', '--', 'WP', '--','WP', '--', 'WP', '--', 'WP', '--', 'WP', '--', 'WP', '--', 'WP', '--', 'WP', '--', 'WP', '--','WP', '--', 'WP', '--', 'WP', '--', 'WP', '--', 'errorspace']
            br28 = ['28','--', 'WP', '--', 'WP', '--', 'WP', '--', 'WP','--', 'WP', '--', 'WP', '--', 'WP', '--', 'WP', '--', 'WP', '--', 'WP', '--', 'WP', '--', 'WP','--', 'WP', '--', 'WP', '--', 'WP', '--', 'WP', 'errorspace']
            br29 = ['29','WP', '--', 'WP', '--', 'WP', '--', 'WP', '--','WP', '--', 'WP', '--', 'WP', '--', 'WP', '--', 'WP', '--', 'WP', '--', 'WP', '--', 'WP', '--','WP', '--', 'WP', '--', 'WP', '--', 'WP', '--', 'errorspace']
            br30 = ['30','--', 'WP', '--', 'WP', '--', 'WP', '--', 'WP','--', 'WP', '--', 'WP', '--', 'WP', '--', 'WP', '--', 'WP', '--', 'WP', '--', 'WP', '--', 'WP','--', 'WP', '--', 'WP', '--', 'WP', '--', 'WP', 'errorspace']
            br31 = ['31','WP', '--', 'WP', '--', 'WP', '--', 'WP', '--','WP', '--', 'WP', '--', 'WP', '--', 'WP', '--', 'WP', '--', 'WP', '--', 'WP', '--', 'WP', '--','WP', '--', 'WP', '--', 'WP', '--', 'WP', '--', 'errorspace']
            br32 = ['32','--', 'WP', '--', 'WP', '--', 'WP', '--', 'WP','--', 'WP', '--', 'WP', '--', 'WP', '--', 'WP', '--', 'WP', '--', 'WP', '--', 'WP', '--', 'WP','--', 'WP', '--', 'WP', '--', 'WP', '--', 'WP', 'errorspace']
            br33 = ['Skip', f"(^v^){turn}(^v^)", 'done']
            game_board = [br0, br1, br2, br3, br4, br5, br6, br7, br8, br9, br10, br11, br12, br13, br14, br15, br16, br17, br18, br19, br20, br21, br22, br23, br24, br25, br26, br27, br28, br29, br30, br31, br32, br33]
        elif test == True:
            br0 = ['0','1 ', '2 ', '3 ', '4 ', '5 ', '6 ', '7 ', '8 ', 'errorspace']
            br1 = ['1','BR', 'BH', 'BB', 'BQ', 'BK', 'BB', 'BH', 'BR', 'errorspace']
            br2 = ['2','WP', 'WP', 'WP', 'BP', 'BP', 'BP', 'WP', 'WP', 'errorspace']
            br3 = ['3','--', '--', '--', '--', '--', '--', '--', '--', 'errorspace']
            br4 = ['4','--', '--', '--', '--', '--', '--', '--', '--', 'errorspace']
            br5 = ['5','--', '--', '--', '--', '--', '--', '--', '--', 'errorspace']
            br6 = ['6','--', '--', '--', '--', '--', '--', '--', '--', 'errorspace']
            br7 = ['7','BP', 'BP', 'BP', 'WP', 'WP', 'WP', 'BP', 'BP', 'errorspace']
            br8 = ['8','WR', 'WH', 'WB', 'WQ', 'WK', 'WB', 'WH', 'WR', 'errorspace']
            br9 = ['Skip', f"(^v^){turn}(^v^)", 'done']
            game_board = [br0, br1, br2, br3, br4, br5, br6, br7, br8, br9]

    def failfunc():
        global Valid, debugon
        Valid = False
        frame = inspect.currentframe().f_back  # caller's frame
        if debugon:
            print(f"[Line {frame.f_lineno}] bro")
        game_board[move[0]][move[1]] = brp
    def setbrp():
        global brp
        global rowm
        global boardx
        rowm = game_board[move[0]]
        for moves in range(boardx):
            if move[0] == moves:
                brp = rowm[move[1]]
    def movement():
        toQValid = False
        toPValid = False
        toHValid = False
        toBValid = False
        toKValid = False
        toRValid = False
        toEValid = False
        moven = True
        global Valid, brp, turn1, Blackset, Whiteset, evolveer1
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
                    #print(Nonev)
                    fail += 1
                else:
                    rowm = game_board[move[0]]
                    if rowm[move[1]] in Blackset:
                        brp = rowm[move[1]]
                        movevalid = True
                    else:
                        #print(Nonev,'1')
                        Valid = False
                        movevalid = False
                        fail += 1
            if Valid == True or to == 'to':
                if to[0] < 1 or to[0] > boardx:
                    #print(Nonev)
                    failfunc()
                    fail += 1
                else:
                    rowt = game_board[to[0]]
                    if rowt[to[1]] == '--' or nojumpcapture == True:
                        if rowm[move[1]] == 'BP' and to[0] == boardx:
                            toEValid = True
                            rowt[to[1]] = 'BE'
                        elif rowm[move[1]] == 'BQ':
                            toQValid = True
                            rowt[to[1]] = 'BQ'
                        elif rowm[move[1]] == 'BH':
                            toHValid = True
                            rowt[to[1]] = 'BH'
                        elif rowm[move[1]] == 'BR':
                            toRValid = True
                            rowt[to[1]] = 'BR'
                        elif rowm[move[1]] == 'BB':
                            toHValid = True
                            rowt[to[1]] = 'BB'
                        elif rowm[move[1]] == 'BK':
                            toRValid = True
                            rowt[to[1]] = 'BK'
                        else:
                            toPValid = True
                            rowt[to[1]] = 'BP'
                            
                    elif rowt[to[1]] in Whiteset:
                        if rowm[move[1]] == 'BP' and to[0] == boardx:
                            toEValid = True
                            rowt[to[1]] = 'BE'
                        elif rowm[move[1]] == 'BQ':
                            toQValid = True
                            rowt[to[1]] = 'BQ'
                        elif rowm[move[1]] == 'BH':
                            rowt[to[1]] = 'BH'
                            toHValid = True
                        elif rowm[move[1]] == 'BR':
                            rowt[to[1]] = 'BR'
                            toRValid = True
                        elif rowm[move[1]] == 'BK':
                            rowt[to[1]] = 'BK'
                            toKValid = True
                        elif rowm[move[1]] == 'BB':
                            rowt[to[1]] = 'BB'
                            toBValid = True
                        elif rowm[move[1]] == 'BP':
                            rowt[to[1]] = 'BP'
                            toPValid = True
                        else:
                            #print(Nonev,'2')
                            stupiderror = True
                            fail += 1
                            movevalid = False
                            toQValid = False
                            toPValid = False
                            toBValid = False
                            toKValid = False
                            toRValid = False
                            toHValid = False
                            toEValid = False
                        rowt = game_board[to[0]]
                    else:
                        #print(Nonev, '3')
                        movevalid = False
                        toQValid = False
                        toPValid = False
                        toBValid = False
                        toKValid = False
                        toRValid = False
                        toHValid = False
                        toEValid = False
                        Valid = False
                        fail += 1
                    if movevalid == True:
                        if toQValid == True or toPValid == True or toBValid == True or toKValid == True or toRValid == True or toHValid == True or toEValid == True:
                            rowm[move[1]] = '--'
            else:
                #failfunc()
                fail += 1

        elif turn == 'White' and moven == True:
            if Valid == True or move == 'move':
                if not (1 <= move[0] <= boardx):
                    #print(Nonev)
                    fail += 1
                else:
                    rowm = game_board[move[0]]
                    if rowm[move[1]] in Whiteset:
                        brp = rowm[move[1]]
                        movevalid = True
                    else:
                        #print(Nonev,'1')
                        Valid = False
                        movevalid = False
                        fail += 1
            if Valid == True or to == 'to':
                if to[0] < 1 or to[0] > boardx:
                    #print(Nonev)
                    failfunc()
                    fail += 1
                else:
                    rowt = game_board[to[0]]
                    if rowt[to[1]] == '--' or nojumpcapture == True:
                        if rowm[move[1]] == 'WP' and to[0] == 1:
                            toEValid = True
                            rowt[to[1]] = 'WE'
                        elif rowm[move[1]] == 'WQ':
                            toQValid = True
                            rowt[to[1]] = 'WQ'
                        elif rowm[move[1]] == 'WH':
                            toHValid = True
                            rowt[to[1]] = 'WH'
                        elif rowm[move[1]] == 'WR':
                            toRValid = True
                            rowt[to[1]] = 'WR'
                        elif rowm[move[1]] == 'WB':
                            toHValid = True
                            rowt[to[1]] = 'WB'
                        elif rowm[move[1]] == 'WK':
                            toRValid = True
                            rowt[to[1]] = 'WK'
                        else:
                            toPValid = True
                            rowt[to[1]] = 'WP'
                            
                    elif rowt[to[1]] in Blackset:
                        if rowm[move[1]] == 'WP' and to[0] == 1:
                            toEValid = True
                            rowt[to[1]] = 'WE'
                        elif rowm[move[1]] == 'WQ':
                            toQValid = True
                            rowt[to[1]] = 'WQ'
                        elif rowm[move[1]] == 'WH':
                            rowt[to[1]] = 'WH'
                            toHValid = True
                        elif rowm[move[1]] == 'WR':
                            rowt[to[1]] = 'WR'
                            toRValid = True
                        elif rowm[move[1]] == 'WK':
                            rowt[to[1]] = 'WK'
                            toKValid = True
                        elif rowm[move[1]] == 'WB':
                            rowt[to[1]] = 'WB'
                            toBValid = True
                        elif rowm[move[1]] == 'WP':
                            rowt[to[1]] = 'WP'
                            toPValid = True
                        else:
                            #print(Nonev,'2')
                            stupiderror = True
                            fail += 1
                            movevalid = False
                            toQValid = False
                            toPValid = False
                            toBValid = False
                            toKValid = False
                            toRValid = False
                            toHValid = False
                            toEValid = False
                        rowt = game_board[to[0]]
                    else:
                        #print(Nonev, '3')
                        movevalid = False
                        toQValid = False
                        toPValid = False
                        toBValid = False
                        toKValid = False
                        toRValid = False
                        toHValid = False
                        toEValid = False
                        Valid = False
                        fail += 1
                    if movevalid == True:
                        if toQValid == True or toPValid == True or toBValid == True or toKValid == True or toRValid == True or toHValid == True or toEValid == True:
                            rowm[move[1]] = '--'
            else:
                #failfunc()
                fail += 1
        
        if toEValid == True:
            evolveer1 = True
    def queenmovement():
        global boardx, move, to, success, peice, game_board, turn
        for space in range(boardx):
            if (abs(move[1] - to[1]) == space and move[0] == to[0]):
                success = True
                break
            elif (abs(move[0] - to[0]) == space and move[1] == to[1]):
                success = True
                break
            elif abs(move[1] - to[1]) == space and abs(move[0] - to[0]) == space:
                success = True
                break
            else:
                success = False

        if move[0] < to[0] and move[1] < to[1]: #move(2,2) to(1,1) | move[0,1] - to[0,1] = [1,1] down right
            for peicess in range(1, abs(move[0]-to[0])):
                for peicesss in range(1, abs(to[1]-move[1])):
                    if not game_board[move[0]+peicess][move[1]+peicesss] == '--' and peicesss == peicess:
                        success = False

        elif move[0] < to[0] and move[1] > to[1]: #move(2,1) to(1,2) | move[0,1] - to[0,1] = [1,-1] down left
            for peicess in range(1, abs(move[0]-to[0])):
                for peicesss in range(1, abs(move[1]-to[1])):
                    if not game_board[move[0]+peicess][move[1]-peicesss] == '--' and peicesss == peicess:
                        success = False

        elif move[0] > to[0] and move[1] < to[1]: #move(1,2) to(2,1) | move[0,1] - to[0,1] = [-1,1] up right
            for peicess in range(1, abs(to[0]-move[0])):
                for peicesss in range(1, abs(to[1]-move[1])):
                    if not game_board[move[0]-peicess][move[1]+peicesss] == '--' and peicesss == peicess:
                        success = False

        elif move[0] > to[0] and move[1] > to[1]: #move(1,1) to(2,2) | move[0,1] - to[0,1] = [-1,-1] up left
            for peicess in range(1, abs(to[0]-move[0])):
                for peicesss in range(1, abs(move[1]-to[1])):
                    if not game_board[move[0]-peicess][move[1]-peicesss] == '--' and peicesss == peicess:
                        success = False

        elif move[0] < to[0] and move[1] == to[1]: #move(2,1) to(1,1) | move[0,1] - to[0,1] = [1,0] down
            for peicess in range(1, abs(to[0]-move[0])):
                if not game_board[move[0]+peicess][move[1]] == '--':
                    success = False

        elif move[0] > to[0] and move[1] == to[1]: #move(1,1) to(2,1) | move[0,1] - to[0,1] = [-1,0] up
            for peicess in range(1, abs(move[0]-to[0])):
                if not game_board[move[0]-peicess][move[1]] == '--':
                    success = False
                    
        elif move[0] == to[0] and move[1] < to[1]: #move(1,2) to(1,1) | move[0,1] - to[0,1] = [0,1] right
            for peicess in range(1, abs(to[1]-move[1])):
                if not game_board[move[0]][move[1]+peicess] == '--':
                    success = False

        elif move[0] == to[0] and move[1] > to[1]: #move(1,1) to(1,2) | move[0,1] - to[0,1] = [0,-1] left
            for peicess in range(1, abs(move[1]-to[1])):
                if not game_board[move[0]][move[1]-peicess] == '--':
                    success = False
    def rookmovement():
        global boardx, move, to, success, peice, game_board, turn
        for space in range(boardx):
            if (abs(move[1] - to[1]) == space and move[0] == to[0]) or (abs(move[0] - to[0]) == space and move[1] == to[1]):
                success = True
                break
            else:
                success = False

        if move[0] < to[0] and move[1] == to[1]: #move(2,1) to(1,1) | move[0,1] - to[0,1] = [1,0] down
            for peicess in range(1, abs(to[0]-move[0])):
                if not game_board[move[0]+peicess][move[1]] == '--':
                    success = False

        elif move[0] > to[0] and move[1] == to[1]: #move(1,1) to(2,1) | move[0,1] - to[0,1] = [-1,0] up
            for peicess in range(1, abs(move[0]-to[0])):
                if not game_board[move[0]-peicess][move[1]] == '--':
                    success = False
                    
        elif move[0] == to[0] and move[1] < to[1]: #move(1,2) to(1,1) | move[0,1] - to[0,1] = [0,1] right
            for peicess in range(1, abs(to[1]-move[1])):
                if not game_board[move[0]][move[1]+peicess] == '--':
                    success = False

        elif move[0] == to[0] and move[1] > to[1]: #move(1,1) to(1,2) | move[0,1] - to[0,1] = [0,-1] left
            for peicess in range(1, abs(move[1]-to[1])):
                if not game_board[move[0]][move[1]-peicess] == '--':
                    success = False
    def bishopmovement():
        global boardx, move, to, success, peice, game_board, turn
        for space in range(boardx):
            if abs(move[1] - to[1]) == space and abs(move[0] - to[0]) == space:
                success = True
                break
            else:
                success = False

        if move[0] < to[0] and move[1] < to[1]: #move(2,2) to(1,1) | move[0,1] - to[0,1] = [1,1] down right
            for peicess in range(1, abs(move[0]-to[0])):
                for peicesss in range(1, abs(to[1]-move[1])):
                    if not game_board[move[0]+peicess][move[1]+peicesss] == '--' and peicesss == peicess:
                        success = False

        elif move[0] < to[0] and move[1] > to[1]: #move(2,1) to(1,2) | move[0,1] - to[0,1] = [1,-1] down left
            for peicess in range(1, abs(move[0]-to[0])):
                for peicesss in range(1, abs(move[1]-to[1])):
                    if not game_board[move[0]+peicess][move[1]-peicesss] == '--' and peicesss == peicess:
                        success = False

        elif move[0] > to[0] and move[1] < to[1]: #move(1,2) to(2,1) | move[0,1] - to[0,1] = [-1,1] up right
            for peicess in range(1, abs(to[0]-move[0])):
                for peicesss in range(1, abs(to[1]-move[1])):
                    if not game_board[move[0]-peicess][move[1]+peicesss] == '--' and peicesss == peicess:
                        success = False

        elif move[0] > to[0] and move[1] > to[1]: #move(1,1) to(2,2) | move[0,1] - to[0,1] = [-1,-1] up left
            for peicess in range(1, abs(to[0]-move[0])):
                for peicesss in range(1, abs(move[1]-to[1])):
                    if not game_board[move[0]-peicess][move[1]-peicesss] == '--' and peicesss == peicess:
                        success = False
    def pawnmovement():
        global boardx, move, to, success, peice, game_board, turn, enpasantb, enpasantw
        if peice == "BP":
            if to[0] - move[0] == 1 or to[0] - move[0] == 2 and move[0] == 2 and game_board[to[0]-1][to[1]] == "--":
                if to[0] - move[0] == 2 and move[0] == 2:
                    enpasantb.append(to[1])
                else:
                    count = -1
                    for pasant in enpasantb:
                        count +=1
                        if pasant == to[1]:
                            enpasantb.pop(count)
                    count = -1
                if to[1] == move[1] and not peicet in Whiteset or to[1] in (move[1]+1, move[1]-1) and peicet in Whiteset:
                    success = True
                else:
                    success = False
                if to[1] in (move[1]+1, move[1]-1) and game_board[to[0]-1][to[1]] == "WP" and to[0] == 6 and to[1] in enpasantw:
                    success = True
                    game_board[to[0]-1][to[1]] = "--"
                    count = -1
                    for pasant in enpasantw:
                        count +=1
                        if pasant == to[1]:
                            enpasantw.pop(count)
                    count = -1
            else:
                success = False
        elif peice == "WP":
            if move[0] - to[0] == 1 or move[0] - to[0] == 2 and move[0] == 7 and game_board[to[0]+1][to[1]] == "--":
                if move[0] - to[0] == 2 and move[0] == 7:
                    enpasantw.append(to[1])
                else:
                    count = -1
                    for pasant in enpasantw:
                        count +=1
                        if pasant == to[1]:
                            enpasantw.pop(count)
                    count = -1
                if to[1] == move[1] and not peicet in Blackset or to[1] in (move[1]+1, move[1]-1) and peicet in Blackset:
                    success = True
                else:
                    success = False
                if to[1] in (move[1]+1, move[1]-1) and game_board[to[0]+1][to[1]] == "BP" and to[0] == 3 and to[1] in enpasantb:
                    success = True
                    game_board[to[0]+1][to[1]] = "--"
                    count = -1
                    for pasant in enpasantb:
                        count +=1
                        if pasant == to[1]:
                            enpasantb.pop(count)
                    count = -1
            else:
                success = False
        else:
            success = False
    def check_check():
        global boardx, game_board, BKcheck, WKcheck, BKcheck, WKcheck, Blackset, Whiteset, Stalemate, BCheck, WCheck, Checkmate, Wok, Bok
        direction = 0
        knight_moves = [(2,1), (2,-1), (-2,1), (-2,-1), (1,2), (1,-2), (-1,2), (-1,-2)]
        for rowK in range(boardx+1):
            for colK in range(boardx+1):
                if game_board[rowK][colK] == "BK":
                    BKpos = [rowK, colK]
                    direction = 0
                    for vertical in range(-1,2):
                        for horizontal in range(-1,2):
                            DKpos = [BKpos[0]+vertical, BKpos[1]+horizontal]
                            if DKpos[0] > boardx or DKpos[1] > boardx or DKpos[0] < 1 or DKpos[1] < 1:
                                BKcheck[direction] = False
                            else:
                                if game_board[DKpos[0]][DKpos[1]] in ("BP", "BR", "BH", "BB", "BQ", "BK", "BE", "WP", "WR", "WH", "WB", "WQ", "WK", "WE", "--"):
                                    if game_board[DKpos[0]][DKpos[1]] in Blackset:
                                        BKcheck[direction] = False
                                        Bok[direction] = True
                                    else:
                                        BKcheck[direction] = True
                                else:
                                    BKcheck[direction] = False
                                for space in range(boardx + 1):
                                    if DKpos[0] + space == boardx:
                                        for spaces in range(1,space+1):
                                            if game_board[DKpos[0] + spaces][DKpos[1]] in ("WQ", "WR"):
                                                BKcheck[direction] = False
                                            elif game_board[DKpos[0] + spaces][DKpos[1]] not in ("WQ", "WR", "--", "BK"):
                                                break
                                        for blanks in range(boardx + 1):
                                            if DKpos[1] + blanks == boardx:
                                                for blank in range(1,blanks+1):
                                                    try:
                                                        if game_board[DKpos[0] + blank][DKpos[1] + blank] in ("WQ", "WB"):
                                                            BKcheck[direction] = False
                                                        elif game_board[DKpos[0] + blank][DKpos[1] + blank] not in ("WQ", "WR", "--", "BK"):
                                                            break
                                                    except:
                                                        continue
                                            if DKpos[1] - blanks == 0:
                                                for blank in range(1,blanks+1):
                                                    try:
                                                        if game_board[DKpos[0] + blank][DKpos[1] - blank] in ("WQ", "WB"):
                                                            BKcheck[direction] = False
                                                        elif game_board[DKpos[0] + blank][DKpos[1] - blank] not in ("WQ", "WR", "--", "BK"):
                                                            break
                                                    except:
                                                        continue
                                    if DKpos[0] - space == 0:
                                        for spaces in range(1,space+1):
                                            if game_board[DKpos[0] - spaces][DKpos[1]] in ("WQ", "WR"):
                                                BKcheck[direction] = False
                                            elif game_board[DKpos[0] - spaces][DKpos[1]] not in ("WQ", "WR", "--", "BK"):
                                                break
                                        for blanks in range(boardx + 1):
                                            if DKpos[1] + blanks == boardx:
                                                for blank in range(1,blanks+1):
                                                    try:
                                                        if game_board[DKpos[0] - blank][DKpos[1] + blank] in ("WQ", "WB"):
                                                            BKcheck[direction] = False
                                                        elif game_board[DKpos[0] - blank][DKpos[1] + blank] not in ("WQ", "WR", "--", "BK"):
                                                            break
                                                    except:
                                                        continue
                                            if DKpos[1] - blanks == 0:
                                                for blank in range(1,blanks+1):
                                                    try:
                                                        if game_board[DKpos[0] - blank][DKpos[1] - blank] in ("WQ", "WB"):
                                                            BKcheck[direction] = False
                                                        elif game_board[DKpos[0] - blank][DKpos[1] - blank] not in ("WQ", "WR", "--", "BK"):
                                                            break
                                                    except:
                                                        continue

                                    if DKpos[1] + space == boardx:
                                        for spaces in range(1,space+1):
                                            if game_board[DKpos[0]][DKpos[1] + spaces] in ("WQ", "WR"):
                                                BKcheck[direction] = False
                                            elif game_board[DKpos[0]][DKpos[1] + spaces] not in ("WQ", "WR", "--", "BK"):
                                                break
                                    if DKpos[1] - space == 0:
                                        for spaces in range(1,space+1):
                                            if game_board[DKpos[0]][DKpos[1] - spaces] in ("WQ", "WR"):
                                                BKcheck[direction] = False
                                            elif game_board[DKpos[0]][DKpos[1] - spaces] not in ("WQ", "WR", "--", "BK"):
                                                break

                            if any(0 <= DKpos[0]+x < boardx and 0 <= DKpos[1]+y < boardx and game_board[DKpos[0]+x][DKpos[1]+y] == "WH" for x, y in knight_moves):
                                BKcheck[direction] = False
                            direction +=1
                    for space in range(boardx + 1):
                        if BKpos[0] + space == boardx:
                            for spaces in range(1,space+1):
                                if game_board[BKpos[0] + spaces][BKpos[1]] in ("WQ", "WR"):
                                    BCheck = True
                                elif game_board[BKpos[0] + spaces][BKpos[1]] not in ("WQ", "WR", "--", "BK"):
                                    break
                            for blanks in range(boardx + 1):
                                if BKpos[1] + blanks == boardx:
                                    for blank in range(1,blanks+1):
                                        try:
                                            if game_board[BKpos[0] + blank][BKpos[1] + blank] in ("WQ", "WB"):
                                                BCheck = True
                                            elif game_board[BKpos[0] + blank][BKpos[1] + blank] not in ("WQ", "WR", "--", "BK"):
                                                break
                                        except:
                                            continue
                                if BKpos[1] - blanks == 0:
                                    for blank in range(1,blanks+1):
                                        try:
                                            if game_board[BKpos[0] + blank][BKpos[1] - blank] in ("WQ", "WB"):
                                                BCheck = True
                                            elif game_board[BKpos[0] + blank][BKpos[1] - blank] not in ("WQ", "WR", "--", "BK"):
                                                break
                                        except:
                                            continue
                        if BKpos[0] - space == 0:
                            for spaces in range(1,space+1):
                                if game_board[BKpos[0] - spaces][BKpos[1]] in ("WQ", "WR"):
                                    BCheck = True
                                elif game_board[BKpos[0] - spaces][BKpos[1]] not in ("WQ", "WR", "--", "BK"):
                                    break
                            for blanks in range(boardx + 1):
                                if BKpos[1] + blanks == boardx:
                                    for blank in range(1,blanks+1):
                                        try:
                                            if game_board[BKpos[0] - blank][BKpos[1] + blank] in ("WQ", "WB"):
                                                BCheck = True
                                            elif game_board[BKpos[0] - blank][BKpos[1] + blank] not in ("WQ", "WR", "--", "BK"):
                                                break
                                        except:
                                            continue
                                if BKpos[1] - blanks == 0:
                                    for blank in range(1,blanks+1):
                                        try:
                                            if game_board[BKpos[0] - blank][BKpos[1] - blank] in ("WQ", "WB"):
                                                BCheck = True
                                            elif game_board[BKpos[0] - blank][BKpos[1] - blank] not in ("WQ", "WR", "--", "BK"):
                                                break
                                        except:
                                            continue

                        if BKpos[1] + space == boardx:
                            for spaces in range(1,space+1):
                                if game_board[BKpos[0]][BKpos[1] + spaces] in ("WQ", "WR"):
                                    BCheck = True
                                elif game_board[BKpos[0]][BKpos[1] + spaces] not in ("WQ", "WR", "--", "BK"):
                                    break
                        if BKpos[1] - space == 0:
                            for spaces in range(1,space+1):
                                if game_board[BKpos[0]][BKpos[1] - spaces] in ("WQ", "WR"):
                                    BCheck = True
                                elif game_board[BKpos[0]][BKpos[1] - spaces] not in ("WQ", "WR", "--", "BK"):
                                    break
                    
                    if any(0 <= BKpos[0]+x < boardx and 0 <= BKpos[1]+y < boardx and game_board[BKpos[0]+x][BKpos[1]+y] == "WH" for x, y in knight_moves):
                        BCheck = True
                elif game_board[rowK][colK] == "WK":
                    WKpos = [rowK, colK]
                    direction = 0
                    for vertical in range(-1,2):
                        for horizontal in range(-1,2):
                            DKpos = [WKpos[0]+vertical, WKpos[1]+horizontal]
                            if DKpos[0] > boardx or DKpos[1] > boardx or DKpos[0] < 1 or DKpos[1] < 1:
                                WKcheck[direction] = False
                            else:
                                if game_board[DKpos[0]][DKpos[1]] in ("BP", "BR", "BH", "BB", "BQ", "BK", "BE", "WP", "WR", "WH", "WB", "WQ", "WK", "WE", "--"):
                                    if game_board[DKpos[0]][DKpos[1]] in Whiteset:
                                        WKcheck[direction] = False
                                        Wok[direction] = True
                                    else:
                                        WKcheck[direction] = True
                                else:
                                    WKcheck[direction] = False

                                for space in range(boardx + 1):
                                    if DKpos[0] + space == boardx:
                                        for spaces in range(1,space+1):
                                            if game_board[DKpos[0] + spaces][DKpos[1]] in ("BQ", "BR"):
                                                WKcheck[direction] = False
                                            elif game_board[DKpos[0] + spaces][DKpos[1]] not in ("BQ", "BR", "--", "WK"):
                                                break
                                        for blanks in range(boardx + 1):
                                            if DKpos[1] + blanks == boardx:
                                                for blank in range(1,blanks+1):
                                                    try:
                                                        if game_board[DKpos[0] + blank][DKpos[1] + blank] in ("BQ", "BB"):
                                                            WKcheck[direction] = False
                                                        elif game_board[DKpos[0] + blank][DKpos[1] + blank] not in ("BQ", "BR", "--", "WK"):
                                                            break
                                                    except:
                                                        continue
                                            if DKpos[1] - blanks == 0:
                                                for blank in range(1,blanks+1):
                                                    try:
                                                        if game_board[DKpos[0] + blank][DKpos[1] - blank] in ("BQ", "BB"):
                                                            WKcheck[direction] = False
                                                        elif game_board[DKpos[0] + blank][DKpos[1] - blank] not in ("BQ", "BR", "--", "WK"):
                                                            break
                                                    except:
                                                        continue
                                    if DKpos[0] - space == 0:
                                        for spaces in range(1,space+1):
                                            if game_board[DKpos[0] - spaces][DKpos[1]] in ("BQ", "BR"):
                                                WKcheck[direction] = False
                                            elif game_board[DKpos[0] - spaces][DKpos[1]]not in ("BQ", "BR", "--", "WK"):
                                                break
                                        for blanks in range(boardx + 1):
                                            if DKpos[1] + blanks == boardx:
                                                for blank in range(1,blanks+1):
                                                    try:
                                                        if game_board[DKpos[0] - blank][DKpos[1] + blank] in ("BQ", "BB"):
                                                            WKcheck[direction] = False
                                                        elif game_board[DKpos[0] - blank][DKpos[1] + blank] not in ("BQ", "BR", "--", "WK"):
                                                            break
                                                    except:
                                                        continue
                                            if DKpos[1] - blanks == 0:
                                                for blank in range(1,blanks+1):
                                                    try:
                                                        if game_board[DKpos[0] - blank][DKpos[1] - blank] in ("BQ", "BB"):
                                                            WKcheck[direction] = False
                                                        elif game_board[DKpos[0] - blank][DKpos[1] - blank] not in ("BQ", "BR", "--", "WK"):
                                                            break
                                                    except:
                                                        continue

                                    if DKpos[1] + space == boardx:
                                        for spaces in range(1,space+1):
                                            if game_board[DKpos[0]][DKpos[1] + spaces] in ("BQ", "BR"):
                                                WKcheck[direction] = False
                                            elif game_board[DKpos[0]][DKpos[1] + spaces] not in ("BQ", "BR", "--", "WK"):
                                                break
                                    if DKpos[1] - space == 0:
                                        for spaces in range(1,space+1):
                                            if game_board[DKpos[0]][DKpos[1] - spaces] in ("BQ", "BR"):
                                                WKcheck[direction] = False
                                            elif game_board[DKpos[0]][DKpos[1] - spaces] not in ("BQ", "BR", "--", "WK"):
                                                break
                            if any(0 <= DKpos[0]+x < boardx and 0 <= DKpos[1]+y < boardx and game_board[DKpos[0]+x][DKpos[1]+y] == "BH" for x, y in knight_moves):
                                WKcheck[direction] = False
                            direction += 1
                    for space in range(boardx + 1):
                        if WKpos[0] + space == boardx:
                            for spaces in range(1,space+1):
                                if game_board[WKpos[0] + spaces][WKpos[1]] in ("BQ", "BR"):
                                    WCheck = True
                                elif game_board[WKpos[0] + spaces][WKpos[1]]not in ("BQ", "BR", "--", "WK"):
                                    break
                            for blanks in range(boardx + 1):
                                if WKpos[1] + blanks == boardx:
                                    for blank in range(1,blanks+1):
                                        try:
                                            if game_board[WKpos[0] + blank][WKpos[1] + blank] in ("BQ", "BB"):
                                                WCheck = True
                                            elif game_board[WKpos[0] + blank][WKpos[1] + blank] not in ("BQ", "BR", "--", "WK"):
                                                break
                                        except:
                                            continue
                                if WKpos[1] - blanks == 0:
                                    for blank in range(1,blanks+1):
                                        try:
                                            if game_board[WKpos[0] + blank][WKpos[1] - blank] in ("BQ", "BB"):
                                                WCheck = True
                                            elif game_board[WKpos[0] + blank][WKpos[1] - blank] not in ("BQ", "BR", "--", "WK"):
                                                break
                                        except:
                                            continue
                        if WKpos[0] - space == 0:
                            for spaces in range(1,space+1):
                                if game_board[WKpos[0] - spaces][WKpos[1]] in ("BQ", "BR"):
                                    WCheck = True
                                elif game_board[WKpos[0] - spaces][WKpos[1]]not in ("BQ", "BR", "--", "WK"):
                                    break
                            for blanks in range(boardx + 1):
                                if WKpos[1] + blanks == boardx:
                                    for blank in range(1,blanks+1):
                                        try:
                                            if game_board[WKpos[0] - blank][WKpos[1] + blank] in ("BQ", "BB"):
                                                WCheck = True
                                            elif game_board[WKpos[0] - blank][WKpos[1] + blank] not in ("BQ", "BR", "--", "WK"):
                                                break
                                        except:
                                            continue
                                if WKpos[1] - blanks == 0:
                                    for blank in range(1,blanks+1):
                                        try:
                                            if game_board[WKpos[0] - blank][WKpos[1] - blank] in ("BQ", "BB"):
                                                WCheck = True
                                            elif game_board[WKpos[0] - blank][WKpos[1] - blank] not in ("BQ", "BR", "--", "WK"):
                                                break
                                        except:
                                            continue

                        if WKpos[1] + space == boardx:
                            for spaces in range(1,space+1):
                                if game_board[WKpos[0]][WKpos[1] + spaces] in ("BQ", "BR"):
                                    WCheck = True
                                elif game_board[WKpos[0]][WKpos[1] + spaces] not in ("BQ", "BR", "--", "WK"):
                                    break
                        if WKpos[1] - space == 0:
                            for spaces in range(1,space+1):
                                if game_board[WKpos[0]][WKpos[1] - spaces] in ("BQ", "BR"):
                                    WCheck = True
                                elif game_board[WKpos[0]][WKpos[1] - spaces] not in ("BQ", "BR", "--", "WK"):
                                    break
                    if any(0 <= WKpos[0]+x < boardx and 0 <= WKpos[1]+y < boardx and game_board[WKpos[0]+x][WKpos[1]+y] == "BH" for x, y in knight_moves):
                        WCheck = True
                    direction = 0
        
        falsecount = 0
        for checks in range(0,len(BKcheck)):
            if checks == 4:
                continue
            if BKcheck[checks] == False:
                    falsecount += 1
        if falsecount == 8:
            Stalemate = True
        falsecount = 0

        for checks in range(0,len(WKcheck)):
            if checks == 4:
                continue
            if WKcheck[checks] == False:
                falsecount += 1
        if falsecount == 8:
            for boolsB in Bok:
                if boolsB == True:
                    Stalemate = False
                    break
                else:
                    Stalemate = True
            for boolsW in Wok:
                if boolsW == True:
                    Stalemate = False
                    break
                else:
                    Stalemate = True
        if Stalemate and BCheck or Stalemate and WCheck:
            Checkmate = True
        
    def check_king():
        for rowK in range(boardx+1):
            for colK in range(boardx+1):
                if game_board[rowK][colK] == "BK":
                    BKpos = [rowK, colK]
                if game_board[rowK][colK] == "WK":
                    WKpos = [rowK, colK]
        return BKpos, WKpos
guifuctions = True
if guifuctions:
    def clear_board():
        for widget in root.winfo_children():
            if isinstance(widget, Button) or isinstance(widget, Entry):
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
        global checkerp, boardx, Blackset, Whiteset, BCheck, WCheck
        checkerp = True
        lbl4.configure(text = f"Turn: {turn}")
        lbl6.configure(text = f"Fail: {failr}")
        if WCheck and BCheck:
            lbl7.configure(text = f"Dual Check")
        elif WCheck:
            lbl7.configure(text = f"W in Check")
        elif BCheck:
            lbl7.configure(text = f"B in Check")
        else:
            lbl7.configure(text = f"Mateless")
        for r in range(boardx):
            for c in range(boardx+1):
                if c == boardx:
                    if checkerp == False:
                        checkerp = True
                    else:
                        checkerp = False
                rowm2 = [r+1,c+1]
                rowm = game_board[rowm2[0]]
                if rowm[rowm2[1]] in ('--'):
                    if checkerp == True:
                        Button(
                            root, width=widths,
                            background=emptycolor2,
                            activebackground=emptytextcolor2
                        ).grid(row=r+1, column=c+1)
                        checkerp = False
                    elif checkerp == False:
                        Button(
                            root, width=widths,
                            background=emptycolor1,
                            activebackground=emptytextcolor1
                        ).grid(row=r+1, column=c+1)
                        checkerp = True
                elif rowm[rowm2[1]] in Blackset:
                    if rowm[rowm2[1]] == 'BQ':
                        Button(
                            root,
                            text="BQ", width=widths,
                            command=lambda posy=r, posx=c: clicked(posy+1, posx+1),
                            background= BQcolor,
                            foreground= BQtextcolor,
                            activebackground= BQtextcolor,
                            activeforeground= BQcolor
                        ).grid(row=r+1, column=c+1)
                    elif rowm[rowm2[1]] == 'BP':
                        Button(
                            root,
                            text="BP", width=widths,
                            command=lambda posy=r, posx=c: clicked(posy+1, posx+1),
                            background=BPcolor,
                            foreground= BPtextcolor,
                            activebackground=BPtextcolor,
                            activeforeground=BPcolor
                        ).grid(row=r+1, column=c+1)
                    elif rowm[rowm2[1]] == 'BR':
                        Button(
                            root,
                            text="BR", width=widths,
                            command=lambda posy=r, posx=c: clicked(posy+1, posx+1),
                            background=BRcolor,
                            foreground= BRtextcolor,
                            activebackground=BRtextcolor,
                            activeforeground=BRcolor
                        ).grid(row=r+1, column=c+1)
                    elif rowm[rowm2[1]] == 'BH':
                        Button(
                            root,
                            text="BH", width=widths,
                            command=lambda posy=r, posx=c: clicked(posy+1, posx+1),
                            background=BHcolor,
                            foreground= BHtextcolor,
                            activebackground=BHtextcolor,
                            activeforeground=BHcolor
                        ).grid(row=r+1, column=c+1)
                    elif rowm[rowm2[1]] == 'BK':
                        Button(
                            root,
                            text="BK", width=widths,
                            command=lambda posy=r, posx=c: clicked(posy+1, posx+1),
                            background=BKcolor,
                            foreground= BKtextcolor,
                            activebackground=BKtextcolor,
                            activeforeground=BKcolor
                        ).grid(row=r+1, column=c+1)
                    elif rowm[rowm2[1]] == 'BB':
                        Button(
                            root,
                            text="BB", width=widths,
                            command=lambda posy=r, posx=c: clicked(posy+1, posx+1),
                            background=BBcolor,
                            foreground= BBtextcolor,
                            activebackground=BBtextcolor,
                            activeforeground=BBcolor
                        ).grid(row=r+1, column=c+1)
                    if checkerp == False:
                        checkerp = True
                    else:
                        checkerp = False
                elif rowm[rowm2[1]] in Whiteset:
                    if rowm[rowm2[1]] == 'WQ':
                        Button(
                            root,
                            text="WQ", width=widths,
                            command=lambda posy=r, posx=c: clicked(posy+1, posx+1),
                            background=WQcolor,
                            foreground=WQtextcolor,
                            activebackground=WQtextcolor,
                            activeforeground=WQcolor
                        ).grid(row=r+1, column=c+1)
                    elif rowm[rowm2[1]] == 'WP':
                        Button(
                            root,
                            text="WP", width=widths,
                            command=lambda posy=r, posx=c: clicked(posy+1, posx+1),
                            background=WPcolor,
                            foreground=WPtextcolor,
                            activebackground=WPtextcolor,
                            activeforeground=WPcolor
                        ).grid(row=r+1, column=c+1)
                    elif rowm[rowm2[1]] == 'WR':
                        Button(
                            root,
                            text="WR", width=widths,
                            command=lambda posy=r, posx=c: clicked(posy+1, posx+1),
                            background=WRcolor,
                            foreground= WRtextcolor,
                            activebackground=WRtextcolor,
                            activeforeground=WRcolor
                        ).grid(row=r+1, column=c+1)
                    elif rowm[rowm2[1]] == 'WH':
                        Button(
                            root,
                            text="WH", width=widths,
                            command=lambda posy=r, posx=c: clicked(posy+1, posx+1),
                            background=WHcolor,
                            foreground= WHtextcolor,
                            activebackground=WHtextcolor,
                            activeforeground=WHcolor
                        ).grid(row=r+1, column=c+1)
                    elif rowm[rowm2[1]] == 'WK':
                        Button(
                            root,
                            text="WK", width=widths,
                            command=lambda posy=r, posx=c: clicked(posy+1, posx+1),
                            background=WKcolor,
                            foreground= WKtextcolor,
                            activebackground=WKtextcolor,
                            activeforeground=WKcolor
                        ).grid(row=r+1, column=c+1)
                    elif rowm[rowm2[1]] == 'WB':
                        Button(
                            root,
                            text="WB", width=widths,
                            command=lambda posy=r, posx=c: clicked(posy+1, posx+1),
                            background=WBcolor,
                            foreground= WBtextcolor,
                            activebackground=WBtextcolor,
                            activeforeground=WBcolor
                        ).grid(row=r+1, column=c+1)
                    if checkerp == False:
                        checkerp = True
                    else:
                        checkerp = False
        
        if debugon:
            global entry1, entry2, entry3, entry4, entry5, entry6, entry7, entry8, entry9, entry10, entry11, entry12, entry13, entry14, entry15
            Button( #skip turn
            root, text='Skip Turn', width=9,
            background=buttonscolor,
            foreground=Buttontextcolor,
            activebackground=Buttontextcolor,
            activeforeground=buttonscolor,
            command=lambda: skiper()
            ).place(x=int((boardx*33+33)/3), y=(boardx*32))
            Button( #end game
                root, text="End game", width=9,
                background=buttonscolor,
                foreground=Buttontextcolor,
                activebackground=Buttontextcolor,
                activeforeground=buttonscolor,
                command=lambda: ender() 
            ).place(x=int((boardx*33+33)/1.5), y=(boardx*32))
            Button( #Roll color
                root, text="Roll color", width=9,
                background=buttonscolor,
                foreground=Buttontextcolor,
                activebackground=Buttontextcolor,
                activeforeground=buttonscolor,
                command=lambda: rollcolor2()
            ).place(x=int((boardx*33+33)/(boardx+4)), y=(boardx*32))
            Button( #debugempty1-1
                root, width=10, height=5, name= "debugempty1-1",
                background=emptycolor1,
                activebackground=emptytextcolor1
                ).grid(padx=(50,0), row=int(boardx*3.75), column=int(boardx*3.75))
            Button( #debugempty1-2
                root, width=10, height=5, name= "debugempty1-2",
                background=emptytextcolor1,
                activebackground=emptycolor1
                ).grid(padx=(50,0), row=int(boardx*3.75)+1, column=int(boardx*3.75))
            Button( #debugempty2-1
                root, width=10, height=5, name= "debugempty2-1",
                background=emptycolor2,
                activebackground=emptytextcolor2
                ).grid(row=int(boardx*3.75), column=int(boardx*3.75)+1)
            Button( #debugempty2-2
                root, width=10, height=5, name= "debugempty2-2",
                background=emptytextcolor2,
                activebackground=emptycolor2
                ).grid(row=int(boardx*3.75)+1, column=int(boardx*3.75)+1)
            Button( #debugbuttoncolor1
                root, width=10, height=5,  name= "debugbuttoncolor1",
                background=buttonscolor,
                activebackground=Buttontextcolor
                ).grid(row=int(boardx*3.75), column=int(boardx*3.75)+2)
            Button( #debugbuttoncolor2
                root, width=10, height=5,  name= "debugbuttoncolor2",
                background=Buttontextcolor,
                activebackground=buttonscolor
                ).grid(row=int(boardx*3.75)+1, column=int(boardx*3.75)+2)
            
            buttonbase = 1
            Button( #debugWP1
                root, width=10, height=5, name= "debugWP1", text="WP-Base",
                background=WPcolor,
                activebackground=WPtextcolor
                ).grid(row=int(boardx*3.75)+3, column=int(boardx*3.75)+buttonbase)
            Button( #debugWP2
                root, width=10, height=5, name= "debugWP2",text="WP-Active",
                background=WPtextcolor,
                activebackground=WPcolor
                ).grid(row=int(boardx*3.75)+4, column=int(boardx*3.75)+buttonbase)
            Button( #debugWR1
                root, width=10, height=5, name= "debugWR1", text="WR-Base",
                background=WRcolor,
                activebackground=WRtextcolor
                ).grid(row=int(boardx*3.75)+3, column=int(boardx*3.75)+buttonbase+1)
            Button( #debugWR2
                root, width=10, height=5, name= "debugWR2",text="WR-Active",
                background=WRtextcolor,
                activebackground=WRcolor
                ).grid(row=int(boardx*3.75)+4, column=int(boardx*3.75)+buttonbase+1)
            Button( #debugWH1
                root, width=10, height=5,  name= "debugWH1",text="WH-Base",
                background=WHcolor,
                activebackground=WHtextcolor
                ).grid(row=int(boardx*3.75)+3, column=int(boardx*3.75)+buttonbase+2)
            Button( #debugWH2
                root, width=10, height=5,  name= "debugWH2",text="WH-Active",
                background=WHtextcolor,
                activebackground=WHcolor
                ).grid(row=int(boardx*3.75)+4, column=int(boardx*3.75)+buttonbase+2)
            Button( #debugWB1
                root, width=10, height=5,  name= "debugWB1",text="WB-Base",
                background=WBcolor,
                activebackground=WBtextcolor
                ).grid(row=int(boardx*3.75)+3, column=int(boardx*3.75)+buttonbase+3)
            Button( #debugWB2
                root, width=10, height=5,  name= "debugWB2",text="WB-Active",
                background=WBtextcolor,
                activebackground=WBcolor
                ).grid(row=int(boardx*3.75)+4, column=int(boardx*3.75)+buttonbase+3)
            Button( #debugWQ1
                root, width=10, height=5,  name= "debugWQ1",text="WQ-Base",
                background=WQcolor,
                activebackground=WQtextcolor
                ).grid(row=int(boardx*3.75)+3, column=int(boardx*3.75)+buttonbase+4)
            Button( #debugWQ2
                root, width=10, height=5,  name= "debugWQ2",text="WQ-Active",
                background=WQtextcolor,
                activebackground=WQcolor
                ).grid(row=int(boardx*3.75)+4, column=int(boardx*3.75)+buttonbase+4)
            Button( #debugWK1
                root, width=10, height=5,  name= "debugWK1",text="WK-Base",
                background=WKcolor,
                activebackground=WKtextcolor
                ).grid(row=int(boardx*3.75)+3, column=int(boardx*3.75)+buttonbase+5)
            Button( #debugWK2
                root, width=10, height=5,  name= "debugWK2",text="WK-Active",
                background=WKtextcolor,
                activebackground=WKcolor
                ).grid(row=int(boardx*3.75)+4, column=int(boardx*3.75)+buttonbase+5)
            
            Button( #debugBP1
                root, width=10, height=5, name= "debugBP1", text="BP-Base",
                background=BPcolor,
                activebackground=BPtextcolor
                ).grid(row=int(boardx*3.75)+6, column=int(boardx*3.75)+buttonbase)
            Button( #debugBP2
                root, width=10, height=5, name= "debugBP2",text="BP-Active",
                background=BPtextcolor,
                activebackground=BPcolor
                ).grid(row=int(boardx*3.75)+7, column=int(boardx*3.75)+buttonbase)
            Button( #debugBR1
                root, width=10, height=5, name= "debugBR1", text="BR-Base",
                background=BRcolor,
                activebackground=BRtextcolor
                ).grid(row=int(boardx*3.75)+6, column=int(boardx*3.75)+buttonbase+1)
            Button( #debugBR2
                root, width=10, height=5, name= "debugBR2",text="BR-Active",
                background=BRtextcolor,
                activebackground=BRcolor
                ).grid(row=int(boardx*3.75)+7, column=int(boardx*3.75)+buttonbase+1)
            Button( #debugBH1
                root, width=10, height=5,  name= "debugBH1",text="BH-Base",
                background=BHcolor,
                activebackground=BHtextcolor
                ).grid(row=int(boardx*3.75)+6, column=int(boardx*3.75)+buttonbase+2)
            Button( #debugBH2
                root, width=10, height=5,  name= "debugBH2",text="BH-Active",
                background=BHtextcolor,
                activebackground=BHcolor
                ).grid(row=int(boardx*3.75)+7, column=int(boardx*3.75)+buttonbase+2)
            Button( #debugBB1
                root, width=10, height=5,  name= "debugBB1",text="BB-Base",
                background=BBcolor,
                activebackground=BBtextcolor
                ).grid(row=int(boardx*3.75)+6, column=int(boardx*3.75)+buttonbase+3)
            Button( #debugBB2
                root, width=10, height=5,  name= "debugBB2",text="BB-Active",
                background=BBtextcolor,
                activebackground=BBcolor
                ).grid(row=int(boardx*3.75)+7, column=int(boardx*3.75)+buttonbase+3)
            Button( #debugBQ1
                root, width=10, height=5,  name= "debugBQ1",text="BQ-Base",
                background=BQcolor,
                activebackground=BQtextcolor
                ).grid(row=int(boardx*3.75)+6, column=int(boardx*3.75)+buttonbase+4)
            Button( #debugBQ2
                root, width=10, height=5,  name= "debugBQ2",text="BQ-Active",
                background=BQtextcolor,
                activebackground=BQcolor
                ).grid(row=int(boardx*3.75)+7, column=int(boardx*3.75)+buttonbase+4)
            Button( #debugBK1
                root, width=10, height=5,  name= "debugBK1",text="BK-Base",
                background=BKcolor,
                activebackground=BKtextcolor
                ).grid(row=int(boardx*3.75)+6, column=int(boardx*3.75)+buttonbase+5)
            Button( #debugBK2
                root, width=10, height=5,  name= "debugBK2",text="BK-Active",
                background=BKtextcolor,
                activebackground=BKcolor
                ).grid(row=int(boardx*3.75)+7, column=int(boardx*3.75)+buttonbase+5)
            
            entries = True
            if entries == True:
                entry1 = Entry(
                    root, width=12, name= "debugempty1-3",
                    background= "#FFFFFF"
                    )
                entry1.grid(padx=(50,0), row=int(boardx*3.75)+2, column=int(boardx*3.75))
                entry1.bind("<Return>", colorsetter1)
                entry1.insert(0, emptycolor1)
                #
                entry2 = Entry(
                    root, width=12, name= "debugempty2-3",
                    background="#FFFFFF"
                    )
                entry2.grid(row=int(boardx*3.75)+2, column=int(boardx*3.75)+1)
                entry2.bind("<Return>", colorsetter1)
                entry2.insert(0, emptycolor2)
                #
                entry3 = Entry(
                    root, width=12, name= "debugbuttoncolor3",
                    background="#FFFFFF"
                    )
                entry3.grid(row=int(boardx*3.75)+2, column=int(boardx*3.75)+2)
                entry3.bind("<Return>", colorsetter1)
                entry3.insert(0, buttonscolor)
                #
                entry4 = Entry(
                    root, width=12, name= "debugWP3",
                    background="#FFFFFF"
                    )
                entry4.grid(row=int(boardx*3.75)+5, column=int(boardx*3.75)+1)
                entry4.bind("<Return>", colorsetter1)
                entry4.insert(0, WPcolor)
                #
                entry5 = Entry(
                    root, width=12, name= "debugWR3",
                    background="#FFFFFF"
                    )
                entry5.grid(row=int(boardx*3.75)+5, column=int(boardx*3.75)+2)
                entry5.bind("<Return>", colorsetter1)
                entry5.insert(0, WRcolor)
                #
                entry6 = Entry(
                    root, width=12, name= "debugWH3",
                    background="#FFFFFF"
                    )
                entry6.grid(row=int(boardx*3.75)+5, column=int(boardx*3.75)+3)
                entry6.bind("<Return>", colorsetter1)
                entry6.insert(0, WHcolor)
                #
                entry7 = Entry(
                    root, width=12, name= "debugWB3",
                    background="#FFFFFF"
                    )
                entry7.grid(row=int(boardx*3.75)+5, column=int(boardx*3.75)+4)
                entry7.bind("<Return>", colorsetter1)
                entry7.insert(0, WBcolor)
                #
                entry8 = Entry(
                    root, width=12, name= "debugWQ3",
                    background="#FFFFFF"
                    )
                entry8.grid(row=int(boardx*3.75)+5, column=int(boardx*3.75)+5)
                entry8.bind("<Return>", colorsetter1)
                entry8.insert(0, WQcolor)
                #
                entry9 = Entry(
                    root, width=12, name= "debugWK3",
                    background="#FFFFFF"
                    )
                entry9.grid(row=int(boardx*3.75)+5, column=int(boardx*3.75)+6)
                entry9.bind("<Return>", colorsetter1)
                entry9.insert(0, WKcolor)
                #
                entry10 = Entry(
                    root, width=12, name= "debugBP3",
                    background="#FFFFFF"
                    )
                entry10.grid(row=int(boardx*3.75)+8, column=int(boardx*3.75)+1)
                entry10.bind("<Return>", colorsetter1)
                entry10.insert(0, BPcolor)
                #
                entry11 = Entry(
                    root, width=12, name= "debugBR3",
                    background="#FFFFFF"
                    )
                entry11.grid(row=int(boardx*3.75)+8, column=int(boardx*3.75)+2)
                entry11.bind("<Return>", colorsetter1)
                entry11.insert(0, BRcolor)
                #
                entry12 = Entry(
                    root, width=12, name= "debugBH3",
                    background="#FFFFFF"
                    )
                entry12.grid(row=int(boardx*3.75)+8, column=int(boardx*3.75)+3)
                entry12.bind("<Return>", colorsetter1)
                entry12.insert(0, BHcolor)
                #
                entry13 = Entry(
                    root, width=12, name= "debugBB3",
                    background="#FFFFFF"
                    )
                entry13.grid(row=int(boardx*3.75)+8, column=int(boardx*3.75)+4)
                entry13.bind("<Return>", colorsetter1)
                entry13.insert(0, BBcolor)
                #
                entry14 = Entry(
                    root, width=12, name= "debugBQ3",
                    background="#FFFFFF"
                    )
                entry14.grid(row=int(boardx*3.75)+8, column=int(boardx*3.75)+5)
                entry14.bind("<Return>", colorsetter1)
                entry14.insert(0, BQcolor)
                #
                entry15 = Entry(
                    root, width=12, name= "debugBK3",
                    background="#FFFFFF"
                    )
                entry15.grid(row=int(boardx*3.75)+8, column=int(boardx*3.75)+6)
                entry15.bind("<Return>", colorsetter1)
                entry15.insert(0, BKcolor)

        else:
            Button(
                root, text="End game", width=9,
                background=buttonscolor,
                foreground=Buttontextcolor,
                activebackground=Buttontextcolor,
                activeforeground=buttonscolor,
                command=lambda: ender() 
            ).place(x=int((boardx*33+33)/2), y=(boardx*32))
        Button(
            root, width=widths,
            command=lambda: debugadd(),
            background=emptycolor1,
            activebackground=emptytextcolor2,
        ).grid(row=boardx+1, column=1)
    def draw_board2():
        clear_board()
        global checkerp, boardx, turn1, Blackset, Whiteset
        checkerp = True
        for r in range(boardx):
            for c in range(boardx+1):
                if c == boardx:
                    if checkerp == False:
                        checkerp = True
                    else:
                        checkerp = False
                rowm2 = [r+1,c+1]
                rowm = game_board[rowm2[0]]
                if rowm[rowm2[1]] in ('--'):
                    if checkerp == True:
                        Button(
                            root, width=widths,
                            background=emptycolor2,
                            command=lambda posy=r, posx=c: clicked2(posy+1, posx+1),
                            activebackground=emptytextcolor2,
                        ).grid(row=r+1, column=c+1)
                        checkerp = False
                    elif checkerp == False:
                        Button(
                            root, width=widths,
                            background=emptycolor1,
                            command=lambda posy=r, posx=c: clicked2(posy+1, posx+1),
                            activebackground=emptytextcolor1,
                        ).grid(row=r+1, column=c+1)
                        checkerp = True
                elif rowm[rowm2[1]] in Blackset:
                    if rowm[rowm2[1]] == 'BQ':
                        Button(
                            root,
                            text="BQ", width=widths,
                            command=lambda posy=r, posx=c: clicked2(posy+1, posx+1),
                            background= BQcolor,
                            foreground= BQtextcolor,
                            activebackground= BQtextcolor,
                            activeforeground= BQcolor
                        ).grid(row=r+1, column=c+1)
                    elif rowm[rowm2[1]] == 'BP':
                        Button(
                            root,
                            text="BP", width=widths,
                            command=lambda posy=r, posx=c: clicked2(posy+1, posx+1),
                            background=BPcolor,
                            foreground= BPtextcolor,
                            activebackground=BPtextcolor,
                            activeforeground=BPcolor
                        ).grid(row=r+1, column=c+1)
                    elif rowm[rowm2[1]] == 'BR':
                        Button(
                            root,
                            text="BR", width=widths,
                            command=lambda posy=r, posx=c: clicked2(posy+1, posx+1),
                            background=BRcolor,
                            foreground= BRtextcolor,
                            activebackground=BRtextcolor,
                            activeforeground=BRcolor
                        ).grid(row=r+1, column=c+1)
                    elif rowm[rowm2[1]] == 'BH':
                        Button(
                            root,
                            text="BH", width=widths,
                            command=lambda posy=r, posx=c: clicked2(posy+1, posx+1),
                            background=BHcolor,
                            foreground= BHtextcolor,
                            activebackground=BHtextcolor,
                            activeforeground=BHcolor
                        ).grid(row=r+1, column=c+1)
                    elif rowm[rowm2[1]] == 'BK':
                        Button(
                            root,
                            text="BK", width=widths,
                            command=lambda posy=r, posx=c: clicked2(posy+1, posx+1),
                            background=BKcolor,
                            foreground= BKtextcolor,
                            activebackground=BKtextcolor,
                            activeforeground=BKcolor
                        ).grid(row=r+1, column=c+1)
                    elif rowm[rowm2[1]] == 'BB':
                        Button(
                            root,
                            text="BB", width=widths,
                            command=lambda posy=r, posx=c: clicked2(posy+1, posx+1),
                            background=BBcolor,
                            foreground= BBtextcolor,
                            activebackground=BBtextcolor,
                            activeforeground=BBcolor
                        ).grid(row=r+1, column=c+1)
                    if checkerp == False:
                        checkerp = True
                    else:
                        checkerp = False
                elif rowm[rowm2[1]] in Whiteset:
                    if rowm[rowm2[1]] == 'WQ':
                        Button(
                            root,
                            text="WQ", width=widths,
                            command=lambda posy=r, posx=c: clicked2(posy+1, posx+1),
                            background=WQcolor,
                            foreground=WQtextcolor,
                            activebackground=WQtextcolor,
                            activeforeground=WQcolor
                        ).grid(row=r+1, column=c+1)
                    elif rowm[rowm2[1]] == 'WP':
                        Button(
                            root,
                            text="WP", width=widths,
                            command=lambda posy=r, posx=c: clicked2(posy+1, posx+1),
                            background=WPcolor,
                            foreground=WPtextcolor,
                            activebackground=WPtextcolor,
                            activeforeground=WPcolor
                        ).grid(row=r+1, column=c+1)
                    elif rowm[rowm2[1]] == 'WR':
                        Button(
                            root,
                            text="WR", width=widths,
                            command=lambda posy=r, posx=c: clicked2(posy+1, posx+1),
                            background=WRcolor,
                            foreground= WRtextcolor,
                            activebackground=WRtextcolor,
                            activeforeground=WRcolor
                        ).grid(row=r+1, column=c+1)
                    elif rowm[rowm2[1]] == 'WH':
                        Button(
                            root,
                            text="WH", width=widths,
                            command=lambda posy=r, posx=c: clicked2(posy+1, posx+1),
                            background=WHcolor,
                            foreground= WHtextcolor,
                            activebackground=WHtextcolor,
                            activeforeground=WHcolor
                        ).grid(row=r+1, column=c+1)
                    elif rowm[rowm2[1]] == 'WK':
                        Button(
                            root,
                            text="WK", width=widths,
                            command=lambda posy=r, posx=c: clicked2(posy+1, posx+1),
                            background=WKcolor,
                            foreground= WKtextcolor,
                            activebackground=WKtextcolor,
                            activeforeground=WKcolor
                        ).grid(row=r+1, column=c+1)
                    elif rowm[rowm2[1]] == 'WB':
                        Button(
                            root,
                            text="WB", width=widths,
                            command=lambda posy=r, posx=c: clicked2(posy+1, posx+1),
                            background=WBcolor,
                            foreground= WBtextcolor,
                            activebackground=WBtextcolor,
                            activeforeground=WBcolor
                        ).grid(row=r+1, column=c+1)
                    if checkerp == False:
                        checkerp = True
                    else:
                        checkerp = False
        if debugon:
            global entry1, entry2, entry3, entry4, entry5, entry6, entry7, entry8, entry9, entry10, entry11, entry12, entry13, entry14, entry15
            Button( #skip turn
            root, text='Skip Turn', width=9,
            background=buttonscolor,
            foreground=Buttontextcolor,
            activebackground=Buttontextcolor,
            activeforeground=buttonscolor,
            command=lambda: skiper()
            ).place(x=int((boardx*33+33)/3), y=(boardx*32))
            Button( #end game
                root, text="End game", width=9,
                background=buttonscolor,
                foreground=Buttontextcolor,
                activebackground=Buttontextcolor,
                activeforeground=buttonscolor,
                command=lambda: ender() 
            ).place(x=int((boardx*33+33)/1.5), y=(boardx*32))
            Button( #Roll color
                root, text="Roll color", width=9,
                background=buttonscolor,
                foreground=Buttontextcolor,
                activebackground=Buttontextcolor,
                activeforeground=buttonscolor,
                command=lambda: rollcolor3()
            ).place(x=int((boardx*33+33)/(boardx+4)), y=(boardx*32))
            Button( #debugempty1-1
                root, width=10, height=5, name= "debugempty1-1",
                background=emptycolor1,
                activebackground=emptytextcolor1
                ).grid(padx=(50,0), row=int(boardx*3.75), column=int(boardx*3.75))
            Button( #debugempty1-2
                root, width=10, height=5, name= "debugempty1-2",
                background=emptytextcolor1,
                activebackground=emptycolor1
                ).grid(padx=(50,0), row=int(boardx*3.75)+1, column=int(boardx*3.75))
            Button( #debugempty2-1
                root, width=10, height=5, name= "debugempty2-1",
                background=emptycolor2,
                activebackground=emptytextcolor2
                ).grid(row=int(boardx*3.75), column=int(boardx*3.75)+1)
            Button( #debugempty2-2
                root, width=10, height=5, name= "debugempty2-2",
                background=emptytextcolor2,
                activebackground=emptycolor2
                ).grid(row=int(boardx*3.75)+1, column=int(boardx*3.75)+1)
            Button( #debugbuttoncolor1
                root, width=10, height=5,  name= "debugbuttoncolor1",
                background=buttonscolor,
                activebackground=Buttontextcolor
                ).grid(row=int(boardx*3.75), column=int(boardx*3.75)+2)
            Button( #debugbuttoncolor2
                root, width=10, height=5,  name= "debugbuttoncolor2",
                background=Buttontextcolor,
                activebackground=buttonscolor
                ).grid(row=int(boardx*3.75)+1, column=int(boardx*3.75)+2)
            
            buttonbase = 1
            Button( #debugWP1
                root, width=10, height=5, name= "debugWP1", text="WP-Base",
                background=WPcolor,
                activebackground=WPtextcolor
                ).grid(row=int(boardx*3.75)+3, column=int(boardx*3.75)+buttonbase)
            Button( #debugWP2
                root, width=10, height=5, name= "debugWP2",text="WP-Active",
                background=WPtextcolor,
                activebackground=WPcolor
                ).grid(row=int(boardx*3.75)+4, column=int(boardx*3.75)+buttonbase)
            Button( #debugWR1
                root, width=10, height=5, name= "debugWR1", text="WR-Base",
                background=WRcolor,
                activebackground=WRtextcolor
                ).grid(row=int(boardx*3.75)+3, column=int(boardx*3.75)+buttonbase+1)
            Button( #debugWR2
                root, width=10, height=5, name= "debugWR2",text="WR-Active",
                background=WRtextcolor,
                activebackground=WRcolor
                ).grid(row=int(boardx*3.75)+4, column=int(boardx*3.75)+buttonbase+1)
            Button( #debugWH1
                root, width=10, height=5,  name= "debugWH1",text="WH-Base",
                background=WHcolor,
                activebackground=WHtextcolor
                ).grid(row=int(boardx*3.75)+3, column=int(boardx*3.75)+buttonbase+2)
            Button( #debugWH2
                root, width=10, height=5,  name= "debugWH2",text="WH-Active",
                background=WHtextcolor,
                activebackground=WHcolor
                ).grid(row=int(boardx*3.75)+4, column=int(boardx*3.75)+buttonbase+2)
            Button( #debugWB1
                root, width=10, height=5,  name= "debugWB1",text="WB-Base",
                background=WBcolor,
                activebackground=WBtextcolor
                ).grid(row=int(boardx*3.75)+3, column=int(boardx*3.75)+buttonbase+3)
            Button( #debugWB2
                root, width=10, height=5,  name= "debugWB2",text="WB-Active",
                background=WBtextcolor,
                activebackground=WBcolor
                ).grid(row=int(boardx*3.75)+4, column=int(boardx*3.75)+buttonbase+3)
            Button( #debugWQ1
                root, width=10, height=5,  name= "debugWQ1",text="WQ-Base",
                background=WQcolor,
                activebackground=WQtextcolor
                ).grid(row=int(boardx*3.75)+3, column=int(boardx*3.75)+buttonbase+4)
            Button( #debugWQ2
                root, width=10, height=5,  name= "debugWQ2",text="WQ-Active",
                background=WQtextcolor,
                activebackground=WQcolor
                ).grid(row=int(boardx*3.75)+4, column=int(boardx*3.75)+buttonbase+4)
            Button( #debugWK1
                root, width=10, height=5,  name= "debugWK1",text="WK-Base",
                background=WKcolor,
                activebackground=WKtextcolor
                ).grid(row=int(boardx*3.75)+3, column=int(boardx*3.75)+buttonbase+5)
            Button( #debugWK2
                root, width=10, height=5,  name= "debugWK2",text="WK-Active",
                background=WKtextcolor,
                activebackground=WKcolor
                ).grid(row=int(boardx*3.75)+4, column=int(boardx*3.75)+buttonbase+5)
            
            Button( #debugBP1
                root, width=10, height=5, name= "debugBP1", text="BP-Base",
                background=BPcolor,
                activebackground=BPtextcolor
                ).grid(row=int(boardx*3.75)+6, column=int(boardx*3.75)+buttonbase)
            Button( #debugBP2
                root, width=10, height=5, name= "debugBP2",text="BP-Active",
                background=BPtextcolor,
                activebackground=BPcolor
                ).grid(row=int(boardx*3.75)+7, column=int(boardx*3.75)+buttonbase)
            Button( #debugBR1
                root, width=10, height=5, name= "debugBR1", text="BR-Base",
                background=BRcolor,
                activebackground=BRtextcolor
                ).grid(row=int(boardx*3.75)+6, column=int(boardx*3.75)+buttonbase+1)
            Button( #debugBR2
                root, width=10, height=5, name= "debugBR2",text="BR-Active",
                background=BRtextcolor,
                activebackground=BRcolor
                ).grid(row=int(boardx*3.75)+7, column=int(boardx*3.75)+buttonbase+1)
            Button( #debugBH1
                root, width=10, height=5,  name= "debugBH1",text="BH-Base",
                background=BHcolor,
                activebackground=BHtextcolor
                ).grid(row=int(boardx*3.75)+6, column=int(boardx*3.75)+buttonbase+2)
            Button( #debugBH2
                root, width=10, height=5,  name= "debugBH2",text="BH-Active",
                background=BHtextcolor,
                activebackground=BHcolor
                ).grid(row=int(boardx*3.75)+7, column=int(boardx*3.75)+buttonbase+2)
            Button( #debugBB1
                root, width=10, height=5,  name= "debugBB1",text="BB-Base",
                background=BBcolor,
                activebackground=BBtextcolor
                ).grid(row=int(boardx*3.75)+6, column=int(boardx*3.75)+buttonbase+3)
            Button( #debugBB2
                root, width=10, height=5,  name= "debugBB2",text="BB-Active",
                background=BBtextcolor,
                activebackground=BBcolor
                ).grid(row=int(boardx*3.75)+7, column=int(boardx*3.75)+buttonbase+3)
            Button( #debugBQ1
                root, width=10, height=5,  name= "debugBQ1",text="BQ-Base",
                background=BQcolor,
                activebackground=BQtextcolor
                ).grid(row=int(boardx*3.75)+6, column=int(boardx*3.75)+buttonbase+4)
            Button( #debugBQ2
                root, width=10, height=5,  name= "debugBQ2",text="BQ-Active",
                background=BQtextcolor,
                activebackground=BQcolor
                ).grid(row=int(boardx*3.75)+7, column=int(boardx*3.75)+buttonbase+4)
            Button( #debugBK1
                root, width=10, height=5,  name= "debugBK1",text="BK-Base",
                background=BKcolor,
                activebackground=BKtextcolor
                ).grid(row=int(boardx*3.75)+6, column=int(boardx*3.75)+buttonbase+5)
            Button( #debugBK2
                root, width=10, height=5,  name= "debugBK2",text="BK-Active",
                background=BKtextcolor,
                activebackground=BKcolor
                ).grid(row=int(boardx*3.75)+7, column=int(boardx*3.75)+buttonbase+5)
            
            entries = True
            if entries == True:
                entry1 = Entry(
                    root, width=12, name= "debugempty1-3",
                    background= "#FFFFFF"
                    )
                entry1.grid(padx=(50,0), row=int(boardx*3.75)+2, column=int(boardx*3.75))
                entry1.bind("<Return>", colorsetter2)
                entry1.insert(0, emptycolor1)
                #
                entry2 = Entry(
                    root, width=12, name= "debugempty2-3",
                    background="#FFFFFF"
                    )
                entry2.grid(row=int(boardx*3.75)+2, column=int(boardx*3.75)+1)
                entry2.bind("<Return>", colorsetter2)
                entry2.insert(0, emptycolor2)
                #
                entry3 = Entry(
                    root, width=12, name= "debugbuttoncolor3",
                    background="#FFFFFF"
                    )
                entry3.grid(row=int(boardx*3.75)+2, column=int(boardx*3.75)+2)
                entry3.bind("<Return>", colorsetter2)
                entry3.insert(0, buttonscolor)
                #
                entry4 = Entry(
                    root, width=12, name= "debugWP3",
                    background="#FFFFFF"
                    )
                entry4.grid(row=int(boardx*3.75)+5, column=int(boardx*3.75)+1)
                entry4.bind("<Return>", colorsetter2)
                entry4.insert(0, WPcolor)
                #
                entry5 = Entry(
                    root, width=12, name= "debugWR3",
                    background="#FFFFFF"
                    )
                entry5.grid(row=int(boardx*3.75)+5, column=int(boardx*3.75)+2)
                entry5.bind("<Return>", colorsetter2)
                entry5.insert(0, WRcolor)
                #
                entry6 = Entry(
                    root, width=12, name= "debugWH3",
                    background="#FFFFFF"
                    )
                entry6.grid(row=int(boardx*3.75)+5, column=int(boardx*3.75)+3)
                entry6.bind("<Return>", colorsetter2)
                entry6.insert(0, WHcolor)
                #
                entry7 = Entry(
                    root, width=12, name= "debugWB3",
                    background="#FFFFFF"
                    )
                entry7.grid(row=int(boardx*3.75)+5, column=int(boardx*3.75)+4)
                entry7.bind("<Return>", colorsetter2)
                entry7.insert(0, WBcolor)
                #
                entry8 = Entry(
                    root, width=12, name= "debugWQ3",
                    background="#FFFFFF"
                    )
                entry8.grid(row=int(boardx*3.75)+5, column=int(boardx*3.75)+5)
                entry8.bind("<Return>", colorsetter2)
                entry8.insert(0, WQcolor)
                #
                entry9 = Entry(
                    root, width=12, name= "debugWK3",
                    background="#FFFFFF"
                    )
                entry9.grid(row=int(boardx*3.75)+5, column=int(boardx*3.75)+6)
                entry9.bind("<Return>", colorsetter2)
                entry9.insert(0, WKcolor)
                #
                entry10 = Entry(
                    root, width=12, name= "debugBP3",
                    background="#FFFFFF"
                    )
                entry10.grid(row=int(boardx*3.75)+8, column=int(boardx*3.75)+1)
                entry10.bind("<Return>", colorsetter2)
                entry10.insert(0, BPcolor)
                #
                entry11 = Entry(
                    root, width=12, name= "debugBR3",
                    background="#FFFFFF"
                    )
                entry11.grid(row=int(boardx*3.75)+8, column=int(boardx*3.75)+2)
                entry11.bind("<Return>", colorsetter2)
                entry11.insert(0, BRcolor)
                #
                entry12 = Entry(
                    root, width=12, name= "debugBH3",
                    background="#FFFFFF"
                    )
                entry12.grid(row=int(boardx*3.75)+8, column=int(boardx*3.75)+3)
                entry12.bind("<Return>", colorsetter2)
                entry12.insert(0, BHcolor)
                #
                entry13 = Entry(
                    root, width=12, name= "debugBB3",
                    background="#FFFFFF"
                    )
                entry13.grid(row=int(boardx*3.75)+8, column=int(boardx*3.75)+4)
                entry13.bind("<Return>", colorsetter2)
                entry13.insert(0, BBcolor)
                #
                entry14 = Entry(
                    root, width=12, name= "debugBQ3",
                    background="#FFFFFF"
                    )
                entry14.grid(row=int(boardx*3.75)+8, column=int(boardx*3.75)+5)
                entry14.bind("<Return>", colorsetter2)
                entry14.insert(0, BQcolor)
                #
                entry15 = Entry(
                    root, width=12, name= "debugBK3",
                    background="#FFFFFF"
                    )
                entry15.grid(row=int(boardx*3.75)+8, column=int(boardx*3.75)+6)
                entry15.bind("<Return>", colorsetter2)
                entry15.insert(0, BKcolor)
        
        else:
            Button(
                root, text="End game", width=9,
                background=buttonscolor,
                foreground=Buttontextcolor,
                activebackground=Buttontextcolor,
                activeforeground=buttonscolor,
                command=lambda: ender() 
            ).place(x=int((boardx*33+33)/2), y=(boardx*32))
        turn1 = False
    def end_draw_board():
        clear_board()
        global checkerp, boardx, Blackset, Whiteset, Stalemate, Checkmate, lbl7
        checkerp = True
        if wpeices == 0:
            lbl5.configure(text = f"White Loses")
        elif bpeices == 0:
            #print('bwha')
            lbl5.configure(text = f"Black Loses")
        elif Checkmate == True and turn == "Black":
            lbl7.configure(text = f"Checkmate")
            lbl5.configure(text = f"Black Wins")
        elif Checkmate == True and turn == "White":
            lbl7.configure(text = f"Checkmate")
            lbl5.configure(text = f"White Wins")
        elif Stalemate == True:
            lbl7.configure(text = f"Stalemate")
        for r in range(boardx):
            for c in range(boardx+1):
                if c == boardx:
                    if checkerp == False:
                        checkerp = True
                    else:
                        checkerp = False
                rowm2 = [r+1,c+1]
                rowm = game_board[rowm2[0]]
                if rowm[rowm2[1]] in ('--'):
                    if checkerp == True:
                        Button(
                            root, width=widths,
                            background=emptycolor2,
                            activebackground=emptytextcolor2
                        ).grid(row=r+1, column=c+1)
                        checkerp = False
                    elif checkerp == False:
                        Button(
                            root, width=widths,
                            background=emptycolor1,
                            activebackground=emptytextcolor1
                        ).grid(row=r+1, column=c+1)
                        checkerp = True
                elif rowm[rowm2[1]] in Blackset:
                    if rowm[rowm2[1]] == 'BQ':
                        Button(
                            root,
                            text="BQ", width=widths,
                            background= BQcolor,
                            foreground= BQtextcolor,
                            activebackground= BQtextcolor,
                            activeforeground= BQcolor
                        ).grid(row=r+1, column=c+1)
                    elif rowm[rowm2[1]] == 'BP':
                        Button(
                            root,
                            text="BP", width=widths,
                            background=BPcolor,
                            foreground= BPtextcolor,
                            activebackground=BPtextcolor,
                            activeforeground=BPcolor
                        ).grid(row=r+1, column=c+1)
                    elif rowm[rowm2[1]] == 'BR':
                        Button(
                            root,
                            text="BR", width=widths,
                            background=BRcolor,
                            foreground= BRtextcolor,
                            activebackground=BRtextcolor,
                            activeforeground=BRcolor
                        ).grid(row=r+1, column=c+1)
                    elif rowm[rowm2[1]] == 'BH':
                        Button(
                            root,
                            text="BH", width=widths,
                            background=BHcolor,
                            foreground= BHtextcolor,
                            activebackground=BHtextcolor,
                            activeforeground=BHcolor
                        ).grid(row=r+1, column=c+1)
                    elif rowm[rowm2[1]] == 'BK':
                        Button(
                            root,
                            text="BK", width=widths,
                            background=BKcolor,
                            foreground= BKtextcolor,
                            activebackground=BKtextcolor,
                            activeforeground=BKcolor
                        ).grid(row=r+1, column=c+1)
                    elif rowm[rowm2[1]] == 'BB':
                        Button(
                            root,
                            text="BB", width=widths,
                            background=BBcolor,
                            foreground= BBtextcolor,
                            activebackground=BBtextcolor,
                            activeforeground=BBcolor
                        ).grid(row=r+1, column=c+1)
                    if checkerp == False:
                        checkerp = True
                    else:
                        checkerp = False
                elif rowm[rowm2[1]] in Whiteset:
                    if rowm[rowm2[1]] == 'WQ':
                        Button(
                            root,
                            text="WQ", width=widths,
                            background=WQcolor,
                            foreground=WQtextcolor,
                            activebackground=WQtextcolor,
                            activeforeground=WQcolor
                        ).grid(row=r+1, column=c+1)
                    elif rowm[rowm2[1]] == 'WP':
                        Button(
                            root,
                            text="WP", width=widths,
                            background=WPcolor,
                            foreground=WPtextcolor,
                            activebackground=WPtextcolor,
                            activeforeground=WPcolor
                        ).grid(row=r+1, column=c+1)
                    elif rowm[rowm2[1]] == 'WR':
                        Button(
                            root,
                            text="WR", width=widths,
                            background=WRcolor,
                            foreground= WRtextcolor,
                            activebackground=WRtextcolor,
                            activeforeground=WRcolor
                        ).grid(row=r+1, column=c+1)
                    elif rowm[rowm2[1]] == 'WH':
                        Button(
                            root,
                            text="WH", width=widths,
                            background=WHcolor,
                            foreground= WHtextcolor,
                            activebackground=WHtextcolor,
                            activeforeground=WHcolor
                        ).grid(row=r+1, column=c+1)
                    elif rowm[rowm2[1]] == 'WK':
                        Button(
                            root,
                            text="WK", width=widths,
                            background=WKcolor,
                            foreground= WKtextcolor,
                            activebackground=WKtextcolor,
                            activeforeground=WKcolor
                        ).grid(row=r+1, column=c+1)
                    elif rowm[rowm2[1]] == 'WB':
                        Button(
                            root,
                            text="WB", width=widths,
                            background=WBcolor,
                            foreground= WBtextcolor,
                            activebackground=WBtextcolor,
                            activeforeground=WBcolor
                        ).grid(row=r+1, column=c+1)
                    if checkerp == False:
                        checkerp = True
                    else:
                        checkerp = False
        
        Button(
            root, text='Restart', width=9,
            background=buttonscolor,
            foreground=Buttontextcolor,
            activebackground=Buttontextcolor,
            activeforeground=buttonscolor,
            command=lambda: restarter()
        ).place(x=int((boardx*33+33)/3), y=(boardx*32))
        Button(
            root, text="Don't", width=9,
            background=buttonscolor,
            foreground=Buttontextcolor,
            activebackground=Buttontextcolor,
            activeforeground=buttonscolor,
            command=lambda: norestarter() 
        ).place(x=int((boardx*33+33)/1.5), y=(boardx*32))
    def evolve_board():
        clear_board()
        global checkerp, boardx, Blackset, Whiteset, evolveer2
        checkerp = True
        for r in range(boardx):
            for c in range(boardx+1):
                if c == boardx:
                    if checkerp == False:
                        checkerp = True
                    else:
                        checkerp = False
                rowm2 = [r+1,c+1]
                rowm = game_board[rowm2[0]]
                if rowm[rowm2[1]] in ('--'):
                    if checkerp == True:
                        Button(
                            root, width=widths,
                            background=emptycolor2,
                            activebackground=emptytextcolor2
                        ).grid(row=r+1, column=c+1)
                        checkerp = False
                    elif checkerp == False:
                        Button(
                            root, width=widths,
                            background=emptycolor1,
                            activebackground=emptytextcolor1
                        ).grid(row=r+1, column=c+1)
                        checkerp = True
                elif rowm[rowm2[1]] in Blackset:
                    if rowm[rowm2[1]] == 'BQ':
                        Button(
                            root,
                            text="BQ", width=widths,
                            background= BQcolor,
                            foreground= BQtextcolor,
                            activebackground= BQtextcolor,
                            activeforeground= BQcolor
                        ).grid(row=r+1, column=c+1)
                    elif rowm[rowm2[1]] == 'BP':
                        Button(
                            root,
                            text="BP", width=widths,
                            background=BPcolor,
                            foreground= BPtextcolor,
                            activebackground=BPtextcolor,
                            activeforeground=BPcolor
                        ).grid(row=r+1, column=c+1)
                    elif rowm[rowm2[1]] == 'BR':
                        Button(
                            root,
                            text="BR", width=widths,
                            background=BRcolor,
                            foreground= BRtextcolor,
                            activebackground=BRtextcolor,
                            activeforeground=BRcolor
                        ).grid(row=r+1, column=c+1)
                    elif rowm[rowm2[1]] == 'BH':
                        Button(
                            root,
                            text="BH", width=widths,
                            background=BHcolor,
                            foreground= BHtextcolor,
                            activebackground=BHtextcolor,
                            activeforeground=BHcolor
                        ).grid(row=r+1, column=c+1)
                    elif rowm[rowm2[1]] == 'BK':
                        Button(
                            root,
                            text="BK", width=widths,
                            background=BKcolor,
                            foreground= BKtextcolor,
                            activebackground=BKtextcolor,
                            activeforeground=BKcolor
                        ).grid(row=r+1, column=c+1)
                    elif rowm[rowm2[1]] == 'BB':
                        Button(
                            root,
                            text="BB", width=widths,
                            background=BBcolor,
                            foreground= BBtextcolor,
                            activebackground=BBtextcolor,
                            activeforeground=BBcolor
                        ).grid(row=r+1, column=c+1)
                    elif rowm[rowm2[1]] == 'BE':
                        Button(
                            root,
                            text="BE", width=widths,
                            background=BBcolor,
                            foreground= BBtextcolor,
                            activebackground=BBtextcolor,
                            activeforeground=BBcolor
                        ).grid(row=r+1, column=c+1)
                    if checkerp == False:
                        checkerp = True
                    else:
                        checkerp = False
                elif rowm[rowm2[1]] in Whiteset:
                    if rowm[rowm2[1]] == 'WQ':
                        Button(
                            root,
                            text="WQ", width=widths,
                            background=WQcolor,
                            foreground=WQtextcolor,
                            activebackground=WQtextcolor,
                            activeforeground=WQcolor
                        ).grid(row=r+1, column=c+1)
                    elif rowm[rowm2[1]] == 'WP':
                        Button(
                            root,
                            text="WP", width=widths,
                            background=WPcolor,
                            foreground=WPtextcolor,
                            activebackground=WPtextcolor,
                            activeforeground=WPcolor
                        ).grid(row=r+1, column=c+1)
                    elif rowm[rowm2[1]] == 'WR':
                        Button(
                            root,
                            text="WR", width=widths,
                            background=WRcolor,
                            foreground= WRtextcolor,
                            activebackground=WRtextcolor,
                            activeforeground=WRcolor
                        ).grid(row=r+1, column=c+1)
                    elif rowm[rowm2[1]] == 'WH':
                        Button(
                            root,
                            text="WH", width=widths,
                            background=WHcolor,
                            foreground= WHtextcolor,
                            activebackground=WHtextcolor,
                            activeforeground=WHcolor
                        ).grid(row=r+1, column=c+1)
                    elif rowm[rowm2[1]] == 'WK':
                        Button(
                            root,
                            text="WK", width=widths,
                            background=WKcolor,
                            foreground= WKtextcolor,
                            activebackground=WKtextcolor,
                            activeforeground=WKcolor
                        ).grid(row=r+1, column=c+1)
                    elif rowm[rowm2[1]] == 'WB':
                        Button(
                            root,
                            text="WB", width=widths,
                            background=WBcolor,
                            foreground= WBtextcolor,
                            activebackground=WBtextcolor,
                            activeforeground=WBcolor
                        ).grid(row=r+1, column=c+1)
                    elif rowm[rowm2[1]] == 'WE':
                        Button(
                            root,
                            text="WE", width=widths,
                            background=WBcolor,
                            foreground= WBtextcolor,
                            activebackground=WBtextcolor,
                            activeforeground=WBcolor
                        ).grid(row=r+1, column=c+1)
                    if checkerp == False:
                        checkerp = True
                    else:
                        checkerp = False
        
        if debugon:
            global entry1, entry2, entry3, entry4, entry5, entry6, entry7, entry8, entry9, entry10, entry11, entry12, entry13, entry14, entry15
            Button( #skip turn
            root, text='Skip Turn', width=9,
            background=buttonscolor,
            foreground=Buttontextcolor,
            activebackground=Buttontextcolor,
            activeforeground=buttonscolor,
            command=lambda: skiper()
            ).place(x=int((boardx*33+33)/3), y=(boardx*32))
            Button( #end game
                root, text="End game", width=9,
                background=buttonscolor,
                foreground=Buttontextcolor,
                activebackground=Buttontextcolor,
                activeforeground=buttonscolor,
                command=lambda: ender() 
            ).place(x=int((boardx*33+33)/1.5), y=(boardx*32))
            Button( #Roll color
                root, text="Roll color", width=9,
                background=buttonscolor,
                foreground=Buttontextcolor,
                activebackground=Buttontextcolor,
                activeforeground=buttonscolor,
                command=lambda: rollcolor2()
            ).place(x=int((boardx*33+33)/(boardx+4)), y=(boardx*32))
            Button( #debugempty1-1
                root, width=10, height=5, name= "debugempty1-1",
                background=emptycolor1,
                activebackground=emptytextcolor1
                ).grid(padx=(50,0), row=int(boardx*3.75), column=int(boardx*3.75))
            Button( #debugempty1-2
                root, width=10, height=5, name= "debugempty1-2",
                background=emptytextcolor1,
                activebackground=emptycolor1
                ).grid(padx=(50,0), row=int(boardx*3.75)+1, column=int(boardx*3.75))
            Button( #debugempty2-1
                root, width=10, height=5, name= "debugempty2-1",
                background=emptycolor2,
                activebackground=emptytextcolor2
                ).grid(row=int(boardx*3.75), column=int(boardx*3.75)+1)
            Button( #debugempty2-2
                root, width=10, height=5, name= "debugempty2-2",
                background=emptytextcolor2,
                activebackground=emptycolor2
                ).grid(row=int(boardx*3.75)+1, column=int(boardx*3.75)+1)
            Button( #debugbuttoncolor1
                root, width=10, height=5,  name= "debugbuttoncolor1",
                background=buttonscolor,
                activebackground=Buttontextcolor
                ).grid(row=int(boardx*3.75), column=int(boardx*3.75)+2)
            Button( #debugbuttoncolor2
                root, width=10, height=5,  name= "debugbuttoncolor2",
                background=Buttontextcolor,
                activebackground=buttonscolor
                ).grid(row=int(boardx*3.75)+1, column=int(boardx*3.75)+2)
            
            buttonbase = 1
            Button( #debugWP1
                root, width=10, height=5, name= "debugWP1", text="WP-Base",
                background=WPcolor,
                activebackground=WPtextcolor
                ).grid(row=int(boardx*3.75)+3, column=int(boardx*3.75)+buttonbase)
            Button( #debugWP2
                root, width=10, height=5, name= "debugWP2",text="WP-Active",
                background=WPtextcolor,
                activebackground=WPcolor
                ).grid(row=int(boardx*3.75)+4, column=int(boardx*3.75)+buttonbase)
            Button( #debugWR1
                root, width=10, height=5, name= "debugWR1", text="WR-Base",
                background=WRcolor,
                activebackground=WRtextcolor
                ).grid(row=int(boardx*3.75)+3, column=int(boardx*3.75)+buttonbase+1)
            Button( #debugWR2
                root, width=10, height=5, name= "debugWR2",text="WR-Active",
                background=WRtextcolor,
                activebackground=WRcolor
                ).grid(row=int(boardx*3.75)+4, column=int(boardx*3.75)+buttonbase+1)
            Button( #debugWH1
                root, width=10, height=5,  name= "debugWH1",text="WH-Base",
                background=WHcolor,
                activebackground=WHtextcolor
                ).grid(row=int(boardx*3.75)+3, column=int(boardx*3.75)+buttonbase+2)
            Button( #debugWH2
                root, width=10, height=5,  name= "debugWH2",text="WH-Active",
                background=WHtextcolor,
                activebackground=WHcolor
                ).grid(row=int(boardx*3.75)+4, column=int(boardx*3.75)+buttonbase+2)
            Button( #debugWB1
                root, width=10, height=5,  name= "debugWB1",text="WB-Base",
                background=WBcolor,
                activebackground=WBtextcolor
                ).grid(row=int(boardx*3.75)+3, column=int(boardx*3.75)+buttonbase+3)
            Button( #debugWB2
                root, width=10, height=5,  name= "debugWB2",text="WB-Active",
                background=WBtextcolor,
                activebackground=WBcolor
                ).grid(row=int(boardx*3.75)+4, column=int(boardx*3.75)+buttonbase+3)
            Button( #debugWQ1
                root, width=10, height=5,  name= "debugWQ1",text="WQ-Base",
                background=WQcolor,
                activebackground=WQtextcolor
                ).grid(row=int(boardx*3.75)+3, column=int(boardx*3.75)+buttonbase+4)
            Button( #debugWQ2
                root, width=10, height=5,  name= "debugWQ2",text="WQ-Active",
                background=WQtextcolor,
                activebackground=WQcolor
                ).grid(row=int(boardx*3.75)+4, column=int(boardx*3.75)+buttonbase+4)
            Button( #debugWK1
                root, width=10, height=5,  name= "debugWK1",text="WK-Base",
                background=WKcolor,
                activebackground=WKtextcolor
                ).grid(row=int(boardx*3.75)+3, column=int(boardx*3.75)+buttonbase+5)
            Button( #debugWK2
                root, width=10, height=5,  name= "debugWK2",text="WK-Active",
                background=WKtextcolor,
                activebackground=WKcolor
                ).grid(row=int(boardx*3.75)+4, column=int(boardx*3.75)+buttonbase+5)
            
            Button( #debugBP1
                root, width=10, height=5, name= "debugBP1", text="BP-Base",
                background=BPcolor,
                activebackground=BPtextcolor
                ).grid(row=int(boardx*3.75)+6, column=int(boardx*3.75)+buttonbase)
            Button( #debugBP2
                root, width=10, height=5, name= "debugBP2",text="BP-Active",
                background=BPtextcolor,
                activebackground=BPcolor
                ).grid(row=int(boardx*3.75)+7, column=int(boardx*3.75)+buttonbase)
            Button( #debugBR1
                root, width=10, height=5, name= "debugBR1", text="BR-Base",
                background=BRcolor,
                activebackground=BRtextcolor
                ).grid(row=int(boardx*3.75)+6, column=int(boardx*3.75)+buttonbase+1)
            Button( #debugBR2
                root, width=10, height=5, name= "debugBR2",text="BR-Active",
                background=BRtextcolor,
                activebackground=BRcolor
                ).grid(row=int(boardx*3.75)+7, column=int(boardx*3.75)+buttonbase+1)
            Button( #debugBH1
                root, width=10, height=5,  name= "debugBH1",text="BH-Base",
                background=BHcolor,
                activebackground=BHtextcolor
                ).grid(row=int(boardx*3.75)+6, column=int(boardx*3.75)+buttonbase+2)
            Button( #debugBH2
                root, width=10, height=5,  name= "debugBH2",text="BH-Active",
                background=BHtextcolor,
                activebackground=BHcolor
                ).grid(row=int(boardx*3.75)+7, column=int(boardx*3.75)+buttonbase+2)
            Button( #debugBB1
                root, width=10, height=5,  name= "debugBB1",text="BB-Base",
                background=BBcolor,
                activebackground=BBtextcolor
                ).grid(row=int(boardx*3.75)+6, column=int(boardx*3.75)+buttonbase+3)
            Button( #debugBB2
                root, width=10, height=5,  name= "debugBB2",text="BB-Active",
                background=BBtextcolor,
                activebackground=BBcolor
                ).grid(row=int(boardx*3.75)+7, column=int(boardx*3.75)+buttonbase+3)
            Button( #debugBQ1
                root, width=10, height=5,  name= "debugBQ1",text="BQ-Base",
                background=BQcolor,
                activebackground=BQtextcolor
                ).grid(row=int(boardx*3.75)+6, column=int(boardx*3.75)+buttonbase+4)
            Button( #debugBQ2
                root, width=10, height=5,  name= "debugBQ2",text="BQ-Active",
                background=BQtextcolor,
                activebackground=BQcolor
                ).grid(row=int(boardx*3.75)+7, column=int(boardx*3.75)+buttonbase+4)
            Button( #debugBK1
                root, width=10, height=5,  name= "debugBK1",text="BK-Base",
                background=BKcolor,
                activebackground=BKtextcolor
                ).grid(row=int(boardx*3.75)+6, column=int(boardx*3.75)+buttonbase+5)
            Button( #debugBK2
                root, width=10, height=5,  name= "debugBK2",text="BK-Active",
                background=BKtextcolor,
                activebackground=BKcolor
                ).grid(row=int(boardx*3.75)+7, column=int(boardx*3.75)+buttonbase+5)
            
            entries = True
            if entries == True:
                entry1 = Entry(
                    root, width=12, name= "debugempty1-3",
                    background= "#FFFFFF"
                    )
                entry1.grid(padx=(50,0), row=int(boardx*3.75)+2, column=int(boardx*3.75))
                entry1.bind("<Return>", colorsetter1)
                entry1.insert(0, emptycolor1)
                #
                entry2 = Entry(
                    root, width=12, name= "debugempty2-3",
                    background="#FFFFFF"
                    )
                entry2.grid(row=int(boardx*3.75)+2, column=int(boardx*3.75)+1)
                entry2.bind("<Return>", colorsetter1)
                entry2.insert(0, emptycolor2)
                #
                entry3 = Entry(
                    root, width=12, name= "debugbuttoncolor3",
                    background="#FFFFFF"
                    )
                entry3.grid(row=int(boardx*3.75)+2, column=int(boardx*3.75)+2)
                entry3.bind("<Return>", colorsetter1)
                entry3.insert(0, buttonscolor)
                #
                entry4 = Entry(
                    root, width=12, name= "debugWP3",
                    background="#FFFFFF"
                    )
                entry4.grid(row=int(boardx*3.75)+5, column=int(boardx*3.75)+1)
                entry4.bind("<Return>", colorsetter1)
                entry4.insert(0, WPcolor)
                #
                entry5 = Entry(
                    root, width=12, name= "debugWR3",
                    background="#FFFFFF"
                    )
                entry5.grid(row=int(boardx*3.75)+5, column=int(boardx*3.75)+2)
                entry5.bind("<Return>", colorsetter1)
                entry5.insert(0, WRcolor)
                #
                entry6 = Entry(
                    root, width=12, name= "debugWH3",
                    background="#FFFFFF"
                    )
                entry6.grid(row=int(boardx*3.75)+5, column=int(boardx*3.75)+3)
                entry6.bind("<Return>", colorsetter1)
                entry6.insert(0, WHcolor)
                #
                entry7 = Entry(
                    root, width=12, name= "debugWB3",
                    background="#FFFFFF"
                    )
                entry7.grid(row=int(boardx*3.75)+5, column=int(boardx*3.75)+4)
                entry7.bind("<Return>", colorsetter1)
                entry7.insert(0, WBcolor)
                #
                entry8 = Entry(
                    root, width=12, name= "debugWQ3",
                    background="#FFFFFF"
                    )
                entry8.grid(row=int(boardx*3.75)+5, column=int(boardx*3.75)+5)
                entry8.bind("<Return>", colorsetter1)
                entry8.insert(0, WQcolor)
                #
                entry9 = Entry(
                    root, width=12, name= "debugWK3",
                    background="#FFFFFF"
                    )
                entry9.grid(row=int(boardx*3.75)+5, column=int(boardx*3.75)+6)
                entry9.bind("<Return>", colorsetter1)
                entry9.insert(0, WKcolor)
                #
                entry10 = Entry(
                    root, width=12, name= "debugBP3",
                    background="#FFFFFF"
                    )
                entry10.grid(row=int(boardx*3.75)+8, column=int(boardx*3.75)+1)
                entry10.bind("<Return>", colorsetter1)
                entry10.insert(0, BPcolor)
                #
                entry11 = Entry(
                    root, width=12, name= "debugBR3",
                    background="#FFFFFF"
                    )
                entry11.grid(row=int(boardx*3.75)+8, column=int(boardx*3.75)+2)
                entry11.bind("<Return>", colorsetter1)
                entry11.insert(0, BRcolor)
                #
                entry12 = Entry(
                    root, width=12, name= "debugBH3",
                    background="#FFFFFF"
                    )
                entry12.grid(row=int(boardx*3.75)+8, column=int(boardx*3.75)+3)
                entry12.bind("<Return>", colorsetter1)
                entry12.insert(0, BHcolor)
                #
                entry13 = Entry(
                    root, width=12, name= "debugBB3",
                    background="#FFFFFF"
                    )
                entry13.grid(row=int(boardx*3.75)+8, column=int(boardx*3.75)+4)
                entry13.bind("<Return>", colorsetter1)
                entry13.insert(0, BBcolor)
                #
                entry14 = Entry(
                    root, width=12, name= "debugBQ3",
                    background="#FFFFFF"
                    )
                entry14.grid(row=int(boardx*3.75)+8, column=int(boardx*3.75)+5)
                entry14.bind("<Return>", colorsetter1)
                entry14.insert(0, BQcolor)
                #
                entry15 = Entry(
                    root, width=12, name= "debugBK3",
                    background="#FFFFFF"
                    )
                entry15.grid(row=int(boardx*3.75)+8, column=int(boardx*3.75)+6)
                entry15.bind("<Return>", colorsetter1)
                entry15.insert(0, BKcolor)

        else:
            Button(
                root, text="End game", width=9,
                background=buttonscolor,
                foreground=Buttontextcolor,
                activebackground=Buttontextcolor,
                activeforeground=buttonscolor,
                command=lambda: ender() 
            ).place(x=int((boardx*33+33)/2), y=(boardx*32))
        
        Button(
            root, text="Q", width=9,
            background=buttonscolor,
            foreground=Buttontextcolor,
            activebackground=Buttontextcolor,
            activeforeground=buttonscolor,
            command=lambda: evolver("Q") 
        ).place(x=0, y=100)
        Button(
            root, text="H", width=9,
            background=buttonscolor,
            foreground=Buttontextcolor,
            activebackground=Buttontextcolor,
            activeforeground=buttonscolor,
            command=lambda: evolver("H") 
        ).place(x=0, y=130)
        Button(
            root, text="B", width=9,
            background=buttonscolor,
            foreground=Buttontextcolor,
            activebackground=Buttontextcolor,
            activeforeground=buttonscolor,
            command=lambda: evolver("B") 
        ).place(x=0, y=160)
        Button(
            root, text="R", width=9,
            background=buttonscolor,
            foreground=Buttontextcolor,
            activebackground=Buttontextcolor,
            activeforeground=buttonscolor,
            command=lambda: evolver("R") 
        ).place(x=0, y=190)
        
        

extrafuctions = True
if extrafuctions:
    def skiper():
        global skip, donesetter
        skip = True
        donesetter.set(True)
    def ender():
        global done, donesetter, move, to
        done = True
        donesetter.set(True)
    def restarter():
        global restart, choice, randomcolor
        choice = True
        if randomcolor:
            rollcolor()
        restart.set(True)
    def norestarter():
        global restart, choice
        choice = False
        restart.set(True)
    def debugadd():
        global debugad, debugon
        debugad += 1
        if debugad == 5:
            debugon = True
            draw_board()
    def rollcolor2():
        global emptycolor1, WRtextcolor, WHtextcolor, WBtextcolor, WRcolor, WHcolor, WBcolor, WKcolor, BRcolor, BHcolor, BBcolor, BKcolor, BHtextcolor, BBtextcolor, BKtextcolor, WKtextcolor, BRtextcolor, emptycolor2, WPcolor, WQcolor, BQcolor, BPcolor, buttonscolor, emptytextcolor1, emptytextcolor2, WPtextcolor, WQtextcolor, BPtextcolor, BQtextcolor, Buttontextcolor
        emptycolor1 = "#{:06x}".format(random.randint(0, 0xFFFFFF))
        emptycolor2 ="#{:06x}".format(random.randint(0, 0xFFFFFF))
        WPcolor = "#{:06x}".format(random.randint(0, 0xFFFFFF))
        WRcolor = "#{:06x}".format(random.randint(0, 0xFFFFFF))
        WHcolor = "#{:06x}".format(random.randint(0, 0xFFFFFF))
        WBcolor = "#{:06x}".format(random.randint(0, 0xFFFFFF))
        WQcolor = "#{:06x}".format(random.randint(0, 0xFFFFFF))
        WKcolor = "#{:06x}".format(random.randint(0, 0xFFFFFF))

        BPcolor = "#{:06x}".format(random.randint(0, 0xFFFFFF))
        BRcolor = "#{:06x}".format(random.randint(0, 0xFFFFFF))
        BHcolor = "#{:06x}".format(random.randint(0, 0xFFFFFF))
        BBcolor = "#{:06x}".format(random.randint(0, 0xFFFFFF))
        BQcolor = "#{:06x}".format(random.randint(0, 0xFFFFFF))
        BKcolor = "#{:06x}".format(random.randint(0, 0xFFFFFF))
        buttonscolor = "#{:06x}".format(random.randint(0, 0xFFFFFF))

        emptytextcolor1 = Importfunc.invert_color(emptycolor1)
        emptytextcolor2 = Importfunc.invert_color(emptycolor2)

        WPtextcolor = Importfunc.invert_color(WPcolor)
        WRtextcolor = Importfunc.invert_color(WRcolor)
        WHtextcolor = Importfunc.invert_color(WHcolor)
        WBtextcolor = Importfunc.invert_color(WBcolor)
        WQtextcolor = Importfunc.invert_color(WQcolor)
        WKtextcolor = Importfunc.invert_color(WKcolor)

        BPtextcolor = Importfunc.invert_color(BPcolor)
        BRtextcolor = Importfunc.invert_color(BRcolor)
        BHtextcolor = Importfunc.invert_color(BHcolor)
        BBtextcolor = Importfunc.invert_color(BBcolor)
        BQtextcolor = Importfunc.invert_color(BQcolor)
        BKtextcolor = Importfunc.invert_color(BKcolor)

        Buttontextcolor = Importfunc.invert_color(buttonscolor)
        draw_board()
    def rollcolor3():
        global emptycolor1, WRtextcolor, WHtextcolor, WBtextcolor, WRcolor, WHcolor, WBcolor, WKcolor, BRcolor, BHcolor, BBcolor, BKcolor, BHtextcolor, BBtextcolor, BKtextcolor, WKtextcolor, BRtextcolor, emptycolor2, WPcolor, WQcolor, BQcolor, BPcolor, buttonscolor, emptytextcolor1, emptytextcolor2, WPtextcolor, WQtextcolor, BPtextcolor, BQtextcolor, Buttontextcolor
        emptycolor1 = "#{:06x}".format(random.randint(0, 0xFFFFFF))
        emptycolor2 ="#{:06x}".format(random.randint(0, 0xFFFFFF))
        WPcolor = "#{:06x}".format(random.randint(0, 0xFFFFFF))
        WRcolor = "#{:06x}".format(random.randint(0, 0xFFFFFF))
        WHcolor = "#{:06x}".format(random.randint(0, 0xFFFFFF))
        WBcolor = "#{:06x}".format(random.randint(0, 0xFFFFFF))
        WQcolor = "#{:06x}".format(random.randint(0, 0xFFFFFF))
        WKcolor = "#{:06x}".format(random.randint(0, 0xFFFFFF))

        BPcolor = "#{:06x}".format(random.randint(0, 0xFFFFFF))
        BRcolor = "#{:06x}".format(random.randint(0, 0xFFFFFF))
        BHcolor = "#{:06x}".format(random.randint(0, 0xFFFFFF))
        BBcolor = "#{:06x}".format(random.randint(0, 0xFFFFFF))
        BQcolor = "#{:06x}".format(random.randint(0, 0xFFFFFF))
        BKcolor = "#{:06x}".format(random.randint(0, 0xFFFFFF))
        buttonscolor = "#{:06x}".format(random.randint(0, 0xFFFFFF))

        emptytextcolor1 = Importfunc.invert_color(emptycolor1)
        emptytextcolor2 = Importfunc.invert_color(emptycolor2)

        '''WPtextcolor = Importfunc.invert_color(WPcolor)
        WRtextcolor = Importfunc.invert_color(WRcolor)
        WHtextcolor = Importfunc.invert_color(WHcolor)
        WBtextcolor = Importfunc.invert_color(WBcolor)
        WQtextcolor = Importfunc.invert_color(WQcolor)
        WKtextcolor = Importfunc.invert_color(WKcolor)

        BPtextcolor = Importfunc.invert_color(BPcolor)
        BRtextcolor = Importfunc.invert_color(BRcolor)
        BHtextcolor = Importfunc.invert_color(BHcolor)
        BBtextcolor = Importfunc.invert_color(BBcolor)
        BQtextcolor = Importfunc.invert_color(BQcolor)
        BKtextcolor = Importfunc.invert_color(BKcolor)'''

        Buttontextcolor = Importfunc.invert_color(buttonscolor)
        draw_board2()
    def colorsetter1(event):
        global entry1, entry2, entry3, entry4, entry5, entry6, entry7, entry8, entry9, entry10, entry11, entry12, entry13, entry14, entry15, emptycolor1, WRtextcolor, WHtextcolor, WBtextcolor, WRcolor, WHcolor, WBcolor, WKcolor, BRcolor, BHcolor, BBcolor, BKcolor, BHtextcolor, BBtextcolor, BKtextcolor, WKtextcolor, BRtextcolor, emptycolor2, WPcolor, WQcolor, BQcolor, BPcolor, buttonscolor, emptytextcolor1, emptytextcolor2, WPtextcolor, WQtextcolor, BPtextcolor, BQtextcolor, Buttontextcolor
        value = [entry1.get(),entry2.get(),entry3.get(),entry4.get(),entry5.get(),entry6.get(),entry7.get(),entry8.get(),entry9.get(),entry10.get(),entry11.get(),entry12.get(),entry13.get(),entry14.get(),entry15.get()]
        for entry in range(len(value)):
            hexdec = False
            colored = value[entry].strip("#")
            if len(colored) == 6:
                try:
                    int(colored, 16)
                    hexdec = True
                except ValueError:
                    x2 =1
            if len(value[entry]) == 6:
                value[entry] = "#" + value[entry]
            if entry == 0 and hexdec == True:
                emptycolor1 = value[0]
                emptytextcolor1 = Importfunc.invert_color(emptycolor1)
            elif entry == 1 and hexdec == True:
                emptycolor2 = value[1]
                emptytextcolor2 = Importfunc.invert_color(emptycolor2)
            elif entry == 2 and hexdec == True:
                buttonscolor = value[2]
                Buttontextcolor = Importfunc.invert_color(buttonscolor)
            elif entry == 3 and hexdec == True:
                WPcolor = value[3]
                WPtextcolor = Importfunc.invert_color(WPcolor)
            elif entry == 4 and hexdec == True:
                WRcolor = value[4]
                WRtextcolor = Importfunc.invert_color(WRcolor)
            elif entry == 5 and hexdec == True:
                WHcolor = value[5]
                WHtextcolor = Importfunc.invert_color(WHcolor)
            elif entry == 6 and hexdec == True:
                WBcolor = value[6]
                WBtextcolor = Importfunc.invert_color(WBcolor)
            elif entry == 7 and hexdec == True:
                WQcolor = value[7]
                WQtextcolor = Importfunc.invert_color(WQcolor)
            elif entry == 8 and hexdec == True:
                WKcolor = value[8]
                WKtextcolor = Importfunc.invert_color(WKcolor)

            elif entry == 9 and hexdec == True:
                BPcolor = value[9]
                BPtextcolor = Importfunc.invert_color(BPcolor)
            elif entry == 10 and hexdec == True:
                BRcolor = value[10]
                BRtextcolor = Importfunc.invert_color(BRcolor)
            elif entry == 11 and hexdec == True:
                BHcolor = value[11]
                BHtextcolor = Importfunc.invert_color(BHcolor)
            elif entry == 12 and hexdec == True:
                BBcolor = value[12]
                BBtextcolor = Importfunc.invert_color(BBcolor)
            elif entry == 13 and hexdec == True:
                BQcolor = value[13]
                BQtextcolor = Importfunc.invert_color(BQcolor)
            elif entry == 14 and hexdec == True:
                BKcolor = value[14]
                BKtextcolor = Importfunc.invert_color(BKcolor)
        draw_board()
    def colorsetter2(event):
        global entry1, entry2, entry3, entry4, entry5, entry6, entry7, entry8, entry9, entry10, entry11, entry12, entry13, entry14, entry15, emptycolor1, WRtextcolor, WHtextcolor, WBtextcolor, WRcolor, WHcolor, WBcolor, WKcolor, BRcolor, BHcolor, BBcolor, BKcolor, BHtextcolor, BBtextcolor, BKtextcolor, WKtextcolor, BRtextcolor, emptycolor2, WPcolor, WQcolor, BQcolor, BPcolor, buttonscolor, emptytextcolor1, emptytextcolor2, WPtextcolor, WQtextcolor, BPtextcolor, BQtextcolor, Buttontextcolor
        value = [entry1.get(),entry2.get(),entry3.get(),entry4.get(),entry5.get(),entry6.get(),entry7.get(),entry8.get(),entry9.get(),entry10.get(),entry11.get(),entry12.get(),entry13.get(),entry14.get(),entry15.get()]
        for entry in range(len(value)):
            hexdec = False
            colored = value[entry].strip("#")
            if len(colored) == 6:
                try:
                    int(colored, 16)
                    hexdec = True
                except ValueError:
                    x2 =1
            if len(value[entry]) == 6:
                value[entry] = "#" + value[entry]
            if entry == 0 and hexdec == True:
                emptycolor1 = value[0]
                emptytextcolor1 = Importfunc.invert_color(emptycolor1)
            elif entry == 1 and hexdec == True:
                emptycolor2 = value[1]
                emptytextcolor2 = Importfunc.invert_color(emptycolor2)
            elif entry == 2 and hexdec == True:
                buttonscolor = value[2]
                Buttontextcolor = Importfunc.invert_color(buttonscolor)
            elif entry == 3 and hexdec == True:
                WPcolor = value[3]
                WPtextcolor = Importfunc.invert_color(WPcolor)
            elif entry == 4 and hexdec == True:
                WRcolor = value[4]
                WRtextcolor = Importfunc.invert_color(WRcolor)
            elif entry == 5 and hexdec == True:
                WHcolor = value[5]
                WHtextcolor = Importfunc.invert_color(WHcolor)
            elif entry == 6 and hexdec == True:
                WBcolor = value[6]
                WBtextcolor = Importfunc.invert_color(WBcolor)
            elif entry == 7 and hexdec == True:
                WQcolor = value[7]
                WQtextcolor = Importfunc.invert_color(WQcolor)
            elif entry == 8 and hexdec == True:
                WKcolor = value[8]
                WKtextcolor = Importfunc.invert_color(WKcolor)

            elif entry == 9 and hexdec == True:
                BPcolor = value[9]
                BPtextcolor = Importfunc.invert_color(BPcolor)
            elif entry == 10 and hexdec == True:
                BRcolor = value[10]
                BRtextcolor = Importfunc.invert_color(BRcolor)
            elif entry == 11 and hexdec == True:
                BHcolor = value[11]
                BHtextcolor = Importfunc.invert_color(BHcolor)
            elif entry == 12 and hexdec == True:
                BBcolor = value[12]
                BBtextcolor = Importfunc.invert_color(BBcolor)
            elif entry == 13 and hexdec == True:
                BQcolor = value[13]
                BQtextcolor = Importfunc.invert_color(BQcolor)
            elif entry == 14 and hexdec == True:
                BKcolor = value[14]
                BKtextcolor = Importfunc.invert_color(BKcolor)
        draw_board2()
    def evolver(evolve):
        global boardx, game_board, evolveer2
        for space in range(boardx+1):
            if game_board[1][space] == "WE":
                if evolve == "Q":
                    game_board[1][space] = "WQ"
                elif evolve == "H":
                    game_board[1][space] = "WH"
                elif evolve == "R":
                    game_board[1][space] = "WR"
                elif evolve == "B":
                    game_board[1][space] = "WB"
            elif game_board[boardx][space] == "BE":
                if evolve == "Q":
                    game_board[boardx][space] = "BQ"
                elif evolve == "H":
                    game_board[boardx][space] = "BH"
                elif evolve == "R":
                    game_board[boardx][space] = "BR"
                elif evolve == "B":
                    game_board[boardx][space] = "BB"
        evolveer2.set(True)

while gamer_state == True:
    board()
    while game_state == True:
        brp = '--'
        check_check()

        for row in game_board:
            for peice in row:
                if peice == 'BK':
                    bpeices += 1
                if peice == 'WK':
                    wpeices += 1
        if bpeices == 0 or wpeices == 0:
            game_end = True
            extraturn = 0
        if game_end == True or Stalemate == True or Checkmate == True:
            end_draw_board()
            game_state = False
            extraturn = 0
        if game_state == True:
            try:
                draw_board()
                root.wait_variable(donesetter)

                move = [int(move[0]),int(move[1])]
                to = [int(to[0]),int(to[1])]
                if move[0] > boardx or to[0] > boardx or move[1] > boardx or to[1] > boardx:
                    brp = '0'
                    move = [0,0]
                    to = [0,0]
                    fail += 1
            except:
                fail += 1
                brp = '0'
                move = [0,0]
                to = [0,0]


            if skip == False and done == False: ###################################
                row = game_board[move[0]]
                rowt = game_board[to[0]]
                peice = row[move[1]]
                peicet = rowt[to[1]]
                Kpos = check_king()
                

                if peice in ("BQ", "WQ"):
                    queenmovement()
                elif peice in ("BR", "WR"):
                    rookmovement()
                elif peice in ("BB", "WB"):
                    bishopmovement()
                elif peice in ("BP", "WP"):
                    pawnmovement()
                elif peice in ("BH", "WH"):
                    if abs(move[0]-to[0]) in (1,2) and abs(move[1]-to[1]) in (1,2) and abs(move[0]-to[0]) != abs(move[1]-to[1]):
                        success = True
                    else:
                        success = False
                elif peice in ("BK","WK"):
                    if abs(move[0]-to[0]) in (0,1) and abs(move[1]-to[1]) in (0,1):
                        direction = 0
                        if peice == "BK":
                            for vertical in range(-1,2):
                                for horizontal in range(-1,2):
                                    if move[0] + vertical == to[0] and move[1] + horizontal == to[1]:
                                        if BKcheck[direction] == True:
                                            success = True
                                    direction += 1
                        elif peice == "WK":
                            for vertical in range(-1,2):
                                for horizontal in range(-1,2):
                                    if move[0] + vertical == to[0] and move[1] + horizontal == to[1]:
                                        if WKcheck[direction] == True:
                                            success = True
                                    direction +=1
                    else:
                        success = False
                else:
                    success = False

                if success == False:
                    move = [0,0]
                    to = [0,0]
                    fail += 1
                            
                '''if turn == 'Black' ane and not move[0] == to[0]-1:
                    move = [0,0]
                    to = [0,0]
                    fail += 1
                if turn == 'White' ande and not move[0] == to[0]+1:
                    move = [0,0]
                    to = [0,0]
                    fail += 1'''

                movement()

            if done == True or game_end == True:
                end_draw_board()
                game_state = False
                extraturn = 0

            if evolveer1 == True:
                evolve_board()
                root.wait_variable(evolveer2)


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

            if tfailW > 3 or tfailB > 3:
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
            movevalid = False
            skip = False
            fail = 0
            peices = 0
            wpeices = 0
            bpeices = 0
            tosetter = False
            success = False
            WCheck = False
            BCheck = False
            evolveer1 = BooleanVar(value=False)
            evolveer2 = BooleanVar(value=False)
            donesetter = BooleanVar(value=False)


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
        debugon = False
        debugad = 0
        BKcheck = [True, True, True, True, True, True, True, True, True]
        WKcheck = [True, True, True, True, True, True, True, True, True]
        Bok = [False, False, False, False, False, False, False, False, False]
        Wok = [False, False, False, False, False, False, False, False, False]
        turn1 = True
        enpasantb = []
        enpasantw = []
        Stalemate = False
        WCheck = False
        BCheck = False
        Checkmate = False
        lbl5.configure(text = f"No winner")
        lbl7.configure(text = f"Mateless")
        ##print('3 failed movements skips your turn. 3 skips in a row = loss')
    else:
        gamer_state = False
        ##print('game end')
        root.destroy()
root.mainloop()