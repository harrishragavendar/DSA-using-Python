def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

nums = [9, 3, 2, 4, 6, 3]

ind = linear_search(nums, 2)
print(ind)

ind = linear_search(nums, 10)
print(ind)