def two_sum(arr, target):
    point_one = 0
    point_two = len(arr) - 1

    while point_one < point_two:
        sum = arr[point_one] + arr[point_two]

        if sum == target:
            return True
        elif sum < target:
            point_one += 1
        else:
            point_two -= 1

    return False


print("\n")
print(two_sum([2, 3, 4, 6, 10], 13))
print("\n")
