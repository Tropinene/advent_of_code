def parse_input() -> (int, dict):
    line1, line2 = open('input.txt', 'r').readlines()
    depart_time = int(line1.strip())
    bus = {int(x): idx for idx, x in enumerate(line2.strip().split(',')) if x != 'x'}
    return depart_time, bus


def chinese_remainder_theorem(buses):
    remainders = [(bus - idx) % bus for bus, idx in buses.items()]
    buses = list(buses.keys())

    N = 1
    for bus in buses:
        N *= bus

    result = sum(remainder * (N // bus) * pow(N // bus, -1, bus) for remainder, bus in zip(remainders, buses))

    return result % N


def main():
    depart_time, buses = parse_input()

    earlist, bus_id = float('inf'), 0
    for bus in buses.keys():
        tmp = (depart_time // bus + 1) * bus
        if tmp < earlist:
            earlist = tmp
            bus_id = bus

    print(f"[Part1] : {(earlist - depart_time) * bus_id}")

    timestamp = chinese_remainder_theorem(buses)

    print(f"[Part2] : {timestamp}")

    # bus_keys = list(buses.keys())
    # # lcm_value = bus_keys[0]
    # # for bus in bus_keys[1:]:
    # #     lcm_value = lcm(lcm_value, bus)
    #
    # start = (depart_time // bus_keys[0] + 1) * bus_keys[0]
    # # print(lcm_value)
    #
    # cnt = 0
    # while any((start + buses.get(bus)) % bus != 0 for bus in bus_keys):
    #     cnt += 1
    #     start += bus_keys[0]
    #     if cnt % 10000000 == 0:
    #         print(start)
    # print(f"[Part2] : {start}")


if __name__ == '__main__':
    main()
