class Solution:
    def countSeniors(self, details: List[str]) -> int:
        x=[int(i[-4:-2]) for i in details]
        return sum([1 for i in x if i>60])
        