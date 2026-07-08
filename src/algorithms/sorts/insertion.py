def insertion_sort(array):
    # Traverse from second element to end
    for i in range(1, len(array)):
        # Current element to be inserted
        key = array[i]
        # Start comparing with previous element
        j = i - 1

        # Shift elements greater than key to the right
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j -= 1

        # Insert key in its correct position
        array[j + 1] = key

    # Return sorted array
    return array