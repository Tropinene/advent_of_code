from collections import defaultdict


def parse_reaction(reaction_str):
    inputs, output = reaction_str.split(" => ")
    input_list = [parse_chemical(chemical) for chemical in inputs.split(", ")]
    output_chemical = parse_chemical(output)
    return input_list, output_chemical


def parse_chemical(chemical_str):
    quantity, chemical = chemical_str.split(" ")
    return chemical, int(quantity)


def calculate_ore_for_fuel(reactions, fuel_amount=1):
    # Create a dictionary to store the available quantity of each chemical
    available_quantity = defaultdict(int)
    available_quantity['FUEL'] = fuel_amount

    while any(available_quantity[chemical] > 0 and chemical != 'ORE' for chemical in available_quantity):
        # Find a chemical that needs to be produced
        chemical_to_produce = next(chemical for chemical in available_quantity if available_quantity[chemical] > 0 and chemical != 'ORE')

        # Find the reaction that produces the required chemical
        reaction = next(r for r in reactions if r[1][0] == chemical_to_produce)

        # Calculate the number of times the reaction needs to be repeated
        # 两次取反相当于向下取整变成向上取整
        reaction_multiplier = -(-available_quantity[chemical_to_produce] // reaction[1][1])

        # Update the available quantity of the produced chemical
        available_quantity[chemical_to_produce] -= reaction_multiplier * reaction[1][1]

        # Update the available quantity of the input chemicals
        for input_chemical, input_quantity in reaction[0]:
            available_quantity[input_chemical] += reaction_multiplier * input_quantity

    return available_quantity['ORE']


def calculate_fuel_for_ore(reactions, ore_limit=10**12):
    lower_bound = 1
    upper_bound = 10**12  # A sufficiently large value

    while lower_bound < upper_bound:
        fuel_guess = (lower_bound + upper_bound + 1) // 2
        ore_needed = calculate_ore_for_fuel(reactions, fuel_guess)

        if ore_needed > ore_limit:
            upper_bound = fuel_guess - 1
        else:
            lower_bound = fuel_guess

    return lower_bound


if __name__ == "__main__":
    lines = open('input.txt', 'r').readlines()
    input_data = [x.strip() for x in lines]

    reactions = [parse_reaction(reaction_str) for reaction_str in input_data]

    ore_needed = calculate_ore_for_fuel(reactions)
    print(f"[Part1] {ore_needed}")

    max_fuel = calculate_fuel_for_ore(reactions)
    print(f"[Part2] {max_fuel}")
