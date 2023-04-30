class Solution:
    def minimumCost(self, start: List[int], target: List[int], specialRoads: List[List[int]]) -> int:
        a=tuple(start)
        b=tuple(target)
        d={}  
        def dist(a,b):
            x1,y1=a
            x2,y2=b
            x=abs(x1-x2)
            y=abs(y1-y2)
            return x+y
        nodes=set()
        nodes.add(a)
        nodes.add(b)
        def add_edge(p,q,c):
            if (p,q) not in d:
                d[(p,q)]=c
            else:
                d[(p,q)]=min(d[(p,q)],c)

        for x1,y1,x2,y2,c in specialRoads:
            p=(x1,y1)
            q=(x2,y2)
            add_edge(p,q,c)
            nodes.add(p)
            nodes.add(q)

        nodelist=list(nodes)
        for p in nodelist:
            for q in nodelist:
                c=dist(p,q)
                add_edge(p,q,c)
                add_edge(q,p,c)

        def dijkstra(a, b):
                distances = {node: float('inf') for node in nodelist}
                distances[a]=0
                priority_queue = [(0, a)]
                visited = set()
                while priority_queue:
                    current_distance, current_node = heapq.heappop(priority_queue)
                    if current_node == b:
                        break
                    if current_node not in visited:
                        visited.add(current_node)
                        for neighbor in nodelist:
                            p,q=current_node,neighbor
                            tentative_distance = current_distance + d[(p,q)]
                            if tentative_distance < distances[neighbor]:
                                distances[neighbor] = tentative_distance
                                heapq.heappush(priority_queue, (tentative_distance, neighbor))
                return int(distances[b])
        return dijkstra(a,b)
        