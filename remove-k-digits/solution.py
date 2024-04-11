class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if k >= len(num):
            return "0"  

        stack = []
        
        for digit in num:
            while stack and stack[-1] > digit and k>0:
                stack.pop()
                k-=1
            
            stack.append(digit)
        
        while k>0:
            stack.pop()
            k-= 1
    
        ans = ''.join(stack).lstrip('0')
        return ans if ans else "0"