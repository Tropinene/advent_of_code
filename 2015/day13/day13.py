def parse_input(lines):
    happiness = {}
    for line in lines:
        words = line.split()
        person1, person2 = words[0], words[-1][:-1]
        units = int(words[3]) if words[2] == 'gain' else -int(words[3])
        happiness[(person1, person2)] = units
    return happiness

def calculate_total_happiness(arrangement, happiness):
    total_happiness = 0
    n = len(arrangement)
    for i in range(n):
        person1, person2 = arrangement[i], arrangement[(i + 1) % n]
        total_happiness += happiness[(person1, person2)] + happiness[(person2, person1)]
    return total_happiness

def generate_all_arrangements(people, current_arrangement, remaining_people, happiness, max_happiness):
    if not remaining_people:
        total_happiness = calculate_total_happiness(current_arrangement, happiness)
        max_happiness[0] = max(max_happiness[0], total_happiness)
        return

    for person in remaining_people:
        new_arrangement = current_arrangement + [person]
        new_remaining_people = [p for p in remaining_people if p != person]
        generate_all_arrangements(people, new_arrangement, new_remaining_people, happiness, max_happiness)

if __name__ == "__main__":
    with open("input.txt", "r") as file:
        input_lines = file.read().strip().split('\n')

    happiness_values = parse_input(input_lines)
    people = set(person for person, _ in happiness_values)

    # Part 1
    max_happiness = [float('-inf')]
    generate_all_arrangements(people, [], list(people), happiness_values, max_happiness)
    print(f"[Part1] : {max_happiness[0]}")

    # Part 2: Add yourself as a neutral person
    for person in people:
        happiness_values[("You", person)] = 0
        happiness_values[(person, "You")] = 0

    max_happiness = [float('-inf')]
    generate_all_arrangements(people | {"You"}, [], list(people | {"You"}), happiness_values, max_happiness)
    print(f"[Part2] : {max_happiness[0]}")