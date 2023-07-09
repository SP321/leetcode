class Solution:
  def largestVariance(self, s: str) -> int:
    def solve_pair(x: str, y: str) -> int:
      ans = 0
      c1 = 0
      c2 = 0
      can_add_prev_y = False
      for i in s:
        if i not in [x,y]:
          continue
        if i == x:
          c1 += 1
        else:
          c2 += 1
        if c2 > 0:
          ans = max(ans, c1 - c2)
        elif c2 == 0 and can_add_prev_y:
          ans = max(ans, c1 - 1)
        if c2 > c1:
          c1 = 0
          c2 = 0
          can_add_prev_y = True
      return ans
    return max(solve_pair(i, j) for i, j in itertools.permutations([chr(k) for k in range(ord('a'),ord('z')+1)], 2))