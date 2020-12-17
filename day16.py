import re
matcher = re.compile(fr'(.+):\s(\d+)-(\d+) or (\d+)-(\d+)')

with open('input16.txt') as f:
    rules = dict()
    myticket = None
    neartickets = []
    line = f.readline()
    while line != '\n':
        result = matcher.match(line)
        if result is None or not result.group(0):
            print(f'wtf,\"{line}\" broke??')
            continue
        group = result.group(1)
        min1 = int(result.group(2))
        max1 = int(result.group(3))
        min2 = int(result.group(4))
        max2 = int(result.group(5))
        rules[group] = ((min1,max1),(min2,max2))

        line = f.readline()
    line = f.readline()
    while line != '\n':
        if line == 'your ticket:\n':
            pass
        else:
            myticket = [int(l) for l in line.strip().split(',')]

        line = f.readline()
    line = f.readline()
    while line != '':
        if line == 'nearby tickets:\n':
            pass
        else:
            neartickets.append([int(l) for l in line.strip().split(',')])

        line = f.readline()

#print(rules)
#print(myticket)
#print(neartickets)

def check_val_against_all_rules(rules, val):
    valid = False
    for rule in rules.values():
        for r in rule:
            if r[0] <= val <= r[1]:
                valid = True
                return True
    return valid

def check_val_against_rule(rule, val):
    valid = False
    for r in rule:
        if r[0] <= val <= r[1]:
            valid = True
            return valid
    return valid



def check_error_rate(rules, neartickets):
    invalids = []
    valid_tickets = []
    for i, ticket in enumerate(neartickets):
        valid = True
        for val in ticket:
            valid = check_val_against_all_rules(rules, val)
            if valid == False:
                invalids.append(val)
                break
        if valid:
            valid_tickets.append(ticket)
    return sum(invalids), valid_tickets


result, neartickets = check_error_rate(rules, neartickets)

print(result)

def figure_out_rows_and_stuff(rules, tickets):
    possible = [list(rules.keys()) for _ in range(len(rules.keys()))]

    def remove_possible(rule_name, pos):
        possible[pos].remove(rule_name)

        if len(possible[pos]) == 1:
            #print(f'hello, removing {possible[pos]}')
            for j, p in enumerate(possible):
                if pos == j:
                    continue
                if possible[pos][0] in p:
                    remove_possible(possible[pos][0], j)

    for ticket in tickets:
        for i, val in enumerate(ticket):
            for rule_name, rule in rules.items():
                if rule_name in possible[i]:
                    valid = check_val_against_rule(rule, val)
                    #print(i, rule_name, rule, val, valid)
                    if valid == False:
                        remove_possible(rule_name, i)

        if sum(len(p) for p in possible) == len(rules.keys()):
            final_pos = [p[0] for p in possible]
            product = 1
            for i, p in enumerate(final_pos):
                if p.startswith('departure'):
                    product *= tickets[0][i]
            return product
    #print('\n'+'\n'.join(str(p) for p in possible))

result2 = figure_out_rows_and_stuff(rules, [myticket] + neartickets)
print(result2)