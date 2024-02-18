class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        booked, free = [], list(range(n))
        meetings.sort()
        freq = defaultdict(int)

        for start, end in meetings:
            while booked and booked[0][0] <= start:
                _, room = heappop(booked)
                heappush(free, room)
            
            if free:
                room = heapq.heappop(free)
                heappush(booked, [end, room])
            else:
                release, room = heappop(booked)
                heappush(booked, [release + end - start, room])
            
            freq[room] += 1

        return max(freq, key=freq.get)