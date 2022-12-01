def get_sums():
    with open('AdventOfCode\\2022\\01\\input.txt', 'rt') as f:
        lines = f.read().split('\n\n')
        for i, line in enumerate(lines):
            lines[i] = sum(map(int, line.split('\n')))
        return lines

def main():
    sums = get_sums()
    sums = sorted(sums, reverse=True)
    
    print('Part one:', sums[0])
    print('Part two:', sum(sums[0:3]))


if __name__ == '__main__':
    main()