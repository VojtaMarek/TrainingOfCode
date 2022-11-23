
list_ = [['69', 'x', 'x', 'x', 'x'], ['x', '60', '62', '83', 'x'], ['5', '21', 'x', 'x', 'x'], ['x', 'x', '15', 'x', '24'], ['x', '10', 'x', 'x', 'x']]

sum = 0

for line in list_:
    for ch in line:
        if ch == 'x':
            continue
        sum += int(ch)

print(sum)