from sortedcontainers import SortedList
class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        ans=inf
        n=len(nums)
        prefix=list(accumulate(nums,initial=0))
        n+=1
        sl=SortedList()
        i1=0
        i2=0
        for j in range(n):
            cur=prefix[j]
            if i2<=j-l:
                sl.add(prefix[i2])
                i2+=1
            if i1<j-r:
                sl.remove(prefix[i1])
                i1+=1
            pos=sl.bisect_left(cur)-1
            if pos>=0:
                ans=min(ans,cur-sl[pos])

        return ans if ans !=inf else -1
                