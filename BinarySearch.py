# Returns index of item in arr if present, else -1
def binarySearch(arr, left, right, item):
    # Check base case
    if right >= left:

        mid =  int(left + (right - left) / 2)
        #print("mid:", mid, "l:", left, "r:", right)

        # If element is present at the middle itself
        if arr[mid] == item:
            return mid

        # If element is smaller than mid, then it 
        # can only be present in left subarray
        elif arr[mid] > item:
            return binarySearch(arr, left, mid - 1, item)

        # Else the element can only be present 
        # in right subarray
        else:
            return binarySearch(arr, mid + 1, right, item)

    else:
        # Element is not present in the array
        return -1


# Test array
arr = [2, 3, 4, 10, 40]
item = 40
print("arr:", arr, "item:", item)

# Function call
result = binarySearch(arr, 0, len(arr) - 1, item)

if result != -1:
    print("item found at index", result)
else:
    print("item was not found")