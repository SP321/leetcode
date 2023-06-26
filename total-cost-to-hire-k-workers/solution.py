class Solution:
  def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
    ans = 0
    n=len(costs)
    i, j = 0, n-1
    left = []
    right = []

    for _ in range(k):
      while len(left) < candidates and i <= j:
        heapq.heappush(left, costs[i])
        i += 1
      while len(right) < candidates and i <= j:
        heapq.heappush(right, costs[j])
        j -= 1
      if not left:
        ans += heapq.heappop(right)
      elif not right:
        ans += heapq.heappop(left)
      elif left[0] <= right[0]:
        ans += heapq.heappop(left)
      else:
        ans += heapq.heappop(right)
    return ans