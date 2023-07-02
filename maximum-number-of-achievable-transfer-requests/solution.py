class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        m = len(requests)
        ans = 0
        for x in range(1 << m):
            counts = [0]*n
            c = 0
            for i in range(m):
                if (x & (1 << i)) != 0:
                    a, b = requests[i]
                    counts[a] -= 1
                    counts[b] += 1
                    c += 1

            if all(count == 0 for count in counts):
                ans = max(ans, c)

        return ans