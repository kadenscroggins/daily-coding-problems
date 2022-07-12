array = [10, 5, 2, 7, 8, 7]
k = 3

temp = []
for i in range(len(array) - k + 1):
    temp.append((max(array[i:i+k])))

print(temp)