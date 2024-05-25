class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        n=limit+1
        color={}
        c=Counter()
        ans=[]
        for x,y in queries:
            if x in color:
                c[color[x]]-=1
                if c[color[x]]==0:
                    del c[color[x]]
            color[x]=y
            c[color[x]]+=1
            ans.append(len(c))
        return ans