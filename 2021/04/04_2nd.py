"""
--- Day 4: Giant Squid --- 2021
https://adventofcode.com/2021/day/4
"""


import copy

def load_file():
    with open('c:\\Users\\VM\\Documents\\CODE\\01\\adventofcode\\2021\\04\\data.txt', 'rt') as f:
        lines = f.read().splitlines()
        return lines


def check_bingo(board):
    for line in board:
        if all(x[0]=='(' for x in line):
            #print('Bingo line.')
            return True
    for i in range(5):
        column = []
        for line in board:
            column.append(line[i])
        if all(x[0]=='(' for x in column):
            #print('Bingo column.')
            return True


def get_sum(board):
    total = 0
    for line in board:
        for ch in line:
            if not ch[0]=='(':
                total += int(ch)
    return total


def mark_board(num, board):
    for l, line in enumerate(board):
        for i, item in enumerate(line):
            if item == num:
                board[l][i] = '('+item+')'  
    return board

def main():
    file_lines = load_file()

    # get new num
    first_line = file_lines[0]
    first_line_list = []
    first_line_list = first_line.split(',')
    for num in first_line_list:
        print(num, '- ', end='')
    print('\n')

    # get boards
    boards_list = []
    flag = True
    for i, line in enumerate(file_lines):
        board = []
        if line == '':
            board_line = []
            for line in file_lines[i+1:i+6]:
                board_line.append(line.split())
            board.append(board_line)
            # print('B: ', board[0])
            flag = True
        else: flag = False
        if flag:
            boards_list.append(board[0])
    
    boards_list_backup = copy.deepcopy(boards_list)

    # loop to play bingo


    count_bingos = 0
    flag = False
    
    

    for num in first_line_list:
        #reset = True
        bingo_boards = []        
        for b, board in enumerate(boards_list):
            #while reset:
            boards_list[b] = mark_board(num, board)
            
            # if (len(boards_list_backup) - count_boards) == 1:         
            #     flag = True

            if check_bingo(board):
                
                sum_board = get_sum(board)
                print(f'{num} - BINGO on board position: {b}, RESULT: {num} * {sum_board} = {int(num)*sum_board}' )
                # print(board)
                # the content insted of break statement

                count_bingos += 1
                #boards_list = boards_list[b].append('x')
                
                bingo_boards.append(b)
                flag = True
                #reset = True
                #break
            
            else:
                pass
                #print(f'{num} No bingo for this board.')
                #print(boards_list)
                #reset = False
        if flag:
            adjust_index = 0
            for board_index in bingo_boards:
                boards_list.pop(board_index-adjust_index)
                adjust_index += 1
            #print(boards_list)
            if len(boards_list) <= 0:
                print(f'>>>>>>>>>>>>>>>That was the last one!<<<<<<<<<<<<<<<<<< {num} * {sum_board} = {int(num)*sum_board}')
                break
        flag = False
        print(f'{num} - {flag}')

        #print(boards_list)
        # print(f'{num} - Done')
        # #else:   # when the loop is not breaked, the else content is executed.
        # if flag: # case when all bingos are done
        #     break
        # #continue



if __name__ == '__main__':
    main()
