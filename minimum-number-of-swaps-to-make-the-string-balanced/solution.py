class Solution:
    def minSwaps(self, s: str) -> int:
        c = 0
        changes = 0
        for x in s:
            if x == ']':
                c += 1
            else:
                c -= 1
            changes = max(changes, c)
        return (changes + 1) // 2

