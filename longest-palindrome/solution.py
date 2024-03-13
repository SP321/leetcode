class Solution:
    def longestPalindrome(self, s: str) -> int:
        c=Counter(s)
        ans=0
        for x in c.values():
            ans+=x-x%2
            if x%2 and ans%2==0:
                ans+=1
        return ans