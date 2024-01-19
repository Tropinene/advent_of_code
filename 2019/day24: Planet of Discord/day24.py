import copy

def is_valid(col, row):
    if col < 0 or col > 4:
        return False
    if row < 0 or row > 4:
        return False
    return True

def time_pass(state):
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    new_state = copy.deepcopy(state)
    for i in range(5):
        for j in range(5): 
            num_bugs = 0
            for d in directions:
                adjacent_i = i + d[0]
                adjacent_j = j + d[1]
                if is_valid(adjacent_i, adjacent_j):
                    if state[adjacent_i][adjacent_j] == '#':
                        num_bugs += 1
            if (state[i][j] == '#' and num_bugs == 1) or (state[i][j] == '.' and (num_bugs == 1 or num_bugs == 2)):
                new_state[i][j] = '#'
            else:
                new_state[i][j] = '.'
    return new_state

def cal_biodiversity(state):
    rating = 0
    for i in range(5):
        for j in range(5):
            if state[i][j] == '#':
                rating += 2 ** (i*5+j)
    return rating

if __name__ == "__main__":
    lines = [list(line.strip()) for line in open('./input.txt', 'r').readlines()]

    state = copy.deepcopy(lines)
    scenarios = [state]
    while True:
        state = time_pass(state)
        if state in scenarios:
            break
        scenarios.append(state)
    # print(state)
    print(f"[Part1] : {cal_biodiversity(state)}")
    
