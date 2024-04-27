class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        pos=defaultdict(list)
        for i,x in enumerate(ring):
            pos[x].append(i)

        def dist(i,j):
            x=abs(i-j)
            return min(len(ring)-x,x)
        @cache
        def dp(i,j):
            if j==len(key):
                return 0
            ans=inf
            for k in pos[key[j]]:
                ans=min(ans,dist(k,i)+1+dp(k,j+1))
            return ans
        return dp(0,0)
            