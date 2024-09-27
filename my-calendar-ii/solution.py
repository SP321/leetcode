class MyCalendarTwo:

    def __init__(self):
        self.bookings = []
        self.double_bookings = []

        
    def book(self, start: int, end: int) -> bool:
        for booking in self.double_bookings:
            if start < booking[1] and end > booking[0]:
                return False

        for booking in self.bookings:
            if start < booking[1] and end > booking[0]:
                self.double_bookings.append((max(start, booking[0]), min(end, booking[1])))

        self.bookings.append((start, end))
        return True
