class Solution:
    def sortVowels(self, s: str) -> str:
        vowels=[i for i in s if i in "aeiouAEIOU"]
        vowels.sort(reverse=True)
        return "".join(i if i not in "aeiouAEIOU" else vowels.pop() for i in s)