import re

chars = ['G', 'B', 'R', 'R', 'B', 'R', 'G']

while not #chars to string, regex search for R-G-B:
    i = 0
    while i < len(chars) - 1:
        if chars[i] == 'B':
            if i < len(chars) and chars[i+1] == 'B':
                i += 1
            else:
                chars[i], chars[i+1] = chars[i+1], chars[i]
        else:
            i+= 1

    i = 0
    while i < len(chars):
        if chars[i] == 'R':
            if i > 0 and chars[i-1] == 'R':
                i += 1
            else:
                chars[i], chars[i-1] = chars[i-1], chars[i]
        else:
            i+= 1

print(chars)