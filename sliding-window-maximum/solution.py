class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        dq = deque()
        ans = []
        i = 0

        for j in range(len(nums)):
            while dq and nums[dq[-1]] < nums[j]:
                dq.pop()
            
            dq.append(j)
            while j - i + 1 > k:
                if dq[0] == i:
                    dq.popleft()
                i += 1

            if  j - i + 1 == k:
                ans.append(nums[dq[0]])

        return ans