class Solution:
    def kthCharacter(self, k: int) -> str:
        def next(s):
            ans=[]
            for x in s:
                x=ord(x)-ord('a')
                x+=1
                x%=26
                x=chr(ord('a')+x)
                ans.append(x)
            return ''.join(ans)
        cur='a'
        while len(cur)<k:
            cur=cur+next(cur)
        return cur[k-1]