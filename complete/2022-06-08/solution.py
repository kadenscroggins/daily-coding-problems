def step(n, x):
    r = 0
    for i in range(len(x)):
        if x[i] < n:
            r += step(n-x[i], x)
        elif x[i] == n:
            r += 1
    
    return r

print(step(4, [1, 3, 5]))