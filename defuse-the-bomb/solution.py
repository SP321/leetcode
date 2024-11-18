class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n=len(code)
        code=code+code
        if k==0:
            return [0]*n
        if k>0:
            return [sum(code[i+1:i+k+1]) for i in range(n)]
        if k<0:
            return [sum(code[n+i+k:n+i]) for i in range(n)]
