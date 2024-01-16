import copy

if __name__ == "__main__":
    size = 25 * 6
    inp = open('./input.txt', 'r').readline().strip()
    
    num_layers = len(inp) // size
    
    cnt0, p1 = 999, 0
    for i in range(num_layers):
        layer = inp[i*size : (i+1)*size]
        if layer.count('0') < cnt0:
            cnt0 = layer.count('0')
            p1 = layer.count('1') * layer.count('2')
    print(f"[Part1] {p1}")

    arr = list(inp[0:size])
    for i in range(1, num_layers):
        layer = inp[i*size : (i+1)*size]
        for idx, j in enumerate(layer):
            if arr[idx] == '2':
                arr[idx] = j
    
    print("[Part2]")
    for j in range(6):
        for i in range(25):
            if arr[i+j*25] == '1':
                print('█', end="")
            else:
                print(' ', end="")
        print()

