def quick_sort(arr):
    p = 0
    r = len(arr) - 1
    quickSort(arr, p , r)
    return arr

def quickSort(arr, p , r):
    if p < r:
        # partition the subarray around the pivot witch ends up in A[q]
        q = Partition(arr,p,r)
        # recursively sort the low side
        quickSort(arr,p,q-1)
        # recursively sort the high side
        quickSort(arr,q+1,r)


def Partition(arr,p,r):
    pivot = arr[r]
    i = p - 1

    for j in range(p,r):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    temp = arr[i + 1]
    arr[i + 1] = arr[r]
    arr[r] = temp
    return i + 1