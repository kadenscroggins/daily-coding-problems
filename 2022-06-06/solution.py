import time
def schedule(f, n):
    time.sleep(0.001 * n)
    f()

func = lambda : print("Called F")
schedule(func, 1000)