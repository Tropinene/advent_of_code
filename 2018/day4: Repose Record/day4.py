import re
from collections import Counter


def process_logs(logs):
    guard = {}
    id, start, end = -1, '', ''
    for log in logs:
        log = log.strip()
        if log.endswith("begins shift"):
            match = re.search(r'#(\d+)', log)
            id = int(match.group(1))
            if guard.get(id) is None:
                guard[id] = []
        elif log.endswith("falls asleep"):
            match = re.search(r'(\d{2}-\d{2}) (\d{2}:\d{2})', log).group()
            _, start = match.split()
        elif log.endswith("wakes up"):
            match = re.search(r'(\d{2}-\d{2}) (\d{2}:\d{2})', log).group()
            date, end = match.split()
            guard[id].append(date + ' ' + start + ' ' + end)

    filtered_dict = {key: value for key, value in guard.items() if value != []}
    return filtered_dict


if __name__ == '__main__':
    data = open('input.txt', 'r').readlines()
    info = process_logs(sorted(data))

    sleep_time, max_id = -1, -1
    sleep_minute = {}
    for idx, guard in info.items():
        time = 0
        for i in guard:
            _, s, e = i.split()
            s, e = int(s.split(':')[1]), int(e.split(':')[1])
            time += e - s

            if sleep_minute.get(idx):
                sleep_minute[idx] += Counter(range(s, e))
            else:
                sleep_minute[idx] = Counter(range(s, e))
        if time > sleep_time:
            max_id, sleep_time = idx, time

    target = sleep_minute[max_id]
    most_frequent = target.most_common(1)[0][0]
    print(f"[Part1] : {most_frequent * max_id}")

    most_frequent_minute, frequent_id = -1, -1
    for idx, guard in sleep_minute.items():
        if guard.most_common(1)[0][0] > most_frequent_minute:
            frequent_id, most_frequent_minute = idx, guard.most_common(1)[0][0]

    print(f"[Part2] : {most_frequent_minute * frequent_id}")
