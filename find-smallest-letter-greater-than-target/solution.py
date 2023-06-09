class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        ans=chr(190)
        for i in letters:
            if i>target and i<ans:
                ans=i
        if ans==chr(190):
            return letters[0]
        return ans