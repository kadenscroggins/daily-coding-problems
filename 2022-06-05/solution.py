list1 = [2, 4, 6, 2, 5]
list2 = [5, 1, 1, 5]

def non_adjacent(list):
    # Assumes list will be 3 or longer
    sums = []
    for i in range(len(list) - 2):
        for k in list[i+2:]:
            sums.append(list[i] + k)
    
    return max(sums)

print(f'First list: {non_adjacent(list1)}')
print(f'Second list: {non_adjacent(list2)}')