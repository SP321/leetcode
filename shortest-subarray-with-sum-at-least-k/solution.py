class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        q = deque()
        pre = list(accumulate(nums,initial=0))
        ans = float('inf')
        for i,s in enumerate(pre):
            while q and s<=pre[q[-1]]:
                q.pop()
            q.append(i)
            while s - pre[q[0]]>=k:
                ans = min(ans, i-q.popleft())
        return ans if ans!=float("inf") else -1