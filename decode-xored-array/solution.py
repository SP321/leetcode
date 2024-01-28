class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        return accumulate(encoded,lambda x,y:x^y,initial=first)