factors = [[] for _ in range(10 ** 6 + 1)]
for i in range(1, 10 ** 6 + 1):
    for j in range(i, 10 ** 6 + 1, i):
        factors[j].append(i)

class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], k: int) -> int:
        c=Counter()
        for x in nums2:
            x*=k
            if x<=10**6:
                c[x]+=1
        ans=0
        for x in nums1:
            for f in factors[x]:
                ans+=c[f]
        return ans

