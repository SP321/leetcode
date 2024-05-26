class Solution:
    def compressedString(self, word: str) -> str:
        ans=[]
        for x in groupby(word):
            y=len(list(x[1]))
            while y!=0:
                z=min(y,9)
                ans.append(str(z))
                ans.append(x[0])
                y-=z
        return ''.join(ans)