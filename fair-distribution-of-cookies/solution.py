class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        ans = float('inf')
        for order in itertools.permutations(cookies):
            people = [0] * k
            heapq.heapify(people)
            for cookie in order:
                fewest_cookies = heapq.heappop(people)
                heapq.heappush(people, fewest_cookies + cookie)
            ans = min(ans, max(people))
        return ans