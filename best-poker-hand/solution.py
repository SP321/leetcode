class Solution:
    def bestHand(self, ranks: List[int], suits: List[str]) -> str:
        if len(set(suits))==1:
            return 'Flush'
        x= max(Counter(ranks).values())
        if x >=3:
            return 'Three of a Kind'
        if x==2:
            return 'Pair'
        return 'High Card'