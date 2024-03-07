MOD = int(1e9+7)


class SegmentTreeNode:
    def __init__(self, lo, hi) -> None:
        self.lo = lo
        self.hi = hi
        self.val = 0
        self.lazy = 0
        if lo + 1 < hi:
            mid = (lo + hi) // 2
            self.left = SegmentTreeNode(lo, mid)
            self.right = SegmentTreeNode(mid, hi)

    def update(self, val):
        self.lazy += val
        self.val += val * (self.hi - self.lo)

    def query(self, lo, hi):
        if self.lo >= lo and self.hi <= hi:
            ans = self.val
            self.update(1)
            return ans
        mid = (self.lo + self.hi) // 2
        ans = 0
        self.left.update(self.lazy)
        self.right.update(self.lazy)
        self.lazy = 0
        if lo < mid:
            ans += self.left.query(lo, hi)
        if hi > mid:
            ans += self.right.query(lo, hi)
        self.val = self.left.val + self.right.val
        return ans


class Solution:
    def sumCounts(self, nums: list[int]) -> int:
        last_idx_dict = {}
        segment_tree = SegmentTreeNode(0, len(nums))
        ans = 0
        curr_ans = 0
        for i, num in enumerate(nums):
            last_idx = last_idx_dict.get(num, -1) + 1
            curr_ans = (
                curr_ans + i - last_idx + 1 + 2 * segment_tree.query(last_idx, i + 1)
            ) % MOD
            ans += curr_ans
            last_idx_dict[num] = i
        return ans % MOD