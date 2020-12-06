with open('input6.txt') as f:
    all_the_answers_from_all_the_people = [[]]
    line = f.readline()
    while line != '':
        if line == '\n':
            all_the_answers_from_all_the_people.append([])
        else:
            all_the_answers_from_all_the_people[-1].append(line.replace('\n',''))
        line = f.readline()

def combine_answers_into_one(group):
    output = set()
    for g in group:
        output = output | set(g)
    return output

def combine_answers_into_one_fixed_v3_final(group):
    output = set(group[0])
    for g in group[1:]:
        output = output & set(g)
    return output

def sum_all_unique_answers(groups):
    total = 0
    for group in groups:
        total += len(combine_answers_into_one(group))
    return total

def sum_all_unique_answers_but_not_wrong_this_time(groups):
    total = 0
    for group in groups:
        total += len(combine_answers_into_one_fixed_v3_final(group))
    return total
print(sum_all_unique_answers(all_the_answers_from_all_the_people))
print(sum_all_unique_answers_but_not_wrong_this_time(all_the_answers_from_all_the_people))