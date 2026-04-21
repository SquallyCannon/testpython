import sys
a = 1
sys.set_int_max_str_digits(500000)
def fractional():
    for n in range(100):
        print(a/(a+1))
        a += 1
for b in range(100):
    print(f'{b+1}:', int(((a+(a/2))*(a/3))**(a/4)))
    a += 1
'''10,20,25,40,50,80,100'''
'''1'''
'''2,4,8,16,32,64'''
'''5'''