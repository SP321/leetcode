class Solution:
    def stringSequence(self, target: str) -> List[str]:
        ans=[]
        cur=[]
        for x in target:
            for y in range(ord('a'),ord(x)+1):
                ans.append(''.join(cur+[chr(y)]))
            cur.append(x)
        return ans