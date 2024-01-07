MOD=10**9+7
class Solution:
    def count(self, num1: str, num2: str, min_sum: int, max_sum: int) -> int:
            num1 = num1.zfill(len(num2))
            n=len(num2)
            MI=[num1,'0'*n]
            MX=[num2,'9'*n]
            @cache
            def dp(i, mi_, mx_,pre=0):
                mi=MI[mi_]
                mx=MX[mx_]
                if pre>max_sum:
                    return 0
                if i == n:
                    return min_sum <= pre <= max_sum
                cur_min=int(mi[i])
                cur_max=int(mx[i])
                ans = 0
                for dig in range(cur_min, cur_max + 1):
                    next_mi_ = mi_!=0 or dig != cur_min
                    next_mx_ = mx_!=0 or dig != cur_max
                    ans += dp(i + 1, next_mi_, next_mx_, pre+dig)
                return ans%MOD
            return dp(0, 0, 0)