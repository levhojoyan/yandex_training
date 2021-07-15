n = int(input())

l = list(map(int, input().split()))

m = int(input())

for index in map(int, input().split()):
    l[index - 1] -= 1

for number in l:
    if number < 0:
        print('YES')
    else:
        print('NO')
