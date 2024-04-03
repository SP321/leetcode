class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        a,b=0,0
        for x in nums:
            if x<0:
                a+=1
            if x>0:
                b+=1
        return max(a,b)