import re


def stimulate(particles, is_part2):
    destroyed = []
    for _ in range(1000):
        min_dis, closest = None, None
        distribute  = {}
        for idx, particle in enumerate(particles):
            particle[1] = [x + y for x, y in zip(particle[1], particle[2])]
            particle[0] = [x + y for x, y in zip(particle[0], particle[1])]
            dis = 0
            for i in particle[0]:
                dis += abs(i)
            if min_dis is None or dis < min_dis:
                min_dis, closest = dis, idx
            
            if idx not in destroyed:
                if distribute.get(str(particle[0])):
                    distribute[str(particle[0])].append(idx)
                else:
                    distribute[str(particle[0])] = [idx]
        for lst in distribute.values():
            if len(lst) > 1:
                destroyed = list(set(lst+destroyed))
    
    p2 = 0
    for idx in range(len(particles)):
        if idx not in destroyed:
            p2 += 1

    if is_part2:
        return p2
    else:
        return closest



if __name__ == '__main__':
    data = open('input.txt', 'r').readlines()
    particles = []
    for line in data:
        matches = re.findall(r'-?\d+', line)
        matches = [int(x) for x in matches]
        p, v, a = matches[:3], matches[3:6], matches[6:]
        particles.append([p, v, a])
        
    p1 = stimulate(particles, False)
    print(f"[Part1] : {p1}")
    p2 = stimulate(particles, True)
    print(f"[Part2] : {p2}")

    
