class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        ans = []
        for i, r in enumerate(nums):
            for j, a in enumerate(r):
                if len(ans) <= i + j:
                    ans.append([])
                ans[i + j].append(a)
        return [a for r in ans for a in reversed(r)]