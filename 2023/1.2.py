import re

numbers = ["æøå", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
x = 0

with open("input1.txt") as f:
    for line in f:
        n = [re.search(a, line) for a in numbers]
        n = [(a.span()[0], a.group(0)) for a in n if a is not None]
        ni = [a[0] for a in n]
        ni = ni.index(min(ni))
        n = n[ni][1]
        li = max([line.rfind(s) for s in numbers])
        l = line[li:]
        l = [re.search(a, l) for a in numbers]
        l = [a for a in l if a is not None][0]
        l = l.group(0)
        if not n.isnumeric():
            n = str(numbers.index(n))
        if not l.isnumeric():
            l = str(numbers.index(l))
        res = (n, l)
        x += int("".join(res))
        
print(x)