
import copy

def load_file():
    with open('c:\\Users\\VM\\Documents\\CODE\\01\\adventofcode\\2021\\04\\data_example.txt', 'rt') as f:
        lines = f.read().splitlines()
        return lines


def check_bingo(board):
    for line in board:
        if all(x=='x' for x in line):
            return True
    for i in range(5):
        column = []
        for line in board:
            column.append(line[i])
        if all(x=='x' for x in column):
            return True

def get_sum(board):
    total = 0
    for line in board:
        for ch in line:
            if ch != 'x':
                total += int(ch)
    return total


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
    for num in first_line_list:
        for b, board in enumerate(boards_list):
            for l, line in enumerate(board):
                for i, item in enumerate(line):
                    if item == num:
                        boards_list[b][l][i] = 'x'   
        





            if check_bingo(board):
                
                sum_board = get_sum(board)
                print(f'{num} - Done, BINGO on board: {b}, RESULT: {num} * {sum_board} = {int(num)*sum_board}' )
                
                break

        else:   # when the loop is not breaked, the else content is executed.
            print(f'{num} - Done')
            continue
        break
    

    # get sum
    # print(boardsList[b])
    # sum_board = get_sum(boardsList[b])
    # print(sum_board, num, int(num)*sum_board)




if __name__ == '__main__':
    main()
