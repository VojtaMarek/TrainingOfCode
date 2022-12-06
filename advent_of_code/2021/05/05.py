

def load_file():
    with open('c:\\Users\\VM\\Documents\\CODE\\01\\adventofcode\\2021\\05\\data_example.txt', 'rt') as f:
        lines = f.read().splitlines()
        return lines

def get_commands():
    commands = []
    lst = []
    for command in load_file():
        tmp_record = command.split(' -> ')
        record = [tmp_record[0].split(','), tmp_record[1].split(',')]
        commands.append(record)
    return commands

def write_vertical(space, x, y1, y2):
    if y2 < y1:
        y1, y2 = y2, y1
    #length = x2 - x1
    #column = space[x]
    for n in range(int(y1), int(y2)+1):
        space[n][int(x)] += 1
    return space

def write_horizontal(space, y, x1, x2):
    if x2 < x1:
        x1, x2 = x2, x1
    #length = x2 - x1
    line = space[y]
    for n in range(x1, x2+1):
        line[n] += 1
    return space



def main():
    size = 10
    space = []
    space_line = [int(0) for x in range(size)]
    for _ in range(size):
        space.append([int(0) for x in range(size)])



    list_commands = get_commands()
    for line in list_commands:
        x1, y1, x2, y2 = line[0][0], line[0][1], line[1][0], line[1][1]
        if x1 == x2:
            write_vertical(space, x1, y1, y2)
        if y1 == y2:
            pass
            write_horizontal(space, int(y1), int(x1), int(x2))
        else:
            pass
            #print('no use')

    sum = 0
    for line in space:
        print(line)
        for i in line:
            if i >= 2:
                sum += 1
    print(sum)

if __name__ == '__main__':
    main()

