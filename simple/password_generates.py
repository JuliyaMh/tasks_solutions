import random


def generate_password(length, chars):
    password = ''
    for i in range(length):
        password += random.choice(chars)
    return password


chars = ''
digit_signs = '0123456789'
uppers_signs = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
lowers_signs = 'abcdefghijklmnopqrstuvwxyz'
punctuation_signs = '!#$%&*+-=?@^'

amount = input('Сколько паролей нужно сгенерировать? Введите число (например, 5): ')
while not amount.isdigit():
    amount = input('Кажется, вы ввели данные в неверном формате. Введите число (например, 5): ')
amount = int(amount)

length = input('Какой длины должны быть пароли? Введите количество символов (например, 8): ')
while not length.isdigit():
    length = input('Кажется, вы ввели данные в неверном формате. Введите число (например, 8): ')
length = int(length)

while True:
    digits = input('Может ли пароль содержать цифры? Введите "д", если да, и "н", если нет: ')
    while digits != "д" and digits != "н":
        digits = input('Кажется, вы ввели данные в неверном формате. Введите "д", если да, и "н", если нет: ')
    if digits == 'д':
        chars += digit_signs

    uppers = input('Может ли пароль содержать прописные буквы? Введите "д", если да, и "н", если нет: ')
    while uppers != "д" and uppers != "н":
        uppers = input('Кажется, вы ввели данные в неверном формате. Введите "д", если да, и "н", если нет: ')
    if uppers == 'д':
        chars += uppers_signs

    lowers = input('Может ли пароль содержать строчные буквы? Введите "д", если да, и "н", если нет: ')
    while lowers != "д" and lowers != "н":
        lowers = input('Кажется, вы ввели данные в неверном формате. Введите "д", если да, и "н", если нет: ')
    if lowers == 'д':
        chars += lowers_signs

    punctuation = input('Может ли пароль содержать специальные символы? Введите "д", если да, и "н", если нет: ')
    while punctuation != "д" and punctuation != "н":
        punctuation = input('Кажется, вы ввели данные в неверном формате. Введите "д", если да, и "н", если нет: ')
    if punctuation == 'д':
        chars += punctuation_signs

    if chars:
        break
    else:
        print('Кажется, вы не выбрали ни одного типа символов... Попробуйте еще раз.')

except_signs = input('Нужно ли исключить из пароля неоднозначные символы il1Lo0O? Введите "д", если да, и "н", если нет: ')
while except_signs != "д" and except_signs != "н":
    except_signs = input('Кажется, вы ввели данные в неверном формате. Введите "д", если да, и "н", если нет: ')
if except_signs == 'д':
    for i in 'il1Lo0O':
        chars = chars.replace(i, '')

for _ in range(amount):
    password = generate_password(length, chars)
    print(password)
