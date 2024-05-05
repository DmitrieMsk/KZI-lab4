# laba 4 вариант 17
# p = 173
#Я НАШЕЛ число D: = 5087

#Я нашел число e: = 50879
# q = 313
import random
import math
import re
ABC = 'абвгдежзийклмнопрстуфхцчшщъыьэюя '

p = 173
q = 313
n = p * q
d = 5087
e = 50879
def main():
    print('start program')
    print('инициализация переменных')
    print('n =', n)
    print('p =', p)
    print('q =', q)
    #message = input('Enter a message: ')
    message = 'привет мир кукуха едет'
    print('Ваше сообщение:',message)
    Fi = funcOfEuler(n)
    print('Fi = ', Fi)
    #d = choice_Num_D(n, Fi)
    #e = choice_num_e(d, Fi)
    open_key = [e, n]
    closed_key = [d, n]
    print('пара чисел открытый ключ = ', open_key)
    print('пара чисел закрытый ключ = ', closed_key)
    message_in_Codes = abc_in_code(ABC, message)
    print('шифр Строка =', message_in_Codes)
    str_message_Codes = fromIntToStr(message_in_Codes)
    print('перевожу из интов в строку', fromIntToStr(message_in_Codes))
    message_code_in_block = splitting_into_block(n, str_message_Codes)
    print('разбили сообщение на блоки = ', message_code_in_block)

    int_message_code_in_block = fromSrtToInt(message_code_in_block) #по идее можно отправлять на шифрование
    print('можно отправлять на шифрование = ', int_message_code_in_block)
    #encrypt_func(int_message_code_in_block, e, n)
    shtext = give_shtext()
    decrypt_func(shtext, d, n, ABC)



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

def deleteLishnee(strstr):
    strstr = str(strstr)
    strstr = strstr.replace('[', '')
    strstr = strstr.replace(']', '')
    strstr = strstr.replace(',', '')
    strstr = strstr.replace("'", '')

    return strstr


def fromSrtToInt(big_str):
    print('пришло такое = ', big_str)
    i = 0
    big_int = []
    while i < len(big_str):
        big_int.append(int(big_str[i]))
        i = i + 1

    print('массив интов = ',big_int)
    return big_int

def splitting_into_block(n, message_in_codes):
    print('начинаю разбивать на блоки')
    n_to_str = str(n)
    digits = len(n_to_str)
    print('длина модуля шифрования (разрядность) = ', digits)
    digits_block = digits - 1
    print('разрядность блока = ',digits_block)
    lenMessageCode = len(message_in_codes)
    numOfBlock = lenMessageCode // digits_block
    print('столько будет блоков = ',numOfBlock)
    i = 0
    results_blocks = re.findall('(.{%s}|.+$)' % digits_block, message_in_codes) #бью на блоки
    print('пробую бить', results_blocks)
    return results_blocks


def encrypt_func(source_code, e ,n):
    print('начинаю зашифровывать')
    print('source_code =', source_code)

    i = 0
    shtext = []
    print(len(source_code))
    while i < len(source_code):
        stepen = source_code[i]**e

        shtext.append(stepen%n)
        i = i + 1

    print('шифр текст = ',shtext)
    with open("bufer.txt", "w") as f:
        f.write(str(shtext))

def give_shtext():
    with open('bufer.txt', 'r') as f:
        shtext = f.read()
        print('считал шифротекст из файла', shtext)
        return shtext

#def code_To_ABC():

def decrypt_func(shtext, d, n, ABC):
    i = 0

    lenqqq = len(shtext)
    print('длина считанного ',shtext)
    shtext = shtext.replace('[', '')
    shtext = shtext.replace(']', '')
    shtext = shtext.replace(' ', '')
    print('длина считанного ', shtext)

    shtext = shtext.split(',')
    int_shtext = fromSrtToInt(shtext)
    print('длина считанного ', shtext)
    print('длина считанного INTOVOGO ', int_shtext)
    open_text = []
    i = 0
    print('длина шифрованных интов = ', len(int_shtext))
    while i<len(int_shtext):
        open_text.append(((int_shtext[i])**d)%n)
        i = i + 1
    print('коды открытого текста = ', open_text)
    openArraytext = fromIntToStr(open_text)
    print('open array = ', openArraytext)
    openArraytext = re.findall('(.{%s}|.+$)' % 2, openArraytext)
    print('open = ', openArraytext)
    from_array = fromSrtToInt(openArraytext)
    print('from = ', type(from_array))
    openOpenOpentext = []
    i = 0
    while(i<len(from_array)):

        if from_array[i] == 99:
            openOpenOpentext.append(' ')
            i = i + 1
        else:
            openOpenOpentext.append(ABC[from_array[i] - 10])
            i = i + 1
    clear = deleteLishnee(openOpenOpentext)
    clear = deleteLishnee(openOpenOpentext)
    print('openOpenOpentext = ', clear)






main()