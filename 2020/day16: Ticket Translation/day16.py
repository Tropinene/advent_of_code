import re


def parse_file():
    fields, my_tickets, nearby_tickets = open('input.txt', 'r').read().split('\n\n')

    matches = re.findall(r'\d+-\d+', fields)
    ranges = []
    for match in matches:
        start, end = map(int, match.split('-'))
        ranges.append((start, end))

    nearby_tickets = map(int, nearby_tickets.replace("nearby tickets:\n", '').replace('\n', ',').split(','))

    return ranges, nearby_tickets


def main():
    ranges, nearby_tickets = parse_file()
    p1 = 0
    for ticket in nearby_tickets:
        if any(start <= ticket <= end for start, end in ranges):
            pass
        else:
            p1 += ticket
    print(f"[Part1] : {p1}")


if __name__ == '__main__':
    main()
