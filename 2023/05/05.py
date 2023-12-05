class Line:
    def __init__(self):
        self.relation = None

    def add(self, input_):
        to_ = int(input_.split()[0])
        from_ = int(input_.split()[1])
        length = int(input_.split()[2])
        self.relation = dict()
        for i in range(length):
            self.relation[from_+i] = to_+i
        return self.relation



def parse_input(input_file='input.txt'):
    with open(input_file, 'r') as f:
        input_lines = f.read().splitlines()

        seeds = input_lines[0].split()[1:]

        groups = dict()
        group_num = 0
        group = False
        for i in range(1, len(input_lines)):
            if group and input_lines[i] != '' and input_lines[i].split()[0].isnumeric():
                if groups[group_num]:
                    groups[group_num].update(line.add(input_lines[i]))
                else:
                    groups[group_num] = line.add(input_lines[i])
            if input_lines[i] == '':
                group = True
                group_num += 1
                groups[group_num] = []
                line = Line()
    return groups, seeds


groups, seeds = parse_input()
seeds_paths = []
for seed in seeds:
    seed_path = [int(seed)]
    for group in groups.values():
        seed_path.append(group.get(seed_path[-1], seed_path[-1]))
    seeds_paths.append(seed_path)

res = [x[-1] for x in seeds_paths]

print('part1. ', min(res))
