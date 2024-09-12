class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowed=set(allowed)
        ans=len(words)
        for x in words:
            if any(y not in allowed for y in x):
                ans-=1
        return ans