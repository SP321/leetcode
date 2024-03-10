class Solution:
    def shortestSubstrings(self, arr: List[str]) -> List[str]:
        c=Counter()
        def all_sub(x):
            ans=set()
            for i in range(len(x)):
                for j in range(i+1,(len(x)+1)):
                    ans.add(x[i:j])
            return list(ans)
        for x in arr:
            for y in all_sub(x):
                c[y]+=1
        ans=[]
        for x in arr:
            opt=[]
            for y in all_sub(x):
                opt.append(y)
            opt.sort(key=lambda x:(len(x),x))
            for ch in opt:
                if c[ch]==1:
                    ans.append(ch)
                    break
            else:
                ans.append("")
        return ans 