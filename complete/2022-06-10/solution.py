import random

# Needlessly large number to get estimate to 3.14
INTERVAL = 10000000

inside_square = 0
inside_circle = 0

for i in range(INTERVAL):
    a = random.uniform(-1, 1)
    b = random.uniform(-1, 1)

    inside_square += 1
    # sqrt(a^2+b^2) = c
    if (a**2 + b**2)**0.5 <= 1.0:
        inside_circle += 1


pi = 4 * inside_circle / inside_square
print(f'Pi calculated with {INTERVAL} random numbers: {pi:.2f}')