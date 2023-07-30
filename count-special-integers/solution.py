class Solution:
    def countSpecialNumbers(self, n: int) -> int:
        @cache
        def dp(i, mask, is_most_significant,is_capped):
            if i==0:
                return 1
            ans=0
            cap=9
            if is_capped:
                cap=int(str_n[len(str_n) - i])
            for j in range(10): 
                if j>cap:
                    continue
                if not (mask >> j) & 1:
                    continue
                is_capped_new = is_capped and j == cap
                if j == 0 and is_most_significant:
                    ans += dp(i-1, mask, is_most_significant,is_capped_new)
                else:
                    next_mask = mask & ~(1 << j)
                    ans += dp(i-1, next_mask, False,is_capped_new)
            return ans
        str_n=str(n)
        return dp(len(str(n)), 1023, True,True)-1