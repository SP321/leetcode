class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xor_all=0
        for x in nums:
            xor_all^=x
        mask=1
        while not xor_all&1:
            xor_all>>=1
            mask<<=1
        num1=0
        num2=0
        for x in nums:
            if x&mask:
                num1^=x
            else:
                num2^=x
        return [num1,num2]