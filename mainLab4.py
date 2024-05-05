# laba 4 вариант 17
# p = 173
# q = 313
import random
import math

p = 173
q = 313
n = p * q
def main():
    print('start program')
    print('инициализация переменных')
    print('n =', n)
    print('p =', p)
    print('q =', q)
    #message = input('Enter a message: ')
    message = 'Привет мир'
    print('Ваше сообщение:',message)
    Fi = funcOfEuler(n)
    print('Fi = ', Fi)
    d = choice_Num_D(n, Fi)
    e = choice_num_e(d, Fi)
    open_key = [e, n]
    closed_key = [d, n]
    print('пара чисел открытый ключ = ', open_key)
    print('пара чисел закрытый ключ = ', closed_key)

def funcOfEuler(n):
    print('вычисление функции эйлера')
    Fn = (p-1)*(q-1)
    return Fn
def choice_Num_D(n, Fi):
    print('выбираю число d')
    flag = True
    while flag:
        d = random.randint(1000,10000)
        if math.gcd(d,Fi) == 1:
            flag = False
            print('Я НАШЕЛ число D: =', d)
    return d

def choice_num_e(d, Fi):

    print('старт функции поиска числа e')
    flag = True
    e = 1
    while flag:
        if ((e*d) % Fi) == 1:
            flag = False
            print('Я нашел число e: =', e)
        else:
            e = e + 1
    return e





main()