n = int(input())
list1 = [[0 for i in range(n)] for i in range(n)]
number = 1
i = 0
j = 0
heading = 'horizontal'
border = 0
up = 1
while number != n ** 2 + 1:
    if heading == 'horizontal':
        while (j != n - border or up != 1)  and (j != border - 1 or up != -1):
            list1[i][j] = number
            j += 1 * up
            number += 1
        j -= 1 * up
        i += 1 * up
        heading = 'vertical'
    else:
        while (i != n - border - 1 or up != 1) and (i != border + 1 or up != -1):
            list1[i][j] = number
            i += 1 * up
            number += 1
        heading = 'horizontal'
        if up == -1:
            border += 1
        up *= -1
for i in range(n):
    print(*list1[i])





