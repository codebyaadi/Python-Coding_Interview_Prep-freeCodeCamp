def ceil(arr, target):
    start = 0
    end = len(arr) - 1

    if target > arr[end]:
        return -1

    while start <= end:
        mid = start + (end - start) // 2

        if target < arr[mid]:
            end = mid - 1
        elif target > arr[mid]:
            start = mid + 1
        else:
            return arr[mid]

    return arr[start]

# Main program
arr = [2, 3, 5, 9, 14, 16, 18, 19, 20]
target = 13
ans = ceil(arr, target)
print(ans)
