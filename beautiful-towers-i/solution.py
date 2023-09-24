class Solution:
    def maximumSumOfHeights(self, maxHeights: List[int]) -> int:
        def helper(start,end):
            if start>=end:
                return 0
            mi=min(maxHeights[i] for i in range(start,end))
            ranges = []
            prev = start - 1
            for i in range(start, end):
                if maxHeights[i] == mi:
                    if i > prev + 1:
                        ranges.append((prev+1, i))
                    prev = i
            if prev + 1 < end:
                ranges.append((prev+1, end))
            if len(ranges)==0:
                return (end-start)*mi
            ans = 0
            for (left, right) in ranges:
                su = helper(left, right)
                ans=max(ans,su+(end-start-(right-left))*mi)
            return ans
        return helper(0,len(maxHeights))
