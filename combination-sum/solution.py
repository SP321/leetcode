class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(target, combination, start):
            if target == 0:
                result.append(list(combination))
                return
            if target < 0:
                return
            for i in range(start, len(candidates)):
                combination.append(candidates[i])
                dfs(target-candidates[i], combination, i)
                combination.pop()

        result = []
        dfs(target, [], 0)
        return result