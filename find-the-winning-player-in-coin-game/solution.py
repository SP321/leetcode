class Solution:
    def losingPlayer(self, x: int, y: int) -> str:
        a=min(x,y//4)
        return "Alice" if a%2 else 'Bob'