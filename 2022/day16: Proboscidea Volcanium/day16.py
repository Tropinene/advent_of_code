import functools
import re


def parse() -> dict:
    data = [line.strip() for line in open('input.txt', 'r').readlines()]
    pattern = r"Valve (\w+) has flow rate=(\d+); tunnel leads to valve (.+)"
    pattern2 = r"Valve (\w+) has flow rate=(\d+); tunnels lead to valves (.+)"

    valves = {}
    for d in data:
        match = re.search(pattern, d)

        if not match:
            match = re.search(pattern2, d)
        valve_name = match.group(1)
        flow_rate = match.group(2)
        tunnels = match.group(3)
        tunnels_list = tunnels.split(", ")
        valves[valve_name] = (int(flow_rate), tunnels_list)

    return valves


@functools.cache
def calc_max_relief(valves, opened, time, curr_valve_id):
    if time <= 0:
        return 0

    most_pressure = 0
    current_valve = valves[curr_valve_id]
    for neighbour in current_valve[1]:
        # Recurse for each neighbouring position
        most_pressure = max(most_pressure, calc_max_relief(valves, opened, time - 1, neighbour))

    # We only want to open valves that are closed, and where flow rate is > 0
    if curr_valve_id not in opened and current_valve[0] > 0 and time > 0:
        opened = set(opened)
        opened.add(curr_valve_id)
        time -= 1
        total_released = time * current_valve[0]

        for neighbour in current_valve[1]:
            # Try each neighbour and recurse in. Save the best one.
            most_pressure = max(most_pressure,
                                total_released + calc_max_relief(valves, frozenset(opened), time - 1, neighbour))

    return most_pressure


def solve(valves: dict) -> int:
    time, pressure, opened = 30, 0, set()
    start = 'DD'
    a = calc_max_relief(valves, opened, time, start)


def main():
    valves = parse()
    p1 = solve(valves)
    print(f"[Part1] : {p1}")


if __name__ == '__main__':
    main()
