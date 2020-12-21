with open('input21.txt') as f:
    ingredients = set()
    allergens = set()
    noms = []
    line = f.readline()
    while line != '':
        ingrs, algns = line.split(' (contains ')
        ingrs = ingrs.split(' ')
        algns = algns.strip().replace(')','').split(', ')
        noms.append((set(ingrs),set(algns)))
        ingredients.update(ingrs)
        allergens.update(algns)
        line = f.readline()
#print(ingredients)
print(allergens)
#print('\n'.join(f'{l}' for l in noms))
print()

possibilities = {algn : ingredients.copy() for algn in list(allergens)}

for algn in list(allergens):
    for ingrs, algns in noms:
        if algn not in algns:
            continue
        possible = possibilities[algn]
        possible = possible & ingrs
        possibilities[algn] = possible

#prune

def remove_from_whatever(ingr, possibilities, ignore):
    for algn, ingrs in possibilities.items():
        if algn == ignore:
            continue
        if ingr not in ingrs:
            continue
        ingrs.remove(ingr)
        if len(ingrs) == 1:
            remove_from_whatever(list(ingrs)[0], possibilities, algn)
for algn, ingrs in possibilities.items():
    if len(ingrs) == 1:
        remove_from_whatever(list(ingrs)[0], possibilities, algn)

possibilities = {list(ingrs)[0] : algn for algn, ingrs in possibilities.items()}

print('\n'.join(f'{p}' for p in possibilities.items()))

total = 0
for ingrs, algns in noms:
    for ingr in list(ingrs):
        if ingr in possibilities:
            continue
        total += 1
print(total)
shopping_list = [(ingr, algn) for ingr, algn in possibilities.items()]
print(shopping_list)
shopping_list = sorted(shopping_list, key=lambda n : n[1])
print(shopping_list)
shopping_list = [ingr for ingr, algn in shopping_list]
print(shopping_list)
shopping_list = ','.join(shopping_list)
print(shopping_list)
with open('why_do_I_have_to_type_this_out_I_will_just_copy_paste_it_because_my_terminal_sucks.txt', 'w') as f:
    f.write(shopping_list)