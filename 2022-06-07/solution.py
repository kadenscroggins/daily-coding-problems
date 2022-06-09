import re

QUERY = 'de'
STRINGS = ['dog', 'deer', 'deal']

processed = []
for s in STRINGS:
    if re.search(f'\\A{QUERY}', s) is None:
        pass
    else:
        processed.append(s)

print(processed)
