from itertools import product
import os
PATH = os.path.dirname(os.path.realpath(__file__))

def get_lines(test=False):
    
    if test: _test = '_test'
    else: _test = ''

    with open(f'{PATH}\\input{_test}.txt', 'rt') as f:
        lines = f.read().split('\n')
        return lines


def get_drive(lines):
    """[0] - name of folder, [1+] - files and folders inside"""
    drive = ["/"]
    dir = ""
    nested_path = "drive"
    dir_no = 0
    for line in lines:
        if line.startswith("$ cd"):
            if line == "$ cd ..":
                # move backwards
                nested_path = nested_path.rsplit('[', 1)[0]
            else:
                # create new file
                dir = line[5:]
                for i, position in enumerate(eval(f"{nested_path}")):
                    if isinstance(position, list):
                        if dir == position[0]:
                            dir_no = i             
                if dir != "/":
                    nested_path += f"[{dir_no}]"
        elif line == "$ ls":
            file_no = 0
            continue
        elif line.startswith("dir"):
            file_no += 1
            new_dir = line[4:]
            exec(f"{nested_path}.append(['{new_dir}'])")
        else:
            file_no += 1
            num = int(line.split(" ")[0])
            # print(f"{nested_path}.append(line.split(" ")[0])")
            exec(f"{nested_path}.append({num})")
    return drive

SUMS = 0
SUM_LIST = []

def count_sum(lst, folder_name=""):
    sum = 0
    global SUMS
    global SUM_LIST
    folder_name = lst[0]
    for item in lst[1:]:
        if isinstance(item, list):
            sum += count_sum(item, folder_name)
        elif isinstance(item, int):
            sum += item


    # print(f"Folder name: {folder_name} ", end="")
    # print(f"Sum: {sum}")
    if sum <= 100000:
        # print(f"::{sum}")
        # print("smaller than 100000!")
        SUMS += sum
    SUM_LIST.append(sum)
    return sum


def main(lines):
    drive = get_drive(lines)
    count_sum(drive)


if __name__ == '__main__':
    main(get_lines(test=False))
    SUM_LIST.sort()

    space = SUM_LIST[-1] - 70000000 + 30000000
    #print(space)
    print(f"Part one: {SUMS}")
    # print(f"List of sums: {SUM_LIST}")
    for sum in SUM_LIST:
        if sum > space:
            print(f'Part two: {sum}')
            break

