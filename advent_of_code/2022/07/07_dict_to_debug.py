import os
PATH = os.path.dirname(os.path.realpath(__file__))

def get_lines(test=False):
    
    if test: _test = '_test'
    else: _test = ''

    with open(f'{PATH}\\input{_test}.txt', 'rt') as f:
        lines = f.read().split('\n')
        return lines


def get_drive(lines):
    drive = [dict()]
    dir, nested_path = "", "drive"
    file_no = 0
    new_dir = "/_0"
    for line in lines:
        if line.startswith("$ cd"):
            if line == "$ cd ..":
                # move back in list
                nested_path = nested_path.rsplit('][', 2)[0]+"]"
            else:
                # create new file
                dir = line[5:]
                dir = dir + "_" + str(file_no)
                for i in eval(f"{nested_path}"):
                    print(f"{nested_path}[{dir}][{i}].keys()")
                    if isinstance(i, type(str)): pass
                    elif dir in eval(f"{nested_path}[{i}].keys()"):
                        file_no = (list(eval(nested_path)).index().startswith(dir))

                #file_no = dir.split("_")[1]
                
                nested_path += f"[{file_no}]['{dir}']"
                exec(f"{nested_path} = []")
                # eval(f"{nested_path}.append({{dir: []}})")

                print(f"{nested_path} = []")
                
                print(nested_path)
                

        elif line == "$ ls":
            file_no = -1
            continue
        elif line.startswith("dir"):
            file_no += 1
            new_dir = line[4:] + "_" + str(file_no)
            print(f"""{nested_path}.append(dict({new_dir}=None))""")
            exec(f"""{nested_path}.append(dict({new_dir}=None))""")
        else:
            file_no += 1
            exec(f"{nested_path}.append(line.split(" ")[0])")
        print("Drive:", drive)
    print("path:", nested_path)
    return drive


def main(lines):
    drive = get_drive(lines)

    

    return drive

if __name__ == '__main__':

    print(f"Part one: {main(get_lines(test=True))}")