def back_insert_locate(nums,target):

    for key,value in enumerate(nums):
        # print(key,value)
        while value < target:
           
           key =key
           return key

    # while left <len(nums):
    #     if nums[left] <target:

       


nums = [1,3,5,6,7]
target = 8

print(back_insert_locate(nums,target))

# def removeElement(nums, val):
#     left = 0
#     right = 0
#     while left < len(nums):
#         if nums[left] != val:
#             nums[right] = nums[left]
#             right += 1
#         left += 1
#     return right