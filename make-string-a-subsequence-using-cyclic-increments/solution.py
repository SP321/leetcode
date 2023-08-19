class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        n, m = len(str1), len(str2)
        def cyclnext(a):
            return chr(ord(a) + 1) if a != 'z' else 'a'
        i, j = 0, 0
        while i < n and j < m:
            if str1[i] == str2[j] or cyclnext(str1[i]) == str2[j]:
                j += 1
            i += 1
        return j == m