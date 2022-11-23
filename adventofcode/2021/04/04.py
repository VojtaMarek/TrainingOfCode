
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
    fileLines = load_file()

    # get new num
    firstLine = fileLines[0]
    firstLineList = []
    firstLineList = firstLine.split(',')
    for num in firstLineList:
        print(num, '- ', end='')
    print('\n')

    # get boards
    boardsList = []
    flag = True
    for i, line in enumerate(fileLines):
        board = []
        if line == '':
            boardLine = []
            for line in fileLines[i+1:i+6]:
                boardLine.append(line.split())
            board.append(boardLine)
            # print('B: ', board[0])
            flag = True
        else: flag = False
        if flag:
            boardsList.append(board[0])
    
    boardsListBackup = copy.deepcopy(boardsList)

    # loop to play bingo
    for num in firstLineList:
        for b, board in enumerate(boardsList):
            for l, line in enumerate(board):
                for i, item in enumerate(line):
                    if item == num:
                        boardsList[b][l][i] = 'x'   
        
            if check_bingo(boardsList[b]):
                
                sum_board = get_sum(boardsList[b])
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
