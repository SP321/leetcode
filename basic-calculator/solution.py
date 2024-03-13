class Solution:
    def calculate(self, s: str) -> int:
        output, curr, sign, stack = 0, 0, 1, []
        for c in s:
            if c.isdigit():
                curr = (curr * 10) + int(c)
            
            elif c in '+-':
                output += curr * sign
                curr = 0
                if c == '+':
                    sign = 1

                else:
                    sign = -1
            
            elif c == '(':
                stack.append(output)
                stack.append(sign)
                sign = 1
                output = 0
            
            elif c == ')':
                output += curr * sign
                output *= stack.pop()
                output += stack.pop()
                curr = 0
        return output + (curr * sign)