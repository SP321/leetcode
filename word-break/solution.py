class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordSet = set(wordDict)
        @cache
        def dp(i):
            if i == len(s):
                return True
            for k in range(i+1, min(i+21,len(s)+1)):
                if s[i:k] in wordSet and dp(k):
                    return True
            return False
        return dp(0)