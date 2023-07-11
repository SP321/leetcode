class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        def rev(i,j):
            if i>=j:
                return
            s[i],s[j]=s[j],s[i]
            rev(i+1,j-1)
        rev(0,len(s)-1)