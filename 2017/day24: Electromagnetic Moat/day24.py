def parse_components() -> list:
    components = [tuple(map(int, line.strip().split('/'))) for line in open('input.txt', 'r').readlines()]
    return components


def build_bridges(components, current_bridge, used_components, port):
    valid_bridges = [current_bridge]

    for i, component in enumerate(components):
        if i not in used_components:
            if port in component:
                new_bridge = current_bridge + [component]
                new_used_components = set(used_components)
                new_used_components.add(i)

                other_port = component[0] if component[1] == port else component[1]
                sub_bridges = build_bridges(components, new_bridge, new_used_components, other_port)
                valid_bridges.extend(sub_bridges)

    return valid_bridges


def calculate_strength(bridge):
    return sum(sum(component) for component in bridge)


def find_strongest_bridge(components):
    bridges = build_bridges(components, [], set(), 0)
    return max(bridges, key=calculate_strength)


def find_longest_bridge(components):
    bridges = build_bridges(components, [], set(), 0)
    max_length = max(len(bridge) for bridge in bridges)
    longest_bridges = [bridge for bridge in bridges if len(bridge) == max_length]
    return max(longest_bridges, key=calculate_strength)


if __name__ == "__main__":
    components = parse_components()

    # Part 1
    strongest_bridge = find_strongest_bridge(components)
    strength_part1 = calculate_strength(strongest_bridge)
    print(f"[Part1] : {strength_part1}")

    # Part 2
    longest_bridge = find_longest_bridge(components)
    strength_part2 = calculate_strength(longest_bridge)
    print(f"[Part2] : {strength_part2}")
