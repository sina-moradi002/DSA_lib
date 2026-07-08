def counting_sort(arr):
    if not arr:
        return []

    n = len(arr)
    max_value = max(arr)

    count_array = [0 for _ in range(max_value + 1)]

    for i in arr:
        count_array[i] += 1

    for i in range(1, max_value + 1):
        count_array[i] += count_array[i - 1]

    sorted_array = [0 for _ in range(n)]

    for i in range(n - 1, -1, -1):
        sorted_array[count_array[arr[i]] - 1] = arr[i]
        count_array[arr[i]] -= 1

    return sorted_array
