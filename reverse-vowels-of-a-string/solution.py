class Solution:
    def reverseVowels(self, s: str) -> str:
        a=[x for x in s if x in 'aeiouAEIOU']
        return ''.join(a.pop() if x in 'aeiouAEIOU' else x for x in s)