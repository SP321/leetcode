class Solution:
    def makeFancyString(self, s: str) -> str:
        ans=[s[:2]]
        for i in range(2,len(s)):
            if s[i]==s[i-1] and s[i]==s[i-2]:
                continue
            ans.append(s[i])
        return ''.join(ans)