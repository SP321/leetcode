class Solution:
    def validStrings(self, n: int) -> List[str]:
        def backtrack(i,prev=''):
            if i==n:
                return [""]
            ans=[]
            if prev!='0':
                for x in backtrack(i+1,"0"):
                    ans.append('0'+x)
            for x in backtrack(i+1,"1"):
                ans.append('1'+x)
            return ans
        return backtrack(0)