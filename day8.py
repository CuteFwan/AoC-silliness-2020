ops = {
    'acc' : lambda idx, acc, val : (idx + 1, acc + val),
    'jmp' : lambda idx, acc, val : (idx + val, acc),
    'nop' : lambda idx, acc, val : (idx + 1, acc)
}

with open('input8.txt') as f:
    program = [(n[:3], int(n[4:])) for n in f.read().split('\n')]

def debuf_program(p):
    visited = []
    idx = acc = 0
    while idx not in visited:
        visited.append(idx)
        idx, acc = ops[p[idx][0]](idx, acc, p[idx][1])
    return acc


def debuf_program2(p):
    flip_attempted = []
    while True:
        flipped = False
        visited = []
        idx = acc = 0
        while True:
            if idx in visited:
                break
            visited.append(idx)
            if not flipped and p[idx][0] in ['jmp','nop'] and idx not in flip_attempted:
                op = 'jmp' if p[idx][0] == 'nop' else 'nop'
                flipped = True
                flip_attempted.append(idx)
            else:
                op = p[idx][0]
            idx, acc = ops[op](idx, acc, p[idx][1])
            if idx >= len(program):
                return acc
        

result = debuf_program(program)
print(result)
result2 = debuf_program2(program)
print(result2)