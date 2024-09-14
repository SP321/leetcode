class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        envelopes.sort()
        envelopes.sort(key=lambda tup: (tup[0], -tup[1]))
        ans = []
        for x,y in envelopes:
            if not ans or y > ans[-1]:
                ans.append(y)
            else:
                i = bisect_left(ans, y)
                ans[i] = y
        return len(ans)