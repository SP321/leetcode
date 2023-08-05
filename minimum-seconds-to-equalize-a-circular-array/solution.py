
class Solution:
    def minimumSeconds(self, nums: List[int]) -> int:
        n = len(nums)
        d = defaultdict(list)
        for i, num in enumerate(nums):
            d[num].append(i)
        ans = float('inf')
        for indices in d.values():
            indices.sort()
            indices += [n + indices[0]]
            ma=0
            for i in range(1, len(indices)):
                dist = (indices[i] - indices[i-1]) // 2
                ma = max(ma, dist)
            ans=min(ans,ma)
        return ans
