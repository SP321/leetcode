class Solution:
    def resultsArray(self, queries: List[List[int]], k: int) -> List[int]:
        h=[]
        ans=[]
        for x,y in queries:
            heappush(h,-abs(x)-abs(y))
            if len(h)==k+1:
                heappop(h)
            if len(h)<k:
                ans.append(-1)
            else:
                ans.append(-h[0])
        return ans
