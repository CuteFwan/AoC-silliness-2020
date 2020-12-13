from math import ceil

with open('input13.txt') as f:
    timestamp = int(f.readline().strip())
    busses = [int(b) if b.isnumeric() else b for b in f.readline().split(',')]

next_busses = [(b, b * ceil(timestamp / b)) for b in busses if b != 'x']


next_bus = min([(bus, next_bus - timestamp) for bus, next_bus in next_busses], key = lambda a : a[1])
print(next_bus[0] * next_bus[1])


expected_remaining = []
modder = []
for i, b in enumerate(busses):
    if b == 'x':
        continue
    expected_remaining.append((b - i)%b)
    modder.append(b)

bigmod = 1
total = 0
for m in modder:
    bigmod *= m
for e, m in zip(expected_remaining, modder):
    b = bigmod // m
    total += e * b * pow(b, m - 2, m)
    total %= bigmod
print(total)