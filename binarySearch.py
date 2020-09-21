def binarySearch(arr, val):
    """Iterative binary search for integers."""
    
    left = 0
    right = len(arr) - 1
    mid = 0

    while left <= right:
        mid = (left + right)//2
        if arr[mid] == val:
            return mid
        else:
            if (arr[mid] < val):
                left = mid + 1
            else:
                right = mid - 1
    return False


arr = [1,2,3,4,5,6,7,8]
val = 7
result = binarySearch(arr, val)

if (result != False):
    print("Found at index", str(result))
else:
    print("Not found")

def binaryStringSearch(arr, val):
    """Iterative binary search for strings."""
    left = 0
    right = len(arr) - 1
    mid = 0

    while left <= right:

        mid = (left + right)//2

        if arr[mid] == val:
            return mid
        else:
            if arr[mid] < val:
                left = mid + 1
            else:
                right = mid - 1
    return False


arr = ['a','b','c','d','e','f','g','h','i']
val = 'f'
result = binaryStringSearch(arr, val)

if (result != False):
    print("Found at index: ", str(result))
else:
    print("Not found")

def binaryRecursive(arr, left, right, val):
    """Recursive binary search."""

    if left <= right:
        mid = (left + right)//2
        if arr[mid] == val:
            return mid
        else:
            if arr[mid] < val:
                return binaryRecursive(arr, mid + 1, right, val)
            else:
                return binaryRecursive(arr, left, mid - 1, val)
    
    return False

arr = ['a','b','c','d','e','f','g','h','i']
val = 'b'
result = binaryStringSearch(arr, val)

if (result != False):
    print("Found at index: ", str(result))
else:
    print("Not found")