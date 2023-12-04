class Game:
    num: int = 0
    winning: list[int] = []
    hand: list[int] = []
    copies: int = 1


def parse_input(input_file='input.txt'):
    with open(input_file, 'r') as f:
        input_ = f.read().splitlines()
    games: list[Game] = []
    for line in input_:
        game = None
        game = Game()
        _, raw_num, sets = line.split(None, 2)
        winning, hand = sets.split('|', 1)
        game.winning = winning.split()
        game.hand = hand.split()
        game.num = int(raw_num[:-1])
        games.append(game)

    for i, game in enumerate(games):
        for _ in range(game.copies):
            points = 0
            for num in game.hand:
                if num in set(game.winning) and num:
                    points += 1
            for point in range(1, points+1):
                if i+point >= len(games):
                    continue
                games[i+point].copies += 1
        print(i)            
    return games


res = 0
for game in parse_input():
    res += game.copies
print('part2: ', res)
