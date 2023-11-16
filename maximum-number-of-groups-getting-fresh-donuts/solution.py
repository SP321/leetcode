
class Solution:
    def maxHappyGroups(self, batchSize: int, groups: List[int]) -> int:
        mod_count = Counter(g % batchSize for g in groups)
        
        ans = mod_count[0]
        mod_count[0] = 0
        
        @cache
        def dfs(remaining_mods, mod=0):
            if sum(remaining_mods) == 0:
                return 0
            
            ans = 0
            for m in range(batchSize):
                if remaining_mods[m] > 0:
                    new_remaining = tuple(remaining_mods[i] - (i == m) for i in range(batchSize))
                    ans = max(ans, dfs(new_remaining, (mod + m) % batchSize))
            
            return ans + (mod == 0)

        remaining_mods = tuple(mod_count[i] for i in range(batchSize))

        return ans + dfs(remaining_mods)