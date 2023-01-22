
def parse_input():
    with open("2016//01//input.txt") as f:
        return f.readline().split(", ")


def change_position(initial_coordinates, instruction, direction, direction_lock=False):
    directions = ["N", "E", "S", "W"]
    if direction_lock: pass
    elif instruction[0] == "R":
        direction += 1
    elif instruction[0] == "L":
        direction += 3
    
    direction = direction % 4
    [x, y] = initial_coordinates

    if direction == 0: x += int(instruction[1:])
    elif direction == 1: y += int(instruction[1:])
    elif direction == 2: x -= int(instruction[1:])
    elif direction == 3: y -= int(instruction[1:])

    # print(directions[direction], [x, y],'| ' , end='')
    

    return [x, y], direction

def main_part_one():
    position = [0, 0]
    direction = 0
    for instruction in parse_input():
        position, direction = change_position(position, instruction, direction)

    return (position[0]) + (position[1])


def main_part_two():
    position = [0, 0]
    positions = [position]
    direction = 0
    flag = False
    for instruction in parse_input():
        # print(f"\n:: {instruction}")
        direction_lock = False
        for step in range(int(instruction[1:])):
            step = instruction[0]+"1"      
            position, direction = change_position(position, step, direction, direction_lock)
            for i in positions:
                if i == position:
                    # print('!!!', position)
                    flag = True
                    break
            if flag: break
            positions.append(position)
            direction_lock = True
        if flag: break
    return abs(position[0]) + abs(position[1])



if __name__ == "__main__":
    print("Part one: ", main_part_one())
    print("Part two: ", main_part_two())