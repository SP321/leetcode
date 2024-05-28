class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        c=Counter()
        ans=0
        for x in deliciousness:
            for bit in range(22):
                if (1<<bit)-x in c:
                    ans+=c[(1<<bit)-x]
                    ans%=(10**9+7)
            c[x]+=1
        return ans