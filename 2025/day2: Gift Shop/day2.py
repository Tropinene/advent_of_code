from typing import List

def find_invalid_id(start: int, end: int) -> List[int]:
    res = []
    for i in range(start, end + 1):
        s = str(i)
        half_idx = len(s) // 2
        left = s[:half_idx]
        right = s[half_idx:]
        if left == right:
            res.append(i)
    return res


def find_invalid_id2(start: int, end: int) -> List[int]:
    res = []
    for i in range(start, end + 1):
        s = str(i)
        s2 = s[1:] + s[:-1]
        if s in s2:
            res.append(i)
    return res

if __name__ == '__main__':
    file_path = './input.txt'
    with open(file_path, 'r') as f:
        line = f.readline()
        f.close()

    items = line.split(',')
    p1, p2 = 0, 0
    for item in items:
        start, end = item.split('-')
        start = int(start)
        end = int(end)
        lst = find_invalid_id(start, end)
        lst2 = find_invalid_id2(start, end)
        p1 += sum(lst)
        p2 += sum(lst2)

    print(f"[Part 1] : {p1}")
    print(f"[Part 2] : {p2}")