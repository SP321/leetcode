class Solution:
    def getSmallestString(self, s: str) -> str:
        a=list(s)
        for i in range(len(s)-1):
            if int(s[i])%2==int(s[i+1])%2 and s[i+1]<s[i]:
                a[i],a[i+1]=a[i+1],a[i]
                break
        return ''.join(a)