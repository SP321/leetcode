class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort(reverse=True)
        ans=0
        i=1
        while (i<len(piles)):
            ans+=piles[i]
            piles.pop()
            i+=2
        return ans