from collections import defaultdict, deque

def solve():
    with open('input.txt', 'r') as f:
        lines = f.read().strip().splitlines()

    bricks = []
    for line in lines:
        u, v = line.split('~')
        c1 = list(map(int, u.split(',')))
        c2 = list(map(int, v.split(',')))
        bricks.append((c1, c2))

    bricks.sort(key=lambda b: min(b[0][2], b[1][2]))

    skyline = {}
    supports = defaultdict(set)
    supported_by = defaultdict(set)
    
    final_bricks = []

    for idx, (c1, c2) in enumerate(bricks):
        x1, x2 = min(c1[0], c2[0]), max(c1[0], c2[0])
        y1, y2 = min(c1[1], c2[1]), max(c1[1], c2[1])
        z1, z2 = min(c1[2], c2[2]), max(c1[2], c2[2])
        
        height = z2 - z1 + 1
        base_z = 0
        
        for x in range(x1, x2 + 1):
            for y in range(y1, y2 + 1):
                if (x, y) in skyline:
                    base_z = max(base_z, skyline[(x, y)][0])
        
        new_z1 = base_z + 1
        new_z2 = new_z1 + height - 1
        
        for x in range(x1, x2 + 1):
            for y in range(y1, y2 + 1):
                if (x, y) in skyline:
                    top_z, owner_id = skyline[(x, y)]
                    if top_z == base_z:
                        supported_by[idx].add(owner_id)
                        supports[owner_id].add(idx)
                skyline[(x, y)] = (new_z2, idx)
        
        final_bricks.append(idx)

    safe_count = 0
    for i in range(len(bricks)):
        is_safe = True
        for dependent in supports[i]:
            if len(supported_by[dependent]) == 1:
                is_safe = False
                break
        if is_safe:
            safe_count += 1

    print(f"[Part1]: {safe_count}")

    total_falls = 0
    for i in range(len(bricks)):
        falling = {i}
        queue = deque([i])
        
        while queue:
            curr = queue.popleft()
            
            for dependent in supports[curr]:
                if dependent not in falling:
                    if supported_by[dependent].issubset(falling):
                        falling.add(dependent)
                        queue.append(dependent)
        
        total_falls += len(falling) - 1

    print(f"[Part2]: {total_falls}")

if __name__ == "__main__":
    solve()