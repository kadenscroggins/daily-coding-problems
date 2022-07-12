fsys1 = "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext"
fsys2 = "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"

def print_longest(string):
    '''Shout out to '''
    paths = [None]
    longest = 0

    for s in string.split('\n'):
        tabs = 0
        while s[tabs] == '\t':
            tabs += 1
        if tabs == len(paths):
            paths.append(None)
        else:
            paths = paths[:tabs + 1]
        paths[-1] = str.strip(s)
        if '.' in paths[-1]:
            longest = max(longest, len('/'.join(paths)))
    
    longest_str = ''
    for s in paths:
        longest_str += s + '/'
    longest_str.rstrip('/')
    print(f'Longest length: {longest}, path: {longest_str}')

print_longest(fsys1)
print_longest(fsys2)