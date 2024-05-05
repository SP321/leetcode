class Solution:
    def isValid(self, word: str) -> bool:
        if len(word)<3:
            return False
        if not all(x in digits+ascii_lowercase+ascii_uppercase for x in word):
            return False
        if not any(x in word for x in "AEIOIUaeiou"):
            return False
        if not any(x in word for x in list(set(ascii_lowercase+ascii_uppercase)-set("AEIOIUaeiou"))):
            return False
        return True