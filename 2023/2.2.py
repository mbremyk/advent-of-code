num = 0

with open('input2_clean.txt') as f:
    for line in f:
        cols = {
            'r': 0,
            'g': 0,
            'b': 0
        }
        sets = line.split(';')
        for s in sets:
            s = s.strip()
            groups = s.split(',')
            for g in groups:
                g = g.strip()
                g = g.split(' ')
                if int(g[0]) > cols[g[1]]:
                    cols[g[1]] = int(g[0])
        num += cols['r'] * cols['g'] * cols['b']
                
print(num)