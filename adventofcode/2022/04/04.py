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
        print(round)
        a1, a2, b1, b2 = round[0], round[1], round[2], round[3]
        if a1 >= b1 and a2 <= b2:
            print(f"{round} match a in b")
            total += 1
        elif b1 >= a1 and b2 <= a2:
            print(f"{round} match b in a")
            total += 1
        else: print(f"{round} no match")



    return total


if __name__ == '__main__':
    print(f"Part one: {main(get_rounds())}")
    