class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        c=[0]*k
        ct=0
        for x in arr:
            x%=k
            y=(k-x)%k
            if c[y]:
                c[y]-=1
                ct-=1
            else:
                c[x]+=1
                ct+=1
        return ct==0