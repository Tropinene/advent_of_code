import re
from collections import Counter

def procss_logs(logs):
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
    info = procss_logs(sorted(data))

    sleep_time, max_id = -1, -1
    for idx, guard in info.items():
        time = 0
        for i in guard:
            _, s, e = i.split()
            s, e = int(s.split(':')[1]), int(e.split(':')[1])
            time += e - s
        if time > sleep_time:
            max_id, sleep_time = idx, time

    target = info[max_id]
    run_dates, sleep_time_cnt = [], Counter()
    for i in target:
        date, s, e = i.split()
        s, e = int(s.split(':')[1]), int(e.split(':')[1])
        sleep_time_cnt += Counter(range(s, e))
    most_frequent = sleep_time_cnt.most_common(1)[0][0]
    print(f"[Part1] : {most_frequent * max_id}")

