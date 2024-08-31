class Solution:
    def stringHash(self, s: str, k: int) -> str:
        n=len(s)
        def get_hash(s):
            ans=0
            for x in s:
                ans+=ord(x)-ord("a")
            return ord('a')+ans%26
        ans=""
        for i in range(0,n,k):
            cur=s[i:i+k]
            ans+=chr(get_hash(cur))
            
        return ans