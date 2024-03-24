class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        ch=lambda s:max(Counter(s).values())<=2
        ans=1
        for i in range(len(s)):
            for j in range(i+1,len(s)+1):
                if ch(s[i:j]):
                    ans=max(ans,j-i)
        return ans