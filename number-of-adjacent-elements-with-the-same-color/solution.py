class Solution:
    def colorTheArray(self, n: int, queries: List[List[int]]) -> List[int]:
        a=[0]*(n+1)
        ans=[]
        c=0
        for i,x in queries:
            if a[i]!=0 and a[i-1]==a[i]:
                c-=1
            if a[i]!=0 and a[i+1]==a[i]:
                c-=1
            a[i]=x
            if a[i-1]==x:
                c+=1
            if a[i+1]==x:
                c+=1
            ans.append(c)
        return ans
            