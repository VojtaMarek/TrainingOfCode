
class Game:
    num: int = 0
    hand = None

class Hand:
    blue: int = 0
    green: int = 0
    red: int = 0


def parse_input(input_file='input.txt'):
    with open(input_file, 'r') as f:
        input_ = f.read().splitlines()
    games: list[Game] = []
    for line in input_:
        game = Game()
        _, raw_num, sets = line.split(' ', 2)
        game.num = int(raw_num[:-1])
        game.hand = Hand()
        for set_ in sets.split(';'):
            for color in set_.split(','):
                if 'blue' in color:
                    game.hand.blue = max(int(color.strip().split()[0]), game.hand.blue)
                elif 'green' in color:
                    game.hand.green = max(int(color.strip().split()[0]), game.hand.green)
                elif 'red' in color:
                    game.hand.red = max(int(color.strip().split()[0]), game.hand.red)
        games.append(game)
    return games


in_the_bag = (0, 14, 13, 12)
res = 0
for game in parse_input():
    in_a_game = (game.num, game.hand.blue, game.hand.green, game.hand.red)
    if any(in_a_game[i] > in_the_bag[i] for i in range(1, 4)):
        continue
    res += game.num
print('part1: ', res)


res = 0
for game in parse_input():
    power = game.hand.blue * game.hand.green * game.hand.red
    res += power
print('part2: ', res)