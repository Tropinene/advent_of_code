def find_elements_with_sum(nums, target, current=[]):
    if target == 0:
        return [current]
    if target < 0 or not nums:
        return []

    include_current = find_elements_with_sum(nums[1:], target - nums[0], current + [nums[0]])
    exclude_current = find_elements_with_sum(nums[1:], target, current)

    return include_current + exclude_current


def cal_QE(lst):
    QE = float("inf")
    for i in lst:
        cur = 1
        for pkg in i:
            cur *= pkg

        if cur < QE:
            QE = cur
    return QE


if __name__ == "__main__":
    packages = [1, 2, 3, 7, 11, 13, 17, 19, 23, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103,
                107, 109, 113]
    average_weight = int(sum(packages) / 3)

    choice = find_elements_with_sum(packages, average_weight)
    p1 = cal_QE(choice)
    print(f"[Part1] : {p1}")

    average_weight = int(sum(packages) / 4)
    choice = find_elements_with_sum(packages, average_weight)
    p2 = cal_QE(choice)
    print(f"[Part2] : {p2}")
