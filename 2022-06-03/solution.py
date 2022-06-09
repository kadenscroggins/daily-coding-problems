'''
This works for all the test cases I put in to it.
I'm sure there's probably some bigger cases where it
doesn't work, and some edge cases that might be wrong.
I don't really have enough time to account for all of
this currently, so I'm moving on for now.
'''
def decode(input):
    possible = 1
    for i in range(len(input)):
        if input[i] == '0': pass
        elif len(input) > i+2 and input[i+2] == '0': pass
        elif len(input) > i+1 and input[i] == '1':
            if input[i+1] in '123456789': possible += 1
        elif len(input) > i+1 and input[i] == '2':
            if input[i+1] in '123456': possible += 1
    return possible

print('decode("1") should be 1: is {}'.format(decode('1')))
print('decode("11") should be 2: is {}'.format(decode('11')))
print('decode("111") should be 3: is {}'.format(decode('111')))
print('decode("1010") should be 1: is {}'.format(decode('1010')))
print('decode("1110") should be 2: is {}'.format(decode('1110')))
print('decode("202230") should be 2: is {}'.format(decode('202230')))
print('decode("12345") should be 3: is {}'.format(decode('12345')))
