list = [1, 2, 3, 4, 5]
output = []

for i in range(len(list)):
    temp = 1
    for j in range (len(list)):
        if i == j: pass
        else: temp *= list[j]
    output.append(temp)
print(output)