# passed with Pypy only

import collections

g, s = list(map(int, input().split()))

W = input()

S = input()

d = dict(collections.Counter(W))

cur_d = dict(collections.Counter(S[:len(W)]))

counter = 0

if d == cur_d:
    counter += 1

for i in range(len(W), len(S)):
    cur_char = S[i]
    if cur_char not in cur_d:
        cur_d[cur_char] = 0

    cur_d[cur_char] += 1

    cur_d[S[i - len(W)]] -= 1

    if cur_d[S[i - len(W)]] == 0:
        del cur_d[S[i - len(W)]]

    if d == cur_d:
        counter += 1

print(counter)
