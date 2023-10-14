class Solution:
    def getWordsInLongestSubsequence(self, n: int, words: List[str], groups: List[int]) -> List[str]:
        @cache
        def check(i, j):
            return  j==-1 or len(words[i])==len(words[j]) and groups[i] != groups[j] and sum(c1 != c2 for c1, c2 in zip(words[i], words[j]))==1

        @cache
        def dp(i, prev_index):
            if i == n:
                return 0

            leave = dp(i + 1, prev_index)
            take = 0
            if check(i, prev_index):
                take = 1 + dp(i + 1, i)

            return max(take, leave)

        best = dp(0, -1)

        ans = []
        i = 0
        prev = -1

        while i < n and best > 0:
            if dp(i + 1, prev) == best or not check(i, prev):
                i += 1
            else:
                ans.append(words[i])
                best -= 1
                prev = i
                i += 1

        return ans