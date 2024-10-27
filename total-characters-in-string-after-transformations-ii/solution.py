import numpy as np
MOD = 10 ** 9 + 7
n=26
unity=np.eye(26, dtype=object)
def fast_exponentiation(matrix, exponent):
    size = matrix.shape[0]
    result = unity
    while exponent > 0:
        if exponent % 2 == 1:
            result = (np.matmul(result, matrix) % MOD)
        matrix = (np.matmul(matrix, matrix) % MOD)
        exponent //= 2
    return result

class Solution:
    def lengthAfterTransformations(self, s: str, t: int, nums: List[int]) -> int:
        a=[ord(x)%32-1 for x in s]
        M = np.zeros((n, n), dtype=object)
        for i in range(n):
            for j in range(i+1,i+nums[i]+1):
                M[i][j%n]=1

        cnts = np.zeros(n, dtype=object)
        for x in a:
            cnts[x]+=1
        M_t = fast_exponentiation(M, t)
        counts_t =np.matmul(cnts, M_t)
        return np.sum(counts_t) % MOD