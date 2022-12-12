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


# def count_sum(items, folder_name="", sum=0):
#     for i, item in enumerate(items):
#         if isinstance(item, list):
#             folder_name = item
#             count_sum(item, folder_name, sum)
#         else:
#             if isinstance(item, int):
#                 sum += item
#             elif i != 0:
#                 print(item)
#                 #sum += count_sum(items, folder_name, sum)[1]

#     return (sum)


def count_sum(lst, folder_name="", sum=0, sums=[]):
    for item in lst:
        if isinstance(item, list):
            count_sum(item, folder_name, sum)
        elif isinstance(item, int):
            sum += item
        else:
            folder_name = item

    print(f"Folder name: {folder_name} ", end="")
    print(f"Sum: {sum}")
    if sum <= 100000:
        print(f"::{sum}")
        # print("smaller than 100000!")
        sums.append(sum)
    return sums


def main(lines):
    drive = get_drive(lines)

    count_sum(drive)

    # print(sums)

    return drive
    
if __name__ == '__main__':

    print(f"Part one: {main(get_lines(test=True))}")