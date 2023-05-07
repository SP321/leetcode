class Solution:
    def longestObstacleCourseAtEachPosition(self, obstacles: List[int]) -> List[int]:
        dp=[]
        ans=[]
        for i in obstacles:
            index=bisect_right(dp,i)
            if index<len(dp):
                dp[index]=i
            else:
                dp.append(i)
            ans.append(index+1)
        return ans
