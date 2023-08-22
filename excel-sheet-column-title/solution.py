class Solution:
    def convertToTitle(self, n: int) -> str:
        ans = ""
        n -= 1
        while n >= 0:
            x = n % 26
            ans = chr(ord("A") + x) + ans
            n = n // 26
            n -= 1
        return ans