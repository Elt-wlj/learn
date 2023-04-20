
class Solution:
    def mergeTwoLists(self, list1, list2):
        # l = []
        l= list(list1 + list2)
        l.sort()
        # print(type(l))
        return l

l1 = [1,2,4]
l2 = [1,3,4]
s =Solution()
print(s.mergeTwoLists(l1,l2))