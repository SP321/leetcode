class Solution:
    def minimumOperationsToMakeKPeriodic(self, word: str, k: int) -> int:
        n=len(word)
        c=Counter()
        m=n//k
        for i in range(m):
            cur=word[i*k:i*k+k]
            c[cur]+=1
        return m-max(c.values())
            