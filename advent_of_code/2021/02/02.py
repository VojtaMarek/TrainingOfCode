

total_distance = 0
depth = 0
aim = 0

with open('c:\\Users\\VM\\Documents\\CODE\\01\\adventofcode\\2021\\02\\data.txt', 'rt') as f:
    lines = f.read().splitlines()
    for line in lines:
        direction = line[0]
        distance = int(line[-1])
        print(direction, distance)

        if direction == 'f':
            total_distance += distance
            depth += distance*aim
        elif direction == 'd': aim += distance
        elif direction == 'u': aim -= distance

print(total_distance, depth, total_distance*depth)