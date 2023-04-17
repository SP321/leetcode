class Solution:
    def gen(self,i,j,pre):
        if i==0 and j==0:
            self.ans.append(pre)
            return
        if i>0:
            self.gen(i-1,j,pre+"(")
        if i<j :
            self.gen(i,j-1,pre+")")
    def generateParenthesis(self, n: int) -> List[str]:
        self.ans=[]
        self.gen(n,n,"")
        return self.ans
