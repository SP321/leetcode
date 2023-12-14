class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        n=len(nums)
        ans=[0]*n
        cur=0
        for i,x in enumerate(nums):
            cur^=x
            k=cur^((1<<maximumBit) -1 )
            ans[n-i-1]=k
        return ans