class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0

        d = defaultdict(set)
        for i, route in enumerate(routes):
            for stop in route:
                d[stop].add(i)

        visited_stops = set()
        queue = deque([(source, 0)])

        while queue:
            current_stop, num_buses = queue.popleft()

            for route_index in d[current_stop]:
                for next_stop in routes[route_index]:
                    if next_stop == target:
                        return num_buses + 1

                    if next_stop not in visited_stops:
                        visited_stops.add(next_stop)
                        queue.append((next_stop, num_buses + 1))

                routes[route_index] = []

        return -1 