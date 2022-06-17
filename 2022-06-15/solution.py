HOUSES = [ [5, 4, 2, 2, 3], \
           [1, 5, 8, 5, 1], \
           [2, 2, 2, 2, 2], \
           [3, 4, 5, 6, 7]  ]
costs = []

###
left_house = 0
for i in range(len(HOUSES[0])):
    temp_cost = HOUSES[0][i]
    left_house = i
    
    for j in range(1, len(HOUSES)):
        temp_lowest = -1
        for k in range(len(HOUSES[j])):
            if k == left_house:
                continue
            elif temp_lowest == -1:
                temp_lowest = HOUSES[j][k]
            elif HOUSES[j][k] < temp_lowest:
                temp_lowest = HOUSES[j][k]
                left_house = k
        temp_cost += temp_lowest

    costs.append(temp_cost)
print(min(costs))