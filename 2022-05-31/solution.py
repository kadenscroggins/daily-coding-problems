input = [3, 4, -1, 1]
input.sort()
while input[0] < 1: input.pop(0)
for i in range(len(input)):
    if i + 1 != input[i]:
        print(i+1)
        break
    elif i+1 == len(input):
        print(i+2)