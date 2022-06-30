str1 = "([])[]({})"
str2 = "([)]"
str3 = "((()"

def check_balance(s):
    for i in range(len(s)):
        print(s[i])
    
    return True

print(check_balance(str1))