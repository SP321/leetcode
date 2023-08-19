class Solution:
    def numberOfBeautifulIntegers(self, low: int, high: int, k: int) -> int:
        def to_list(n: int):
            return [int(x) for x in str(n)]
        
        def helper(num: list[int]):
            n = len(num)
            
            @cache
            def dfs(pos: int, e_c: int, o_c: int, mod_val: int, tight: bool,first_digit:bool): 
                if pos == n:
                    return e_c == o_c and mod_val == 0
                if e_c > n // 2 or o_c > n // 2:
                    return 0
                limit = num[pos] if tight else 9
                total = 0
                for dig in range(1 if first_digit else 0,limit + 1):
                    newTight = tight and (dig == num[pos])
                    newModVal = (mod_val * 10 + dig) % k
                    if dig % 2 == 0:
                        total += dfs(pos + 1, e_c + 1, o_c, newModVal, newTight,False)
                    else:
                        total += dfs(pos + 1, e_c, o_c + 1, newModVal, newTight,False)
                return total

            return dfs(0, 0, 0, 0, True,True)
        
        def helper_lte(num: list[int]):
            ans = helper(num)
            for i in range(2, len(num), 2):
                x=[9] * i
                ans += helper(x)
            return ans
        b=helper_lte(to_list(high)) 
        a=helper_lte(to_list(low - 1))
        return b-a