def parse_file(filename: str) -> list[list[str]]:
    answers = open(filename, 'r').read()
    answers = answers.split('\n\n')
    answers = [x.split('\n') for x in answers]
    return answers


def main():
    answers = parse_file('input.txt')

    p1 = 0
    for ans in answers:
        p1 += len(set(''.join(ans)))
    print(f"[Part1] : {p1}")

    p2 = 0
    for ans in answers:
        tmp = set(ans[0])
        for idx in range(1, len(ans)):
            tmp = tmp.intersection(set(ans[idx]))
        p2 += len(tmp)
    print(f"[Part2] : {p2}")


if __name__ == '__main__':
    main()
