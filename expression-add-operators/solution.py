class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        n=len(num)
        ans=[]
        def backtrack(i,pre):
            pre=pre+num[i]
            if i==n-1:
                if eval(pre)==target:
                    ans.append(pre)
                return
            pos=len(pre)-1
            while pos>=0 and pre[pos].isdigit():
              pos-=1
            if pre[pos+1]!='0':
              backtrack(i+1,pre)
            backtrack(i+1,pre+"*")
            backtrack(i+1,pre+"+")
            backtrack(i+1,pre+"-")
        backtrack(0,"")
        return ans