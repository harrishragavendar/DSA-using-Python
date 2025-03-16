def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid # target found, return index
        
        elif arr[mid] > target:
            right = mid - 1

        else:
            left = mid + 1
            
    return -1 # target not found

nums = [1, 2, 3, 4, 5, 6]

ind = binary_search(nums, 2)
print(ind)

ind = binary_search(nums, 10)
print(ind)