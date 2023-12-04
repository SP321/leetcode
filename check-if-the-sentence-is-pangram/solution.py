class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        c=Counter(sentence)
        for i in range(ord('a'),ord('a')+26):
          ch=chr(i)
          if c[ch]==0:
            return False
        return True