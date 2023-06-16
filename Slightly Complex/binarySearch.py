import math

def search(set, left, right, item):

    while left <= right:
        middle = (left + right) / 2
        middle = int(math.floor(middle))


        if set[middle] == item:
            return middle
        elif set[middle] < item:
            left = middle + 1
        else:
            right = middle - 1

    return False

set = [5,11,24,36,45,49,56,67,81,89,100,105]

item = 67

look = search(set, 0, len(set) - 1, item)

if look == False:
    print("False")
else:
    print("True")
