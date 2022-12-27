import os
PATH = os.path.dirname(os.path.realpath(__file__))
from copy import deepcopy

def get_line(test=False):
    
    if test: _test = '_test'
    else: _test = ''

    with open(f'{PATH}\\input{_test}.txt', 'rt') as f:
        line = f.read().split('\n')
        return line

def hide_tree(tree, another_trees):
    highest_tree = sorted(another_trees)[-1]
    if int(tree) <= int(highest_tree):
        return True
    return False

def count_trees(trees_list):
    count = 0
    for line in trees_list:
        for character in line:
            if character == '_':
                pass
            else: count += 1
    return count

def main_part_1(trees_list):
    visible_trees = deepcopy(trees_list)
    for line_pos, trees_line in enumerate(trees_list):
        for ch_pos, tree in enumerate(trees_line):
            flag = False
            if (line_pos-1)<0 or (ch_pos-1)<0 or (line_pos+1)>=len(trees_list) or (ch_pos+1)>=len(trees_line):
                flag = False
                continue

            # horizontal:
            index_ch = int(ch_pos)
            trees_1, trees_2 = trees_line[:index_ch], trees_line[index_ch+1:] # left, right

            # vertical:
            index_line = int(line_pos)
            trees_vertical = ''.join([line[ch_pos] for line in trees_list]) 
            trees_3, trees_4 = trees_vertical[:index_line], trees_vertical[index_line+1:] # up, down
            
            flag = hide_tree(tree, trees_1) and hide_tree(tree, trees_2) and hide_tree(tree, trees_3) and hide_tree(tree, trees_4)

            if flag:
                index = int(ch_pos)
                line = visible_trees[int(line_pos)]
                visible_trees[int(line_pos)] = line[:index]+'_'+line[index+1:]


    # print(trees_list)
    # print(visible_trees)

    return count_trees(visible_trees)

def count_trees_part2(tree, another_trees):
    count = 0
    for i in another_trees:
        if tree <= i:
            count += 1
            return count
        else:
            count += 1
    return int(len(another_trees))


def turn_list(str_in):
    str_out = ""
    for i, ch in enumerate(str_in):
        str_out += str_in[-1*(i+1)]
    return str_out


def main_part_2(trees_list):
    visible_trees = deepcopy(trees_list)
    count_list = []
    for line_pos, trees_line in enumerate(trees_list):
        for ch_pos, tree in enumerate(trees_line):
            count = 0
            if (line_pos-1)<0 or (ch_pos-1)<0 or (line_pos+1)>=len(trees_list) or (ch_pos+1)>=len(trees_line):
                continue

            # horizontal:
            index_ch = int(ch_pos)
            trees_1, trees_2 = trees_line[:index_ch], trees_line[index_ch+1:] # left, right

            # vertical:
            index_line = int(line_pos)
            trees_vertical = ''.join([line[ch_pos] for line in trees_list]) 
            trees_3, trees_4 = trees_vertical[:index_line], trees_vertical[index_line+1:] # up, down
            
            count = count_trees_part2(tree, turn_list(trees_1)) * count_trees_part2(tree, trees_2) * count_trees_part2(tree, turn_list(trees_3)) * count_trees_part2(tree, trees_4)
            count_list.append(count)

    return sorted(count_list)[-1]


if __name__ == '__main__':
    print(f"Part one: {main_part_1(get_line(test=False))}")
    print(f"Part two: {main_part_2(get_line(test=False))}")