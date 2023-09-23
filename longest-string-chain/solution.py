class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words.sort(key=len)
        dp = {word: 1 for word in words}
        for word in words:
            for j in range(1, len(word) + 1):
                possible_prev = word[:j-1] + word[j:]
                if possible_prev in dp:
                    dp[word] = max(dp[word], dp[possible_prev] + 1)
        return max(dp.values())