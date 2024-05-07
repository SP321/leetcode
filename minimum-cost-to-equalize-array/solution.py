class Solution:
    def minCostToEqualizeArray(self, nums: List[int], cost1: int, cost2: int) -> int:
        n = len(nums)
        s = sum(nums)
        mi = min(nums)
        mx = max(nums)

        if cost1*2<=cost2:
            return (mx*n-s)*cost1 %(10**9+7)

        def get_cost(k):
            diffs = k * n - s
            n1 = max(2 * (k - mi) - diffs, 0)
            n2 = diffs - n1
            n1 += n2%2
            n2 -= n2%2
            return n1 * cost1 + n2 // 2 * cost2

        m = max(nums)
        search=range(m, 3*m+1, 2)
        x = m+2*bisect_left(search, True, key=lambda k:get_cost(k+2)>get_cost(k))
        y = m+2*bisect_left(search, True, key=lambda k:get_cost(k+3)>get_cost(k+1))+1 
        return min(get_cost(x),get_cost(y)) % (10**9+7)