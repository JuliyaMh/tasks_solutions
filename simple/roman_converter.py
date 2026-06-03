def to_arabic(number):
    values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    result = 0
    
    index = 0
    while index < len(number):
        if index < len(number) - 1 and values[number[index + 1]] > values[number[index]]:
            result += values[number[index + 1]] - values[number[index]]
            index += 2
        else:
            result += values[number[index]]
            index += 1
    return result


def to_roman(number):
    values = {1000: 'M', 900: 'CM', 500: 'D', 400: 'CD', 100: 'C', 90: 'XC', 50: 'L', 40: 'XL', 10: 'X', 9: 'IX', 5: 'V', 4: 'IV', 1: 'I'}
    result = ''
    
    for key in values.keys():
        result += number // key * values[key]
        number %= key
    return result


