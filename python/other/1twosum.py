nums = [2, 9, 10, 11]
target = 19


def two_sum():
    records = dict()
    for key, value in enumerate(nums):
        # print(key,value)
        if target - value not in records:
            records[value] = key
        else:
            return [records[target - value], key]


# print(two_sum())
# a = {'one':1,'two':2,'there':3}
# records = {2:0,9:1,10:2,11:3}
# print(a['two'])
