import math


def search(set, left, right, item):
    # set four arguments. You have your main set, left pointer, right pointer and the item you are trying to find

    while left <= right:
        middle = (left + right) / 2
        middle = int(math.floor(middle))
        # while the left most side is less or equal to the right side. Set the middle index as the left and right divided by 2
        # get the integer of the middle index

        if set[middle] == item:
            return middle
        elif set[middle] < item:
            left = middle + 1
        else:
            right = middle - 1

        # if the middle value of the set is less than the item you're looking for, then increment the left by 1
        # if its the opposite, decrement the right by 1. Keep going until you find the middle value

    return False


set = [5, 11, 24, 36, 45, 49, 56, 67, 81, 89, 100, 105]

item = 67

look = search(set, 0, len(set) - 1, item)
# the variable here is using the function search using the four arguments above. The given set, left that starts from 0, the end of the set length and the item you want to get

if look == False:
    print("False")
else:
    print("True")

# pretty straightforward. If it's there then it's there...if not *shrug*
