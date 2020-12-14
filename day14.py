import re
matcher = re.compile(fr"(mask|mem)\[?(\d+)?\]?\s=\s(.*)")

with open('input14.txt') as f:
    instructions = matcher.findall(f.read())
def porse(instructions):
    mem = dict()
    mask = None
    for inst in instructions:
        if inst[0] == 'mask':
            mask = [(i, m) for i, m in enumerate(inst[2]) if m.isnumeric()]
        elif inst[0] == 'mem':
            temp = list(f'{int(inst[2]):0>36b}')
            for pos, v in mask:
                temp[pos] = v
            mem[inst[1]] = int(''.join(temp),2)
    return sum(mem.values())

def porse2(instructions):
    mem = dict()
    mask = None
    for inst in instructions:
        if inst[0] == 'mask':
            mask = inst[2]
        elif inst[0] == 'mem':
            temp = list(f'{int(inst[1]):0>36b}')
            addresses = [[]]
            for i, m in enumerate(mask):
                if m == '0':
                    for a in addresses:
                        a.append(temp[i])
                elif m == '1':
                    for a in addresses:
                        a.append('1')
                else:
                    temp_addresses = [[aaa for aaa in aa] for aa in addresses] # lazy copy
                    for a in addresses:
                        a.append('0')
                    for a in temp_addresses:
                        a.append('1')

                    addresses.extend(temp_addresses)
            for a in addresses:
                address = int(''.join(a),2)
                mem[address] = int(inst[2])

    return sum(mem.values())

result = porse(instructions)
print(result)

result2 = porse2(instructions)
print(result2)