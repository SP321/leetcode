class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort(key=lambda x: x[1])
        n=len(pairs)
        @cache
        def dp(i, prev_second):
            if i == n:
                return 0
            ans = dp(i + 1, prev_second)
            if pairs[i][0] > prev_second:
                ans=max(ans,1 + dp(i + 1, pairs[i][1]))
            return ans
        
        return dp(0, float('-inf'))