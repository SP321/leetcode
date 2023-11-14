class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        left = [0] * 26
        right = [0] * 26
        for char in s:
            right[ord(char) - ord('a')] += 1

        ans = set()

        for char in s:
            rightIndex = ord(char) - ord('a')
            right[rightIndex] -= 1

            for j in range(26):
                if left[j] > 0 and right[j] > 0:
                    ans.add((char, chr(j + ord('a'))))

            left[rightIndex] += 1

        return len(ans)
