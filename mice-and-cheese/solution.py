class Solution:
    def miceAndCheese(self, reward1: List[int], reward2: List[int], k: int) -> int:
        a=[ (y-x,x,y) for x,y in zip(reward1,reward2)]
        a.sort()
        return sum(x[1] for x in a[:k])+sum(x[-1] for x in a[k:])