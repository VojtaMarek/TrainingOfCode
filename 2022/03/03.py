import os
import string
PATH = os.path.dirname(os.path.realpath(__file__))


def get_rounds(test=False):
    
    if test: _test = '_test'
    else: _test = ''

    with open(f'{PATH}\\input{_test}.txt', 'rt') as f:
        lines = f.read().split('\n')
        return lines


def decode(ch):
    dic_ch_num = {}
    alphabet = string.ascii_lowercase + string.ascii_uppercase
    for i, letter in enumerate(alphabet):
        dic_ch_num[letter] = i+1
    
    return dic_ch_num[ch]



def main(lines):
    total = 0

    for line in lines:
        length_rucksack = int(len(line) / 2)
        rucksack1, rucksack2 = line[:length_rucksack], line[length_rucksack:]
        print(rucksack1, rucksack2)

        for ch in rucksack1:
            if rucksack2.find(ch) != -1:
                total += decode(ch)
                print("match", ch, total)
                break

    return total


if __name__ == '__main__':
    print(f"Part one: {main(get_rounds())}")
    