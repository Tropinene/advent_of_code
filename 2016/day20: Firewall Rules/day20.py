# input are ranges
# part1: find the first number not in the range
# part2: find the total number of ips not in the range

def get_first_element(item):
    return item[0]

if __name__ == '__main__':
    data = open('input.txt', 'r').readlines()

    lst = []
    for line in data:
        input_list = line.strip().split('-')
        input_list = list(map(int, input_list))
        lst.append(input_list)
    lst.sort(key=get_first_element)
    
    ip_range = lst[0]
    for i in range(1, len(lst)):
        if lst[i][0] > ip_range[1]+1:
            print(f"[Part1] : {ip_range[1]+1}")
            break
        ip_range[1] = max(ip_range[1], lst[i][1])
    
    p2, ip_range = 0, lst[0]
    for i in range(1, len(lst)):
        if lst[i][0] > ip_range[1]+1:
            p2 += lst[i][0] - ip_range[1] - 1
            ip_range = lst[i]
        ip_range[1] = max(ip_range[1], lst[i][1])
    print(f"[Part2] : {p2}")