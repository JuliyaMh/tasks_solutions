values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
number = input()
result = 0

index = 0
while index < len(number):
    if index < len(number) - 1 and values[number[index + 1]] > values[number[index]]:
        result += values[number[index + 1]] - values[number[index]]
        index += 2
    else:
        result += values[number[index]]
        index += 1
print(result)



