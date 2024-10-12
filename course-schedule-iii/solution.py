class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        courses.sort(key=lambda x:x[::-1])
        h = []
        day = 0
        for t, end in courses:
            day += t
            heappush(h, -t)
            while day > end:
                day += heapq.heappop(h)
        return len(h)