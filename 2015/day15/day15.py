import re


def getData(path):
    with open(path, 'r') as f:
        data = f.readlines()
        f.close()
    return data


def find(ingredients, flag):
    m = -1
    for a in range(101):
        for b in range(101 - a):
            for c in range(101 - a - b):
                d = 100 - a - b - c
                if flag:
                    calories = ingredients[0][4] * a \
                               + ingredients[1][4] * b \
                               + ingredients[2][4] * c \
                               + ingredients[3][4] * d
                    if calories != 500:
                        continue

                capacity = ingredients[0][0] * a \
                           + ingredients[1][0] * b \
                           + ingredients[2][0] * c \
                           + ingredients[3][0] * d
                if capacity <= 0:
                    continue

                durability = ingredients[0][1] * a \
                             + ingredients[1][1] * b \
                             + ingredients[2][1] * c \
                             + ingredients[3][1] * d
                if durability <= 0:
                    continue

                flavor = ingredients[0][2] * a \
                         + ingredients[1][2] * b \
                         + ingredients[2][2] * c \
                         + ingredients[3][2] * d
                if flavor <= 0:
                    continue

                texture = ingredients[0][3] * a \
                          + ingredients[1][3] * b \
                          + ingredients[2][3] * c \
                          + ingredients[3][3] * d
                if texture <= 0:
                    continue

                tmp = capacity * durability * flavor * texture
                if tmp > m:
                    m = tmp
    return m


if __name__ == '__main__':
    file_path = './input.txt'
    data = getData(file_path)

    ingredients = []
    for line in data:
        matches = re.findall(r'-?\d+', line)
        lst = []
        for x in matches:
            if x[0] == '-':
                lst.append(-int(x[1:]))
            else:
                lst.append(int(x))
        ingredients.append(lst)

    p1 = find(ingredients, False)
    print(f'[Part1] : {p1}')
    p2 = find(ingredients, True)
    print(f'[Part1] : {p2}')
