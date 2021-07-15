n = int(input())

d = {}
for _ in range(n):
    x, y = tuple(map(int, input().split()))

    if x not in d:
        d[x] = 0
    d[x] = max(d[x], y)

print(sum(d.values()))