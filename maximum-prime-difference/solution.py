s=set([2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97])
class Solution:
    def maximumPrimeDifference(self, nums: List[int]) -> int:
        a,b=None,None
        for i,x in enumerate(nums):
            if x in s:
                if a==None:
                    a=i
                b=i
        return b-a
