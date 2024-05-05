# laba 4 вариант 17
# p = 173
# q = 313
import random
import math

ABC = 'абвгдежзийклмнопрстуфхцчшщъыьэюя '

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
    message = 'привет мир'
    print('Ваше сообщение:',message)
    Fi = funcOfEuler(n)
    print('Fi = ', Fi)
    d = choice_Num_D(n, Fi)
    e = choice_num_e(d, Fi)
    open_key = [e, n]
    closed_key = [d, n]
    print('пара чисел открытый ключ = ', open_key)
    print('пара чисел закрытый ключ = ', closed_key)
    message_in_Codes = abc_in_code(ABC, message)
    print('шифр Строка =', message_in_Codes)
    str_message_Codes = fromIntToStr(message_in_Codes)
    print('перевожу из интов в строку', fromIntToStr(message_in_Codes))

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
def abc_in_code(ABC, message):
    print('вывожу кодировки из условия')
    print('длинна алфавита', len(ABC))
    i = 0
    arrayCodes = []
    print('ищу пробел', ABC.find(' '))
    while i < len(message):
        if message[i] == ' ':
            arrayCodes.append(99)
            i = i + 1
        else:
            arrayCodes.append(10 + ABC.find(message[i]))
            i = i + 1
    i = 0
    print('закодированное сообщение = ', arrayCodes)
    return arrayCodes


def fromIntToStr(int_array):
    print('перевожу из массива интов в строку без всего лишнего')
    strDima = str(int_array)
    strDima = strDima.replace(',', '')
    strDima = strDima.replace('[', '')
    strDima = strDima.replace(']', '')
    strDima = strDima.replace(' ', '')
    return strDima


def encrypt_func():
    print('начинаю зашифровывать')





main()