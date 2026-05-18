import time
import math
import tkinter as tk
from tkinter import *
root = Tk()
root.geometry(f'{650}x{350}')
root.title('Timer')

boot = time.perf_counter()
Tickspeed = 1 #60*60*24
offset = 0
pauseoffset = 0
addtime = 0
multime = 1
Tp = 0
Ts = 0
Tm = 0
Th = 0
Td = 0
Ty = 0
TD = 0
TC = 0
TM = 0
Rs = 0
Rm = 0
Rm2 = 0
Rh = 0
Rh2 = 0
Rd = 0
Rd1 = 0
Rd2 = 0
Rd3 = 0
Ry = 0
RD = 0
RC = 0
RM = 0
endcorrect = True
pause = False

lbl = Label(root, text = f"{int(RM)}{int(RC)}{int(RD)}{int(Ry)}  {Rd3}{Rd2}{Rd1}  {Rh2}{Rh}:{Rm2}{Rm}:{Rs}", padx=10, pady= 10, font=("Impact",30))
lbl.grid(row=1, column=0, columnspan= 7)

def draw():
    if pause == False:
        lbl.configure(text = f"{int(RM)}{int(RC)}{int(RD)}{int(Ry)}  {Rd3}{Rd2}{Rd1}  {Rh2}{Rh}:{Rm2}{Rm}:{Rs}")

def reset():
    global multime, timer
    multime -= timer
    print('time reset')
def pauses():
    global pause
    if pause:
        pause = False
    else:
        pause = True


addition = True
if addition:
    def ad1s():
        global addtime
        addtime +=1
        print('+1')
    def ad10s():
        global addtime
        addtime +=10
        print('+10')
    def ad1m():
        global addtime
        addtime +=60
        print('+60')
    def ad10m():
        global addtime
        addtime +=600
        print('+600')
    def ad1h():
        global addtime
        addtime +=3600
        print('+3600')
    def ad10h():
        global addtime
        addtime +=36000
        print('+36000')
    def ad1d():
        global addtime
        addtime +=86400
        print('+86400')
    def ad10d():
        global addtime
        addtime +=864000
        print('+864000')
    def ad100d():
        global addtime
        addtime +=8640000
        print('+8640000')
    def ad1y():
        global addtime
        addtime +=31556952
        print('+31556952')
    def ad1D():
        global addtime
        addtime +=315569520
        print('+315569520')
    def ad1C():
        global addtime
        addtime +=3155695200
        print('+3155695200')
    def ad1M():
        global addtime
        addtime +=31556952000
        print('+31556952000')
    def ad10M():
        global addtime
        addtime +=315569520000
        print('+315569520000')
    def ad100M():
        global addtime
        addtime +=3155695200000
        print('+3155695200000')

multiply = True
if multiply:
    def mult2():
        global multime, timer
        multime += timer
        print('x2')
    def mult10():
        global multime, timer
        multime += timer*9
        print('x10')
    def mult100():
        global multime, timer
        multime += timer *99
        print('x100')
    def mult1k():
        global multime, timer
        multime +=timer *999
        print('x1000')
    def mult1m():
        global multime, timer
        multime +=timer *999999
        print('x1000000')
    def mult1b():
        global multime, timer
        multime +=timer *999999999
        print('x1000000000')
    def mult1t():
        global multime, timer
        multime +=timer *999999999999
        print('x1000000000000')

subtract = True
if subtract:
    def sub1s():
        global addtime, timer
        if timer < 1:
            addtime -= timer
        else:
            addtime -=1
        print('-1')
    def sub10s():
        global addtime, timer
        if timer < 10:
            addtime -= timer
        else:
            addtime -=10
        print('-10')
    def sub1m():
        global addtime, timer
        if timer < 60:
            addtime -= timer
        else:
            addtime -=60
        print('-60')
    def sub10m():
        global addtime, timer
        if timer < 600:
            addtime -= timer
        else:
            addtime -=600
        print('-600')
    def sub1h():
        global addtime, timer
        if timer < 3600:
            addtime -= timer
        else:
            addtime -=3600
        print('-3600')
    def sub10h():
        global addtime, timer
        if timer < 36000:
            addtime -= timer
        else:
            addtime -=36000
        print('-36000')
    def sub1d():
        global addtime, timer
        if timer < 86400:
            addtime -= timer
        else:
            addtime -=86400
        print('-86400')
    def sub10d():
        global addtime, timer
        if timer < 864000:
            addtime -= timer
        else:
            addtime -=864000
        print('-864000')
    def sub100d():
        global addtime, timer
        if timer < 8640000:
            addtime -= timer
        else:
            addtime -=8640000
        print('-8640000')
    def sub1y():
        global addtime, timer
        if timer < 31556952:
            addtime -= timer
        else:
            addtime -=31556952
        print('-31556952')
    def sub1D():
        global addtime, timer
        if timer < 315569520:
            addtime -= timer
        else:
            addtime -=315569520
        print('-315569520')
    def sub1C():
        global addtime, timer
        if timer < 3155695200:
            addtime -= timer
        else:
            addtime -=3155695200
        print('-3155695200')
    def sub1M():
        global addtime, timer
        if timer < 31556952000:
            addtime -= timer
        else:
            addtime -=31556952000
        print('-31556952000')
    def sub10M():
        global addtime, timer
        if timer < 315569520000:
            addtime -= timer
        else:
            addtime -=315569520000
        print('-315569520000')
    def sub100M():
        global addtime, timer
        if timer < 3155695200000:
            addtime -= timer
        else:
            addtime -=3155695200000
        print('-3155695200000')
    
    
    
    
divide = True
if divide:
    def div2():
        global multime, timer
        multime -= timer/2
        print('/2')
    def div10():
        global multime, timer
        multime -= timer/(10/9)
        print('/10')
    def div100():
        global multime, timer
        multime -= timer/(100/99)
        print('/100')
    def div1k():
        global multime, timer
        multime -= timer/(1000/999)
        print('/1000')
    def div1m():
        global multime, timer
        multime -= timer/(1000000/999999)
        print('/1000000')
    def div1b():
        global multime, timer
        multime -= timer/(1000000000/999999999)
        print('/1000000000')
    def div1t():
        global multime, timer
        multime -= timer/(1000000000000/999999999999)
        print('/1000000000000')
    

buttons = True
if buttons:
    Button(
        root, text='Reset', width=9,
        command=lambda: reset()
        ).grid(row = 4, column=0, padx=10, pady=5)
    Button(
        root, text='Pause', width=9,
        command=lambda: pauses()
        ).grid(row = 5, column=0, padx=10, pady=5)

    Button(
        root, text='Add 1s', width=9,
        command=lambda: ad1s(),
        ).grid(row = 2, column=0, padx=10, pady=5)
    Button(
        root, text='Add 10s', width=9,
        command=lambda: ad10s()
        ).grid(row = 2, column=1, padx=10, pady=5)
    Button(
        root, text='Add 1m', width=9,
        command=lambda: ad1m()
        ).grid(row = 2, column=2, padx=10, pady=5)
    Button(
        root, text='Add 10m', width=9,
        command=lambda: ad10m()
        ).grid(row = 2, column=3, padx=10, pady=5)
    Button(
        root, text='Add 1h', width=9,
        command=lambda: ad1h()
        ).grid(row = 2, column=4, padx=10, pady=5)
    Button(
        root, text='Add 10h', width=9,
        command=lambda: ad10h()
        ).grid(row = 2, column=5, padx=10, pady=5)
    Button(
        root, text='Add 1d', width=9,
        command=lambda: ad1d()
        ).grid(row = 2, column=6, padx=10, pady=5)
    Button(
        root, text='Add 10d', width=9,
        command=lambda: ad10d()
        ).grid(row = 3, column=0, padx=10, pady=5)
    Button(
        root, text='Add 100d', width=9,
        command=lambda: ad100d()
        ).grid(row = 3, column=1, padx=10, pady=5)
    Button(
        root, text='Add 1y', width=9,
        command=lambda: ad1y()
        ).grid(row = 3, column=2, padx=10, pady=5)
    Button(
        root, text='Add 1D', width=9,
        command=lambda: ad1D()
        ).grid(row = 3, column=3, padx=10, pady=5)
    Button(
        root, text='Add 1C', width=9,
        command=lambda: ad1C()
        ).grid(row = 3, column=4, padx=10, pady=5)
    Button(
        root, text='Add 1M', width=9,
        command=lambda: ad1M()
        ).grid(row = 3, column=5, padx=10, pady=5)
    Button(
        root, text='Add 10M', width=9,
        command=lambda: ad10M()
        ).grid(row = 3, column=6, padx=10, pady=5)
    Button(
        root, text='Add 100M', width=9,
        command=lambda: ad100M()
        ).grid(row = 3, column=7, padx=10, pady=5)
    
    Button(
        root, text='x2', width=9,
        command=lambda: mult2()
        ).grid(row = 4, column=1, padx=10, pady=5)
    Button(
        root, text='x10', width=9,
        command=lambda: mult10()
        ).grid(row = 4, column=2, padx=10, pady=5)
    Button(
        root, text='x100', width=9,
        command=lambda: mult100()
        ).grid(row = 4, column=3, padx=10, pady=5)
    Button(
        root, text='x1000', width=9,
        command=lambda: mult1k()
        ).grid(row = 4, column=4, padx=10, pady=5)
    Button(
        root, text='x1000000', width=9,
        command=lambda: mult1m()
        ).grid(row = 4, column=5, padx=10, pady=5)
    Button(
        root, text='x1000000000', width=9,
        command=lambda: mult1b()
        ).grid(row = 4, column=6, padx=10, pady=5)
    Button(
        root, text='x1000000000000', width=9,
        command=lambda: mult1t()
        ).grid(row = 4, column=7, padx=10, pady=5)
    
    Button(
        root, text='/2', width=9,
        command=lambda: div2()
        ).grid(row = 5, column=1, padx=10, pady=5)
    Button(
        root, text='/10', width=9,
        command=lambda: div10()
        ).grid(row = 5, column=2, padx=10, pady=5)
    Button(
        root, text='/100', width=9,
        command=lambda: div100()
        ).grid(row = 5, column=3, padx=10, pady=5)
    Button(
        root, text='/1000', width=9,
        command=lambda: div1k()
        ).grid(row = 5, column=4, padx=10, pady=5)
    Button(
        root, text='/1000000', width=9,
        command=lambda: div1m()
        ).grid(row = 5, column=5, padx=10, pady=5)
    Button(
        root, text='/1000000000', width=9,
        command=lambda: div1b()
        ).grid(row = 5, column=6, padx=10, pady=5)
    Button(
        root, text='/1000000000000', width=9,
        command=lambda: div1t()
        ).grid(row = 5, column=7, padx=10, pady=5)
    
    Button(
        root, text='-1s', width=9,
        command=lambda: sub1s()
        ).grid(row = 6, column=0, padx=10, pady=5)
    Button(
        root, text='-10s', width=9,
        command=lambda: sub10s()
        ).grid(row = 6, column=1, padx=10, pady=5)
    Button(
        root, text='-1m', width=9,
        command=lambda: sub1m()
        ).grid(row = 6, column=2, padx=10, pady=5)
    Button(
        root, text='-10m', width=9,
        command=lambda: sub10m()
        ).grid(row = 6, column=3, padx=10, pady=5)
    Button(
        root, text='-1h', width=9,
        command=lambda: sub1h()
        ).grid(row = 6, column=4, padx=10, pady=5)
    Button(
        root, text='-10h', width=9,
        command=lambda: sub10h()
        ).grid(row = 6, column=5, padx=10, pady=5)
    Button(
        root, text='-1d', width=9,
        command=lambda: sub1d()
        ).grid(row = 6, column=6, padx=10, pady=5)
    Button(
        root, text='-10d', width=9,
        command=lambda: sub10d()
        ).grid(row = 7, column=0, padx=10, pady=5)
    Button(
        root, text='-100d', width=9,
        command=lambda: sub100d()
        ).grid(row = 7, column=1, padx=10, pady=5)
    Button(
        root, text='-1y', width=9,
        command=lambda: sub1y()
        ).grid(row = 7, column=2, padx=10, pady=5)
    Button(
        root, text='-1D', width=9,
        command=lambda: sub1D()
        ).grid(row = 7, column=3, padx=10, pady=5)
    Button(
        root, text='-1C', width=9,
        command=lambda: sub1C()
        ).grid(row = 7, column=4, padx=10, pady=5)
    Button(
        root, text='-1M', width=9,
        command=lambda: sub1M()
        ).grid(row = 7, column=5, padx=10, pady=5)
    Button(
        root, text='-10M', width=9,
        command=lambda: sub10M()
        ).grid(row = 7, column=6, padx=10, pady=5)
    Button(
        root, text='-100M', width=9,
        command=lambda: sub100M()
        ).grid(row = 7, column=7, padx=10, pady=5)
    
    Entry(root)


    


Wt = 10000
Wm = False
Wh = False
Wd = False
Wy = True
WD = False
WC = False
WM = False
WE = False
if Wm:
    Wt = Wt*60
elif Wh:
    Wt = Wt*3600
elif Wd:
    Wt = Wt*86400
elif Wy or WD or WC or WM:
    years_to_add = Wt
    if WD:
        years_to_add *= 10
    elif WC:
        years_to_add *= 100
    elif WM:
        years_to_add *= 1000
    total_days = 0

    for year in range(years_to_add):
        is_leap = (
            (year % 4 == 0 and year % 100 != 0)
            or (year % 400 == 0)
        )

        if is_leap:
            total_days += 366
        else:
            total_days += 365

    Wt = total_days * 86400
elif WE:
    Wt = int(Wt*86400*365.2425*1000000000)
if endcorrect:
    timerT = Wt
    TsT = int(Wt)
    TtT = round(Wt, 2)
    RsT = round(Wt%60,3)
    RmT = (TsT//60)%10
    Rm2T =(TsT//600)%6
    RhT = (TsT//3600)%24%10
    Rh2T = (TsT//3600)%24//10
    remaining_secondsT = TsT
    total_yearsT = 0
    while True:
        current_yearT = total_yearsT
        is_leapT = (
            (current_yearT % 4 == 0 and current_yearT % 100 != 0)
            or (current_yearT % 400 == 0)
        )

        seconds_in_yearT = (366 if is_leapT else 365) * 86400

        if remaining_secondsT >= seconds_in_yearT:
            remaining_secondsT -= seconds_in_yearT
            total_yearsT += 1
        else:
            break
    RdT = remaining_secondsT//86400
    Rd1T = RdT % 10
    Rd2T = (RdT // 10) % 10
    Rd3T = RdT // 100
    RyT = total_yearsT % 10
    RDT = (total_yearsT // 10) % 10
    RCT = (total_yearsT // 100) % 10
    RMT = total_yearsT // 1000

lbl2 = Label(root, text = f"{int(RMT)}{int(RCT)}{int(RDT)}{int(RyT)}  {Rd3T}{Rd2T}{Rd1T}  {Rh2T}{RhT}:{Rm2T}{RmT}:{RsT}", padx=10, pady= 10, font=("Impact",30))
lbl2.grid(row=8, column=0, columnspan= 7)

while Ts < Wt:
    if pause:
        pauseoffset = timer-1
    timer = (round(time.perf_counter() - boot + offset + addtime + multime, 2)*Tickspeed)-pauseoffset
    
    
    Ts = int(timer)
    Tt = round(timer, 2)
    Rs = round(timer%60,3)
    Rm = (Ts//60)%10
    Rm2 =(Ts//600)%6
    Rh = (Ts//3600)%24%10
    Rh2 = (Ts//3600)%24//10

    remaining_seconds = Ts
    total_years = 0

    while True:
        current_year = total_years
        is_leap = (
            (current_year % 4 == 0 and current_year % 100 != 0)
            or (current_year % 400 == 0)
        )

        seconds_in_year = (366 if is_leap else 365) * 86400

        if remaining_seconds >= seconds_in_year:
            remaining_seconds -= seconds_in_year
            total_years += 1
        else:
            break
    

    Rd = remaining_seconds//86400
    Rd1 = Rd % 10
    Rd2 = (Rd // 10) % 10
    Rd3 = Rd // 100
    Ry = total_years % 10
    RD = (total_years // 10) % 10
    RC = (total_years // 100) % 10
    RM = total_years // 1000
    if Tt > Tp:
        try:
            draw()
            root.update()
        except TclError:
            break
        Tp = timer
    else:
        Tp = timer
try:
    if endcorrect:
        timer = Wt
        Ts = int(Wt)
        Tt = round(Wt, 2)
        Rs = round(Wt%60,3)
        Rm = (Ts//60)%10
        Rm2 =(Ts//600)%6
        Rh = (Ts//3600)%24%10
        Rh2 = (Ts//3600)%24//10
        remaining_seconds = Ts
        total_years = 0
        while True:
            current_year = total_years
            is_leap = (
                (current_year % 4 == 0 and current_year % 100 != 0)
                or (current_year % 400 == 0)
            )

            seconds_in_year = (366 if is_leap else 365) * 86400

            if remaining_seconds >= seconds_in_year:
                remaining_seconds -= seconds_in_year
                total_years += 1
            else:
                break
        Rd = remaining_seconds//86400
        Rd1 = Rd % 10
        Rd2 = (Rd // 10) % 10
        Rd3 = Rd // 100
        Ry = total_years % 10
        RD = (total_years // 10) % 10
        RC = (total_years // 100) % 10
        RM = total_years // 1000
        draw()
        root.update
except TclError:
    x=1

#time.sleep(10)
#root.destroy
root.mainloop()