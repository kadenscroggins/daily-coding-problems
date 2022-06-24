import re

words = ['quick', 'brown', 'the', 'fox']
sentence = 'thequickbrownfox'

ordered = []
for i in range(len(words)):
    if (bool(re.search('^'+words[i], sentence))):
        ordered.append(words[i])

print(ordered)