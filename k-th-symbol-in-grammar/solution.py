class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        if n == 1:
            return 0
        
        prev_n = self.kthGrammar(n - 1, (k + 1) // 2)
        return prev_n if k % 2 == 1 else 1 - prev_n