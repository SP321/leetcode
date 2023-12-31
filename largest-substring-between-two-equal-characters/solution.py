class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        first={}
        ans=-1
        for i,x in enumerate(s):
            if x in first:
                ans=max(ans,i-first[x]-1)
            else:
                first[x]=i
        return ans