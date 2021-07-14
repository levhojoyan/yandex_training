n = int(input())

d = {}
for _ in range(n):
    s = input()
    lower = s.lower()
    if lower not in d:
        d[lower] = set()
    d[lower].add(s)

mistakes = 0
for word in input().split():
    counter = 0
    for ch in word:
        if ch.isupper():
            counter += 1

    if counter != 1:
        mistakes += 1
        continue

    lower = word.lower()
    if lower in d:
        if word not in d[lower]:
            mistakes += 1


print(mistakes)
