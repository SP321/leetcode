class Solution:
    def medianOfUniquenessArray(self, nums: List[int]) -> int:
        n = len(nums)
        total=n*(n+1)//2
        target=(total+1)//2
        def at_most_k(k):
            if k == 0:
                return 0
            count = Counter()
            i = 0
            ans = 0
            for j in range(len(nums)):
                if count[nums[j]] == 0:
                    k -= 1
                count[nums[j]] += 1
                while k < 0:
                    count[nums[i]] -= 1
                    if count[nums[i]] == 0:
                        k += 1
                    i += 1
                ans += j - i + 1
            return ans
        return bisect_left(range(n+1),target,key=at_most_k)