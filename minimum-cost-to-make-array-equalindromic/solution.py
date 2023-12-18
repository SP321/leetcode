class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        def make_best(x):
            x=int(x)
            palindromes=set()
            for i in range(10):
                s=[i for i in str(x)]
                s[(len(s)-1)//2]=str(i)
                palindromes.add(make_palindrome(s))
                palindromes.add(make_palindrome(s.copy()[:-1]))
            return min(palindromes,key=get_score)
        def make_palindrome(s):
            if not s:
                return 0
            for i in range(len(s)//2):
                s[len(s)-i-1]=s[i]
            a=int(''.join(s))
            return a
        def get_score(x):
            return sum(abs(x-i) for i in nums)
        med=statistics.median(nums)
        palindrome=make_best(med)
        return get_score(palindrome)