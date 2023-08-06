class Solution:
    def finalString(self, s: str) -> str:
        ans=""
        for i in s:
            if i!='i':
                ans+=i
            else:
                ans=ans[::-1]
        return ans