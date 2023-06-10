class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def dfs(seq):
            if len(seq) == len(nums):
                ans.append(list(seq))
                return
            for n in nums:
                if n in seq:
                    continue
                seq.append(n)
                dfs(seq)
                seq.pop()
        dfs([])
        return ans