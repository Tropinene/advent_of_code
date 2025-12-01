import sys

def solve_part_1(instructions):
    current_pos = 50
    count = 0
    
    for line in instructions:
        direction = line[0]
        distance = int(line[1:])
        
        if direction == 'R':
            current_pos = (current_pos + distance) % 100
        elif direction == 'L':
            current_pos = (current_pos - distance) % 100
            
        if current_pos == 0:
            count += 1
            
    return count

def solve_part_2(instructions):
    current_pos = 50
    count = 0
    
    for line in instructions:
        direction = line[0]
        distance = int(line[1:])
        step = 1 if direction == 'R' else -1
        
        for _ in range(distance):
            current_pos = (current_pos + step) % 100
            if current_pos == 0:
                count += 1
                
    return count


def main():
    with open('./input.txt', 'r') as f:
        file_input = [line.strip() for line in f.readlines() if line.strip()]
            
    print(f"[Part1]: {solve_part_1(file_input)}")
    print(f"[Part2]: {solve_part_2(file_input)}")

if __name__ == "__main__":
    main()