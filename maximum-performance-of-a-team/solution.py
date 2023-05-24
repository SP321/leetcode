class Solution:
  def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
    kMod = 1_000_000_007
    ans = 0
    speedSum = 0
    A = sorted([(e, s) for s, e in zip(speed, efficiency)], reverse=True)
    minHeap = []
    for e, s in A:
      heapq.heappush(minHeap, s)
      speedSum += s
      if len(minHeap) > k:
        speedSum -= heapq.heappop(minHeap)
      ans = max(ans, speedSum * e)
    return ans % kMod