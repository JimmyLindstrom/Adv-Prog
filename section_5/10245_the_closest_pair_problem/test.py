def binarysearch(sequence, value, lo, hi):
    while lo <= hi:
        mid = (lo + hi) // 2
        if sequence[mid] < value:
            lo = mid + 1
        elif value < sequence[mid]:
            hi = mid - 1
        else:
            return mid
    return -1

def start():
    arr = [3, 6, 8, 9, 11, 18, 24, 25, 35, 48, 52, 56]
    # print(len(arr))
    print("Input number to search for in array: ")
    number = int(input())
    match = False
    index = -1
    if number > arr[0]:
        for i in range(0, len(arr)):
            if not match:
                num = arr[i]
                index = binarysearch(arr, number - num, i + 1, len(arr) - 1)
                if index >= 0:
                    match = True
                    print("Found a match at index", i, "and index", index)
                    print("Resulting in the following", arr[i], "+", arr[index], "=", arr[i] + arr[index])
    if not match:
        print("There are no 2 elements in this array that can add to the specified number")

start()