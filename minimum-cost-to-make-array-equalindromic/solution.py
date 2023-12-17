class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        def get_score(x):
            return sum(abs(x-i) for i in nums)
        def make_best(x):
            x=int(x)
            palindromes=[]
            s=[i for i in str(x)]
            mid_digit=int(s[(len(s)-1)//2])
            for i in range(mid_digit-1,mid_digit+2):
                if i>=0:
                    s[(len(s)-1)//2]=str(i)
                    palindromes.append(make_palindrome(s.copy()))
            return min(palindromes,key=get_score)
        def make_palindrome(s):
            for i in range(len(s)//2):
                s[len(s)-i-1]=s[i]
            a=int(''.join(s))
            return a
        med=statistics.median(nums)
        palindrome=make_best(med)
        return get_score(palindrome)