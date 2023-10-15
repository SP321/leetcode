class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        ans="111"+s
        temp=ans
        n=len(s)
        i=0
        c=0
        found=False
        for j in range(n):
            if s[j]=='1':
                c+=1
            while c>k:
                if s[i]=='1':
                    c-=1
                i+=1
            while i<=j and s[i]=='0':
                i+=1
            if c==k:
                ans=min(ans,s[i:j+1],key=lambda x:(len(x),x))         
                found=True 
        if not found:
            return ""
        return ans