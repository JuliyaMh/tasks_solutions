def vertical_check(vertical, i, m):
    if 0 <= i + vertical < m:
        return i + vertical
    if i + vertical == -1:
        return m - 1
    if i + vertical == m:
        return 0


def horizontal_check(horizon, j, n):
    if 0 <= j + horizon < n:
        return j + horizon
    if j + horizon == -1:
        return n - 1
    if j + horizon == n:
        return 0


m, n = map(int, input().split())
first_generation = [[0 for _ in range(n)] for _ in range(m)]
second_generation = [[0 for _ in range(n)] for _ in range(m)]
neighbours = [[-1, -1], [-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1], [0, -1]]

for i in range(m):
    values = input()
    for j in range(n):
        first_generation[i][j] = values[j]
        second_generation[i][j] = values[j]

for i in range(m):
    for j in range(n):
        neighbours_amount = 0
        for vertical, horizon in neighbours:
            vertical = vertical_check(vertical, i, m)
            horizon = horizontal_check(horizon, j, n)
            if first_generation[vertical][horizon] == 'X':
                neighbours_amount += 1
        if second_generation[i][j] == 'X' and not (neighbours_amount == 2 or neighbours_amount == 3):
            second_generation[i][j] = '.'
        elif second_generation[i][j] == '.' and neighbours_amount == 3:
            second_generation[i][j] = 'X'

for list1 in second_generation:
    print(*list1, sep='')



