with open('input12.txt') as f:
    aaa = [(n[0], int(n[1:])) for n in f.read().split()]

def follow_instructions(instructions):
    compass = ['N','E','S','W']
    d = 1
    x = y = 0
    for i, n in instructions:
        if i == 'F':
            if d == 0:
                y += n
            elif d == 2:
                y -= n
            elif d == 1:
                x += n
            elif d == 3:
                x -= n
        elif i == 'N':
            y += n
        elif i == 'S':
            y -= n
        elif i == 'E':
            x += n
        elif i == 'W':
            x -= n

        elif i == 'R':
            d = (d + (n / 90)) % 4
        elif i == 'L':
            d = (d - (n / 90)) % 4
    return abs(x) + abs(y)

print(follow_instructions(aaa))

def follow_instructions2(instructions):
    x = y = 0
    wx, wy = 10, 1
    for i, n in aaa:
        if i == 'F':
            x += wx*n
            y += wy*n
        elif i == 'N':
            wy += n
        elif i == 'S':
            wy -= n
        elif i == 'E':
            wx += n
        elif i == 'W':
            wx -= n

        elif i == 'R':
            turns = n // 90
            for t in range(turns):
                wx, wy = wy, -wx
                #10, 4 -> 4, -10
        elif i == 'L':
            turns = n // 90
            for t in range(turns):
                wx, wy = -wy, wx
                #10, 4 -> -4, 10

    return abs(x) + abs(y)

print(follow_instructions2(aaa))