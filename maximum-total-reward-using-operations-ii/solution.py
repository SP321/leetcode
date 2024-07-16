class Solution:
    def maxTotalReward(self, rewardValues: List[int]) -> int:
        def smmax(x,depth=0):
            p = bisect_left(val, x) - 1
            if p < 0:
                return 0
            ans = -1
            count=0
            while p >= 0:
                if (vp:=val[p]) <= x // 2:
                    ans = max(ans, vp + smmax(vp,depth+1))
                    break
                ans = max(ans, vp + smmax(x - vp,depth+1))
                if ans == x - 1:
                    break
                count+=1
                p -= 1
            assert(depth<= val[-1].bit_length()*1.3)
            assert(count<= val[-1].bit_length()*1.3)
            return ans
        val = sorted(set(rewardValues))
        return val[-1] + smmax(val[-1])