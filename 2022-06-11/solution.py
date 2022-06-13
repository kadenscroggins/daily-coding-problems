from random import randint

count = 0
with open('lines.txt') as file:
    for line in file:
        count += 1

index = randint(0, count)

count = 0
with open('lines.txt') as file:
    for line in file:
        if index != count:
            pass
        else:
            print(f'Line {count}: {line}')
            break
        count += 1