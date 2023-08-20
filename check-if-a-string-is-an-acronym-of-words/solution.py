class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        return [i[0] for i in words]==[i for i in s]