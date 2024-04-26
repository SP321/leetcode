class Solution:
    def smallestBeautifulString(self, s: str, k: int) -> str:
        a = [ord(c) - ord('a') for c in s]
        n=len(a)
        def get_valid(i,ch):
            ans={ch,ch+1,ch+2}
            if i>0:
                ans.discard(a[i-1]) 
            if i>1:
                ans.discard(a[i-2]) 
            return min(ans)
        for i in range(n-1,-1,-1):
            a[i] =get_valid(i,a[i]+1)
            if a[i]<k:
                for j in range(i + 1, n):
                    a[j] = get_valid(j,0)
                return ''.join(chr(ord('a') + x) for x in a)
        return ''