class Solution:
    def validSubstringCount(self, word1: str, word2: str) -> int:
        s=set(word2)
        c=Counter(word2)
        z=set()
        n=len(word1)
        i=0
        ans=n*(n+1)//2
        for j in range(n):
            if word1[j] in s:
                c[word1[j]]-=1
                if c[word1[j]]==0:
                    z.add(word1[j])
            while len(z)==len(s):
                if word1[i] in s:
                    if c[word1[i]]==0:
                        z.discard(word1[i])
                    c[word1[i]]+=1
                i+=1
            if len(z)!=len(s):
                ans-=j-i+1
        return ans