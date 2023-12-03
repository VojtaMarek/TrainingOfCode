
class Position:
    x: int
    y: int


class Number:
    def __init__(self, num_str: str, start_pos: Position, is_valid=False):
        self.num_str: str = num_str
        self.start_pos = start_pos
        self.end_pos = self.get_end_pos()
        self.is_valid: bool = is_valid

    def get_end_pos(self):
        end_pos = Position()
        end_pos.x = self.start_pos.x + len(self.num_str)
        end_pos.y = self.start_pos.y
        return end_pos


class Symbol:
    def __init__(self, character, pos: Position):
        self.character: str = character
        self.pos: Position = pos
        self.start_pos = self.get_start_pos()
        self.end_pos = self.get_end_pos()

    def get_start_pos(self):
        end_pos = Position()
        end_pos.x = self.pos.x - 1
        end_pos.y = self.pos.y - 1
        return end_pos

    def get_end_pos(self):
        end_pos = Position()
        end_pos.x = self.pos.x + 2
        end_pos.y = self.pos.y + 2
        return end_pos


def parse_input(input_file='input.txt'):
    with open(input_file, 'r') as f:
        input_lines = f.read().splitlines()
        # input_lines.split('.')
    return input_lines


def create_grid(collection):
    x, y = 0, 0
    for i in collection:
        x = max(x, i.end_pos.x)
        y = max(y, i.end_pos.y)
    grid = [(x*'.') for _ in range(y)]
    return grid


collection = []
for y, line in enumerate(parse_input()):
    x = 0
    is_still_num = False
    for record in line:
        pos = Position()
        pos.x, pos.y = x, y
        match record:
            case '.':
                is_still_num = False
            case _ if record.isdigit() and is_still_num:
                collection[-1].num_str += record
                collection[-1].end_pos.x += 1
            case _ if record.isdigit() and not is_still_num:
                number = Number(record, pos)
                collection.append(number)
                is_still_num = True
            case _:
                is_still_num = False
                symbol = Symbol(record, pos)
                collection.append(symbol)
        x += 1

grid = create_grid(collection)
for y, line in enumerate(grid):
    for record in collection:
        range_y = range(record.start_pos.y, record.end_pos.y)
        range_x = range(record.start_pos.x, record.end_pos.x)
        if isinstance(record, Symbol) and y in range_y:
            grid[y] = grid[y][:record.start_pos.x] + record.character * len(range_x) + grid[y][record.end_pos.x:]


def print_grid(grid_):
    for i in grid_:
        print(i)


print_grid(grid)


res = []
for y, line in enumerate(grid):
    for record in collection:
        range_y = range(record.start_pos.y, record.end_pos.y+1)
        range_x = range(record.start_pos.x, record.end_pos.x+1)
        if isinstance(record, Number) and y in range_y:
            for ch in line[record.start_pos.x:record.end_pos.x]:
                if not ch.isdigit() and not ch == '.':
                    res.append(int(record.num_str))
                    break
print(res)
print('par1: ', sum(res))
