
def getLines():
    with open('input.txt', 'rt') as f:
        lines = f.read().splitlines()
        return lines

count = 0

num0 = 483
first_element, second_element, thirth_element = 148, 167, 168
for index, line in enumerate(getLines(), start=1):
    if index % 3 == 1:
        first_element = int(line)
    if index % 3 == 2:
        second_element = int(line)
    if index % 3 == 0:
        thirth_element = int(line)
    num1 = first_element + second_element + thirth_element
    print(first_element, second_element, thirth_element)
    print(num1, num0)
    if num1 > num0:
        print('Increased')
        count += 1
    num0 = num1

print('Count is: ', count)