class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ans = []
        def backtrack(i, p):
            if sum(p) == n and len(p) == k:
                ans.append(p.copy())
            else:
                for j in range(i, 10):
                    if sum(p) + j <= n:
                        backtrack(j + 1, p + [j])
        backtrack(1, [])
        return ans