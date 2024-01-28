class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        cur=0
        d=defaultdict(int)
        d[0]=1
        ans=0
        for x in nums:
            cur+=x
            ans+=d[cur-k]
            d[cur]+=1
        return ans