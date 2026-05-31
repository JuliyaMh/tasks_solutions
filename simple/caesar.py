alphabet = ' abcdefghijklmnopqrstuvwxyz'
key = int(input()) % 27
message = input().strip()
result = ''

for i in message:
    position = alphabet.find(i) + key
    if position > len(alphabet) - 1:
        position -= len(alphabet)
    result += alphabet[position]
print(f'Result: "{result}"')
