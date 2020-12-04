with open('input1.txt') as f:
    numbers = [int(n) for n in f.read().split()]
numbers.sort()

def get_answer1(l):
    i = 0
    j = len(l) - 1
    while i != j:
        cur = l[i] + l[j]
        if cur == 2020:
            return l[i], l[j], l[i]*l[j]
        elif cur < 2020:
            i += 1
        elif cur > 2020:
            j -= 1
    print('well shit')

def get_answer2(l):
    for k in range(1, len(l) - 2):
        i = 0
        j = len(l) - 1
        while i < k < j:
            cur = l[i] + l[k] + l[j]
            if cur == 2020:
                return l[i], l[k], l[j], l[i]*l[k]*l[j]
            elif cur < 2020:
                i += 1
            elif cur > 2020:
                j -= 1
        print('well shit')

print(get_answer1(numbers))
print(get_answer2(numbers))