from collections import defaultdict
import re
matcher = re.compile(fr"(.*)\sbags?\scontain\s(.*).")
matcher2 = re.compile(fr"(\d)\s(.*)\sbags?")

with open('input7.txt') as f:
    mapping = defaultdict(list) #Reverse mapping because why not. It makes it slightly easier to count backwards.
    bag_tree = defaultdict(list) #Normie mapping. Very tree-like. Much christmas.
    for line in f.read().split('\n'):
        result = matcher.match(line)
        if result is None or not result.group(0):
            continue
        parent = result.group(1)
        contents = result.group(2)
        if contents == 'no other bags':
            mapping[contents].append(parent)
            bag_tree[parent].append((contents, 0))
        else:
            for child in contents.split(', '):
                result2 = matcher2.match(child)
                if result2 is None or not result2.group(0):
                    continue
                amount = result2.group(1)
                bag = result2.group(2)
                mapping[bag].append(parent)
                bag_tree[parent].append((bag, int(amount)))

def find_all_possible_colors(target, mapping):
    possible = mapping[target] #Save bags seen here
    bags_to_search = mapping[target] #Bags to search go here
    while len(bags_to_search) != 0: #New bags to search is empty. die
        searching = bags_to_search
        bags_to_search = []
        for s in searching:
            result = mapping.get(s, None)
            if result:
                bags_to_search.extend(result) #New generation of bags to search :O
                possible.extend(result)
    return set(possible)

def count_all_sub_bags(target, bags):
    def count_sub_bag(target, mult, bags):
        sub_bags = bags[target]
        total = mult
        for sub_bag in sub_bags:
            total += count_sub_bag(sub_bag[0], mult*sub_bag[1], bags)
        return total
    return count_sub_bag(target, 1, bags) - 1 #Subtract initial bag

bags = find_all_possible_colors('shiny gold', mapping)
print(len(bags))

total = count_all_sub_bags('shiny gold', bag_tree)
print(total)