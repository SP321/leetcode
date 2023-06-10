class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)
        ans=[]
        def dfs(prefix,rem):
            if len(rem)==0 and prefix not in ans:
                ans.append(prefix)
            for i in range(len(rem)):
                dfs([*prefix,rem[i]],rem[:i]+rem[i+1:])
        dfs([],nums)
        return ans
        