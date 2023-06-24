class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if len(s) == 0 or len(s) == 1:
            return len(s)
        kk = k
        i = max_count = 0
        counts = defaultdict(int)
        for char in s:
            counts[char] += 1
            if counts[char] > max_count:
                max_count = counts[char]
            else:
                kk -= 1
            if kk < 0:
                counts[s[i]] -= 1
                i += 1
                kk += 1
        return max_count + k - kk 