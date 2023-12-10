import re


def get_frequency(item):
    return -item[1], item[0]


def frequency(s):
    letter_frequency = {}
    for char in s:
        letter_frequency[char] = letter_frequency.get(char, 0) + 1
    lst = sorted(letter_frequency.items(), key=get_frequency)
    res = []
    for c, _ in lst[:5]:
        res.append(c)
    return res


def shiftAlphabet(c, times):
    res = (times + ord(c) - ord('a')) % 26
    return chr(res+ord('a'))


if __name__ == '__main__':
    file_path = './input.txt'
    data = open(file_path, 'r').readlines()

    sum = 0
    for line in data:
        lst = line.strip().split('-')
        num = int(re.findall(r'\d+', lst[-1])[0])
        checksum = lst[-1][-6:-1]
        name = ''.join(lst[:-1])
        top_five = frequency(name)

        flag = True
        for c in top_five:
            if c not in checksum:
                flag = False
                break
        if flag:
            sum += num
    print(f'[Part1] : {sum}')

    for line in data:
        lst = line.strip().split('-')
        num = int(re.findall(r'\d+', lst[-1])[0])
        name = ''.join(lst[:-1])

        chars = []
        for i in name:
            chars.append(shiftAlphabet(i, num))
        if ''.join(chars).startswith('north'):
            print(f'[Part2] : {num}')
            break
