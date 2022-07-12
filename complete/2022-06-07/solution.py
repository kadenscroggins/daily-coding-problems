'''
This solution is quick and effective.
For a huge dictionary and longer queries, it would be
more efficient to sort the set of strings into a tree where
each node is a letter A-Z so that a query could just go
down the tree to find if there is a string match.
'''
import re

QUERY = 'de'
STRINGS = ['dog', 'deer', 'deal']

processed = []
for s in STRINGS:
    # This regex checks for QUERY at the beginning of s
    if re.search(f'\\A{QUERY}', s) is None:
        pass
    else:
        processed.append(s)

print(processed)
