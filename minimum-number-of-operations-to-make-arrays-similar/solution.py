class Solution:
    def makeSimilar(self, nums: List[int], target: List[int]) -> int:
        nums.sort()
        target.sort()
        a=[x for x in nums if x&1]
        b=[x for x in target if x&1]
        c=[x for x in nums if x&1==0]
        d=[x for x in target if x&1==0]
        ans=0
        for x,y in zip(a,b):
            ans+=abs(x-y)
        for x,y in zip(c,d):
            ans+=abs(x-y)
        return ans//4