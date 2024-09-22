class Solution:
    def validSubstringCount(self, word1: str, word2: str) -> int:
        c = Counter(word2)
        ans = 0
        i=0
        cnt=len(word2)
        for j in range(len(word1)):
            if c[word1[j]]>0:
                cnt-=1
            c[word1[j]]-=1
            while cnt==0:
                if c[word1[i]]==0:
                    cnt+=1
                c[word1[i]]+=1
                i+=1
            ans+=i
        return ans 