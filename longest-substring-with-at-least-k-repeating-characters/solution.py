class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        if len(s) < k:
            return 0

        char_freq = {}
        for char in s:
            char_freq[char] = char_freq.get(char, 0) + 1

        for char, freq in char_freq.items():
            if freq < k:
                max_length = 0
                substrings = s.split(char)
                for sub_str in substrings:
                    max_length = max(max_length, self.longestSubstring(sub_str, k))
                return max_length

        return len(s)