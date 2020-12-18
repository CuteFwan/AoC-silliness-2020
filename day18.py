with open('input18.txt') as f:
    maths = f.read().split('\n')

ops = {
    '*':[2, 'l', 2, lambda x, y : y * x],
    '+':[3, 'l', 2, lambda x, y : y + x]
    }
def solve(read):
    stack = []
    out = []
    numstack = []
    funcstack = []
    last = ''

    for t in read:
        if t.isspace():
            continue
        if len(numstack) and not (t.isdigit() or t == '.'):
            out.append("".join(numstack))
            numstack = []
        if t.isdigit() or t == '.':
            numstack.append(t)
        if t.isalpha():
            funcstack.append(t)
        if t == '(':
            if last.isalpha():
                stack.append("".join(funcstack))
                funcstack = []
            elif last.isdigit() or last == ')':
                cur = ops['*']
                while len(stack) and stack[-1] != '(' and (ops[stack[-1]][0] > cur[0] or (ops[stack[-1]][0] == cur[0] and ops[stack[-1]][1] == 'l')):
                    out.append(stack.pop())
                stack.append('*')
            stack.append(t)
        elif t == ')':
            while stack[-1] != '(':
                out.append(stack.pop())
            stack.pop()
        elif t in ops.keys():
            if t == '-' and not len(numstack) and not (last.isdigit() or last == ')'):
                numstack.append(t)
                continue
            cur = ops[t]
            while len(stack) and stack[-1] != '(' and (ops[stack[-1]][0] > cur[0] or (ops[stack[-1]][0] == cur[0] and ops[stack[-1]][1] == 'l')):
                out.append(stack.pop())
            stack.append(t)
        last = t
    if len(numstack):
        out.append("".join(numstack))
        numstack = []
    while len(stack):
        out.append(stack.pop())
        
    stackeroo = []

    for t in out:
        if t in ops:
            nargs = ops[t][2]
            args = [stackeroo.pop() for i in range(nargs)]
            temp = ops[t][3](*args)
            if temp:
                stackeroo.append(temp)
            else:
                stackeroo.clear()
                stackeroo.append('Undefined')
                break
        else:
            stackeroo.append(float(t))

    return stackeroo[0]

total = 0
for math in maths:
    total += solve(math)
print(total)