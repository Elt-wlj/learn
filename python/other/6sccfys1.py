
# 删除列表重复元素
def del_list_element(num):
    for i in num[:]:
        if num.count(i)>1:
            num.remove(i)
    return ('length: {} output: {}'.format(len(num),num))
l1 = [1,1,2]
print(del_list_element(l1))

# class Solution:
#     def removeDuplicates(self, nums):
#         left = 0
#         for right in range(1,len(nums)):
#             if nums[right] != nums[left]:
#                 left += 1
                
#                 if right - left >0:
#                     nums[left] = nums[right]
            
#         return left+1
    
# l1 = [0,0,1,1,1,2,2,3,3,4]
# s = Solution()
# print(s.removeDuplicates(l1))