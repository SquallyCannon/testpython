import sys
import math
import mpmath as mp

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
print(tetration(100000,1.999))