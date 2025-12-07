if __name__ == "__main__":
    with open("input.txt", "r") as f:
        raw_lines = f.readlines()

    # Part 1
    problems_p1 = [line.strip().split() for line in raw_lines]
    r, l = len(problems_p1), len(problems_p1[0])
    p1 = 0
    for i in range(l):
        tmp = int(problems_p1[0][i])
        for j in range(1, r-1):
            op = problems_p1[r-1][i]
            val = int(problems_p1[j][i])
            if op == '*':
                tmp *= val
            elif op == '+':
                tmp += val
        p1 += tmp
    print(f"[Part1] : {p1}")

    # Part 2
    lines = [line.strip('\n') for line in raw_lines]
    max_len = max(len(line) for line in lines) if lines else 0
    grid = [line.ljust(max_len) for line in lines]
    
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0
    
    is_separator = []
    for c in range(cols):
        is_separator.append(all(grid[r][c] == ' ' for r in range(rows)))

    problems_p2 = []
    current_block = []
    for c in range(cols):
        if is_separator[c]:
            if current_block:
                problems_p2.append(current_block)
                current_block = []
        else:
            current_block.append(c)
    if current_block:
        problems_p2.append(current_block)

    p2 = 0
    for block_cols in problems_p2:
        op = None
        op_line = grid[-1]
        for c in block_cols:
            if op_line[c] != ' ':
                op = op_line[c]
                break
        
        numbers = []
        for c in reversed(block_cols):
            num_str = ""
            for r in range(rows - 1): 
                char = grid[r][c]
                if char.isdigit():
                    num_str += char
            if num_str:
                numbers.append(int(num_str))

        if not numbers:
            continue
            
        result = numbers[0]
        for num in numbers[1:]:
            if op == '+':
                result += num
            elif op == '*':
                result *= num
        p2 += result

    print(f"[Part2] : {p2}")