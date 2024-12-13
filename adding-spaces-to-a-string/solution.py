class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        ans=[]
        j=0
        spaces.append(-1)
        for i,x in enumerate(s):
            if spaces[j]==i:
                ans.append(" ")
                j+=1
            ans.append(x)
        return ''.join(ans)