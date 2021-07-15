n = int(input())

maiki = list(map(int, input().split()))

m = int(input())

shtani = list(map(int, input().split()))

l_maiki, l_shtani = 0, 0

maiki_best, shtani_best, difference_best = maiki[0], shtani[0], abs(maiki[0] - shtani[0])

for maika in maiki:
    while l_shtani < m:
        if difference_best > abs(maika - shtani[l_shtani]):
            maiki_best, shtani_best, difference_best = maika, shtani[l_shtani], abs(maika - shtani[l_shtani])

        if shtani[l_shtani] > maika:
            break

        l_shtani += 1

print(maiki_best, shtani_best, sep=' ')
