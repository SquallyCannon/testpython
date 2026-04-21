import random
import math
import Importfunc


def calculate():
    calc = True
    valid1 = 0
    valid2 = 0
    valid3 = 0
    number1 = float(input('Enter your first number: '))
    if number1%1 == 0:
        number1 = float(number1)
    while calc == True:
        sign = input('Enter your operation symbol or c the calculator: ')
        while valid1 == 0:
            if sign == '+' or sign == '-' or sign == '*' or sign == '/' or sign == '^' or sign == '_/' or sign == '^^':
                valid1 = 1
            elif sign == 'c':
                number1 = float(input('Enter your first number: '))
                if number1%1 == 0:
                    number1 = int(number1)
                sign = input('Enter your operation symbol or c the calculator: ')
            else:
                sign = input('Enter your operation symbol or c the calculator: ')
        valid1 = 0
        number2 = float(input('Enter your second number: '))
        whole2 = number2%1
        if whole2 == 0:
            number2 = int(number2)
        if sign == '+':
            print(number1, "+", number2, "=", number1 + number2)
            number1 = number1 + number2
        elif sign == '-':
            print(number1, "-", number2, "=", number1 - number2)
            number1 = number1 - number2
        elif sign == '*':
            print(number1, "*", number2, "=", number1 * number2)
            number1 = number1 * number2
        elif sign == '/':
            print(number1, "/", number2, "=", number1 / number2)
            number1 = number1 / number2
        elif sign == '^':
            print(number1, "^", number2, "=", number1 ** number2)
            number1 = number1 ** number2
        elif sign == '_/':
            print(number1, "_/", number2, "=", Importfunc.root(number1, number2))
            number1 = Importfunc.root(number1, number2)
        elif sign == '^^':
            print(number1, "^^", number2, "=", Importfunc.tetration(number1, number2))
            number1 = Importfunc.tetration(number1, number2)
        else:
            calc = False

def randomcalc():
    calc = True
    valid1 = 0
    valid2 = 0
    valid3 = 0
    number1 = float(random.randint(1,100))
    print(f'Enter your first number: {number1}')
    whole1 = number1%1
    if whole1 == 0:
        number1 = int(number1)
    while calc == True:
        sign = Importfunc.randsign()
        print(f'Enter your operation symbol or c the calculator: {sign}')
        valid1 = 0
        number2 = float(random.randint(1, 100))
        print(f'Enter your second number: {number2}')
        whole2 = number2%1
        if whole2 == 0:
            number2 = int(number2)
        if sign == '+':
            print(number1, "+", number2, "=", number1 + number2)
            number1 = number1 + number2
        elif sign == '-':
            print(number1, "-", number2, "=", number1 - number2)
            number1 = number1 - number2
        elif sign == '*':
            print(number1, "*", number2, "=", number1 * number2)
            number1 = number1 * number2
        elif sign == '/':
            print(number1, "/", number2, "=", number1 / number2)
            number1 = number1 / number2
        elif sign == '^':
            print(number1, "^", number2, "=", number1 ** number2)
            number1 = number1 ** number2
        elif sign == '_/':
            print(number1, "_/", number2, "=", Importfunc.root(number1, number2))
            number1 = Importfunc.root(number1, number2)
        elif sign == '^^':
            print(number1, "^^", number2, "=", Importfunc.tetration(number1, number2))
            number1 = Importfunc.tetration(number1, number2)
        else:
            calc = False
        endcalc = input('continue?(y/n):')
        if endcalc == 'y':
            calc = False

print(calculate())
#print(randomcalc())
