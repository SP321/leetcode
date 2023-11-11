class Solution:
    def maxSpending(self, values: List[List[int]]) -> int:
        n=len(values)
        m=len(values[0])
        ans=0
        day=1
        for i in heapq.merge(*[x[::-1] for x in values]):
            ans+=i*day
            day+=1
        return ans