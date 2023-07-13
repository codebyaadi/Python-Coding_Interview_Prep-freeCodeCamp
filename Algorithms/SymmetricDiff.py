def sym(*arrays):
    def get_diff(arr1, arr2):
        diff = []

        for item in arr1:
            if item not in arr2 and item not in diff:
                diff.append(item)

        for item in arr2:
            if item not in arr1 and item not in diff:
                diff.append(item)

        return diff

    summary = []

    for array in arrays:
        summary = get_diff(summary, array)

    unique = list(set(summary))
    return unique

result = sym([1, 2, 3], [5, 2, 1, 4])
print(result)
