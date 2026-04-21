import random
import math
import Importfunc
import testerdot
number1 = float(input('Enter your first number: '))
sign = '+'
number2 = 1

def calculate(number1, number2):
    calc = True
    while calc == True:
        sign = input('Enter your operation symbol: ')
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
            print(number1, "_/", number2, "=", Importfunc.root(number1, number2))
            number1 = Importfunc.root(number1, number2)
        elif sign == '^^':
            operator = "^^"
            if number1 > 6 and number2 >= 3 or number1 > 2 and number2 > 3 or number1 > 1 and number2 > 5 or number1 > 10042 and number2 > 1:
                print("this number is to high to reasonably comupute")
            else:
                print(number1, "^^", number2, "=", testerdot.tetration(number1, number2))
                number1 = testerdot.tetration(number1, number2)
        else:
            calc = False
    
outcome = calculate(number1, number2)
print(outcome)