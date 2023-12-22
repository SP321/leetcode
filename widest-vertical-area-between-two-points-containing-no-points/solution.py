class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        ans=0
        for x1,x2 in pairwise(sorted([x for x,y in points])):
            ans=max(x2-x1,ans)
        return ans