class Solution:
    def getMaxFunctionValue(self, receiver: List[int], k: int) -> int:
        n = len(receiver)
        k+=1
        LOG = k.bit_length()

        up = [[-1 for _ in range(LOG)] for _ in range(n)]
        sum_up = [[0 for _ in range(LOG)] for _ in range(n)]
        for i in range(n):
            up[i][0] = receiver[i]
            sum_up[i][0] = i

        for j in range(1, LOG):
            for i in range(n):
                if up[i][j-1] != -1:
                    up[i][j] = up[up[i][j-1]][j-1]
                    sum_up[i][j] = sum_up[i][j-1] + sum_up[up[i][j-1]][j-1]


        def kth_ancestor(i, k):
            ans = 0
            for j in range(LOG):
                if k>>j & 1:
                    ans += sum_up[i][j]
                    i = up[i][j]
            return ans

        ans = 0
        for i in range(n):
            ans = max(ans, kth_ancestor(i, k))

        return ans

