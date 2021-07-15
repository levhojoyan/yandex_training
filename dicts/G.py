from collections import defaultdict

with open('input.txt', 'r') as f:
    d = defaultdict(int)
    for line in f:
        spl = line.split()
        op = spl[0]

        if op == 'DEPOSIT':
            name, summ = spl[1:]
            summ = int(summ)

            d[name] += summ
        elif op == 'WITHDRAW':
            name, summ = spl[1:]
            summ = int(summ)

            d[name] -= summ
        elif op == 'BALANCE':
            name = spl[1]
            if name not in d:
                print('ERROR')
            else:
                print(d[name])
        elif op == 'TRANSFER':
            name1, name2, summ = spl[1:]
            summ = int(summ)

            d[name2] += summ
            d[name1] -= summ

        elif op == 'INCOME':
            p = int(spl[1])
            for key in d.keys():
                if d[key] > 0:
                    d[key] = int(d[key] * (1 + p / 100))
