from sortedcontainers import SortedList
class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        n=len(nums)
        sl=SortedList()
        ans=[]
        def med(sl):
            n=len(sl)
            if n%2!=0:
                return sl[n//2]
            else:
                return (sl[n//2]+sl[n//2-1])/2
        i=0
        for j in range(n):
            sl.add(nums[j])
            if j-i+1>k:
                sl.remove(nums[i])
                i+=1
            if j-i+1==k:
                ans.append(med(sl))
        return ans