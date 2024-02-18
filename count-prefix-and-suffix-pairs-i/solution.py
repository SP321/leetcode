class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        n=len(words)
        ans=0
        for i in range(n):
            for j in range(i+1,n):
                x=words[j]
                if x.startswith(words[i]) and x[::-1].startswith(words[i][::-1]):
                    ans+=1
        return ans