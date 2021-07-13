d = {}

with open('/home/lev/Study/YandexAlgoTraining/input.txt', 'r') as f:
    for l in f:
        if l[-1] == '\n':
            l = l[:-1]
        spl = l.split(' ')
        for word in spl:
            if word == '':
                continue
            if word not in d:
                d[word] = 0
            d[word] += 1

min = -1
best_key = ''
for key, value in d.items():
    if value < min or min == -1:
        min = value
        best_key = key
    elif value == min and key < best_key:
        best_key = key

print(best_key)
