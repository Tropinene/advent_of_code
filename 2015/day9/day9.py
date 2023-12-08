def getData(file):
    with open(file, 'r') as f:
        lines = f.readlines()
        f.close()
    return lines


if __name__ == '__main__':
    file_path = './eg.txt'
    lines = getData(file_path)

    cityMap = {}
    for line in lines:
        line = line.strip()
        tmp = line.split(' = ')
        info = tmp[0].strip()
        dis = int(tmp[1].strip())

        tmp = info.split(' ')
        city1 = tmp[0].strip()
        city2 = tmp[2].strip()
        if cityMap.get(city1):
            cityMap.get(city1)[city2] = dis
        else:
            cityMap[city1] = {city2: dis}
        if cityMap.get(city2):
            cityMap.get(city2)[city1] = dis
        else:
            cityMap[city2] = {city1: dis}

    shortest = float('inf')
    cities = cityMap.keys()
    for c in cities:
        pass

