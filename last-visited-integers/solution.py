class Solution:
    def lastVisitedIntegers(self, words: List[str]) -> List[int]:
        a=[]
        ans=[]
        c=0
        for i in words:
            if i =="prev":
                c+=1
                if c>len(a):
                    ans.append(-1)
                else:
                    ans.append(a[-c])
            else:
                c=0
                a.append(int(i))
        return ans