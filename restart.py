import re

S = input()
k = input()
pattern = re.compile(k)
r = re.search(pattern, S)
if r != None:
    while r:
        x = r.span()
        print("({}, {})".format(x[0], x[1]-1))
        r = pattern.search(S, x[0] + 1)
else:
    print("(-1, -1)")

