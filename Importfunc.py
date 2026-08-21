import random
import math
import sys
import mpmath as mp
rankmax = 30
sign = '+'
scorem = 0
def redux(number):
    print(f'Reduxag {number}')
player1 = {
    "User": "Player1",
    "Rank": 20,
    "minrandom": 20.
}

def total_score():
    scoreb = 1000
    rankm = 10
    ranm = 10
    Lossm = 1
    scorem = 10
    total_score = math.ceil(scoreb*rankm*ranm*Lossm*scorem)
    return total_score

def root(b, r):
    return b ** (1/r)



def tetration1(a, n):
    sys.set_int_max_str_digits(500000)
    result = a
    for _ in range(n - 1):
        result = a ** result
    return result

mp.mp.dps = 10  # decimal places

def tetration2(a, h):
    lower = int(h)
    upper = lower + 1
    
    t_low = tetration1(a, lower)
    t_high = tetration1(a, upper)
    
    frac = h - lower
    
    return mp.e ** (
        mp.log(t_low) + (mp.log(t_high) - mp.log(t_low)) * frac
    )

def tetration(a,n):
    wholen = n%1
    #wholea = a%1
    if n <= 1:
        return a
    elif wholen > 0:
        if a == 1:
            res = 1
        elif a > 1.6617 and n > 6:
            print("this number can not be comuputed using float method(error:lim6)")
            return a
        elif a > 1.7547 and n > 5:
            print("this number can not be comuputed using float method(error:lim5)")
            return a
        elif a > 2 and n > 4:
            print("this number can not be comuputed using float method(error:lim4)")
            return a
        elif a > 2.3726 and n > 3:
            print("this number can not be comuputed using float method(error:lim3)")
            return a
        elif a > 4.2676 and n > 2:
            print("this number can not be comuputed using float method(error:lim2)")
            return a
        elif a > 100000:
            print("this number can not be comuputed using float method(error:baselim)")
            return a
        else:
            try:
                res = tetration2(a,n)
            except:
                print("this number can not be computed comupute using float method (error:general)")
                return a
    else:
        n = int(n)
        a = int(a)
        if a > 6 and n >= 3 or a > 2 and n > 3 or a > 1 and n > 5 or a > 10042 and n > 1:
            print("this number is to high to reasonably comupute")
            return a
        else:
            res = tetration1(a,n)
    return res



def round_half_up(n, decimals=0):
    multiplier = 10 ** decimals
    return int(int(n * multiplier + 0.5) / multiplier)

randsigner = 1
def randsign():
    '+','-','*','/','^','_/','^^'
    randsigner = random.randint(1,7)
    if randsigner == 1:
        sign = '+'
    elif randsigner == 2:
        sign = '-'
    elif randsigner == 3:
        sign = '*'
    elif randsigner == 4:
        sign = '/'
    elif randsigner == 5:
        sign = '^'
    elif randsigner == 6:
        sign = '_/'
    elif randsigner == 7:
        sign = '^^'
    elif randsigner == 8:
        sign = 'c'
    return sign



def calculate_scorem(score):
    scoremr = 5000
    scorems = 0
    scorem = 1
            
    while score >= scoremr:
        scorem = (score / scoremr) + scorems
        scoremr *= 2
        scorems += 1
            
    return scorem

def invert_color(color):
    color = color.lstrip('#')
    inverted = list(255 - int(color[i:i+2], 16) for i in (0, 2, 4))
    return '#{:02x}{:02x}{:02x}'.format(*inverted)

#print(invert_color('#999999'))

digits = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ`~!@#$%^&*()-_=+[{]}|;:,<.>/?'"

def int2(number, base):
    global digits
    if number == 0:
        return "0"
    if base > len(digits):
        raise ValueError(f"Base exceeds available character set length: {len(digits)}")
    
    result = []
    while number > 0:
        number, remainder = divmod(number, base)
        result.append(digits[remainder])
    return "".join(reversed(result))

def str_int2(text, base=92):
    number = 0
    global digits
    for char in text:
        number = number * base + digits.index(char)
    return number


print(int2(str_int2("Hello") + str_int2("20000"), 92))