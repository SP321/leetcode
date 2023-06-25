class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        n=len(locations)
        @lru_cache(None)
        def dfs(i,fuel):
            ans=0
            if i==finish:
                ans+=1
                ans%=(10**9+7)
            for j in range(n):
                if j!=i:
                    fuelleft=fuel-abs(locations[j]-locations[i])
                    if fuelleft>=0:
                        ans+=dfs(j,fuelleft)
                        ans%=(10**9+7)
            return ans
        return dfs(start,fuel)
                    