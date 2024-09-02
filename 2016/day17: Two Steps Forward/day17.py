import hashlib


def getDoorState(psw: str) -> str:
    md5_hash = hashlib.md5()
    md5_hash.update(psw.encode('utf-8'))
    md5_result = md5_hash.hexdigest()
    return md5_result[:4]


def findOpenDoor(psw: str, position: tuple) -> list:
    symbols, result = ['b', 'c', 'd', 'e', 'f'], []
    x, y, path = position
    doorState = getDoorState(psw)
    if doorState[0] in symbols and y-1 >= 0:
        result.append((x, y-1, path+'U'))
    if doorState[1] in symbols and y+1 <= 3:
        result.append((x, y+1, path+'D'))
    if doorState[2] in symbols and x-1 >= 0:
        result.append((x-1, y, path+'L'))
    if doorState[3] in symbols and x+1 <= 3:
        result.append((x+1, y, path+'R'))
    return result


def solve(psw: str) -> (str, int):
    states, result = [], []
    start = (0, 0, '')
    states.append(start)

    while len(states) > 0:
        current = states.pop(0)
        passcode = psw + current[2]
        if current[0] == 3 and current[1] == 3:
            result.append(current[2])
        else:
            states.extend(findOpenDoor(passcode, current))

    shortest = str(min(result, key=len))
    longest = str(max(result, key=len))
    return shortest, len(longest)


def main():
    p1, p2 = solve('lpvhkcbi')
    print(f"[Part1] : {p1}")
    print(f"[Part2] : {p2}")
    return


if __name__ == '__main__':
    main()
