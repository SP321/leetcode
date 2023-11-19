class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        ans=defaultdict(set)
        n=len(s)
        def backtrack(i,prefix,c=0):
            if i==n:
                if c==0:
                    ans[len(prefix)].add(prefix)
                return
            if s[i]  in '()':
                if c>0 and s[i]==')':
                    backtrack(i+1,prefix+s[i],c-1)  
                elif s[i]=='(':
                    backtrack(i+1,prefix+s[i],c+1)
                backtrack(i+1,prefix,c)
            else:
                backtrack(i+1,prefix+s[i],c)
        backtrack(0,"",0)
        return ans[max(ans)]