def merge_sort(arr, left, right):
    if left < right:
        mid = int((left + right) / 2)

        merge_sort(arr, left, mid)
        merge_sort(arr, mid+1, right)
        merge(arr, left, mid, right)


def merge(arr, left, mid, right):
    n1 = mid - left + 1
    n2 = right - mid

    # create temp arrays
    larr = []
    rarr = []

    # Copy data to temp arrays larr[] and rarr[]
    for i in range(0, n1):
        larr.append(arr[left + i])

    for j in range(0, n2):
        rarr.append(arr[mid + 1 + j])

    # Merge the temp arrays back into arr[l..r]
    i = 0  # Initial index of first subarray
    j = 0  # Initial index of second subarray
    k = left  # Initial index of merged subarray

    while i < n1 and j < n2:
        if larr[i] <= rarr[j]:
            arr[k] = larr[i]
            i += 1
        else:
            arr[k] = rarr[j]
            j += 1
        k += 1

    # Copy the remaining elements of larr[], case n1 > n2
    while i < n1:
        arr[k] = larr[i]
        i += 1
        k += 1

    # Copy the remaining elements of rarr[], case n2 > n1
    while j < n2:
        arr[k] = rarr[j]
        j += 1
        k += 1


# Test
arr1 = [6, 3, 4, 8, 5, 1, 7, 0]

print(arr1)

merge_sort(arr1, 0, len(arr1) - 1)

print(arr1)
