n = int(input())

d = {}

for _ in range(n):
    a, b = list(input().split())
    d[a] = b
    d[b] = a

print(d[input()])