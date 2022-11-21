power_consumption = 0

gamma_rate = ''
epsilon_rate = ''

def getLines():
    with open('c:\\Users\\VM\\Documents\\CODE\\01\\adventofcode\\2021\\03\\data.txt', 'rt') as f:
        lines = f.read().splitlines()
        return lines

lines = []
for line in getLines():
    characters = []
    for ch in line:
        characters.append(ch)
    lines.append(characters)


# print(lines)


for column in range(12):
    sequence = ''
    gamma_spoiler = ''
    epsilon_spoiler = ''
    for line in lines:
        #print(line[column])
        sequence += (line[column])
    if sequence.count('1') >= len(sequence)/2:
        #print(sequence.count('1'), len(sequence)/2)
        gamma_spoiler += '1'
        epsilon_spoiler += '0'
    else:
        gamma_spoiler += '0'
        epsilon_spoiler += '1'
    # see the sequences here and add to relevant rates:
    gamma_rate += str(gamma_spoiler)
    epsilon_rate += str(epsilon_spoiler)

    #print(gamma_spoiler, gamma_rate, epsilon_spoiler, epsilon_rate)
print(int(gamma_rate, 2), gamma_rate)# * epsilon_rate)
print(int(epsilon_rate, 2), epsilon_rate)

print(int(gamma_rate, 2)*int(epsilon_rate, 2))
