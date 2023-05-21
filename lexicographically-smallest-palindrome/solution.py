class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        i=0
        j=len(s)-1
        ans=0
        a=[i for i in s]
        while i<j:
            if a[i]!=a[j]:
                x=min(a[i],a[j])
                a[i]=x
                a[j]=x
            i+=1
            j-=1
        return ''.join(a)