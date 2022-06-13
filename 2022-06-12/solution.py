import array

# unsigned int - assume order IDs are positive integers
log = array.array('I', (1, 2, 3, 4, 5))

def get_last(i):
    return log[-i]

def record(id):
    log.append(id)

print(f'2nd last element: {get_last(2)}')
print('Adding order ID 6')
record(6)
print(f'2nd last element: {get_last(2)}')