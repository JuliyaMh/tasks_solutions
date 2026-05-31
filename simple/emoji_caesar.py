key = int(input()) % 80
message = input()
result = ''
MAX_EMOJI = 128591
MIN_EMOJI = 128512

for char in message:
    position = ord(char) + key
    if position > MAX_EMOJI:
        position = MIN_EMOJI + (position - MAX_EMOJI) - 1
    result += chr(position)
print(f'Result: "{result}"')
