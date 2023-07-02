class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        ma, mi = deque(), deque()
        l = 0
        count = 0
        for r, num in enumerate(nums):
            while ma and num > ma[-1]:
                ma.pop()
            while mi and num < mi[-1]:
                mi.pop()
            ma.append(num)
            mi.append(num)
            while ma[0] - mi[0] > 2:
                if ma[0] == nums[l]:
                    ma.popleft()
                if mi[0] == nums[l]:
                    mi.popleft()
                l += 1
            count += r - l + 1
        return count
