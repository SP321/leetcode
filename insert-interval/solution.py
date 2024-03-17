class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals.sort()
        ans=[[-1,-1]]
        for x,y in intervals:
            if x>ans[-1][-1]:
                ans.append([x,y])
            else:
                ans[-1][-1]=max(ans[-1][-1],y)
        return ans[1:]
