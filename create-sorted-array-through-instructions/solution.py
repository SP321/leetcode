from sortedcontainers import SortedList
class Solution:
    def createSortedArray(self, instructions: List[int]) -> int:
        sl=SortedList()
        ans=0
        for x in instructions:
            l=sl.bisect_left(x)
            r=sl.bisect_right(x)
            ans+=min(l,len(sl)-r)
            ans%=10**9+7
            sl.add(x)
        return ans