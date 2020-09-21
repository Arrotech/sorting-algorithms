def numberOfRotations(arr, n):
    """Find the number of rotations for a circular sorted array."""
    # There should be no duplicates in the array.
    # Finding the index number of the minimum element in the array
    # the index number equals the number of rotations for the array.
    # Alternatively you can find the number of elements before the smallest element
    # the total number of those elements equals the number of rotations of the array.

    # Search for the minimum element using linear search O(n) time complexity

    # Search for the minimum element using binary search O(log n) time complexity

    # Case 1:
    # Check if the lower bound is less than the upper bound
    # If so, return the lower bound


    # The left and right element of the pivot/smallest elemet are greater than the pivot element i.e [18, 2, 5,]
    # If so return the index of the mid element
    left = 0
    right = n - 1
    while left <= right:
        if arr[left] <= arr[right]:
            return left
        mid = (left + right)//2
        next = (mid + 1) % n
        previous = (mid + n - 1) % n
        if arr[mid] <= arr[next] and arr[mid] <= arr[previous]:
            return mid
        elif arr[mid] <= right:
            right = mid - 1
        elif arr[mid] >= left:
            left = mid + 1
    return -1

arr = [6,7,8,1,2,3,4]
n = len(arr)
rotations = numberOfRotations(arr, n)

if (rotations != -1):
    print("Number of rotations", str(rotations))
else:
    print("Not found")


