with open('input.txt') as f:
    s = set(map(int, f.readline().split(' '))).intersection(set(map(int, f.readline().split(' '))))

l = sorted(list(s))

with open('output.txt', 'w') as f2:
    for number in l:
        f2.write(str(number) + " ")
