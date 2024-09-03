class Solution:
    def getLucky(self, s: str, k: int) -> int:
        a=''.join([str(ord(x)-ord('a')+1) for x in s])
        for _ in range(k):
            a=str(sum(int(x) for x in a))
        return int(a)
            