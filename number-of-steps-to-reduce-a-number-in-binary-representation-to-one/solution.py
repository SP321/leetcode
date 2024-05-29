class Solution:
    def numSteps(self, s: str) -> int:
        c = 0
        num = int(s, 2)

        while num != 1:
            c+=1
            if num%2 == 0:
                num = num//2
            else:
                num += 1
        return c