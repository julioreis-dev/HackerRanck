colors = ['Black', 'White']
sizes = ['S', 'M', 'L']
for n in ('%s %s' % (c, s) for c in colors for s in sizes):
    print(n)
