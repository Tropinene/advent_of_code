import re


def procss_logs(logs):
    guard = {}
    id, start, end = -1, '', ''
    for log in logs:
        log = log.strip()
        if log.endswith("begins shift"):
            match = re.search(r'#(\d+)', log)
            id = int(match.group(1))
            guard[id] = []
        elif log.endswith("falls asleep"):
            match = re.search(r'(\d{2}-\d{2}) (\d{2}:\d{2})', log).group()
            _, start = match.split()
        elif log.endswith("wakes up"):
            match = re.search(r'(\d{2}-\d{2}) (\d{2}:\d{2})', log).group()
            date, end = match.split()
            guard[id].append(date + ' ' + start + ' ' + end)
    return guard


if __name__ == '__main__':
    data = open('input.txt', 'r').readlines()
    info = procss_logs(sorted(data))
    print(info)