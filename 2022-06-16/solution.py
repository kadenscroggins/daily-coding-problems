'''
While I didn't use actual linked lists in this,
theoretically the logic is the same if we have access
to a function that gets the last element in a list.
It is a singly linked list so it is a bit more
convoluted, but this is the solution I am settling on
because I don't want to dump too much time into it.
'''

list1 = [3, 7, 8, 10]
list2 = [99, 1, 8, 10]

for i in range(len(list1)):
    if list1[len(list1) - (i+1)] \
    == list2[len(list2) - (i+1)]:
        continue
    else:
        print(f'Intersection: {list1[len(list1) - i]}')
        break
