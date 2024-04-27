@cache
def helper(num_vars, total_sum,limit): # https://cp-algorithms.com/combinatorics/inclusion-exclusion.html#number-of-upper-bound-integer-sums
    def f(x):
        return comb(num_vars + x - 1, num_vars - 1) if x >= 0 else 0
    result = 0
    for j in range((total_sum // (limit+1)) + 1):
        result += (-1) ** j * comb(num_vars, j) * f(total_sum - j * (limit+1))
    return result
class Solution:
    def numberOfStableArrays(self, zero, one, limit):
        MOD = int(1e9)+7
        ans = 0
        for groups0 in range((zero + limit - 1) // limit, zero + 1):
            for groups1 in range(max(groups0-1,(one + limit - 1) // limit), min(groups0+1,one) + 1):
                ans += helper(groups1, one-groups1,limit-1) * helper(groups0, zero-groups0,limit-1) * (2 if groups1 == groups0 else 1)
                ans %= MOD
        return ans