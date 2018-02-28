# from random import randint


def quick_sort(arr, left, right):
    if left < right:
        pi = partition(arr, left, right)  # partition index
        quick_sort(arr, left, pi - 1)
        quick_sort(arr, pi + 1, right)


def partition(arr, left, right):
    # rand = randint(left, right)
    # arr[rand], arr[right] = arr[right], arr[rand]

    pivot = arr[right]
    i = left - 1

    for j in range(left, right):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[right] = arr[right], arr[i + 1]
    # print(arr, "pivot:", pivot)
    return i + 1


# Test
arr1 = [6, 3, 4, 8, 5, 1, 7, 0]

print(arr1)

quick_sort(arr1, 0, len(arr1) - 1)

print(arr1)
