with open('input15.txt') as f:
    numbers = [int(g) for g in f.read().split(',')]

print(numbers)


def dinner_time(numbers, target):
    last_heard = {n : [i,i] for i, n in enumerate(numbers)}
    last_number = numbers[-1]
    for t in range(len(numbers), target):
        check_already_heard = last_heard.get(last_number, [t,t])
        next_number = check_already_heard[1] - check_already_heard[0]
        #print(f'{t+1}th turn is {check_already_heard[1]+1} - {check_already_heard[0]+1} = {next_number}')

        prepre, pre = last_heard.get(next_number, [t,t])
        last_heard[next_number] = pre, t

        last_number = next_number
    return last_number
result = dinner_time(numbers, 2020)
print(result)
result2 = dinner_time(numbers, 30000000)
print(result2)