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

#print(calculate_scorem(5000*(2**200)))
#print(2*76)


#print(round_half_up(random.randint(1000000, 10000000), -7))
#print(int(100000 * 0.00001 + 0.5) / 0.00001)

#a = float(3.6)
#n = int(round_half_up(a))
#print(round_half_up(1.3), n)

#num1 = int(input('num1:'))
#num2 = int(input('num2:'))

#rint(tetration(num1,num2))
#print(tetration(6, 3))