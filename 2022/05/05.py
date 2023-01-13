import os
PATH = os.path.dirname(os.path.realpath(__file__))

STACK_MAX_IN = 9 #9
NO_STACKS = 8 #8

def get_lines(test=False):
    
    if test: _test = '_test'
    else: _test = ''

    with open(f'{PATH}\\input{_test}.txt', 'rt') as f:
        lines = f.read().split('\n')
        return lines


def move_stack(stacks, no_items, from_stack, to_stack):

    for i in range(no_items):
        #print(stacks[from_stack-1])
        item_to_move = (stacks[from_stack-1].pop(0))
        stacks[to_stack-1].insert(0, item_to_move)
    #print(stacks, a)

    return stacks



def get_moves(lines, stacks):
    lines = lines[NO_STACKS+2:]
    moves = []
    for line in lines:
        move = line.split()
        moves.append(move)
        no_items, from_stack, to_stack = int(move[1]), int(move[3]), int(move[5])
        
        print(stacks, no_items, from_stack, to_stack)
        stacks = move_stack(stacks, no_items, from_stack, to_stack)


    return stacks

def stack_max(stacks):
    max_len = 0
    for stack in stacks:
        if len(stack) > max_len:
            max_len = len(stack)

    return  max_len

def get_stacks(lines):
    
    stacks = []
    #max_len = STACK_MAX_IN
    for x in range(STACK_MAX_IN):
        stack = []
        for y in range(NO_STACKS, ):
            
            line = lines[y]
            letter = line[x*4+1]
            if letter != ' ':
                stack.append(letter)
        #print(stack)
        stacks.append(stack)
        #max_len = stack_max(lines)
    return(stacks)


def main(lines):
    stacks = get_stacks(lines)
    stacks = get_moves(lines, stacks)
    
    code = ''
    for stack in stacks:
        if stack != []:
            code += stack[0]
    
    
    return(code)

if __name__ == '__main__':
    print(f"Part one: {main(get_lines(test=False))}")