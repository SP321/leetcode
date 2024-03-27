class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        x=Counter(p)
        c=Counter()
        i=0
        ans=[]
        for j in range(len(s)):
            c[s[j]]+=1
            if j-i+1>len(p):
                c[s[i]]-=1
                i+=1
            if j>len(p)-2 and c==x:
                ans.append(i)
        return ans