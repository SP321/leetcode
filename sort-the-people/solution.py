class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        return [x[1] for x in sorted(zip(heights,names),reverse=True)]