class Solution:
    def isNumber(self, s: str) -> bool:
        try:
            if "n" in s:
                return 0
            num = float(s)
            return 1
        except:
            return 0