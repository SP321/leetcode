class MonotonicDeque:
    def __init__(self, comp=None):
        self.deq = deque()
        self.comp = comp

    def push(self, val):
        while self.deq and self.comp(self.deq[-1], val):
            self.deq.pop()
        self.deq.append(val)

    def pop(self, val):
        if self.deq and self.deq[0] == val:
            self.deq.popleft()

    def max(self):
        return self.deq[0] if self.deq else None

class IncreasingMonotonicDeque(MonotonicDeque):
    INCREASING = lambda x, y: x < y
    def __init__(self):
        super().__init__(IncreasingMonotonicDeque.INCREASING)

class DecreasingMonotonicDeque(MonotonicDeque):
    DECREASING = lambda x, y: x > y
    def __init__(self):
        super().__init__(DecreasingMonotonicDeque.DECREASING)

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums: return []
        
        mq = IncreasingMonotonicDeque()
        result = []

        for i in range(len(nums)):
            if i >= k - 1:
                mq.pop(nums[i - k])
            mq.push(nums[i])
            if i >= k - 1:
                result.append(mq.max())
        return result