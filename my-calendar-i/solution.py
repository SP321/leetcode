class MyCalendar:

    def __init__(self):
        self.intervals=[]

    def book(self, start: int, end: int) -> bool:

        end_index = bisect.bisect_left(self.intervals,end,key=lambda x:x[1])
        start_prev, end_prev = self.intervals[end_index-1] if end_index>0 else (None, None)
        start_next, end_next = self.intervals[end_index] if end_index<len(self.intervals) else (None, None)
        if start_prev and (start_prev<=start<end_prev or start <= start_prev): 
            return False
        if end_next and start_next<end: 
            return False
        self.intervals=self.intervals[:end_index]+[(start,end)]+self.intervals[end_index:]
        return True


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)