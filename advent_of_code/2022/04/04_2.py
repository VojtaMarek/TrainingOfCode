import os
PATH = os.path.dirname(os.path.realpath(__file__))


def get_rounds(test=False):
    
    if test: _test = '_test'
    else: _test = ''

    with open(f'{PATH}\\input{_test}.txt', 'rt') as f:
        lines = f.read().split('\n')
        for i, round in enumerate(lines):
            lines[i] = round.split(',')
        return lines


def main(rounds):
   
    for i, round in enumerate(rounds):
        rounds[i] = round[0].split('-') + round[1].split('-')

    total = 0
    for round in rounds:
        round = list(map(int, round))
        a1, a2, b1, b2 = round[0], round[1], round[2], round[3]
        if (b1 <= a1 <= b2) or (b1 <= a2 <= b2):
            print(f"{round} overlap")
            total += 1
        elif (a1 <= b1 <= a2) or (a1 <= b2 <= a2):
            print(f"{round} overlap2")
            total += 1
        else: print(f"{round} no overlap")



    return total


if __name__ == '__main__':
    print(f"Part two: {main(get_rounds())}")
    