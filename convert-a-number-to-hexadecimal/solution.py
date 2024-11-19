class Solution:
    def toHex(self, num: int) -> str:
        if num == 0:
            return '0'
        if num < 0:
            num = (1 << 32) + num
        hex_digits = '0123456789abcdef'
        ans = []
        while num > 0:
            digit = num % 16
            ans.append(hex_digits[digit])
            num //= 16
        return ''.join(ans[::-1])