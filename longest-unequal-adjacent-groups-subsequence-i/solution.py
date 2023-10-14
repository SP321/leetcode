class Solution:
    def getWordsInLongestSubsequence(self, n: int, words: List[str], groups: List[int]) -> List[str]:
        @cache
        def dp(i,prev):
            if i==n:
                return []
            ans=dp(i+1,prev)
            if groups[i]!=prev:
                x=dp(i+1,groups[i])
                if len(x)+1>len(ans):
                    ans=[words[i]]+x
            return ans
        return dp(0,-1)
