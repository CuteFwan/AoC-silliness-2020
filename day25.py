def transform(value, subject):
    value *= subject
    value, r = divmod(value, 20201227)
    return r

value = 1
subject = 7
card = 8458505
door = 16050997
cardloop = 0 or 15260454 # I can't be bothered to recalculate this
doorloop = 0 or 10476062
    
for i in range(100000000):
    value = transform(value, subject)
    if value == card:
        cardloop = i+1
    elif value == door:
        doorloop = i+1
    if cardloop and doorloop:
        break
key = 1
for i in range(cardloop):
    key = transform(key, door)
print(key)