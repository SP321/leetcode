class Solution:
    def numberOfChild(self, n: int, k: int) -> int:
        k%=(n-1)*2
        if k>n-1:
            return (n-1)-(k-(n-1))
        return k