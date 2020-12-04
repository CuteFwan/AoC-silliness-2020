import re
matcher = re.compile(fr"(\d+)-(\d+) ([a-z]): ([a-z]+)")

with open('input2.txt') as f:
    passwords = []
    line = f.readline()
    while line != '':
        result = matcher.match(line)
        line = f.readline()
        if result is None or not result.group(0):
            print(f'wtf,\"{line}\" broke??')
            continue
        mini = int(result.group(1))
        maxi = int(result.group(2))
        char = result.group(3)
        pasw = result.group(4)
        passwords.append([mini, maxi, char, pasw])

def parse_passwords1(pswds):
    valid = 0
    for psw in pswds:
        count = sum(1 for c in psw[3] if c == psw[2])
        if psw[0] <= count <= psw[1]:
            valid += 1
    return valid

def parse_passwords2(pswds):
    valid = 0
    for psw in pswds:
        if (psw[3][psw[0]-1] == psw[2]) + (psw[3][psw[1]-1] == psw[2]) == 1:
            valid += 1
    return valid
print(parse_passwords1(passwords))
print(parse_passwords2(passwords))