list = [10, 15, 3, 7]
k = 17

for x in range(len(list)):
    halt = False
    for y in list[x:]:
        if list[x] + y == k:
            print ("{} + {} = {}".format(list[x], y, list[x] + y))
            halt = True
            break
    if halt: break