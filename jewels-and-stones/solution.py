class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        return sum([1 for i in stones for j in jewels if i==j])