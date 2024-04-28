class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        a = Counter()
        for index, row in enumerate(nums):
            for num in row:
                a[num] |= (1 << index)

        n = len(nums)
        counter = Counter()

        def add(x):
            if x in a:
                mask = a[x]
                for bit in range(n):
                    if mask & (1 << bit):
                        counter[bit] += 1

        def rem(x):
            if x in a:
                mask = a[x]
                for bit in range(n):
                    if mask & (1 << bit):
                        counter[bit] -= 1
                        if counter[bit] == 0:
                            del counter[bit]

        sorted_keys = sorted(a.keys())
        i=0
        ans = [float('-inf'), float('inf')]
        
        for j in range(len(sorted_keys)):
            add(sorted_keys[j])
            while len(counter) == n and i<=j:
                cur = sorted_keys[j] - sorted_keys[i]
                if cur < ans[1] - ans[0]:
                    ans = [sorted_keys[i], sorted_keys[j]]
                rem(sorted_keys[i])
                i += 1
        
        return ans