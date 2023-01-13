import os
PATH = os.path.dirname(os.path.realpath(__file__))


def get_line(test=False):
    
    if test: _test = '_test'
    else: _test = ''

    with open(f'{PATH}\\input{_test}.txt', 'rt') as f:
        line = f.read()
        return line


def main(line):
    total = 0
    marker = ['' for _ in range(14)]
    for pos, ch_input in enumerate(line):
        marker = line[pos:pos+14]
                
        if len(marker) == len(set(marker)):
            #print(marker, pos, total)
            return pos+14


if __name__ == '__main__':

    input_test = "nppdvjthqldpwncqszvftbrmjlhg"
    print(f"Part two(test): {main(input_test)}")

    print(f"Part two: {main(get_line())}")