class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        return len(set(x.lower() for x in word if x.isupper())&set(word))