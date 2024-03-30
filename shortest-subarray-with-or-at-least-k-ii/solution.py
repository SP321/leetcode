class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        n=len(nums)
        c=Counter()
        cur=0
        def add(x):
            nonlocal cur
            for i in range(30):
                if (x>>i) & 1:
                    c[i]+=1
                    if c[i]==1:
                        cur|=1<<i
        def rem(x):
            nonlocal cur
            for i in range(30):
                if (x>>i) & 1:
                    c[i]-=1
                    if c[i]==0:
                        cur^=1<<i
        i=0
        ans=inf
        for j in range(n):
            add(nums[j])
            while i<=j and cur>=k:
                ans=min(ans,j-i+1)
                rem(nums[i])
                i+=1
        return ans if ans!=inf else -1