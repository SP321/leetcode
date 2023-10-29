class Solution:
    def findKOr(self, nums: List[int], k: int) -> int:
        c=defaultdict(int)
        for i in nums:
            x=1
            while i>0:
                if i&1:
                    c[x]+=1
                i>>=1
                x+=1
        ans=0
        for i in c:
            if c[i]>=k:
                ans|=1<<(i-1)
        return ans