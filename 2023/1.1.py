import re

x = 0

with open("input1.txt") as f:
    for line in f:
        res = re.search(r"(\d).*(\d)\D*$", line)
        if(not res):
            res = re.search(r"(\d)", line)
        res = res.groups()
        if len(res) == 1:
            res = (res[0], res[0])
        x += int("".join(res))
        
print(x)