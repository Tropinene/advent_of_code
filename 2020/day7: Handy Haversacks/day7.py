import re
from collections import defaultdict, deque


# Function to parse a rule and return a tuple (outer_bag, list of (inner_bag, count))
def parse_rule(rule):
    outer_bag, contents = rule.split(" bags contain ")
    if "no other bags" in contents:
        return outer_bag, []
    inner_bags = re.findall(r'(\d+) ([a-z ]+) bag', contents)
    return outer_bag, [(int(count), bag) for count, bag in inner_bags]


# Function to build a reverse graph from the rules (for part 1)
def build_reverse_graph(rules):
    graph = defaultdict(list)
    for rule in rules:
        outer_bag, inner_bags = parse_rule(rule)
        for _, inner_bag in inner_bags:
            graph[inner_bag].append(outer_bag)
    return graph


# Function to perform BFS to find all bags that can eventually contain a shiny gold bag (part 1)
def count_outermost_bags(graph, target_bag):
    visited = set()
    queue = deque([target_bag])

    while queue:
        current_bag = queue.popleft()
        for outer_bag in graph[current_bag]:
            if outer_bag not in visited:
                visited.add(outer_bag)
                queue.append(outer_bag)

    return len(visited)


# Function to build the graph for Part 2 (regular graph, not reversed)
def build_graph(rules):
    graph = {}
    for rule in rules:
        outer_bag, inner_bags = parse_rule(rule)
        graph[outer_bag] = inner_bags
    return graph


# Recursive function to calculate the total number of bags inside a given bag (part 2)
def count_bags(bag, graph, memo):
    if bag in memo:
        return memo[bag]

    total = 0
    for count, inner_bag in graph[bag]:
        total += count + count * count_bags(inner_bag, graph, memo)

    memo[bag] = total
    return total


def main():
    # Read the input from the file
    with open('input.txt') as f:
        rules = f.read().strip().split("\n")

    # Part 1: Build the reverse graph and count how many bags can contain a shiny gold bag
    reverse_graph = build_reverse_graph(rules)
    part1_result = count_outermost_bags(reverse_graph, "shiny gold")

    # Part 2: Build the regular graph and count the total number of bags inside a shiny gold bag
    graph = build_graph(rules)
    memo = {}
    part2_result = count_bags("shiny gold", graph, memo)

    # Output both parts
    print(f"[Part1] : {part1_result}")
    print(f"[Part2] : {part2_result}")


if __name__ == "__main__":
    main()
