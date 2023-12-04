
class Game:
    num: int = 0
    winning: list[int] = []
    hand: list[int] = []
    score = 0


def parse_input(input_file='input.txt'):
    with open(input_file, 'r') as f:
        input_ = f.read().splitlines()
    games: list[Game] = []
    for line in input_:
        game = Game()
        _, raw_num, sets = line.split(None, 2)
        winning, hand = sets.split('|', 1)
        game.winning = winning.split()
        game.hand = hand.split()
        points = 0
        for num in game.hand:
            if num in set(game.winning) and num:
                game.num = int(raw_num[:-1])
                if points == 0:
                    points += 1
                else:
                    points *= 2
        game.score = points
        
        games.append(game)
    return games


res = 0
for game in parse_input():
    res += game.score
print('part1: ', res)
