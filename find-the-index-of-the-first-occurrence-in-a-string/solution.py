def kmp(pattern, text):
    k = 0
    lps = [0] 
    for i in range(1, len(pattern)):
        while k and pattern[k] != pattern[i]: k = lps[k-1]
        if pattern[k] == pattern[i]: k += 1
        lps.append(k)
    k = 0
    for i, ch in enumerate(text): 
        while k and (k == len(pattern) or pattern[k] != ch): k = lps[k-1]
        if pattern[k] == ch: k += 1
        if k==len(pattern):
            return i-len(pattern)+1
    return -1
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return kmp(needle,haystack)