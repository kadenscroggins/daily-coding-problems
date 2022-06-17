times = [(30, 75), (0, 50), (60, 150)]
count = 0

for i in range(len(times)):
    for k in range(i+1, len(times)):
        if ( times[i][0] > times[k][0]   \
        and  times[i][0] < times[k][1] ) \
        or ( times[i][1] > times[k][0]   \
        and  times[i][1] < times[k][1] ) :
                count += 1

print(count)