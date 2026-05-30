import random
import math


def is_correct(user_input, ceil_for_check):
    return user_input.isdigit() and 1 <= int(user_input) <= ceil_for_check


def is_correct_ceil(user_input):
    return user_input.isdigit() and int(user_input) > 0


def which_word(num):
    if 11 <= num <= 19:
        return 'попыток'
    if num % 10 == 1:
        return 'попытка'
    if num % 10 in [2, 3, 4]:
        return 'попытки'
    return 'попыток'


continue_game = 'д'
print('Добро пожаловать в игру "Угадайка"! В ней я буду загадывать числа в диапазоне от 0 до выбранного тобой числа'
      ' - а тебе предстоит их угадывать.')

while continue_game == 'д':
    ceil = input('Введи верхнюю границу для выбора числа (цифрами - например, 100). Она должна быть больше 0: ')
    while not is_correct_ceil(ceil):
        print('Кажется, что-то не так... Попробуй снова.')
        ceil = input('Введи верхнюю границу для выбора числа (цифрами - например, 100). Она должна быть больше 0: ')
    ceil = int(ceil)
    n = random.randint(1, ceil)
    print('Я загадал число! Попробуй угадать 😉')
    count = 0
    while True:
        a = input(f'Введи число от 1 до {ceil} (цифрами - например, 53): ')
        if not is_correct(a, ceil):
            print('Давай все-таки введем число в правильном формате?')
            continue
        a = int(a)
        count += 1
        if a == n:
            print('Верно! Ты угадал 😉')
            print(f'Тебе потребовалось {count} {which_word(count)}!')
            print(f'В случае выбора правильной стратегии тебе потребовалось бы максимум {math.floor(math.log(ceil, 2)) + 1} '
                  f'{which_word(math.floor(math.log(ceil, 2)) + 1)}, чтобы гарантированно угадать это число')
            break
        if a > n:
            print('Слишком большое!')
        else:
            print('Слишком маленькое!')
    continue_game = input('Хочешь сыграть снова? Введи "д", если да, и "н", если нет: ').lower()
    while continue_game != "д" and continue_game != "н":
        continue_game = input('Я тебя не понял... Введи "д", если да, и "н", если нет: ')

print('Спасибо, что сыграл в числовую угадайку. Еще увидимся...')
