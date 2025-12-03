import math
from collections import deque

def solve():
    with open('input.txt', 'r') as f:
        lines = f.read().strip().splitlines()

    modules = {}
    broadcast_targets = []

    for line in lines:
        left, right = line.split(' -> ')
        outputs = right.split(', ')
        if left == 'broadcaster':
            broadcast_targets = outputs
        else:
            modules[left[1:]] = {
                'type': left[0], 
                'outputs': outputs, 
                'memory': {}, 
                'state': 'off'
            }

    inputs = {}
    for name in modules:
        inputs[name] = []
    
    for out in broadcast_targets:
        if out not in inputs:
            inputs[out] = []
        inputs[out].append('broadcaster')

    for name, mod in modules.items():
        for out in mod['outputs']:
            if out not in inputs:
                inputs[out] = []
            inputs[out].append(name)

    for name, mod in modules.items():
        if mod['type'] == '&':
            for inp in inputs.get(name, []):
                mod['memory'][inp] = 'lo'

    rx_source = None
    for name, sources in inputs.items():
        if name == 'rx':
            if sources:
                rx_source = sources[0]
            break

    watch_list = []
    if rx_source and rx_source in modules:
        watch_list = inputs[rx_source]

    cycle_lengths = {}
    low_count = 0
    high_count = 0
    presses = 0
    p1_result = 0
    p2_result = 0

    while True:
        presses += 1
        q = deque([('button', 'broadcaster', 'lo')])
        
        while q:
            src, target, pulse = q.popleft()
            
            if presses <= 1000:
                if pulse == 'lo':
                    low_count += 1
                else:
                    high_count += 1

            if target == rx_source and pulse == 'hi':
                if src not in cycle_lengths:
                    cycle_lengths[src] = presses

            if target == 'broadcaster':
                for out in broadcast_targets:
                    q.append(('broadcaster', out, pulse))
            elif target in modules:
                mod = modules[target]
                
                if mod['type'] == '%':
                    if pulse == 'lo':
                        mod['state'] = 'on' if mod['state'] == 'off' else 'off'
                        out_pulse = 'hi' if mod['state'] == 'on' else 'lo'
                        for out in mod['outputs']:
                            q.append((target, out, out_pulse))
                elif mod['type'] == '&':
                    mod['memory'][src] = pulse
                    all_high = all(x == 'hi' for x in mod['memory'].values())
                    out_pulse = 'lo' if all_high else 'hi'
                    for out in mod['outputs']:
                        q.append((target, out, out_pulse))

        if presses == 1000:
            p1_result = low_count * high_count
            if not watch_list:
                break

        if watch_list and len(cycle_lengths) == len(watch_list):
            p2_result = 1
            for v in cycle_lengths.values():
                p2_result = math.lcm(p2_result, v)
            break
        
        if presses > 20000 and not watch_list:
            break

    print(f"[Part1]: {p1_result}")
    if watch_list:
        print(f"[Part2]: {p2_result}")

if __name__ == "__main__":
    solve()