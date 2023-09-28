
class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        MOD = 10**9 + 7

        def prime_score(n):
            distinct_factors = set()
            while n % 2 == 0:
                distinct_factors.add(2)
                n //= 2
            for i in range(3, int(n**0.5) + 1, 2):
                while n % i == 0:
                    distinct_factors.add(i)
                    n //= i
            if n > 2:
                distinct_factors.add(n)
            return len(distinct_factors)

        scores = [prime_score(num) for num in nums]
        left_c = [0] * len(nums)
        stack = []
        for i in range(len(nums)):
            while stack and scores[i] > scores[stack[-1]]:
                stack.pop()
            left_c[i] = i - stack[-1] - 1 if stack else i
            stack.append(i)

        right_c = [0] * len(nums)
        stack = []
        for i in range(len(nums)-1, -1, -1):
            while stack and scores[i] >= scores[stack[-1]]:
                stack.pop()
            right_c[i] = stack[-1] - i - 1 if stack else len(nums) - i - 1
            stack.append(i)


        order = sorted(range(len(nums)), key=lambda x: nums[x], reverse=True)

        ans = 1
        for idx in order:
            val = nums[idx]
            times = min(k, (left_c[idx] + 1) * (right_c[idx] + 1))
            sc= pow(val, times, MOD)
            ans = (ans *sc) % MOD
            k -= times
            if k <= 0:
                break

        return ans