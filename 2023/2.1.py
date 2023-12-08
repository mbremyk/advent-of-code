cols = {
    'r': 12,
    'g': 13,
    'b': 14
}

yes = True
num = 0

with open('input2_clean.txt') as f:
    for ix, line in enumerate(f):
        yes = True
        sets = line.split(';')
        for s in sets:
            s = s.strip()
            groups = s.split(',')
            for g in groups:
                g = g.strip()
                g = g.split(' ')
                if int(g[0]) > cols[g[1]]:
                    yes = False
        if (yes):
            num += ix + 1
                
print(num)