class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        return ''.join([ chr((ord(x)-ord('a')+c)%26 + ord('a')) for x,c in zip(s,reversed(list(accumulate(reversed(shifts)))))])