def find_largest_n_digit(s: str, n: int) -> int:
    L = len(s)
    
    result = []
    start_index = 0
    
    for j in range(1, n + 1):
        k = n - j + 1
        end_index = L - k
        
        max_digit = s[start_index]
        max_idx = start_index
        
        for i in range(start_index, end_index + 1):
            if s[i] > max_digit:
                max_digit = s[i]
                max_idx = i
                if max_digit == '9':
                    break 
        
        result.append(max_digit)
        start_index = max_idx + 1
        
    return int("".join(result))

if __name__ == '__main__':
    file_path = './input.txt'
    with open(file_path, 'r') as f:
        lines = f.readlines()
        f.close()
    
    p1, p2 = 0, 0
    for line in lines:
        p1 += find_largest_n_digit(line.strip(), 2)
        p2 += find_largest_n_digit(line.strip(), 12)
    print(f"[Part1] : {p1}")
    print(f"[Part2] : {p2}")