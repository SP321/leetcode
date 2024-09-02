class Solution:
    def vowelStrings(self, words: List[str], left: int, right: int) -> int:
        return sum(1 for x in words[left:right+1] if x[0] in "aeiou" and x[-1] in "aeiou")