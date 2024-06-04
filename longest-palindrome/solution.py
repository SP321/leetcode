class Solution:
    def longestPalindrome(self, s: str) -> int:
        c=Counter(s)
        ans=0
        o=0
        for x in c.values():
            ans+=x-x%2
            o+=x%2
        return ans+min(1,o)