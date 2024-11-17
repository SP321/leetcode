class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        r=sum(nums)
        ans=0
        l=0
        for i,x in enumerate(nums):
            if x==0:
                if l==r:
                    ans+=2
                elif abs(l-r)==1:
                    ans+=1
            l+=x
            r-=x
        return ans