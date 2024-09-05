from collections import defaultdict, deque
import re


# Function to parse a rule and return a tuple (outer_bag, list of (inner_bag, count))
def parse_rule(rule):
    outer_bag, contents = rule.split(" bags contain ")
    if "no other bags" in contents:
        return outer_bag, []
    inner_bags = re.findall(r'(\d+) ([a-z ]+) bag', contents)
    return outer_bag, [(int(count), bag) for count, bag in inner_bags]


# Function to build a reverse graph from the rules
def build_reverse_graph(rules):
    graph = defaultdict(list)
    for rule in rules:
        outer_bag, inner_bags = parse_rule(rule)
        for _, inner_bag in inner_bags:
            graph[inner_bag].append(outer_bag)
    return graph


# Function to perform BFS to find all bags that can eventually contain a shiny gold bag
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


def main():
    # Read the input from the file
    with open('input.txt') as f:
        rules = f.read().strip().split("\n")

    # Build the reverse graph
    graph = build_reverse_graph(rules)

    # Count how many bags can eventually contain a shiny gold bag
    p1 = count_outermost_bags(graph, "shiny gold")
    print(f"[Part1] : {p1}")


if __name__ == "__main__":
    main()
