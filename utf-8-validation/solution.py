
class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        n = len(data)
        pow2 = [1<<i for i in range(8)][::-1]
        
        def check_seq(i, j):
            rem = data[i+1:i+j]
            ans = (data[i]&pow2[j]) == 0
            for k in range(j):
                ans &= (data[i]&pow2[k]) != 0
            for num in rem:
                ans &= (num&pow2[0]) != 0
                ans &= (num&pow2[1]) == 0
            return ans
            
        @cache
        def res(i = 0):
            ans = False
            if i == n:
                ans = True
            if i + 3 < n:
                ans |= check_seq(i, 4) and res(i + 4)
            if i + 2 < n:
                ans |= check_seq(i, 3) and res(i + 3)
            if i + 1 < n:
                ans |= check_seq(i, 2) and res(i + 2)
            if i < n:
                ans |= check_seq(i, 0) and res(i + 1)
            return ans
        
        return res()