class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        a=Counter(word1)
        b=Counter(word2)
        return sorted(list(a.values()))==sorted(list(b.values())) and sorted(list(a.keys()))==sorted(list(b.keys()))