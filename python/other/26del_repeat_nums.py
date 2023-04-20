def del_num(nums):
    if len(nums) ==0:
        return 0
    slow_p =0
    n= len(nums)
    for fast_p in range(1,n):
        print('fast_p: ',fast_p)
        if nums[slow_p] !=nums[fast_p]:
            slow_p +=1
            nums[slow_p] = nums[fast_p]
    return slow_p +1
nums = [1,2,2,3,4,5,5,6,6,7,7,7,7,8]
n = del_num(nums)
print(n)
print(nums[:n])