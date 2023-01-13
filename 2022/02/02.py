import os
PATH = os.path.dirname(os.path.realpath(__file__))


def get_rounds(test=False):
    
    if test: _test = '_test'
    else: _test = ''

    with open(f'{PATH}\\input{_test}.txt', 'rt') as f:
        lines = f.read().split('\n')
        return lines



def get_points_part1(rounds):
    
    points = 0
    for round in rounds:
        oponent = round[0]
        you = round[-1]

        if you == 'X':
            points += 1
            if oponent == 'A': points += 3
            elif oponent == 'C': points += 6
        if you == 'Y':
            points += 2
            if oponent == 'B': points += 3
            elif oponent == 'A': points += 6
        if you == 'Z':
            points += 3
            if oponent == 'C': points += 3
            elif oponent == 'B': points += 6
    
    return points


def get_points_part2(rounds):
    
    points = 0
    for round in rounds:
        oponent = round[0]
        you = round[-1]

        if you == 'X': #lose
            points += 0
            if oponent == 'A': points += 3 #rock
            elif oponent == 'B': points += 1 #paper
            elif oponent == 'C': points += 2 #scissors
        if you == 'Y': #draw
            points += 3
            if oponent == 'A': points += 1 #rock
            elif oponent == 'B': points += 2 #paper
            elif oponent == 'C': points += 3 #scissors
        if you == 'Z': #win
            points += 6
            if oponent == 'A': points += 2 #rock
            elif oponent == 'B': points += 3 #paper
            elif oponent == 'C': points += 1 #scissors
    
    return points



if __name__ == '__main__':
    
    print('Part one(test):', get_points_part1(get_rounds(test=1)))
    print('Part one:', get_points_part1(get_rounds()))
    
    print('Part one(test):', get_points_part2(get_rounds(test=1)))
    print('Part one:', get_points_part2(get_rounds()))