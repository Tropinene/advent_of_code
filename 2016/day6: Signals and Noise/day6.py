# part1: the most common character in every column
# part2: the least common character in every column

from collections import Counter


if __name__ == '__main__':
    data = open("input.txt", 'r').readlines()
    data = [line.strip() for line in data]
    num_columns = len(data[0].strip())

    res1, res2 = [], []
    for col_index in range(num_columns):
        col_data = [row[col_index] for row in data]
        counter = Counter(col_data)
        most_common = counter.most_common(1)
        least_common = counter.most_common()[:-2:-1]
        most_letter, _ = most_common[0]
        least_letter, _ = least_common[0]
        res1.append(most_letter)
        res2.append(least_letter)
    p1, p2 = ''.join(res1), ''.join(res2)
    print(f"[Part1] : {p1}")
    print(f"[Part2] : {p2}")
