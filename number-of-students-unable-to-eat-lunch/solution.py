class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        c=Counter(students)
        for x in sandwiches:
            if c[x]>0:
                c[x]-=1
            else:
                return c[0]+c[1]
        return 0