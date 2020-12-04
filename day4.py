import re
matcher = re.compile(fr"(ecl|pid|eyr|hcl|byr|iyr|cid|hgt):(#*[0-9a-z]+)")
to_check = ['byr','iyr','eyr','hgt','hcl','ecl','pid']
optionals = ['cid']


with open('input4.txt') as f:
    passports = [dict()]
    text = f.readline()
    while text != '':
        if text == '\n':
            passports.append(dict())
        else:
            for field in text.split():
                result = matcher.match(field)
                if result is None or not result.group(0):
                    print(f'wtf,\"{field}\" broke??')
                    continue
                passports[-1][result.group(1)] = result.group(2)
        text = f.readline()
def check_if_passport_is_super_valid_or_not(passport):
    passport_score = 0
    for check in to_check:
        if passport.get(check, None) is not None:
            passport_score += 1
    return passport_score == len(to_check)
print(sum(check_if_passport_is_super_valid_or_not(passport) for passport in passports))
            
def validate_year(year, mini, maxi):
    if len(year) == 4 and year.isnumeric():
        return mini <= int(year) <= maxi
    else:
        return False

def validate_height(height):
    if height.endswith('cm'):
        height_without_cm = int(height.replace('cm',''))
        return 150 <= height_without_cm <= 193
    elif height.endswith('in'):
        height_without_in = int(height.replace('in',''))
        return 59 <= height_without_in <= 76
    else:
        return False

def validate_color(color):
    if color.startswith('#') and len(color) == 7:
        try:
            int(color.replace('#',''),16)
            return True
        except ValueError:
            return False
    return False

def validate_eyes(eye):
    return eye in ['amb','blu','brn','gry','grn','hzl','oth']

def validate_pid(pid):
    return len(pid) == 9 and pid.isnumeric()

def check_if_passport_is_super_valid_or_not_better_function_definitely_works_not_fake(passport):
    passport_score = 0
    for check in to_check:
        field = passport.get(check, None)
        if field is not None:
            if check == 'byr':
                result = validate_year(field, 1920, 2002)
            elif check == 'iyr':
                result = validate_year(field, 2010, 2020)
            elif check == 'eyr':
                result = validate_year(field, 2020, 2030)
            elif check == 'hgt':
                result = validate_height(field)
            elif check == 'hcl':
                result = validate_color(field)
            elif check == 'ecl':
                result = validate_eyes(field)
            elif check == 'pid':
                result = validate_pid(field)
            passport_score += result

    return passport_score == len(to_check)

print(sum(check_if_passport_is_super_valid_or_not_better_function_definitely_works_not_fake(passport) for passport in passports))