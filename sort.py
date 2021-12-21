def sort(list, item):
    low = 0
    high = len(list) - 1

    while low <= high:
        mid = (low + high)/2
        print(mid, list[mid])
        guess = list[mid]

        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None

ml=[2,15,20,40,77,84]

print(sort(ml, 20))
