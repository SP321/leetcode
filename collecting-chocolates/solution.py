class Solution:
    def minCost(self, nums: List[int], x: int) -> int:
        n = len(nums)
        def get_min_selection(m: int) -> int:
            min_sum = 0
            extended_nums = nums + nums[:m]
            d = deque()
            for i in range(m):
                while d and extended_nums[i] <= extended_nums[d[-1]]:
                    d.pop()
                d.append(i)
            for i in range(n):
                min_sum += extended_nums[d[0]]
                while d and d[0] <= i:
                    d.popleft()
                while d and extended_nums[i + m] <= extended_nums[d[-1]]:
                    d.pop()
                d.append(i + m)

            return min_sum
        min_cost=sum(nums)
        for m in range(1,n):
            min_cost=min(min_cost,(m*x)+get_min_selection(m+1))
        return min_cost