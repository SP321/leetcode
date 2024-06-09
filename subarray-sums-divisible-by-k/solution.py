class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        ans=0
        c=Counter()
        c[0]=1
        cur=0
        for x in nums:
            cur+=x
            cur%=k
            ans+=c[cur]
            c[cur]+=1
        return ans