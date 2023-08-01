class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return "0"
        ans = ""
        is_negative = False

        if num < 0:
            num = -num
            is_negative = True

        while num != 0:
            ans = str(num % 7) + ans
            num //= 7

        if is_negative:
            return "-" + ans

        return ans