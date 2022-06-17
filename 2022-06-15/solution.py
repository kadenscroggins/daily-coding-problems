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
    
    for j in range(len(HOUSES)):
        if j == left_house:
            continue
        else:
            temp_cost 
###

    costs.append(temp_cost)
print(min(costs))