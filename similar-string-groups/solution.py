class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        def similar(a,b):
            c=0;
            for x,y in zip(a,b):
                if c>2:
                    return False
                if x!=y:
                    c+=1
            return c==0 or c==2
        n=len(strs)
        p=[-1]*n
        for i in range(n):
            for j in range(i+1,n):
                if similar(strs[i],strs[j]):
                    x=i;
                    y=j;
                    while p[x]!=-1:
                            x=p[x]
                    while p[y]!=-1:
                            y=p[y]
                    if x!=y:
                        p[y]=x
        return p.count(-1)