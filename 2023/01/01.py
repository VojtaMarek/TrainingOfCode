

numbers_dict = {
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9
}


def translate_word_to_number(word):
    return f"{word[0]}{numbers_dict.get(word)}{word[-1]}"


def parse_input(input_file='input.txt'):
    with open(input_file, 'r') as f:
        input_ = f.read().splitlines()
    return input_


def main(part2=False):
    output = []
    for w in parse_input():
        num_str = ''

        if part2:
            for j in numbers_dict.keys():
                if j in w:
                    w = w.replace(j, str(translate_word_to_number(j)))

        for i in w:
            if i.isnumeric():
                num_str += i
        num_str = num_str[0] + num_str[-1]
        output.append(int(num_str))
    return output


print("part1: ", sum(main()))
print("part2: ", sum(main(part2=True)))
