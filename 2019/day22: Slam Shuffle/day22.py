import copy

def deal_into_new_stack(s):
    return s[::-1]

def cut(n, s):
    return s[n:] + s[:n]

def increment(n ,s):
    new_s = copy.deepcopy(s)
    cnt = 0
    for i in s:
        new_s[cnt % len(s)] = i
        cnt += n
    return new_s

if __name__ == "__main__":
    my_stack = [x for x in range(10007)]
    instros = open('input.txt', 'r').readlines()

    for instro in instros:
        if instro.startswith("deal with increment"):
            offset = instro.split()[-1]
            my_stack = increment(int(offset), my_stack)
        elif instro.startswith("cut"):
            offset = instro.split()[-1]
            my_stack = cut(int(offset), my_stack)
        else:
            my_stack = deal_into_new_stack(my_stack)
    p1 = my_stack.index(2019)
    print(f"[Part1] : {p1}")