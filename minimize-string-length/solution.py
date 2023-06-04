class Solution:
    def minimizedStringLength(self, s: str) -> int:
        ans=[]
        for i in s:
            if i not in ans:
                ans.append(i)
        return len(ans)
        