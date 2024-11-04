class Solution:
    def compressedString(self, word: str) -> str:
        ans=[]
        for x in groupby(word):
            x,y=x[0],len(list(x[1]))
            z=y//9
            if z!=0:
                ans.append(f"9{x}"*z)
            if y%9!=0:
                ans.append(f"{y%9}{x}")
        return ''.join(ans)