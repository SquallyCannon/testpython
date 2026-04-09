import random
import math
import Testmain
valid1 = 0
valid2 = 0
valid3 = 0

def calculate():
    calc = True
    valid1 = 0
    valid2 = 0
    valid3 = 0
    number1 = float(input('Enter your first number: '))
    whole1 = number1%1
    if whole1 == 0:
        number1 = int(number1)
    while calc == True:
        sign = input('Enter your operation symbol or c the calculator: ')
        while valid1 == 0:
            if sign == '+' or sign == '-' or sign == '*' or sign == '/' or sign == '^' or sign == '_/' or sign == '^^':
                valid1 = 1
            elif sign == 'c':
                number1 = float(input('Enter your first number: '))
                whole1 = number1%1
                if whole1 == 0:
                    number1 = int(number1)
                sign = input('Enter your operation symbol or c the calculator: ')
            else:
                sign = input('Enter your operation symbol or c the calculator: ')
        valid1 = 0
        number2 = float(input('Enter your second number: '))
        if sign == '+':
            operator = "+"
            print(number1, "+", number2, "=", number1 + number2)
            number1 = number1 + number2
        elif sign == '-':
            operator = "-"
            print(number1, "-", number2, "=", number1 - number2)
            number1 = number1 - number2
        elif sign == '*':
            operator = "*"
            print(number1, "*", number2, "=", number1 * number2)
            number1 = number1 * number2
        elif sign == '/':
            operator = "/"
            print(number1, "/", number2, "=", number1 / number2)
            number1 = number1 / number2
        elif sign == '^':
            operator = "^"
            print(number1, "^", number2, "=", number1 ** number2)
            number1 = number1 ** number2
        elif sign == '_/':
            operator = "_/"
            print(number1, "_/", number2, "=", Testmain.root(number1, number2))
            number1 = Testmain.root(number1, number2)
        elif sign == '^^':
            operator = "^^"
            print(number1, "^^", number2, "=", Testmain.tetration(number1, number2))
            number1 = Testmain.tetration(number1, number2)
        else:
            calc = False
    

print(calculate())
