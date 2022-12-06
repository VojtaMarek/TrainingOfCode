import os
PATH = os.path.dirname(os.path.realpath(__file__))


def get_sums(test=False):
    
    if test: _test = '_test'
    else: _test = ''

    with open(f'{PATH}\\input{_test}.txt', 'rt') as f:
        lines = f.read().split('\n\n')
        for i, line in enumerate(lines):
            lines[i] = sum(map(int, line.split('\n')))
        return lines


if __name__ == '__main__':
    
    sums = sorted(get_sums(test=1), reverse=True)
    print('Part one(test):', sums[0])
    print('Part two(test):', sum(sums[0:3]))
    
    
    sums = sorted(get_sums(), reverse=True)
    print('Part one:', sums[0])
    print('Part two:', sum(sums[0:3]))