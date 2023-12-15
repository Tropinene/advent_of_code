# part1: start with facing north. distance from the end to start
# part2: the distance form the first walked twice place to start

def get_direction(turn, current):
    if (current == 'N' and turn == 'R') or (current == 'S' and turn == 'L'):
        return 'E'
    elif (current == 'E' and turn == 'R') or (current == 'W' and turn == 'L'):
        return 'S'
    elif (current == 'S' and turn == 'R') or (current == 'N' and turn == 'L'):
        return 'W'
    else:
        return 'N'


if __name__ == "__main__":
    data = open('input.txt', 'r').readline()
    instructions = data.strip().split(', ')

    x, y = 0, 0
    direction = 'N'
    for instro in instructions:
        turn = instro[0]
        steps = int(instro[1:])
        direction = get_direction(turn, direction)
        if direction == 'N':
            y += steps
        elif direction == 'S':
            y -= steps
        elif direction == 'E':
            x += steps
        else:
            x -= steps

    print(f"[Part1] : {abs(x) + abs(y)}")

    visited = [(0, 0)]
    x, y = 0, 0
    direction = 'N'
    for instro in instructions:
        turn = instro[0]
        steps = int(instro[1:])
        direction = get_direction(turn, direction)
        for _ in range(steps):
            if direction == 'N':
                y += 1
            elif direction == 'S':
                y -= 1
            elif direction == 'E':
                x += 1
            else:
                x -= 1
            if (x, y) not in visited:
                visited.append((x, y))
            else:
                print(f"[Part2] : {abs(x) + abs(y)}")
                quit()
