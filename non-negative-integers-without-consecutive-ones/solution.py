class Solution:
    def findIntegers(self, n: int) -> int:
        max_bit_len = n.bit_length()
        @cache
        def dfs(i, prev_bit, limit):
            if i == max_bit_len:
                return 1
            ans = 0
            cur_bit_limit = limit & (1 << (max_bit_len - i - 1))
            if cur_bit_limit == 0:
                ans += dfs(i + 1, 0, limit)
            else:
                ans += dfs(i + 1, 0, (1 << (max_bit_len - i - 1)) - 1)
            if prev_bit == 0:
                if cur_bit_limit != 0:
                    ans += dfs(i + 1, 1, limit)
            return ans

        return dfs(0, 0, n)