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

    for i, line in enumerate(lines):
        if (i+2) >= len(lines):
            print("DONE")
            break
        if (i) % 3 == 0:
            rucksack1, rucksack2, rucksack3 = lines[i], lines[i+1], lines[i+2]
            print(rucksack1, rucksack2, rucksack3)

            for ch in rucksack1:
                if rucksack2.find(ch) != -1:
                    print("match2", ch, total)
                    if rucksack3.find(ch) != -1:
                        total += decode(ch)
                        print("match3", ch, total)
                        break


    return total


if __name__ == '__main__':
    print(f"Part two: {main(get_rounds())}")
    