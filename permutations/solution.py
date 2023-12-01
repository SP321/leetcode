class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def dfs(seq):
            if len(seq) == len(nums):
                ans.append(seq)
                return
            for n in nums:
                if n in seq:
                    continue
                dfs(seq+[n])
        dfs([])
        return ans