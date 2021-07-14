n = int(input())

s = set()
for _ in range(n):
    s.add(input())

mistakes = 0
for word in input().split():
    if word in s:
        continue

    counter = 0
    for ch in word:
        if ch.isupper():
            counter += 1

    if counter == 1:
        continue

    mistakes += 1

print(mistakes)
