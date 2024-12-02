class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        for i,x in enumerate(sentence.split()):
            if x.startswith(searchWord):
                return i+1
        return -1