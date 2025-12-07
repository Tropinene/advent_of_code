def merge_intervals(intervals):
    intervals.sort(key=lambda x: x[0])
    merged = [intervals[0]]
    
    for current in intervals[1:]:
        last = merged[-1]
        if current[0] <= last[1]:
            last[1] = max(last[1], current[1])
        else:
            merged.append(current)
            
    return merged

if __name__ == "__main__":
    with open('input.txt', 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    queries = []
    raw_ranges = []
    for line in lines:
        line = line.strip()

        if '-' in line:
            parts = line.split('-')
            if len(parts) == 2:
                start, end = int(parts[0]), int(parts[1])
                raw_ranges.append([start, end])
        else:
            if line.isdigit():
                queries.append(int(line))

    merged_ranges = merge_intervals(raw_ranges)
    p1 = 0
    for query in queries:
        for merged_range in merged_ranges:
            if merged_range[0] <= query <= merged_range[1]:
                p1 += 1
                break
    print(f"[Part1] : {p1}")

    p2 = 0
    for merged_range in merged_ranges:
        p2 += merged_range[1] - merged_range[0] + 1
    print(f"[Part2] : {p2}")