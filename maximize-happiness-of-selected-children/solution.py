class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        neg=0
        happiness.sort(reverse=True)
        ans=0
        for x in happiness[:k]:
            if neg>x:
                break
            ans+=x-neg
            neg+=1
        return ans
            
        