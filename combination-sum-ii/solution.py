class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        n=len(candidates)
        ans=[]
        def dfs(start, target, prefix):
            if target == 0:
                ans.append(prefix[:])
                return
            for i in range(start, len(candidates)):
                if candidates[i] > target:
                    break
                if i > start and candidates[i] == candidates[i-1]:
                    continue
                prefix.append(candidates[i])
                dfs(i+1, target - candidates[i], prefix)
                prefix.pop()
        candidates.sort()
        dfs(0, target, [])
        return ans