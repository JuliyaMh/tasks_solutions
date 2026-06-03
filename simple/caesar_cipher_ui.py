RUSSIAN_LENGTH = 32
ENGLISH_LENGTH = 26

print('Добро пожаловать в программу "Шифр Цезаря"!')

direction = input('Укажите направление: шифрование или дешифрование. Если требуется зашифровать текст, введите "ш", '
                  'если требуется дешифровать текст, введите "д": ')
while direction != 'ш' and direction != 'д':
    print("Кажется, вы ввели данные в неверном формате. Попробуйте снова.")
    direction = input(
        'Укажите направление: шифрование или дешифрование. Если требуется зашифровать текст, введите "ш", '
        'если требуется дешифровать текст, введите "д": ')

language = input('Укажите язык сообщения: русский или английский. Если русский, введите "ru", если английский, '
                 'введите "eng": ')
while language != 'ru' and language != 'eng':
    print("Кажется, вы ввели данные в неверном формате. Попробуйте снова.")
    language = input('Укажите язык сообщения: русский или английский. Если русский, введите "ru", если английский, '
                     'введите "eng": ')

key = input("Укажите шаг сдвига в числовом формате (например, 10): ")
while not key.isdigit():
    print("Кажется, вы ввели данные в неверном формате. Попробуйте снова.")
    key = input("Укажите шаг сдвига в числовом формате (например, 10): ")
key = int(key)

message = input("Введите текст сообщения: ")
while not message:
    print("Кажется, вы ничего не ввели. Попробуйте снова.")
    message = input("Введите текст сообщения: ")

result = ''
length = RUSSIAN_LENGTH if language == 'ru' else ENGLISH_LENGTH
upper = ord('А') if language == 'ru' else ord('A')
lower = ord('а') if language == 'ru' else ord('a')
key %= length
if direction == 'ш':
    for char in message:
        if char.isalpha():
            position = ord(char) + key
            if char.isupper() and position > upper + length - 1:
                position = position - length
            elif char.islower() and position > lower + length - 1:
                position = position - length
            result += chr(position)
        else:
            result += char
else:
    for char in message:
        if char.isalpha():
            position = ord(char) - key
            if char.isupper() and position < upper:
                position = position + length
            elif char.islower() and position < lower:
                position = position + length
            result += chr(position)
        else:
            result += char

print(result)
