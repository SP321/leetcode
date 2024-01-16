class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        winners = [match[0] for match in matches]
        losers = [match[1] for match in matches]
        perfect_winners = list(set(winners) - set(losers))
        c = Counter(losers)
        one_lost = [i for i in c if c[i]==1]
        return [sorted(perfect_winners), sorted(one_lost)]