import re

words = ['quick', 'brown', 'the', 'fox']
sentence = 'thequickbrownfox'

ordered = []
while len(sentence) > 0:
    for i in range(len(words)):
        if (bool(re.search('^'+words[i], sentence))):
            ordered.append(words[i])
            sentence = sentence[len(words[i]):]

print(ordered)