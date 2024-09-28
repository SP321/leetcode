class Solution:
    def maximumTotalSum(self, maximumHeight: List[int]) -> int:
        maximumHeight.sort(reverse=True)
        ans=0
        for i in range(len(maximumHeight)):
            if i!=0:
                maximumHeight[i]=min(maximumHeight[i-1]-1, maximumHeight[i])
            ans+=maximumHeight[i]
            if maximumHeight[i]<=0:
                return -1
        return ans
