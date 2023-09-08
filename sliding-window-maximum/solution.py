class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return []

        if k == 1:
            return nums

        def clean_deque(i):
            if deq and deq[0] == i - k:
                deq.popleft()
            while deq and nums[i] > nums[deq[-1]]:
                deq.pop()

        deq = deque()
        ans = []
        max_idx = 0

        for i in range(k):
            clean_deque(i)
            deq.append(i)
            if nums[i] > nums[max_idx]:
                max_idx = i
        ans.append(nums[max_idx])

        for i in range(k, len(nums)):
            clean_deque(i)
            deq.append(i)
            ans.append(nums[deq[0]])

        return ans