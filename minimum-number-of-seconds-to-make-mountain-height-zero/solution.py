class Solution:
    def minNumberOfSeconds(self, height: int, worker: List[int]) -> int:
        sumk = lambda k: k * (k + 1) // 2
        def good(t):
            acc = 0
            for w in worker:
                acc += bisect_left(range(t + 1), True, key=lambda k: w * sumk(k) > t) - 1
                if acc >= height:
                    return True
            return False
    
        return bisect_left(range(10**16), True, key=lambda k: good(k))