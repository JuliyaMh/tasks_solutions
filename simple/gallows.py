import random


def play(category, word):
    attempts_count = 0
    gallows = ['—————', '|  | ', '|    ', '|    ', '|    ']
    add_to_gallows = {1: [2, '|  0 '], 2: [3, '|  |  '], 3: [3, '| /|  '], 4: [3, '| /|\\ '], 5: [4, '| /  '],
                      6: [4, '| / \\']}  # количество использованных попыток: [индекс заменяемой строки, на что меняем]

    display_word = word[0] + '*' * (len(word) - 2) + word[-1]
    wrong_letters = ''
    open_letters = ''

    print(f'Добро пожаловать в игру "Виселица"! Я загадал слово из категории {category}- попробуй угадать его 😉')

    while True:
        print(f'Загаданное слово: {display_word}')
        print(f'Буквы, которых точно нет в слове: {wrong_letters} ')
        for part in gallows:
            print(part)

        letter = input('Введи букву (например, "а"): ').lower()
        while not letter or len(letter) != 1 or not 1072 <= ord(letter) <= 1103:
            print('Кажется, ты ввел данные в неправильном формате. Попробуй снова.')
            letter = input('Введи букву (например, "а"): ')
        while letter in open_letters:
            print('Кажется, ты уже называл эту букву... Ты уверен, что хочешь потратить драгоценную попытку на ЭТО? '
                  'Попробуй снова.')
            letter = input('Введи букву (например, "а"): ')

        open_letters += letter
        if letter in word:
            print('Молодец! Ты угадал букву.\n')
            for i in range(len(word)):
                if word[i] == letter:
                    display_word = display_word[:i] + letter + display_word[i + 1:]
            if not '*' in display_word:
                print(display_word)
                print('Ура! Ты угадал слово 🥳. Сегодня никого не повесят...\n')
                break
        else:
            print('О нет... Этой буквы нет в загаданном слове...\n')
            attempts_count += 1
            gallows[add_to_gallows[attempts_count][0]] = add_to_gallows[attempts_count][1]
            wrong_letters += letter

            if attempts_count == 6:
                for part in gallows:
                    print(part)
                print('Ты проиграл, дружище...')
                print(f'Загаданное слово: {word}\n')
                break


words = {'🐱 животные': ['скат', 'выдра', 'лосось', 'соловей', 'попугай', 'скорпион', 'муравьед', 'землеройка'],
         '🍎 еда': ['курага', 'овощи', 'чечевица', 'кинза', 'щавель', 'баклажан', 'смородина', 'миндаль'],
         '🏠 дом': ['плинтус', 'вантуз', 'отвертка', 'наволочка', 'холодильник', 'конфорка', 'зажигалка'],
         '⚽ спорт': ['забег', 'сальто', 'гандбол', 'разминка', 'фехтование', 'олимпиада']
         }

while True:
    category = random.choice(list(words.keys()))
    word = random.choice(words[category])
    play(category, word)

    new_game = input('Хочешь сыграть еще раз? Введи "д", если да, и "н", если нет: ')
    while new_game != 'д' and new_game != 'н':
        print('Кажется, ты ввел данные в неправильном формате. Попробуй снова.')
        new_game = input('Хочешь сыграть еще раз? Введи "д", если да, и "н", если нет: ')
    print()

    if new_game == 'н':
        print('До встречи!')
        break


