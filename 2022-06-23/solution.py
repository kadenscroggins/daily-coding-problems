import re

str1 = '''([])[]({})'''
str2 = "([)]"
str3 = "((()"

def check_balance(s):
    brackets = '\\[\\]'
    braces = '\\{\\}'
    parenthesis = '\\(\\)'
    
    while True:
        if re.search(brackets, s):
            s = re.sub(brackets, '', s)
        elif re.search(braces, s):
            s = re.sub(braces, '', s)
        elif re.search(parenthesis, s):
            s = re.sub(parenthesis, '', s)
        else:
            break
    
    if len(s) == 0:
        return True
    return False

print(f'str1: {check_balance(str1)}')
print(f'str2: {check_balance(str2)}')
print(f'str3: {check_balance(str3)}')