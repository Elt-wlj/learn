# def pop_element(nums,val):
#     if (nums ==0) and (val ==0):
#         return 0
#     new_numr= []
#     for i in range(len(nums)):
#         if i == val:
#             x = nums.pop(i)
#         else:
#            new_numr.append(i)

#     return new_numr,len(new_numr)


def removeElement(nums, val):
    left = 0
    right = 0
    while left < len(nums):
        if nums[left] != val:
            nums[right] = nums[left]
            right += 1
        left += 1
    return right


nums = [3, 2, 2, 3]
val = 3
print(removeElement(nums, val))
