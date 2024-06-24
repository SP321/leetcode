class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        n=len(nums)
        f=0
        flip_end=[0]*(n+1)
        ans=0
        for i,x in enumerate(nums):
            f^=flip_end[i]
            x^=f
            if x==0:
                if i+k>n:
                    return -1
                flip_end[i+k]=1
                f^=1
                ans+=1
        return ans
            
            