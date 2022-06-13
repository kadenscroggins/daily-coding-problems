from anytree import Node, RenderTree
import re

fsys1 = "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext"
fsys2 = "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"

def build_fs(string, depth = 0):
    temp = Node('test')





tree1 = build_fs(fsys1)
tree2 = build_fs(fsys2)

'''
for pre, fill, node in RenderTree(tree1):
    print('%s%s' % (pre, node.name))

for pre, fill, node in RenderTree(tree2):
    print('%s%s' % (pre, node.name))
'''

def trimmy(string):
    regstr = '[\n\t]{1}'
    templist = re.split(regstr, string, 1)
    print(templist[0])
    if len(templist) > 1:
        trimmy(templist[1])



trimmy(fsys1)
#trimmy(fsys2)