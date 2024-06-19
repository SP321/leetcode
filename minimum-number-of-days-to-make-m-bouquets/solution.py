class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        def check(x):
            total = 0
            currcount = 0
            for b in bloomDay:
                if x>=b:
                    currcount += 1
                else:
                    total += currcount // k
                    if total >= m:
                        return True
                    currcount = 0
            total += currcount // k
            if total >= m:
                return True
            return False

        ans=bisect_left(range(max(bloomDay)+1),True,key=check)
        return ans if check(ans) else -1