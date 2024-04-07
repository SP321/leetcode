class Solution:
    def getSmallestString(self, s: str, k: int) -> str:
        ans=""
        for x in s:
            if ord(x)+k>ord('z'):
                move=min(ord('z')-ord(x)+1,ord(x)-ord('a'))
                k-=move
                ans+='a'
            else:
                move=min(ord(x)-ord('a'),k)
                k-=move
                ans+=chr(ord(x)-move)
        return ans