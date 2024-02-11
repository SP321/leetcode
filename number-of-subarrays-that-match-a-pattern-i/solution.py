def search_pattern(pattern, text):
    concatenated = pattern + [2] + text
    z = zf(concatenated)
    pattern_length = len(pattern)
    matches = []

    for i in range(len(concatenated)):
        if z[i] == pattern_length:
            matches.append(i - pattern_length - 1)

    return matches

def zf(s):
    n = len(s)
    z = [0] * n
    z[0]=len(s)
    l, r = 0, 0
    for i in range(1, n):
        if i < r:
            z[i] = min(z[i-l], r - i)
        while i + z[i] < n and s[i + z[i]] == s[z[i]]:
            z[i] += 1
        if i + z[i] > r:
            l = i
            r = i + z[i]
    return z
class Solution:
    def countMatchingSubarrays(self, nums: List[int], pattern: List[int]) -> int:
        x=[]
        n=len(nums)
        for i in range(n-1):
            if nums[i]<nums[i+1]:
                x.append(1)
            elif nums[i]>nums[i+1]:
                x.append(-1)
            else:
                x.append(0)
        return len(search_pattern(pattern,x))