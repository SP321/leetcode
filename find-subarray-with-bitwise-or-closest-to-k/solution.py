class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        ans=inf
        tails=set()
        for x in nums:
            new_tails=set()
            for y in tails:
                new_tails.add(x&y)
                ans=min(ans,x&y,key=lambda x:abs(x-k))
            new_tails.add(x)
            ans=min(ans,x,key=lambda x:abs(x-k))
            tails=new_tails
        return abs(ans-k)