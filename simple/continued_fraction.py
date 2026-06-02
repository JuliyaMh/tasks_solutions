up, down = map(int, input().split('/'))

while down != 0:
    print(up // down, end= ' ')
    up= up % down
    up, down = down, up
