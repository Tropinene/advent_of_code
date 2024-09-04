def mapping(target: int, relation: list) -> int:
    for line in relation:
        dest, source, _range = (int(x) for x in line.split())
        if source <= target <= source + _range:
            return dest + target - source
    return target


def main():
    seeds, seed2soil, soil2fert, fert2water, water2light, light2temp, temp2humi, humi2loca \
        = open('input.txt', 'r').read().split('\n\n')
    seed2soil = seed2soil.split('\n')[1:]
    soil2fert = soil2fert.split('\n')[1:]
    fert2water = fert2water.split('\n')[1:]
    water2light = water2light.split('\n')[1:]
    light2temp = light2temp.split('\n')[1:]
    temp2humi = temp2humi.split('\n')[1:]
    humi2loca = humi2loca.split('\n')[1:]

    num_seeds = [int(x) for x in seeds[7:].split()]
    min_location = 10000000000

    for s in num_seeds:
        soil = mapping(s, seed2soil)
        fert = mapping(soil, soil2fert)
        water = mapping(fert, fert2water)
        light = mapping(water, water2light)
        temp = mapping(light, light2temp)
        humi = mapping(temp, temp2humi)
        location = mapping(humi, humi2loca)
        min_location = min(min_location, location)
    print(min_location)


if __name__ == '__main__':
    main()
