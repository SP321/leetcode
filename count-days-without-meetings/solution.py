class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        meetings=[[0,0]]+meetings+[[days+1,days+1]]
        ans=0
        y=0
        for cur in meetings:
            x,yy=cur
            ans+=max(0,x-y-1)
            y=max(y,yy)
        return ans