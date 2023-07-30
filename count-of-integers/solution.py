md=10**9+7
class Solution:
    def count(self, num1: str, num2: str, min_sum: int, max_sum: int) -> int:
        @cache
        def dp(i, min_flag, max_flag, pre):
            if pre > max_sum:
                return 0
            if i == len(num2):
                return min_sum <= pre <= max_sum
            ans = 0
            lo_digit = int(num1[i]) if min_flag else 0
            hi_digit = int(num2[i]) if max_flag else 9
            for digit in range(lo_digit, hi_digit + 1):
                next_min_flag = min_flag and digit == lo_digit
                next_max_flag = max_flag and digit == hi_digit
                ans += dp(i + 1, next_min_flag, next_max_flag, pre + digit)
            return ans%md
        num1 = num1.zfill(len(num2))
        return dp(0, True, True, 0)