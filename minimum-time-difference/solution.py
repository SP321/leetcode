class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        arr=[]
        for x in timePoints:
            arr.append(int(x[0:2])*60+int(x[3:]))
        arr.sort()
        n=len(arr)
        ans=1440+arr[0]-arr[n-1]
        for x,y in pairwise(arr):
            ans=min(ans,(y-x))
        return ans    