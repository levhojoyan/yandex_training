import typing as tp
from collections import defaultdict

d: tp.DefaultDict[str, tp.DefaultDict[str, int]] = defaultdict(lambda: defaultdict(int))

with open('input.txt', 'r') as f:
    for line in f:
        name, tovar, amount = line.split()
        d[name][tovar] += int(amount)

for name in sorted(d.keys()):
    print(name, ':', sep='')
    for tovar in sorted(d[name].keys()):
        print(tovar, d[name][tovar])

