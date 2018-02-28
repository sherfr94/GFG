# Returns index of item in arr if present, else -1
def binary_search(arr, left, right, item):
    # Check base case
    if right >= left:

        mid = int((left + right) / 2)
        # print("mid:", mid, "l:", left, "r:", right)

        # If element is present at the middle itself
        if arr[mid] == item:
            return mid

        # If element is smaller than mid, then it 
        # can only be present in left subarray
        elif arr[mid] > item:
            return binary_search(arr, left, mid - 1, item)

        # Else the element can only be present 
        # in right subarray
        else:
            return binary_search(arr, mid + 1, right, item)

    else:
        # Element is not present in the array
        return -1


# Test array
arr1 = [2, 3, 4, 10, 40]
item1 = 3
print("arr:", arr1, "item:", item1)

# Function call
result = binary_search(arr1, 0, len(arr1) - 1, item1)

if result != -1:
    print("item found at index", result)
else:
    print("item was not found")
