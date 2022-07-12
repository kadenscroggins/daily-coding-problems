# Input
s = 'abcba'
k = 2

# Get all possible substrings
substrings = [s[i:j] for i in range(len(s))
    for j in range(i+1, len(s) + 1)]

max_distinct_length = 0
max_distinct_string = ''
for string in substrings:
    str_set = set(string)
    if len(str_set) <= k and len(string) >= max_distinct_length:
        max_distinct_length = len(string)
        max_distinct_string = string

print(f'Max distinct length is {max_distinct_length}'
      f' characters in string {max_distinct_string}')
