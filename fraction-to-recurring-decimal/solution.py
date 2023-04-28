class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        ans=""
        if numerator==0:
            return "0";
        sign=-1 if not(numerator<0 and denominator<0) and(numerator<0 or denominator<0) else 1
        numerator=abs(numerator)
        denominator=abs(denominator)
        non_decimal=numerator//denominator;
        if sign==-1:
            ans+='-'
        ans+=str(non_decimal)
        remainder=numerator%denominator
        if remainder==0:
            return ans
        ans+='.'
        remainder_index={}
        while remainder>0:
            if remainder in remainder_index:
                pos=remainder_index[remainder]
                ans=ans[:pos]+"("+ans[pos:]+")"
                break
            remainder_index[remainder]=len(ans)
            remainder*=10
            ans+=str(remainder//denominator)
            remainder%=denominator
        return ans
                