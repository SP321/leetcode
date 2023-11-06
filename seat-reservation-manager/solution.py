class SeatManager:
    def __init__(self, n: int):
        self.x = []
        self.pos=0

    def reserve(self) -> int:
        if not self.x:
            self.pos+=1
            return self.pos
        return heapq.heappop(self.x)

    def unreserve(self, seatNumber: int) -> None:
        heapq.heappush(self.x, seatNumber)

        


# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)