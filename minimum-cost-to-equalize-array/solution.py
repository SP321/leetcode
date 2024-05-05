class Solution:
    def minCostToEqualizeArray(self, nums: List[int], cost1: int, cost2: int) -> int:
        if cost1*2<=cost2:
            return (max(nums)*len(nums)-sum(nums))*cost1 %(10**9+7)

        s = sum(nums)
        mi = min(nums)

        def get_cost(k):
            diffs = k * len(nums) - s
            n1 = max(2 * (k - mi) - diffs, 0)
            n2 = diffs - n1
            n1 += n2%2
            n2 -= n2%2
            return n1 * cost1 + n2 // 2 * cost2
            
        def key_func(k):
            return get_cost(k+2)-get_cost(k)

        m = max(nums)
        search=range(m, 3*m+1, 2)
        x = m+2*bisect_left(search, 0, key=key_func)
        y = m+2*bisect_left(search, 0, key=lambda i: key_func(i + 1))+1 
        return min(get_cost(x),get_cost(y)) % (10**9+7)