import re

file_path = 'input.txt'
with open(file_path, 'r') as f:
    lines = f.readlines()
    f.close()

sum = 0
for line in lines:
    matches = re.findall(r'\d', line)
    sum += int(matches[0] + matches[-1])
print(f'[Part 1] {sum}')

pattern = r'\d|one|two|three|four|five|six|seven|eight|nine'
dict = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9'
}
replace = list(dict.keys())

sum = 0
for line in lines:
    for i in range(len(replace)):
        if replace[i] in line:
            line = line.replace(replace[i], replace[i] + str(i+1) + replace[i])

    matches = re.findall(pattern, line)
    if dict.get(matches[0]):
        matches[0] = dict.get(matches[0])
    if dict.get(matches[-1]):
        matches[-1] = dict.get(matches[-1])

    num_str = matches[0] + matches[-1]
    sum += int(num_str)

print(f'[Part 2] {sum}')



