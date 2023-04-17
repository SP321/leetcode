class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def gethash(s):
            x=[0]*26
            for i in s:
                x[ord(i)-ord('a')]+=1
            return str(x)
        x={}
        for i in strs:
            y=gethash(i)
            if y in x:
                x[y].append(i)
            else:
                x[y]=[i]
        ans=[]
        for i in x:
            ans.append(x[i])
        return ans
            
        