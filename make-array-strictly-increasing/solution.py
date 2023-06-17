class Solution:
    def makeArrayIncreasing(self, arr1: List[int], arr2: List[int]) -> int:
        dp = {-1: 0}

        arr2.sort()

        for a in arr1:
            dp2 = collections.defaultdict(lambda: math.inf)
            for val, c in dp.items():
                if a > val:
                    dp2[a] = min(dp2[a], c)
                i = bisect_right(arr2, val)
                if i < len(arr2):
                    dp2[arr2[i]] = min(dp2[arr2[i]], c + 1)
            if not dp2:
                return -1
            dp = dp2

        return min(dp.values())