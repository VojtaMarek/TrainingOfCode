COLUMNS = 12

def load_file():
    with open('c:\\Users\\VM\\Documents\\CODE\\01\\adventofcode\\2021\\03\\data.txt', 'rt') as f:
        lines = f.read().splitlines()
        return lines

def get_column(lines = [], column_num = 0):
    column = [] 
    for i, line in enumerate(lines):
        column.append(line[column_num])
    return column

def gass(first_att, second_att, gass_lines=load_file()):

    gass_lines = load_file()
    gass_column = []

    for column in range(COLUMNS):

        print(gass_lines)

        if len(gass_lines) == 1: break
        gass_column = get_column(gass_lines, column)
        gass_killer = ''
        
        ones, zeros = gass_column.count(first_att), gass_column.count(second_att)
        print(ones, zeros)
        if ones > zeros: gass_killer = '0'
        elif ones == zeros: gass_killer = second_att
        else: gass_killer = '1'

        # gass_lines_copy = gass_lines
        # for i, line in enumerate(gass_lines_copy):
        #     if line[column] == gass_killer:
        #         gass_lines.pop(i)
        #         #print(gass_lines[column])
        gass_lines = [line for line in gass_lines if line[column] != gass_killer]
        
        print(gass_column)
    print('final', gass_lines)
    return gass_lines


def gass(first_att, second_att, gass_lines=load_file()):

    gass_lines = load_file()
    gass_column = []

    for column in range(COLUMNS):

        print(gass_lines)

        if len(gass_lines) == 1: break
        gass_column = get_column(gass_lines, column)
        gass_killer = ''
        
        ones, zeros = gass_column.count(first_att), gass_column.count(second_att)
        print(ones, zeros)
        if ones > zeros: gass_killer = '0'
        elif ones == zeros: gass_killer = second_att
        else: gass_killer = '1'

        # gass_lines_copy = gass_lines
        # for i, line in enumerate(gass_lines_copy):
        #     if line[column] == gass_killer:
        #         gass_lines.pop(i)
        #         #print(gass_lines[column])
        gass_lines = [line for line in gass_lines if line[column] != gass_killer]
        
        print(gass_column)
    print('final', gass_lines)
    return gass_lines



#___________________un-used code below_________________________________


def get_column_(lines, columns = COLUMNS):
    for column in range(columns):
        c = []
        for line in lines:
            c.append(line[column])
        yield c
        # yield [c.append(line[column]) for line in lines] PROČ NEFUNGUJE: ???


# PS C:\Users\VM\Documents\CODE\01\AdventOfCode> & C:/Users/VM/AppData/Local/Programs/Python/Python310/python.exe c:/Users/VM/Documents/CODE/01/adventofcode/2021/03/03_2.py
# ['0', '1', '1', '1', '1', '0', '0', '1', '1', '1', '0', '0']
# ['0', '1', '0', '0', '0', '1', '0', '1', '0', '1', '0', '1']
# ['1', '1', '1', '1', '1', '1', '1', '1', '0', '0', '0', '0']
# ['0', '1', '1', '1', '0', '1', '1', '0', '0', '0', '1', '1']
# ['0', '0', '0', '1', '1', '1', '1', '0', '0', '1', '0', '0']
# ['00100', '11110', '10110', '10111', '10101', '01111', '00111', '11100', '10000', '11001', '00010', '01010']
# PS C:\Users\VM\Documents\CODE\01\AdventOfCode> & C:/Users/VM/AppData/Local/Programs/Python/Python310/python.exe c:/Users/VM/Documents/CODE/01/adventofcode/2021/03/03_2.py
# [None, None, None, None, None, None, None, None, None, None, None, None]
# [None, None, None, None, None, None, None, None, None, None, None, None]
# [None, None, None, None, None, None, None, None, None, None, None, None]
# [None, None, None, None, None, None, None, None, None, None, None, None]
# [None, None, None, None, None, None, None, None, None, None, None, None]
# ['00100', '11110', '10110', '10111', '10101', '01111', '00111', '11100', '10000', '11001', '00010', '01010']





# def gass_cal_(first_att, second_att, gass_lines=load_file()):
#     i = 0
    
#     for column in get_column(gass_lines, column):
#         print(gass_lines)

#         gass_killer = ''

#         # print(column)
        
#         ones = column.count(first_att)
#         zeros = column.count(second_att)
#         print(ones, zeros)
        
#         if ones > zeros: gass_killer = '0'
#         elif ones == zeros == 1: gass_killer = '0'
#         else: gass_killer = '1'
        
        

#         gass_lines = [line for line in gass_lines if line[i] != gass_killer]

#         if len(gass_lines) == 1: break

#         i += 1

#     print(gass_lines)
#     return gass_lines