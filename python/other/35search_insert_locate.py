def find_target(nums, val):
    left = 0
    right = len(nums) - 1
    while left < right:
        mid = left + (right - left) // 2
        if nums[mid] < val:
            left = mid + 1
        elif nums[mid] > val:
            right = mid - 1
            left = left + 1
        else:
            return mid 
    return left

nums = [1, 3, 5, 6]
val = 2
print(find_target(nums, val))
