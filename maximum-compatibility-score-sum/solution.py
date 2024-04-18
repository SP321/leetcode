class Solution:
    def maxCompatibilitySum(self, students: List[List[int]], mentors: List[List[int]]) -> int:
        ans=0
        for p in permutations(mentors,len(mentors)):
            cur=0
            for x,y in zip(students,p):
                cur+=sum(1 for a,b in zip(x,y) if a==b)
            ans=max(ans,cur)
        return ans
            