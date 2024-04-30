class Solution:
    def wonderfulSubstrings(self, word: str) -> int:
        count = [1] + [0] * 1024
        ans = cur = 0
        for c in word:
            cur ^= 1 << (ord(c) - ord('a'))
            ans += count[cur]
            ans += sum(count[cur ^ (1 << i)] for i in range(10))
            count[cur] += 1
        return ans