class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        x=sentence.split(' ')
        def conv(i):
            word=x[i]
            if word[0] in 'aeiouAEIOU':
                return word+"ma"+"a"*(i+1)
            else:
                return word[1:]+word[0]+"ma"+"a"*(i+1)
        return" ".join([conv(i) for i in range(len(x))])