class Solution:
    def minPartitions(self, n: str) -> int:
        return ord(max(n))-ord('0')