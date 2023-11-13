class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        ans=[]
        n=len(intervals)
        intervals.sort()
        for cur in intervals:
            if ans and cur[0]<=ans[-1][1]:
                ans[-1][1]=max(ans[-1][1],cur[1])
            else:
                ans.append(cur)
        return ans