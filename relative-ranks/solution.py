class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        a = sorted(score, reverse = True)
        d = {val : idx for idx, val in enumerate(score)}
        ans = [None] * len(score)        
        for i, x in enumerate(a):
            if i<3:
                ans[d[x]]=["Gold Medal", "Silver Medal", "Bronze Medal"][i]
            else:
                ans[d[x]] =str(i+1)
        return ans