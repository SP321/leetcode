class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n=len(s)
        ans=[]
        def backtrack(i,pre):
            if i==n:
                ans.append(pre)
                return
            for j in range(i+1,n+1):
                if s[i:j]== s[i:j][::-1]:
                    backtrack(j,pre+[s[i:j]])
        backtrack(0,[])
        return ans            
            