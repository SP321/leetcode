class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        ans=0
        first={}
        last={}
        for i,x in enumerate(word):
            if x not in first:
                first[x]=i
            last[x]=i
        for c in ascii_lowercase:
            if c in first and c.upper() in first and last[c]<first[c.upper()]:
                ans+=1
        return ans