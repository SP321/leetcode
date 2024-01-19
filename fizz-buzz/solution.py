class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        ret = []
        for i in range(n):
            offset = i + 1
            if (offset % 3 == 0) and (offset % 5 == 0):
                ret.append("FizzBuzz")
            elif (offset % 3 == 0):
                ret.append("Fizz")
            elif (offset % 5 == 0):
                ret.append("Buzz")
            else: 
                ret.append(str(offset))
        return ret