def quick_sort(arr):
    # initialize start and end indices
    p = 0
    r = len(arr) - 1
    # call recursive sort function
    quickSort(arr, p, r)
    return arr


def quickSort(arr, p, r):
    # base case: subarray has at least 2 elements
    if p < r:
        # partition the subarray around the pivot which ends up in A[q]
        q = Partition(arr, p, r)
        # recursively sort the low side
        quickSort(arr, p, q - 1)
        # recursively sort the high side
        quickSort(arr, q + 1, r)


def Partition(arr, p, r):
    # choose last element as pivot
    pivot = arr[r]
    # index of smaller element
    i = p - 1

    # traverse array from p to r-1
    for j in range(p, r):
        # if current element <= pivot, swap it to left
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    # place pivot in its correct position
    temp = arr[i + 1]
    arr[i + 1] = arr[r]
    arr[r] = temp
    # return pivot's final position
    return i + 1