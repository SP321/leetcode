class Solution:
    def numberToWords(self, num: int) -> str:
        lessThan20 = ["","One","Two","Three","Four","Five","Six","Seven","Eight","Nine","Ten","Eleven","Twelve","Thirteen","Fourteen","Fifteen","Sixteen","Seventeen","Eighteen","Nineteen"]
        tens = ["","Ten","Twenty","Thirty","Forty","Fifty","Sixty","Seventy","Eighty","Ninety"]
        thousands = ["","Thousand","Million","Billion"]

        def helper( num):
            if num == 0:
                return ""
            elif num < 20:
                return lessThan20[num] + " "
            elif num < 100:
                return tens[num // 10] + " " + helper(num % 10)
            else:
                return lessThan20[num // 100] + " Hundred " + helper(num % 100)

        if num == 0:
            return "Zero"

        ans = ""
        for i in range(len(thousands)):
            triplet = num % 1000
            num = num // 1000
            if triplet != 0:
                ans = helper(triplet) + thousands[i] + " " + ans

        return ans.strip()

