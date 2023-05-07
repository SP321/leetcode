class Solution:
    def colorTheArray(self, n: int, queries: List[List[int]]) -> List[int]:
        a=[0]*n
        c=0
        ans=[]
        for i,x in queries:
            if i>0 and a[i-1]==a[i] and a[i]!=0:
                c-=1
            if i<n-1 and a[i+1]==a[i] and a[i]!=0:
                c-=1
            a[i]=x
            if i>0 and a[i-1]==a[i]:
                c+=1
            if i<n-1 and a[i+1]==a[i]:
                c+=1
            ans.append(c)
        return ans