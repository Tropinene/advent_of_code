import itertools


# 定义图像的旋转和翻转
def rotate(pattern):
    return [''.join(row) for row in zip(*pattern[::-1])]


def flip(pattern):
    return [row[::-1] for row in pattern]


# 生成所有旋转和翻转的可能组合
def get_all_transformations(pattern):
    transformations = []
    current = pattern
    for _ in range(4):
        current = rotate(current)
        transformations.append(current)
        transformations.append(flip(current))
    return transformations


# 解析输入规则
def parse_rules(rules):
    rule_map = {}
    for rule in rules:
        input_pattern, output_pattern = rule.split(' => ')
        input_pattern = input_pattern.split('/')
        output_pattern = output_pattern.split('/')
        transformations = get_all_transformations(input_pattern)
        for transformation in transformations:
            rule_map[tuple(transformation)] = output_pattern
    return rule_map


# 将图像分割成小块
def split_image(image, size):
    new_image = []
    for r in range(0, len(image), size):
        row = []
        for c in range(0, len(image), size):
            block = [image[r + i][c:c + size] for i in range(size)]
            row.append(block)
        new_image.append(row)
    return new_image


# 合并小块形成新的图像
def join_image(blocks):
    new_image = []
    for block_row in blocks:
        for i in range(len(block_row[0])):
            new_image.append(''.join(block[i] for block in block_row))
    return new_image


# 进行一次迭代
def enhance(image, rule_map):
    size = 2 if len(image) % 2 == 0 else 3
    blocks = split_image(image, size)
    new_blocks = []
    for block_row in blocks:
        new_row = []
        for block in block_row:
            new_row.append(rule_map[tuple(block)])
        new_blocks.append(new_row)
    return join_image(new_blocks)


# 统计开启的像素数
def count_on_pixels(image):
    return sum(row.count('#') for row in image)


def main():
    rules_input = [line.strip() for line in open('input.txt', 'r').readlines()]

    # 解析规则
    rule_map = parse_rules(rules_input)

    # 初始图像
    image = [".#.", "..#", "###"]

    # 进行5次迭代
    for _ in range(5):
        image = enhance(image, rule_map)

    # 统计开启像素数
    p1 = count_on_pixels(image)
    print(f"[Part1] : {p1}")

    for _ in range(13):
        image = enhance(image, rule_map)
    p2 = count_on_pixels(image)
    print(f"[Part1] : {p2}")


if __name__ == '__main__':
    main()
