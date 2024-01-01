import copy


def pop_first(l):
    r = l[0]
    l.remove(r)
    return r


def sum_metadata(tree):
    num_children = pop_first(tree)
    amount_metadata = pop_first(tree)

    sum_meta = 0
    for i in range(num_children):
        sum_meta += sum_metadata(tree)

    for i in range(amount_metadata):
        sum_meta += pop_first(tree)

    return sum_meta


def sum_metadata2(tree):
    num_children = pop_first(tree)
    amount_metadata = pop_first(tree)

    has_children = num_children > 0
    potential_sum = []
    for i in range(num_children):
        potential_sum.append(sum_metadata2(tree))

    sum_meta = 0
    if has_children:
        for i in range(amount_metadata):
            e = pop_first(tree)
            if e in range(1, num_children+1):
                sum_meta += potential_sum[e-1]
    else:
        for i in range(amount_metadata):
            sum_meta += pop_first(tree)

    return sum_meta


if __name__ == '__main__':
    inp = open('input.txt', 'r').readline().strip()
    lst = inp.split()
    lst = [int(x) for x in lst]
    lst2 = copy.deepcopy(lst)

    print(f"[Part1] : {sum_metadata(lst)}")
    print(f"[Part2] : {sum_metadata2(lst2)}")
