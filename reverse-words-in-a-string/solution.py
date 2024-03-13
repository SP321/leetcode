class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join([x for x in s.split() if len(x)][::-1])