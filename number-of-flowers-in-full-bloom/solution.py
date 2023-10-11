class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        events = []
        for start, end in flowers:
            events.append((start, 1))
            events.append((end + 1, -1))

        events.sort()

        current_blooms = 0
        event_idx = 0
        
        people_with_indices = sorted((val, idx) for idx, val in enumerate(people))

        ans = [0] * len(people)
        
        for day, idx in people_with_indices:
            while event_idx < len(events) and events[event_idx][0] <= day:
                current_blooms += events[event_idx][1]
                event_idx += 1

            ans[idx] = current_blooms

        return ans