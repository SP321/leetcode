class Solution:
    def minIncrements(self, n: int, cost: List[int]) -> int:
        ans=0
        for i in range(1,n)[::-2]:
            j=i-1
            parent = (i - 1) // 2
            diff=abs(cost[i]-cost[j])
            cost[parent]+=max(cost[i],cost[j])
            ans+=diff
        return ans